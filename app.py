
# module 10 - Flask Application
# Lauren Brodsky 3/28/2026

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)
