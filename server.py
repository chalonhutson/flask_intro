"""Greeting Flask app."""

from random import choice

from flask import Flask, request, render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return '''<!doctype html>
                <html>
                  <a href='http:\/\/localhost:5000\/hello'>Hi! This is the home page.</a>
                  <a href='http:\/\/localhost:5000\/diss'>Get a diss!</a>
                </html>'''


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="compliments" id="compliments">
            <option value="like Samwise">like Samwise Gamgee.</option>
            <option value="like Gandalf the Grey">like Gandalf the Grey.</option>
            <option value="like Gandalf the White">like Gandalf the White.</option>
            <option value="like King Theoden">like King Theoden.</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliments")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route("/diss")
def get_diss():
  return render_template("diss.html")

@app.route("/diss_read")
def diss_read():
  person = request.args.get("person")
  diss = request.args.get("diss")

  return render_template("diss_read.html", person=person, diss=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
