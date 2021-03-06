from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():

    response = request.args.get("play_game")  # From compliment.html.
    person = request.args.get("person")

    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html",
                                person=person)

@app.route('/madlib')
def show_madlib():

    name = request.args.get("firstname")  # From game.html.
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    adjectivetwo = request.args.getlist("adjectivetwo")

    template = choice(["madlib.html", "new_madlib.html"])


    return render_template(template,
                            firstname=name,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            adjectivetwo=adjectivetwo)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
