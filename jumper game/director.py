class Director:
    pass
        """A person who directs the game"""

        """The responsibility of a Director is to control the sequence of play.

        Attributes:
        choose_word (choose_word): takes the word from a list that is return from word class.

        check_word (check_word): analyse if the input letter is correct or not.

        is_playing (boolean): it maneges the game to continue if the word is correct or not.

        finish_game: (finish_game):if the word is completed the game is over.

        parachute_gone (finish_game): it receives an x from the parachute class in order to finish the game 
        """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.choose_word = word()
        self.check_word =
        self.is_playing = True
        self.finish_game =
        self.parachute_gone = parachute()
        pass
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
    
    def update_word(self):
        """takes the word input from a list """
        """analyse if the input letter is correct or not"""
        """it maneges the game to continue if the word is correct or not"""
    
    def finish_game(self):
        """"if the word is completed the game is over"""
        """it receives an x from the parachute class in order to finish the game"""