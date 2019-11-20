# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:28:27 2019

@author: anike
"""
import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = collections.defaultdict(int)
        
class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.prefix = ""
        self.root = TrieNode()
        for i in range(len(sentences)):
            self.add(sentences[i], times[i])

    
    def add(self, str_, times):
        node = self.root
        for char in str_:
            
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            node.count[str_] += times

    def input(self, c: str):
        if c == "#":
            self.add(self.prefix, 1)
            self.prefix = ""
            return []
        self.prefix += c
        node = self.root
        for w in self.prefix:
            if w not in node.children:
                return []
            node = node.children[w]
            print(node.count)
        # Negate the count so python sorts it in ASC order
        res = sorted([(-v, k) for (k, v) in node.count.items()])
        return [item[1] for item in res[:3]]


sentences = ["i love you", "island","ironman", "i love leetcode"]
times = [5,3,2,2,]
c = "i lo"

obj = AutocompleteSystem(sentences, times)
param_1 = obj.input(c)
print(param_1)