# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    # Recursively compute the depth of nested lists
    def calcDepth(self, nestedList, depth):
        
        # Base case required for a lone integer
        if nestedList.isInteger():
            return nestedList.getInteger()
        
        deep_sum = 0
        base_sum = 0
        
        # For each list in the nested list
        for nest in nestedList.getList():
            
            # If nest is an integer, add the integer to the base sum, else,
            # add the recursively computed value to the deep sum
            if nest.isInteger():
                base_sum += nest.getInteger()
            else:
                deep_sum += self.calcDepth(nest, depth+1)

        # Deep sum already has depth factored in, so add the base sum * depth + depth sum
        return base_sum*depth + deep_sum
        
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
    
        # Return the sum of items in the list
        return sum(self.calcDepth(nest, 2) for nest in nestedList)