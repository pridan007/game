import os


class Utils:

    @staticmethod
    def score_file():
        SCORES_FILE_NAME = "Scores.txt"
        return SCORES_FILE_NAME



    # - A function to clear the screen (useful when playing memory game or before a new game starts).
    @staticmethod
    def Screen_cleaner():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

