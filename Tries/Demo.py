class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, words):
        node = self.root
        for c in words:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.end = True

    def search(self, words):
        node = self.root
        
        for c in words:
            if c not in node.children:
                return False
            node = node.children[c]
        
        # If there exists other letters
        return node.end
    
    def startswith(self, words):
        node = self.root
        prefix = ""
        for c in words:
            if c not in node.children:
                break
            node = node.children[c]
            prefix = prefix + "" + c
        return prefix

root = Trie()
words = ['flower','flow','flight']
root.insert(words[0])
root.insert(words[1])
print(root.search(words[0]))

import sys
sys.exit()
for w in words[1:]:
    print(root.startswith(w))


