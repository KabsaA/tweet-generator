from flask import Flask
from frequency import words1, sentence

app = Flask(__name__)


@app.route('/')
def hello_world():
    return sentence("source.txt")
