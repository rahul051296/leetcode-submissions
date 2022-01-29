class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True
        
    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
            
        
        res = ''
        for word in words:
            if self.is_prefix(word, self.root):
                if len(word) > len(res):
                    res = word
                if len(word) == len(res):
                    res = min(res, word)
        return res
        
    def is_prefix(self, word, node):
        for c in word:
            node = node.children[c]
            if not node.end_of_word:
                return False
        return True
        