import time
from random import randint
from human import Human
from ai import Ai


class Gui:

    def __init__(self):
        self.players = []


    # Goes through gui methods to run the game
    def run_game(self):
        self.start_game()
        self.instructions()
        self.create_player()
        self.vs_human_or_ai()
        for player in self.players:
            print(player.name)


    # Displays welcome
    def start_game(self):
        self.new_section()
        print('''                       Welcome to RPSLS!
                
                Rock, Paper, Scissors, Lizard, Spock!

            ''')


    # Seperates sections of the game in the terminal. Optionally, add a title to the section.
    def new_section(self, title='', pause_time=1):
        print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
        time.sleep(pause_time)
        print(title.upper())
        time.sleep(pause_time)
    

    # Instructions for the game
    def instructions(self):
        self.new_section('instructions', 2)
        print('''
Rules:
    - Two ways to play:
        1. against an ai
        2. against a friend
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

        ''')
        input('[ Press Enter to Continue ]')
    

    # Returns a yes or no response from the user
    def yes_or_no(self, question):
        answer = ''
        while answer != 'Y' and answer != 'N':
            print(question)
            answer = input("Enter 'y' to approve or 'n' to not: ").upper()
        return answer


    # Goes through steps to create a Human
    def create_player(self):
        self.new_section('generate Human')
        self.enter_name()
    

    # Will create the Human class after the user successfully enters their name
    def enter_name(self):
        player_name = input('\nEnter your name: ')
        if self.yes_or_no(f'Your name is {player_name} - Is that correct? ') == 'N':
            player_name = self.enter_name()
        # Adding Human to the players list in the gui
        self.players += [Human(player_name)]


    def vs_human_or_ai(self):
        self.new_section()
        if self.yes_or_no('Create another Human? ') == 'Y':
            self.create_player()
        else:
            gen_bot_name = 'bot#' + str(randint(0, 1001)) 
            self.players += [Ai(gen_bot_name)]
        


    def turn(self):
        self.new_section()
    