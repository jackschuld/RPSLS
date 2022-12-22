class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        # Made into dictionary, which has gesture as the key and the values are the gestures the key will beat
        self.gestures = {'Rock': ['Scissors', 'Lizard'], 'Paper': ['Spock', 'Rock'], 'Scissors': ['Paper', 'Lizard'], 'Lizard': ['Paper', 'Spock'], 'Spock': ['Rock', 'Scissors']}
        self.selection = ''
    

    def set_selection(self):
        selection = ''
        while selection not in self.gestures:
            print(f'\n{self.name}\'s turn!')
            for gesture in self.gestures:
                print(f'- ' + gesture)
            selection = input(f'\n{self.name} - Type out the option from above that you want to select: ').title()
        self.selection = selection
        input('\n[ Press Enter to Continue ]')
        print('\n')


    