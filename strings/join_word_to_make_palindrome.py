'''
Join Words To Make A Palindrome

Problem Statement:
------------------
Given a list of strings words, of size n, check if there is any pair of words, that can be joined (in any order) to form a palindrome then return the pair of words forming palindrome.

Input Format:
-------------
Only argument for function, list of strings words.

Output Format:
--------------
Return a pair of words (i.e. list of string result of size 2 such that result[0] + result[1] is a palindrome).

In case of multiple answer return any one of them.

In case of no answer return list ["NOTFOUND", "DNUOFTON"].

Constraints:
------------
Length l for each word of words list, 1<= l <= 30.

Size of list words n, 2 <= n <= 20000.

Characters for each word can be from [a-z], [A-Z], [0-9].

Sample Test Case:
-----------------

Sample Input 1: words = [ "bat", "tab", "zebra" ]
Sample Output 1: result = [ "bat", "tab" ]

Explanation 1:
As "bat" + "tab" = "battab", which is a palindrome.


Sample Input 2: words = [ "ant", "dog", "monkey" ]
Sample Output 2: result = [ "NOTFOUND", "DNUOFTON" ]

Explanation 2:
As for each 6 combinations of string of words, there is no single generated word which is a palindrome hence result list will be [ "NOTFOUND", "DNUOFTON" ].

'''

def reverse_words_list(words):
    res = []
    for w in words:
        res.append(w[::-1])

    return res

def isPalindrome(s):
    if not s:
        return False
    i = 0
    j = len(s)-1
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1 
        j -= 1 
    return True

class Trie(object):
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.children = {}
            self.isWord = False
            self.idx = -1

    def __init__(self):
        self.root = self.Node(0)
        
    def insert(self, word, idx):
        cur = self.root
        
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                nNode = self.Node(c)
                cur.children[c] = nNode
                cur = nNode
        cur.isWord = True
        cur.idx = idx
        return
    
    def search(self, word):
        #pprint.pprint("Searching for {}".format(word))
        res = []
        cur = self.root
        
        for i in range(len(word)):
            c = word[i]
            
            if c not in cur.children:
                break
            cur = cur.children[c]
        
            if cur.isWord:
                res.append(cur.idx)
                
        if cur.isWord:
            #pprint.pprint("Found word and more")
            if isPalindrome(word[i:]):
                #pprint.pprint("Rest of the word {} is a palindrome".format(word[i:]))
                res.append(cur.idx)
        #pprint.pprint(res)
        return res


def join_words_to_make_a_palindrome(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    res =[]
    #Reverse words in list
    rev_words = reverse_words_list(words)

    FwdTrie = Trie()
    RevTrie = Trie()
    
    for i in range(len(words)):
        FwdTrie.insert(words[i], i)
    
    
    for i in range(len(rev_words)):
        RevTrie.insert(rev_words[i], i)
     
    # Look for pairs now
    #pprint.pprint("Looking for words in RevTrie")
    for i in range(len(words)):
        # Look for word in RevTrie
        rev_indices = RevTrie.search(words[i])
        #pprint.pprint(rev_indices)
        for j in rev_indices:
            if i !=j and (words[i],words[j]) not in res:
                res.append([words[i],words[j]])
                break
        if res:
            return res[0]

    for i in range(len(rev_words)):
        fwd_indices = FwdTrie.search(rev_words[i])
        for j in fwd_indices:
            if i !=j and (words[j],words[i]) not in res:
                res.append([words[j],words[i]])
                break
        if res:
            return res[0]
    
    if not res:
        res = [["NOTFOUND", "DNUOFTON"]]
        return res[0]

words = [ "bat", "tab", "zebra" ]
print join_words_to_make_a_palindrome(words)
