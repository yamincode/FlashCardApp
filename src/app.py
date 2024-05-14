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

@app.route("/")
def index():
    return render_template("index.html", flashcards=flashcards)

if __name__ == "__main__":
    app.run(debug=True)

def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text
