class Node:
    def __init__(self):
        self.children= [None]*26
        self.eof = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        cur = self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                cur.children[i] =Node()
            cur = cur.children[i]
        cur.eof = True

    def search(self, word):
        def dfs(index, node):
            cur = node
            for i in range(index, len(word)):
                c= word[i]
                if c==".":
                    for child in cur.children:
                        if child and dfs(i+1, child):
                            return True
                    return False
                else:
                    idx = ord(c)-ord("a")
                    if cur.children[idx] is None:
                        return False
                    cur = cur.children[idx]
            return cur.eof 
        return dfs(0, self.root)
            



wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
print(wordDictionary.search("say"))
print(wordDictionary.search("day"))
print(wordDictionary.search(".ay"))
print(wordDictionary.search("b.."))