from game.word import Word

class Player:
    """A person who plays the game.

    The responsibility of the Player is to obtain user input and compare it with the game's word.

    Attributes:
        user_guess= User's guess
        indeces= List of indices of the User's guessed letter in the game's word.
        wrong_counter= Counter of user's wrong guesses.
        word (Word): The word provided by the word class.
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self._user_guess=' '
        self.indices=[]
        self.wrong_counter=0
        self.word=Word().random_word()
        
    
    def get_input(self):
        """Gets the user input (a letter).

        Args:
            self (Player): an instance of Player.
        """
        self._user_guess=input("Guess a letter: ")
        pass

    def compare_guess(self,game_word):
        """Check if user's input (self._user_guess) is inside the word provided by 
            the Word class (self.word)

        Args:
            self (Player): an instance of Player.
            game_word: a word provided randomly by the word.
        """
        self.get_input()
        if self._user_guess in game_word:
            self.right_guess(game_word)
        else:
            self.wrong_guess()
        pass

    def right_guess(self,game_word):
        """Updates self.index with the word's indices where the user's chosen letter
            is in.

        Args:
            self (Player): an instance of Player.
            game_word: a word provided by the game.
        """
        word=game_word
        guess=self._user_guess
        indices=[]
        for i in range(len(word)):
            if word[i] == guess:
                indices.append(i)
        self.indices= indices
        
    def wrong_guess(self):
        """Adds 1 to the self.wrong_counter counter

        Args:
            self (Player): an instance of Player.
        """
        self.wrong_counter+=1
    

