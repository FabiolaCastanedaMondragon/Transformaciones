from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template_string(open("index.html").read())

@app.route("/image")
def image():
    return send_file("fab.jpeg", mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

