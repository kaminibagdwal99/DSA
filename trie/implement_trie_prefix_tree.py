"""A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) :
        cur= self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                new_node= TrieNode()

                cur.children[i]=new_node
            cur=cur.children[i]
        cur.isEndOfWord=True
        

    def search(self, word: str) :
        cur=self.root
        for c in word:
            i= ord(c)-ord("a")
            if cur.children[i]==None:
                return False
            cur=cur.children[i]
        return cur.isEndOfWord

        

    def startsWith(self, prefix: str) :

        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True

trie = PrefixTree()
trie.insert("apple")
print(trie.search("apple"))  
print(trie.search("app"))    
trie.startsWith("app")
trie.insert("app")
trie.search("app")  