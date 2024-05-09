from flask import Flask, request, redirect, render_template
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(original_url)
    return render_template('result.html',  short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
