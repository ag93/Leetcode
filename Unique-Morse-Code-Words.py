class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse = {
            "a" : ".-",
            "b" : "-...",
            "c" : "-.-.",
            "d" : "-..",
            "e" : ".",
            "f" : "..-.",
            "g" : "--.",
            "h" : "....",
            "i" : "..",
            "j" : ".---",
            "k" : "-.-",
            "l" : ".-..",
            "m" : "--",
            "n" : "-.",
            "o" : "---",
            "p" : ".--.",
            "q" : "--.-",
            "r" : ".-.",
            "s" : "...",
            "t" : "-",
            "u" : "..-",
            "v" : "...-",
            "w" : ".--",
            "x" : "-..-",
            "y" : "-.--",
            "z" : "--..",
        }
        
        morse_list = []
        #string = ""
        for x in words:
            string = ""
            for letter in x:
                string = string + morse[letter]
            morse_list.append(string)
            #string = ""

        from collections import Counter
        cnt = Counter(morse_list)
        return(len(cnt))