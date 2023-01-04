def minimumRounds(tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        tasksDict = {}
        for task in tasks:
            if task not in tasksDict:
                tasksDict[task] = 1
            else:
                tasksDict[task] += 1
        
        total = 0
        for value in tasksDict.values():
            if value == 1:
                return -1

            if value%3 == 0:
                total += value/3
            else:
                total += value/3 + 1

        return total

if __name__ == "__main__":
    tasks = [1,1,1,1,1,1,1,1]
    print(minimumRounds(tasks))

