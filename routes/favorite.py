from flask import render_template
from hw import app

@app.route("/favorite-5")
def favorite_5():
    favorite_5 = ["sports1", "sports2", "sports3", "sports4", "sports5"]
    return render_template("favorite_5.html", favorite_5=favorite_5)