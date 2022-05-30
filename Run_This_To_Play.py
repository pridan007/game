from daniel_game import Game
from Utils import Utils

def get_game(game_choose):
    if game_choose == 1:
        from MemoryGame import MemoryGame
        return MemoryGame()
    elif game_choose == 2:
        from GuessGame import GuessGame
        return GuessGame()
    else:
        from CurrencyRoulette import CurrencyRouletteGame
        return CurrencyRouletteGame()

def welcome(name):
    print(f"Hello {name}, and welcome to the World of Games.\nHere you can find many cool games to play.")

def choose_game():
    return input("Enter the number of your desired game :) -> ")

def game_been_choose(game_choose):
    return 0 < int(game_choose) < 4

def show_game_menu():
    print("""Please choose a game to play:\n
                        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                        guess it back\n
                        2. Guess Game - guess a number and see if you chose like the computer\n
                        3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")

Utils.Screen_cleaner()
welcome(input("Enter your name -> "))
show_game_menu()
game_choose = choose_game()
while not Game.choose_is_valid(game_choose) or not game_been_choose(game_choose):
    game_choose = choose_game()
game_choose = int(game_choose)
game_selected = get_game(game_choose)
game_selected.play()

