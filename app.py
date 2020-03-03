from flask import Flask
from frequency import weighted_sample, weighted_phrase

app = Flask(__name__)


@app.route('/')
def hello_world():
    return weighted_phrase("source.txt")
