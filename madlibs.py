"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("index.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def lib_game():
    """Madlib Game."""

    play = request.args.get("game")
    if play == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def display_game():
    """Madlib output."""

    noun = request.args.get("noun")
    color= request.args.get("color")
    adj=request.args.get("adj")
    person_name=request.args.get("person_name")

    return render_template("madlib.html", noun=noun, color=color, adj=adj, person_name=person_name)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
