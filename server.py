from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("NoNinjas.html")

@app.route('/ninja/')
def ninjaWithoutSlash():
    return ninja()

@app.route('/ninja')
def ninja():
    return render_template("oneNinja.html", pictureToDisplay='/static/tmnt.png', turtleName="All Turtles")

@app.route('/ninja/<color>')
def pickANinja(color):
    pictureToDisplay = "/static/notapril.jpg"
    turtleName = "April"
    # If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
    if (color.lower() == 'blue'):
        pictureToDisplay = "/static/leonardo.jpg"
        turtleName = "Leonardo"
    # /ninja/orange - Ninja Turtle Michelangelo.
    if (color.lower() == 'orange'):
        pictureToDisplay = "/static/michelangelo.jpg"
        turtleName = "Michelangelo"
    # /ninja/red - Ninja Turtle Raphael
    if (color.lower() == 'red'):
        pictureToDisplay = "/static/raphael.jpg"
        turtleName = "Raphael"
    # /ninja/purple - Ninja Turtle Donatello
    if (color.lower() == 'purple'):
        pictureToDisplay = "/static/donatello.jpg"
        turtleName = "Donatello"
    return render_template("oneNinja.html", pictureToDisplay=pictureToDisplay, turtleName=turtleName)

app.run(debug=True)
