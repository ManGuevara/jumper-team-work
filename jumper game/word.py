import random
class Word:
     """ Random word from a list of words
    The responsibility of Word is to provide a random word from a list of words
    
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

    
    def __init__(self):
        """
        Constructs a new instance of Word with a value attribute.
        Args:
            self (Word): An instance of Word.
        
        """
        

        """it creates a list of words"""
        self._list_words = ["one", "two", "three"]
        
        """it takes just one random word"""
        self._word= ""

        """it takes the letters from the random word and put them in underscores"""


    

    def random_word(self):
        """pick a random word"""
        index = random.randint(0,3)
        self._word = self._list_words[index]

    def putting_undescores(self):
        """shows the hiden word in underscores"""
