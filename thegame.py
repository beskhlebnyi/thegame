from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def the_game():
  return render_template('root.html')
