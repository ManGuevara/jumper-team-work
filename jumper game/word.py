import random
class Word:
    pass
    def __init__(self):
        

        """it creates a list of words"""
        self._list_words = ["one", "two", "three"]
        
        """it takes just one random word"""
        self._word= " "

        """it takes the letters from the random word and put them in underscores"""


    

    def random_word(self):
        """pick a random word"""
        index = random.randint(0,3)
        self._word = self._list_words[index]

    def putting_undescores(self):
        """shows the hiden word in underscores"""
        