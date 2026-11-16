"""
Goldfish Bot: An AI Stateful Chatbot with Memory Management
Course: Stanford Code in Place
Author: Alexander Marcelo Thorne
Description: A conversational Python bot that interacts with the OpenAI API 
             while intelligently managing conversational context and memory limits.
"""

from ai import call_gpt

INDENT = "    "
PERSONALITY = "You are a super sassy queen. Keep replies short."
MAX_WORDS = 150

def make_message(role, content):
    """Creates a standardized message dictionary for the LLM chat history."""
    return {"role": role, "content": content}

def peek(messages):
    """Displays the current message history stack and size."""
    print(f"{INDENT}The record has {len(messages)} messages:")
    for msg in messages:
        print(f"{INDENT}{msg['role']}: {msg['content']}")

def format_messages(messages):
    """Formats conversation history into a structured prompt string."""
    result = ""
    for msg in messages:
        if msg["role"] == "system":
            result += f"Instructions: {msg['content']}\n"
        elif msg["role"] == "user":
            result += f"User: {msg['content']}\n"
        else:
            result += f"Assistant: {msg['content']}\n"
    result += "Assistant:"
    return result

def rewind(messages):
    """Removes the last exchange (user + assistant) to reset context safely."""
    if len(messages) < 3:
        return messages
    return messages[:len(messages) - 2]

def count_words(messages):
    """Counts total words across all messages in memory."""
    total = 0
    for msg in messages:
        total += len(msg["content"].split())
    return total

def forget(messages):
    """Prunes oldest messages while keeping system prompt safe."""
    if len(messages) < 6:
        return messages
    return messages[:1] + messages[5:]

def compact(messages):
    """Summarizes old messages using AI to optimize memory budgets."""
    if len(messages) < 3:
        return messages
    old_messages = messages[1:len(messages) - 1]
    prompt = "Summarize this conversation in two or three sentences. Keep names and anything the user said about themselves.\n" + format_messages(old_messages)
    summary = call_gpt(prompt)
    return [messages[0], make_message("system", f"Summary of the conversation so far: {summary}"), messages[-1]]

def main():
    print("Chat with the bot! (press Enter to quit)")
    messages = [make_message("system", PERSONALITY)]
    message = input("You: ")
    while message != "":
        if message == "peek":
            peek(messages)
        elif message == "rewind":
            messages = rewind(messages)
            print(f"{INDENT}Rewound! The record has {len(messages)} messages.")
        else:
            messages.append(make_message("user", message))
            if count_words(messages) > MAX_WORDS:
                choice = input(f"{INDENT}My memory was full ({count_words(messages)} words)! Type 'forget' or 'compact': ")
                if choice == "compact":
                    messages = compact(messages)
                else:
                    messages = forget(messages)
                print(f"{INDENT}Now I remember {len(messages)} messages, {count_words(messages)} words.")
            prompt = format_messages(messages)
            reply = call_gpt(prompt)
            print(f"Bot: {reply}")
            messages.append(make_message("assistant", reply))
        message = input("You: ")

if __name__ == "__main__":
    main()
