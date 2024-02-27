# Anki Word Pair Automation Script

This script is designed to automate the process of adding word pairs (e.g., vocabulary and their meanings) to an Anki deck. It utilizes AnkiConnect that allows external applications to communicate with Anki, to streamline the process of adding new notes to your decks.

## Prerequisites

Before you can use this script, please ensure the following requirements are met:

1. **Anki**: The Anki desktop application must be installed on your computer. You can download it from [the official Anki website](https://apps.ankiweb.net/).

2. **AnkiConnect**: This Anki add-on must be installed to allow the script to communicate with Anki. You can find the installation instructions on [the AnkiConnect GitHub page](https://github.com/FooSoft/anki-connect).

3. **Python 3**: This script is written in Python 3. Ensure that Python 3 is installed on your system.

4. **Requests Library**: The script uses the `requests` library to make HTTP requests. You can install it by running `pip install requests` in your terminal or command prompt.

5. **Deck Created**: Ensure that the deck where you want to add the word pairs is already created in Anki.

## Configuration

Before running the script, you need to configure it to communicate with your Anki setup:

1. Create a `config.json` file in the same directory as the script with the following content, adjusting the `deck_name` and `anki_connect_url` as necessary:

```json
{
    "deck_name": "YourDeckName",
    "anki_connect_url": "http://localhost:8765"
}
