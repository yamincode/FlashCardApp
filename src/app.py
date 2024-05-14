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
    * {
    box-sizing: border-box;
    }

    input[type=text], select, textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    resize: vertical;
    }

    label {
    padding: 12px 12px 12px 0;
    display: inline-block;
    }

    input[type=submit] {
    background-color: #04AA6D;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    float: right;
    }

    input[type=submit]:hover {
    background-color: #45a049;
    }

    .container {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
    }

    .col-25 {
    float: left;
    width: 25%;
    margin-top: 6px;
    }

    .col-75 {
    float: left;
    width: 75%;
    margin-top: 6px;
    }

    /* Clear floats after the columns */
    .row:after {
    content: "";
    display: table;
    clear: both;
    }

    /* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
    @media screen and (max-width: 600px) {
    .col-25, .col-75, input[type=submit] {
        width: 100%;
        margin-top: 0;
    }
    }
    </style>
    </head>
    <body>

    <h2>User Login</h2>

    <div class="container">
    <form action="/action_page.php" method="POST">
        <div class="row">
        <div class="col-25">
            <label for="fname">First Name</label>
        </div>
        <div class="col-75">
            <input type="text" id="fname" name="firstname" placeholder="Your name..">
        </div>
        </div>
        <div class="row">
        <div class="col-25">
            <label for="lname">Last Name</label>
        </div>
        <div class="col-75">
            <input type="text" id="lname" name="lastname" placeholder="Your last name..">
        </div>
        </div>
        <div class="row">
        <input type="submit" value="Submit">
        </div>
    </form>
    </div>

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


@app.route("/action_page.php", methods=["POST"])
def echo_input():
    firstName = request.form.get("firstname", "")
    
    lastName = request.form.get("lastname","")
    return "You name: " + firstName +" "+lastName
    