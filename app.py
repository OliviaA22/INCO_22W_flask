# from dotenv import load_dotenv

# load_dotenv()

from flask import Flask
import json


with open("PatientData.json") as f:
    data = json.load(f)

app = Flask(__name__)

@app.route('/')
def hello():
    return str(data)

