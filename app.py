from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', d= main.printOut())