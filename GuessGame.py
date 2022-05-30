from daniel_game import Game


class GuessGame(Game):
    """
        Guss Game.
    """

    def __init__(self):
        super().__init__()
        self.secret_number = -1  # -1 means that user not been choose.
        self.Difficulty = self.difficulty_choose()

    def generate_number(self):
        from random import randrange
        self.secret_number = (randrange(1,int(self.Difficulty)))
        return self.secret_number

    def get_guess_from_user(self):
        self.user_guess = input("Enter the number between 1 and  "  + self.Difficulty +  ":) -> ")

    def user_guess_choose(self):
        return 1 <= int(self.user_guess) <= int(self.Difficulty)

    def choose_not_valid(self):
        check = self.user_guess
        while not self.choose_is_valid(check) or not self.user_guess_choose() :
            self.get_guess_from_user()
            check = self.user_guess

    def compare_results(self):
        if int(self.secret_number) != int(self.user_guess):
            print("They are not equel")
        else:
            print("They are equel")
            self.add_score(self.Difficulty)

    def play(self):
        self.generate_number()
        self.get_guess_from_user()
        self.choose_not_valid()
        self.compare_results()


if __name__ == "__main__":
    print("please run this game from Run_This_To_Play.py")


