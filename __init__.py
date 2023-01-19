from flask import Flask,render_template

app = Flask(__name__)

app.run()

from routes.home import*
from routes.favorite import*


if __name__ == "__main__":
    app.run()