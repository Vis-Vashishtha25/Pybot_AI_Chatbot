Sure! Below is a **GitHub-style** `README.md` for your project.

---

# PyBot - AI Chatbot with Internet Access

PyBot is an AI-powered chatbot that integrates various data sources to provide answers to user queries. It supports text-to-speech (TTS) for responses, learns from user interactions, and can search both Wikipedia and the web. Built using **Python**, **Tkinter**, and other useful libraries, PyBot is designed to provide an interactive and engaging chatbot experience.

---

## Features

* **Text-to-Speech (TTS)**: Responds verbally to user inputs.
* **Dynamic Learning**: Users can teach the bot by adding question-answer pairs that are saved in a local SQLite database.
* **Wikipedia Integration**: Fetches answers from Wikipedia for various queries.
* **Web Search via SerpAPI**: If the bot cannot answer, it searches the web using SerpAPI to provide relevant information.
* **Interactive GUI**: Built with **Tkinter**, allowing users to easily chat with the bot in a graphical interface.
* **Customizable**: Extend the bot by adding more question-answer pairs and functionalities.

---

## Installation

### Requirements

Make sure you have **Python 3.x** installed. You will also need the following libraries:

* `nltk`: Natural Language Processing toolkit.
* `pyttsx3`: Text-to-speech conversion library.
* `wikipedia`: Wikipedia API.
* `requests`: For web requests (to fetch search results from SerpAPI).
* `tkinter`: GUI library (usually pre-installed with Python).

You can install the required libraries using `pip`:

```bash
pip install nltk pyttsx3 wikipedia requests
```

### Set Up SerpAPI

To enable web searches, you need to sign up at [SerpAPI](https://serpapi.com/) and get an API key. Replace the `SERP_API_KEY` in the script with your own API key:

```python
SERP_API_KEY = "your_serp_api_key"
```

---

## Setup Instructions

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Vis-Vashishtha25/pybot.git
```

### 2. Install NLTK data

Run the following Python script to download the necessary NLTK datasets (for processing text and handling basic chat functionality):

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

### 3. Configure SerpAPI

Ensure you replace the API key in the code to enable the bot to fetch web search results.

---

## Usage

### 1. Run the chatbot

After setting up the dependencies, simply run the Python script:

```bash
python chatbot.py
```

### 2. Chat with the bot

The bot will open a graphical interface using Tkinter. You can type your queries, and the bot will respond either in text or with speech.

### 3. Teach the bot

To add new question-answer pairs to the bot’s database, use the following format:

```
learn: question | answer
```

**Example:**

```
learn: What is the capital of France? | Paris
```

This will store the question and answer in the bot’s local SQLite database, allowing it to respond to the same question later.

### 4. Exit the chatbot

To exit the chatbot, type:

```
quit
```

---

## Functionality

### 1. Text-to-Speech (TTS)

The bot uses the `pyttsx3` library to convert text into speech. This allows the bot to respond to the user verbally, making interactions more engaging.

### 2. Database Integration

The bot stores custom question-answer pairs in a local SQLite database, `chatbot.db`. This enables the bot to recall previously learned information and provide accurate answers.

* **Insert/Fetch**: Users can insert new question-answer pairs via the `learn:` command, and the bot will look up answers from the database when available.

### 3. Wikipedia Integration

When the bot doesn't know an answer from the database, it tries to fetch the answer from **Wikipedia** using the `wikipedia` library. The bot retrieves a brief summary of the relevant topic.

### 4. Web Search using SerpAPI

If the bot cannot find an answer from its database or Wikipedia, it performs a **web search** using **SerpAPI** to fetch the answer from the internet.

---

## Contributing

Contributions are welcome! If you'd like to contribute to PyBot, feel free to fork the repository and create a pull request. Here are a few ways you can contribute:

* Improve the bot’s learning capabilities.
* Add new functionalities (e.g., integrate with other APIs).
* Fix any bugs or improve the existing code.

### Steps to Contribute

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch for your feature or fix.
4. Make your changes.
5. Push the changes to your fork and create a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions or suggestions, feel free to open an issue in the GitHub repository or contact me via email: [vvashishtha25@gmail.com](mailto:vvashishtha25@gmail.com).

---

### Disclaimer

This project uses third-party APIs like **Wikipedia** and **SerpAPI**. Please ensure that you have proper API keys and respect the terms of service of the respective APIs.

---

That's your **GitHub-style** README! You can adjust the information based on your specific needs or project goals.
