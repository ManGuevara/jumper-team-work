from game.construct_para import Parachute
from game.player import Player
from game.word import Word


class Director:
    """A person who directs the game.

        The responsibility of a Director is to control the sequence of play.

        Attributes:
            start_game - Starts the game calling the methods.
            _get_inputs - calls the method to compare the guess and the word
            _do_updates - updates the result accoring to the rules. 
            _do_outputes - Displays the parachute and the final results. 

    """

    def __init__ (self):
        
        """Constructs a new Director. 
        Args:
        Director (self) An instance of director"""
        self._parachute = Parachute()
        self._is_playing=True
        self.player = Player()
        self.words = Word()
        self.game_word=self.words.random_word()
        self.indices=self.player.indices
       

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # To start we print the parachute.
        self._parachute.display_parachute()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
       
    
    def _get_inputs(self):
        """ gets a letter from the user and compares to the random word. 
        
        Args:
            self (Director): An instance of Director.        
        """

        self.player.compare_guess(self.game_word)
        

    def _do_updates (self):
        """Keeps track of the parachute according to the game rules. 

        Args:
            self (Director): An instance of Director.
        """
        wrong_counter=self.player.wrong_counter
        self.indices=self.player.indices
        self._parachute.update_parachute(wrong_counter,self.game_word,self.player._user_guess,self.indices)
        

    def _do_outputs (self):
         """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
         self._parachute.display_parachute()
         if '_' in self._parachute._word_space:
             self._is_playing=True
         else:
             print(f"You won! The word was {self.game_word.upper()}")
             self._is_playing=False
         if self._parachute._parachute=="   x \n  /|\ \n  / \ \n \n^^^^^^^":
             print(f"You lost! The word was {self.game_word.upper()}")
             self._is_playing=False
