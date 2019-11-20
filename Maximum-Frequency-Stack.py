import collections
class FreqStack(object):

    def __init__(self):
        self.group = collections.defaultdict(list)
        self.freq = collections.Counter()
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        f = self.freq[x] + 1
        self.freq[x] = f
        if f>self.max_freq:
            self.max_freq = f
            
        self.group[f].append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -=1
            
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()