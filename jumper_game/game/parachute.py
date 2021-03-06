class Parachute:
    
    """it designs the parachute grid """
    """it deletes one line of the grid parachute when the guess is wrong"""
    """it shows an "x" on the parachute¨s head when there are not more grid lines"""
    
    def __init__(self):
        """designs parachute"""
        self._parachute = "  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
        self._word_space = ""

    def update_parachute (self,guess_wrong,word,letter,index):
        """
        Updating the parachute output according to the answers
        
        Args:
            self (Parachute): an instance of Parachute.
            guess_wrong (integer): Counter of the user's wrong attempts.
            word (str): a word provided by the game.
            letter (str): a letter provided by the user.
            index (list): a list of numbers (indices).
        """
        self.word_line(word,letter,index)
        if guess_wrong == 0:
            self._parachute = f"{self._word_space}\n\n  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
        elif guess_wrong == 1:
            self._parachute = f"{self._word_space}\n\n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
        elif guess_wrong == 2:
            self._parachute = f"{self._word_space}\n\n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
        elif guess_wrong == 3:
            self._parachute = f"{self._word_space}\n\n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
        else:
            self._parachute = "   x \n  /|\ \n  / \ \n \n^^^^^^^"
        
    def display_parachute (self):
        """ 
        shows the parachute
                
        Args:
            self (Parachute): an instance of Parachute.
        """
        print(self._parachute)

    def word_line(self,word,letter,index):
        '''
        Creates the slots for the game's word. Also replaces the slot with the user's
        chosen letter if correct

        Args:
            self (Parachute): an instance of Parachute.
            word (str): a word provided by the game.
            letter (str): a letter provided by the user.
            index (list): a list of numbers (indices).
        '''
        # The length of our word becomes underscore and space between them 
        # is part of the length. In this example would be 5)) +1(6), /2(3) is not equal to the length of the 
        # game's word (According to the example, also 3) AND the length of word_space /2 is not equal 
        # to the game's word: We create a line of underscores and spaces.

        if (len(self._word_space)+1)/2!=len(word) and len(self._word_space)/2!=len(word):
            for i in range(len(word)):
                self._word_space+='_ '
        # If the letter is in the word we create an empty list
        if letter in word:
            new_list=[]
            # We append each element of the word to the list except for white spaces(' ')
            for j in self._word_space:
                if j !=' ':
                    new_list.append(j)
            # For each number in the index's list, we replace the element with the right index with
            # the chosen letter.
            for k in index:
                new_list[k]=letter
            # We join the list into a string with a white space between them
            new_word=' '.join(new_list)
            self._word_space=new_word