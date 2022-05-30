from daniel_game import Game


class CurrencyRouletteGame(Game):
    """
        Roulette Game.
    """
    def __init__(self):
        super().__init__()
        self.Difficulty = self.difficulty_choose()
        self.TotalValueOfMoney = -1
        self.MoneyInUsd = -1
        self.user_guess = -1

    def get_money_interval(self):
        import requests
        response = requests.get('https://freecurrencyapi.net/api/v2/latest?apikey=2989c260-3f0a-11ec-81bf-dd8b484d674a').json()
        current_currency = response["data"]["ILS"]
        from random import randrange
        self.MoneyInUsd = (randrange(1, 100))
        self.TotalValueOfMoney = self.MoneyInUsd * current_currency

    def get_guess_from_user(self):
        self.user_guess = input("Enter how much " + str(self.MoneyInUsd) + " is in ILS  :) -> ")

    def user_guess_choose(self):
        return 1 <= int(self.user_guess)

    def choose_not_valid(self):
        check = self.user_guess
        while not self.choose_is_valid(check) or not self.user_guess_choose() :
            self.get_guess_from_user()
            check = self.user_guess

    def check_if_won(self):
        if int(self.TotalValueOfMoney) - (5 - int(self.Difficulty)) < int(self.user_guess) < int(self.TotalValueOfMoney) + (
                5 - int(self.Difficulty)):
            print("True")
            self.add_score(self.Difficulty)
        else:
            print("False")

    def play(self):
        self.get_money_interval()
        self.get_guess_from_user()
        self.choose_not_valid()
        self.check_if_won()


if __name__ == "__main__":
    print("please run this game from Run_This_To_Play.py")
