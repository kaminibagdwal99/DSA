class TrieNode:
    def __init__(self):
        self.chidren = [None]*26
        self.eof = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, key):
        curr= self.root
        for c in key:
            i = ord(c)- ord("a")
            if curr.chidren[i] is None:
                curr.chidren[i]= TrieNode()
            curr=curr.chidren[i]
        curr.eof =True

    def search(self, key):
        def dfs(index, node):
            curr= node
            for i  in range(index, len(key)):
                c = key[i]
                if c ==".":
                    for child in curr.chidren:
                        if child and dfs(i+1, child):
                            return True
                    return False
                else:

            
                    idx = ord(c)-ord("a")
                    if curr.chidren[idx] is None:
                        return False
                    curr = curr.chidren[idx]
            return curr.eof
        return dfs(0,self.root)
    
    




wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
print(wordDictionary.search("say"))
print(wordDictionary.search("day"))
print(wordDictionary.search(".ay"))
print(wordDictionary.search("b..")) 