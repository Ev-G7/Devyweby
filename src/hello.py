# app.py
from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    return render_template('Gallery.html')

if __name__ == "__main__":
    app.run(debug=True)
