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
