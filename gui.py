import time


class Gui:

    def __init__(self, players):
        self.players = players


    def run_game(self):
        self.start_game()
        self.instructions()
        self.create_player()
        self.vs_human_or_ai()


    def start_game(self):
        self.new_terminal_section()
        print('''           Welcome to RPSLS!
                
    Rock, Paper, Scissors, Lizard, Spock!
        ''')


    def new_terminal_section(self):
        time.sleep(1)
        print('\n# # # # # # # # # # # # # # # # # # # # # # # #\n')
        time.sleep(1)
    

    def instructions(self):
        self.new_terminal_section()
        print('''INSTRUCTIONS\n
    Rules:
    - Two ways to play, either against an ai or enter a friend to play against.
    - Take turns entering 'Rock', 'Paper', 'Scissors', 'Lizard', or 'Spock'.
    - If your selection wins against the opponents, you earn a point.
    - Play to the best of 3 (ie. whoever gets 2 wins first).
    
    Determine Winner:
    - Rock > Scissors
    - Scissors > Paper
    - Paper > Rock
    - Rock > Lizard
    - Paper > Spock
    - Scissors > Lizard
    - Lizard > Spock
    - Lizard > Paper
    - Spock > Scissors
    - Spock > Rock        


# # # # # # # # # # # # # # # # # # # # # # # #
        ''')

    def create_player(self):
        self.new_terminal_section()


    def vs_human_or_ai(self):
        self.new_terminal_section()


    def turn(self):
        self.new_terminal_section()
    