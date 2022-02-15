from jumper_game.game.terminal_service import TerminalService
class Parachute:        

    """it designs the parachute grid """
    """it deletes one line of the grid parachute when the guess is wrong"""
    """it shows an "x" on the parachute¨s head when there are not more grid lines"""

    
    def __init__(self):  
        """designs parachute"""
    
        self.__parachute_life = [
            "   _____   ",
            "  /-----\ ",
            " |       |",
            "  \     /",
            "   \ 0 /"
        ]
        self.__body = [
            "    /|\\",
            "    / \\",
            "",
            "_____________"
        ]
        self.__terminal = TerminalService()
    
    def print_parachute(self):
        """shows the parachute"""
        for line in self.__parachute_life:
            self.__terminal.write_text()
        for line in self.__body:
            self.__terminal.write_text()

    def update_parachute(self):
        """deletes one line of the grid parachute when the guess is wrong"""
        self.__parachute_life.pop()
        if len(self.__parachute_life) == 1:
            self.__parachute_life[0] = "     x  "
    
    def opportunity(self):
        """take an opportunity"""
        return len(self.__parachute_life) - 1