#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

# Define a list of flashcards with Chinese characters and their corresponding English meanings
flashcards = [
    {"chinese": "你好", "english": "Hello"},
    {"chinese": "谢谢", "english": "Thank you"},
    {"chinese": "是的", "english": "Yes"},
    {"chinese": "不", "english": "No"},
    {"chinese": "好的", "english": "OK"}
]

@app.route("/")
def index():
    return render_template("index.html", flashcards=flashcards)

if __name__ == "__main__":
    app.run(debug=True)
