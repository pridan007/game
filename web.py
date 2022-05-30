from daniel_game import Game
current_score = Game.get_current_score()
from flask import Flask

app = Flask(__name__)


@app.route('/')
def web():
    if current_score:
         return "<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is <div id=score>" + current_score + "</div></h1> </body> </html>"
    else:
       return "<html> <head> <title>Scores Game</title> </head> <body> <h1> <div id ='score' style = 'color:red' >  ERROR </div> </h1> </body> </html>"