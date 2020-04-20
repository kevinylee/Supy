from flask import Flask
from flask import render_template

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)