from flask import Flask, request, render_template
import random


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/rps")
def data():
    x = random.randrange(0, 3)
    
    return (
    
        {"result" : "rock"}
        if(x == 0)
        else
        {"result": "paper"}
        if(x == 1)
        else
        {"result" : "scissors"}
        if(x == 2)
        else
        {"error" : "none"}
    )

if __name__ == "__main__":
    app.run(debug = True)
