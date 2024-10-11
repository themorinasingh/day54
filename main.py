from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hesoyam")
def hesoyam():
    return "<H1>Skibidi-bop! Health maxed, armor locked, $25,000 in your pocket, and your ride’s fresh like new! Let’s roll!</H1>"

@app.route("/skibidi")
def skibidi():
    return ("<title>skibidi bop</title>"
            "<H1>Skibidi-dab! I came, I saw, I conquered—Veni, vidi, vibed!</H1>")

app.run()