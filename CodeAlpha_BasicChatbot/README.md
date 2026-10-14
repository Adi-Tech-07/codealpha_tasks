# CodeAlpha Basic Chatbot

A simple, rule-based, console chatbot written in Python 3.

## Description

This project is a beginner-friendly Python console application that simulates a
small conversation. The chatbot matches user input against a set of predefined
rules and returns a fixed reply. It is intentionally simple: no AI, no external
APIs, and no third-party dependencies.

## Features

- Welcoming startup banner.
- Rule-based responses for hello, how are you, and bye.
- Continuous conversation loop.
- Graceful exit when the user types bye.
- Case-insensitive and space-trimmed input handling.
- Safe fallback response for unsupported or empty input.

## Technology / Concepts

- Language: Python 3 (standard library only)
- input() and print() for console I/O
- if-elif-else conditional logic
- Functions for organized logic
- while loop for continuous conversation
- String methods (strip, lower) for normalization

## How to Run

Run the script with Python 3:

```
python chatbot.py
```

No dependencies need to be installed.

## Example Interaction

```
================================
        BASIC CHATBOT
================================

Bot: Hello! Welcome to the chatbot.
Bot: Type "bye" to exit.

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: what is your name?
Bot: Sorry, I don't understand that.

You: bye
Bot: Goodbye!

Chat ended.
```

## Project Structure

```
CodeAlpha_BasicChatbot/
+-- chatbot.py   # Chatbot logic, functions, loop, input/output
+-- README.md    # This file
+-- PRD.md       # Project specification (source of truth)
```
