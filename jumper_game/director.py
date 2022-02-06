from jumper_game.word import word
from jumper_game.parachute import parachute
from jumper_game.player import player

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        word (Word): The game's word provider.
        is_playing (boolean): Whether or not to keep playing.
        parachute (Parachute): Designed to print the parachute and its behavior
        player (Player): The game's player.
        
    """
    def __init__(self):
        pass
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word = word()
        #self._is_playing = True
        self.parachute = parachute()
        self.player = player()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

    def _get_inputs(self):
        """Gets a word from the user.
        Args:
            self (Director): An instance of Director.
        """

    def _do_updates(self):
        """Checks if the word has the letter entered by the user
        Args:
            self (Director): An instance of Director.
        """

    def _do_outputs(self):
        """Provides a feedback for the player to use. The entered letter is in the word or not.
        Args:
            self (Director): An instance of Director.
        """ 