'''
problem statement: Boggle Solver

This is an age-old question, which leads to some excellent discussions in an interview. Here, you're essentially comparing one set of strings to another set of strings. As you try to solve it, you'll go thru various approaches e.g. hashing the strings, sorting and binary search, tries, recursion (DFS), and even BFS:

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell. Get all possible such words and return them.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ

Test cases: If your test cases fail, then check why they failed. If it's simply because of the ordering of printed words, then it's okay.

Note:
https://leetcode.com/problems/word-search-ii/

This is easy to understand, but is inefficient compared to using a Trie: http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/

This uses a Trie: http://stackoverflow.com/a/746102/327310 (This is what is expected in an interview)

This explanation come up often in Google searches, but is NOT optimal: http://exceptional-code.blogspot.com/2012/02/solving-boggle-game-recursion-prefix.html [The author claims to be doing DP, but it's essentially just BFS, and that too is not implemented completely. Plus, it is not faster than a Trie-based solution when it comes to even slightly larger board sizes. Stick to Tries and DFS for an optimal solution, but clearly understand why other solutions won't be optimal]

'''

class TrieNode(object):
    def __init__(self, data = None):
        self.children = {}
        self.end_of_word = False
        self.word = data

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
   
    def add(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.end_of_word = True
        current_node.word = word

    def find_word(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True

    def search(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        if current_node.word == word:
            return True
        return False

def dfs(boggle, visited, string, i, j, trie, res):
    m = len(boggle)
    n = len(boggle[0])

    if i<0 or j<0 or i>=m or j>=n:
        return

    if visited[i][j]:
        return

    string = string + boggle[i][j]

    if not trie.starts_with(string):
        return

    if trie.search(string):
        res.append(string)

    visited[i][j] = True

    neighbours = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    for a,b in neighbours:
        dfs(boggle, visited, string, i+a, j+b, trie, res)
    visited[i][j] = False

def find_words(boggle, words):
    res = []
    trie = Trie()
    for word in words:
        trie.add(word)

    m = len(boggle)
    n = len(boggle[0])
   
    visited = [[False]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            dfs(boggle, visited, '', i, j, trie, res)

    return res

dict = ["GEEKS", "FOR", "QUIZ", "GO"]
boggle = [['G','I','Z'],
          ['U','E','K'],
          ['Q','S','E']]
print find_words(boggle, dict)

