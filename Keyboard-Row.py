class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z','x','c','v','b','n','n','m'])
        
        def convert_to_set(word):
            s = set()
            for c in word:
                s.add(c.lower())
            return s
        
        result = []
        for word in words:
            word_set = convert_to_set(word)
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                result.append(word)
                
        return(result)