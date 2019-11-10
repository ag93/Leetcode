class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = {}
        for item in items:
            if item[0] in scores:
                scores[item[0]].append(item[1])
            else:
                scores[item[0]] = [item[1],]


        result = []        
        for student in scores:
            result.append([student, sum(list(sorted(scores[student], reverse = True))[:5])//5])
            
        return result