from flask import Flask

app = Flask(__name__)

# create routes
@app.route("/home")
def home():
    return "Hello, World!"