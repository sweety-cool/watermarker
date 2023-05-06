from flask import Flask
import os


app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))

@app.route("/")
def main():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")
