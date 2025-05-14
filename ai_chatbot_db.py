import nltk
import sqlite3
import pyttsx3
import wikipedia
import requests
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Set up database
def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS qa (
            question TEXT PRIMARY KEY,
            answer TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_qa(question, answer):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO qa (question, answer) VALUES (?, ?)", (question.lower(), answer))
    conn.commit()
    conn.close()

def get_answer_from_db(question):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM qa WHERE question=?", (question.lower(),))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Wikipedia Search
def get_wikipedia_answer(question):
    try:
        return wikipedia.summary(question, sentences=2)
    except:
        return None

# Web Search using SerpAPI
SERP_API_KEY = "d66c742d95468abbdfe588f10c470f9f0196f3310c89fe2182e58706052a80db"  # Replace with your SerpAPI key

def get_web_answer(query):
    try:
        url = "https://serpapi.com/search"
        params = {
            "q": query,
            "api_key": SERP_API_KEY,
            "num": 1
        }
        res = requests.get(url, params=params)
        data = res.json()
        if "answer_box" in data and "answer" in data["answer_box"]:
            return data["answer_box"]["answer"]
        elif "organic_results" in data:
            return data["organic_results"][0]["snippet"]
        else:
            return "I couldn't find a good answer online."
    except:
        return "Error while searching online."

# Basic fallback responses
default_pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"what is your name ?", ["I'm PyBot!", "You can call me PyBot."]],
    [r"how are you ?", ["I'm doing great!", "All systems running fine."]],
    [r"quit", ["Goodbye!", "See you soon."]],
]

chatbot = Chat(default_pairs, reflections)

# GUI logic
def send():
    user_input = entry.get().strip()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    
    if user_input.lower().startswith("learn:"):
        try:
            parts = user_input[6:].strip().split("|")
            question = parts[0].strip()
            answer = parts[1].strip()
            insert_qa(question, answer)
            response = f"I've learned how to answer: '{question}'"
        except:
            response = "Invalid format. Use: learn: question | answer"
    else:
        db_response = get_answer_from_db(user_input)
        if db_response:
            response = db_response
        else:
            response = chatbot.respond(user_input)
            if not response:
                response = get_wikipedia_answer(user_input)
            if not response:
                response = get_web_answer(user_input)
            if not response:
                response = "Sorry, I couldn't understand or find that."

    chat_log.insert(tk.END, "PyBot: " + response + "\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    speak(response)
    entry.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("PyBot - AI Chatbot with Internet Access")

chat_log = scrolledtext.ScrolledText(window, state='disabled', width=60, height=20, font=("Arial", 12))
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(window, width=45, font=("Arial", 12))
entry.grid(row=1, column=0, padx=10, pady=10)

send_btn = tk.Button(window, text="Send", command=send, font=("Arial", 12))
send_btn.grid(row=1, column=1)

chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "PyBot: Hi! Ask me anything.\nYou can also teach me:\nlearn: question | answer\nType 'quit' to exit.\n")
chat_log.config(state=tk.DISABLED)

init_db()
window.mainloop()
