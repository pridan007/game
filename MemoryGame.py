from daniel_game import Game
from Utils import Utils

class MemoryGame(Game,Utils):
    """
        Memory Game.
    """

    def __init__(self):
        super().__init__()
        self.Difficulty = self.difficulty_choose()
        self.Game_list = -1
        self.user_guess = -1


    def generate_sequence(self):
        from random import randrange
        import time
        ListOfGame = []
        for i in range(int(self.Difficulty)):
            List_generate_number=(randrange(1,101))
            ListOfGame.append(int(List_generate_number))

        print(ListOfGame)
        time.sleep(0.7)
        self.Screen_cleaner()
        self.Game_list = ListOfGame

    def get_guess_from_user(self):
        self.Number_from_user = input("    what is the " + self.Location_in_for + " you show?")

    def get_list_from_user(self):
        List_Of_User = []
        for i in range(int(self.Difficulty)):
           self.Location_in_for = str(i + 1)
           self.get_guess_from_user()
           self.choose_not_valid()
           List_Of_User.append(int(self.Number_from_user))
           self.user_guess = List_Of_User

    def user_guess_choose(self):
        return 1 <= int(self.Number_from_user) <= 101

    def choose_not_valid(self):
        while not self.choose_is_valid(self.Number_from_user) or not self.user_guess_choose():
            self.Number_from_user = input("    what is the " + self.Location_in_for + " you show?")


    def is_list_equal(self):
        if self.user_guess == self.Game_list:
            print("True")
            self.add_score(self.Difficulty)


        else:
            print("False")

    def play(self):
        self.generate_sequence()
        self.get_list_from_user()
        self.is_list_equal()

if __name__ == "__main__":
    print("please run this game from Run_This_To_Play.py")