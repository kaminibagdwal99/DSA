class Node:
    def __init__(self):
        self.children =[None]*26
        self.eof=False

class PrefixTree:
    def __init__(self):
        self.root=Node()

    def insert(self, word):
        cur=self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                cur.children[i]= Node()
            cur=cur.children[i]
        cur.eof=True

    def startsWith(self, word):
        cur=self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                return False
            cur=cur.children[i]
        return True

    def search(self, word):
        cur=self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                return False
            cur=cur.children[i]
        return cur.eof

    

trie = PrefixTree()
trie.insert("apple")
print(trie.search("apple"))  
print(trie.search("app"))    
trie.startsWith("app")
trie.insert("app")
trie.search("app")  