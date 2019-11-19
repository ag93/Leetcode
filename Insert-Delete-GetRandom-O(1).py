from random import choice
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_map = {}
        self.array_list = []
        self.len_list = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            return False
        
        self.index_map[val] = self.len_list
        self.len_list += 1
        self.array_list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            idx = self.index_map[val]
            last = self.array_list[-1]
            self.array_list[idx], self.index_map[last] = last, idx
            self.array_list.pop()
            del self.index_map[val]
            self.len_list -= 1
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.array_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()