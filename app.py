from flask import Flask, render_template, send_file
import os

app = Flask(__name__)
@app.route('/')
def home():
    # Render the existing templates/index.html
    return render_template('index.html', sections=[])

if __name__ == '__main__':
    app.run(debug=True)
