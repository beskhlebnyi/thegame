import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def the_game():
  env = os.environ['FLASK_ENV']
  return render_template('root.html', env=env)
