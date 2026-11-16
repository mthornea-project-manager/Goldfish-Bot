# 🐟 Goldfish Bot: Stateful AI Assistant

> Developed as the Final Project for **Stanford Code in Place**.

## 🚀 Overview
**Goldfish Bot** is an interactive, stateful command-line chatbot built in Python. Unlike stateless models, Goldfish Bot maintains conversation context using structured dictionaries and implements sophisticated memory management techniques to handle token limits and context windows efficiently.

## 🛠️ Core Features
- **Interactive Chat Loop**: Real-time conversation interface powered by the OpenAI API wrapper.
- **`peek` Command**: Inspects the raw underlying message history and stack size.
- **`rewind` Command**: Safely removes the last exchange (user input and assistant response) without risking system instructions.
- **Memory Budgeting (`MAX_WORDS`)**: Automatically monitors word counts to prevent context overflow.
- **`forget` vs `compact` Strategies**: 
  - *Forget*: Prunes legacy conversation blocks.
  - *Compact*: Dynamically invokes the LLM to generate semantic summaries of past interactions while preserving vital user data and names.

## 💻 Code Architecture
The project leverages modular functional programming principles in Python:
- List-of-dictionary state management (`messages` stack).
- String parsing and prompt engineering (`format_messages`).
- Dynamic memory pruning and background LLM summarization.

---
*Certified Stanford Code in Place Project.*
