import random

class Words:
    def __init__(self):
        '''attribute word this is the word selected by randon from a list'''    
        self._word = " "
       
    def random_word(self):
        words_list = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom",
          "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "boggle",
          "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing",
          "buzzwords", "breath","brick", "bridge", "bright","broken","brother","brown","brush","bucket",
          "building", "bulb","burst","business","but","butter","button","cake","camera","canvas" "card","care",
          "carriage", "caliph", "cobweb", "cockiness", "crypt", "cycle", "daiquiri", "disavow", "dizzying",
          "duplex", "dwarves", "embezzle", "equip", "espionage", "empathy",
          "exodus", "faking", "fixable", "fjord", "flapjack", "gabby", "galaxy", "galvanize", "gazebo",
          "giaour", "haiku", "haphazard", "hyphen", "icebox", "jackpot", "jaundice", "jawbreaker",
          "jaywalk", "jazziest", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "larynx", "lengths", "lucky",
          "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "naphtha", "nightclub",
          "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm",
          "pixel", "pizazz", "quartz", "queue", "quips", "quixotic", "quiz", "razzmatazz", "rhubarb", "rhythm",
          "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "thriftless", "thumbscrew", "topaz",
          "transcript", "transgress", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "victory",
          "voodoo", "vortex", "walkway", "waltz", "wave", "wavy", "wyvern", "xylophone", "yachtsman", "yippee", "yoked",
          "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zombie"]
       
        randon_word = random.choice(words_list)
        self._word = randon_word 
        word_lenght = len(self._word)
        self._word_lenght = word_lenght
        return self._word

