from flask import Flask

app = Flask(__name__)

@app.route("/")
def the_game():
  return '<p>THE GAME</p>'
