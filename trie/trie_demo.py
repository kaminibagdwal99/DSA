# https://www.geeksforgeeks.org/trie-insert-and-search/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):
        curr = self.root

        for c in key:
            index = ord(c)-ord("a")
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr= curr.children[index]
        curr.isEndOfWord = True

    def search(self,key):
        curr= self.root
        for c in key:
            index = ord(c)-ord("a")
            if curr.children[index] is None:
                return False
            curr= curr.children[index]
        return curr.isEndOfWord
    
    def prefix(self, key):
        curr= self.root
        for c in key:
            i = ord(c)-ord("a")
            if curr.children[i] is None:
                return False
            curr= curr.children[i]
        return True


trie = Trie()
arr = ["and", "ant", "do", "dad"]
for s in arr:
    trie.insert(s)


searchKeys = ["do", "gee", "bat"]
for s in searchKeys:
    if trie.search(s):
        print("true", end= " ")
    else:
        print("false", end=" ")


print()
prefixKeys = ["ge", "ba", "do", "de"]
for s in prefixKeys:
    if trie.prefix(s):
        print("true", end = " ")
    else:
        print("false", end = " ")

