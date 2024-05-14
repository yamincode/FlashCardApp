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
def main():
    return """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        body {
        font-family: Arial, Helvetica, sans-serif;
        }

        .flip-box {
        background-color: transparent;
        width: 200px;
        height: 100px;
        border: 1px solid #f1f1f1;
        perspective: 1000px;
        }

        .flip-box-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
        }

        .flip-box:hover .flip-box-inner {
        transform: rotateY(180deg);
        }

        .flip-box-front, .flip-box-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        }

        .flip-box-front {
        background-color: #bbb;
        color: Black;
        }

        .flip-box-back {
        background-color: dodgerblue;
        color: white;
        transform: rotateY(180deg);
        }
        </style>
        </head>
        <body>

        <h1>Flashcards</h1>
        <h3>Hover over the box below to see the translation in English:</h3>

        <div class="flip-box">
        <div class="flip-box-inner">
            <div class="flip-box-front">
            <h2>你好</h2>
            </div>
            <div class="flip-box-back">
            <h2>Hello</h2>
            </div>
        </div>
        </div>

        </body>
        </html>


    """

