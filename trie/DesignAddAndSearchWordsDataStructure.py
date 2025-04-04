"""Design Add And Search Words Data Structure

Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true"""

class TrieNode:
    def __init__(self):
        self.children=[None] * 26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root= TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            index= ord(c)-ord("a")
            if cur.children[index]  is None:
                
                cur.children[index] = TrieNode()
            cur= cur.children[index]
        cur.endOfWord=True

    def search(self, word):
        def dfs(index, node):
            cur = node
            for i in range(index, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in cur.children:
                        if child and dfs(i + 1, child):  # Fix: Pass the TrieNode instead of index
                            return True
                    return False

                else:
                    idx = ord(c) - ord("a")  # Fix: Convert character to index
                    if cur.children[idx] is None:
                        return False
                    cur = cur.children[idx]  # Fix: Access the correct TrieNode

            return cur.endOfWord  # Fix: Return only after processing the whole word

        return dfs(0, self.root)  # Fix: Return the result of DFS call
wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
print(wordDictionary.search("say"))
print(wordDictionary.search("day"))
print(wordDictionary.search(".ay"))
print(wordDictionary.search("b.."))