class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.split(" ")

        from collections import Counter
        cnts = Counter(paragraph)

        counts = list(zip(cnts.keys(), cnts.values()))

        cnts = sorted(counts, key = lambda x: x[1], reverse = True)

        for item in cnts:
            if item[0] not in banned and item[0]!= "":
                return(item[0])