import abc,os
from Utils import Utils

class Game(metaclass=abc.ABCMeta):


    def __init__(self):
        self.user_guess = -1  # -1 means that user not been choose.

    def choose_difficulty(self):
        return input("choose difficulty -> ")

    def difficulty_choose(self):
        # check if difficulty is int and between 1 and 5
        difficult = self.choose_difficulty()
        while not self.choose_is_valid(difficult) or not self.difficulty_been_choose(difficult):
            difficult = self.choose_difficulty()
        return difficult

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def user_guess_choose(self):
        pass

    @abc.abstractmethod
    def get_guess_from_user(self):
        pass

    @abc.abstractmethod
    def choose_not_valid(self):
        pass

    def difficulty_been_choose(self, difficulty):
        return 0 < int(difficulty) < 6

    @staticmethod
    def choose_is_valid(parameter):
        """
            Used by game choosing and difficult choosing.

        :param parameter: will be valid only if it int
        :return: boolean
        """
        try:
            int(parameter)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_current_score():
        score_file = Utils.score_file()
        if os.stat(score_file).st_size != 0:
            f = open(score_file, "r")
            content_of_file = f.read()
            f.close()
            return content_of_file

    @staticmethod
    def write_to_file(content_of_file):
        score_file = Utils.score_file()
        f = open(score_file, 'w')
        f.write(str(content_of_file))
        f.close()

    @staticmethod
    def add_score(Difficulty):
        Difficulty = int(Difficulty)
        POINTS_OF_WINNING = (Difficulty * 3) + 5
        if Game.get_current_score():
            content_of_file = int(Game.get_current_score())
            content_of_file = content_of_file + POINTS_OF_WINNING
            Game.write_to_file(content_of_file)
        else:
            Game.write_to_file(POINTS_OF_WINNING)
