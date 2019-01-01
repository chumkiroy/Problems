'''
Problem statement: Find Order Of Characters From Alien Dictionary

Given a sorted dictionary of an alien language. You have to find the order of characters in that language.

Generally, dictionary does not contain duplicate values, but for the sake of this problem, assume that dictionary might have duplicate values. (Sometimes interviewer tricks the question, to see, how you will handle it.

Input Format:
-------------
There is only one argument, array of strings which denotes sorted dictionary of an alien language. 

Output Format:
--------------

Return a string denoting order of characters in the alien language.
Length of the output string will be the number of different characters present in input dictionary. 
For more clarity see the sample test cases.

Constraints:
------------

> 1 <= total number of characters in dictionary (not words) <= 10^5.
> Character in any word will be lower case alphabet letter.
> Input will be such that it is possible to determine the order uniquely. 

Sample Test Cases:

Sample Input1 : words = ["baa", "abcd", "abca", "cab", "cad"]
Sample Output1: "bdac"

Sample Input2 : words = ["caa", "aaa", "aab"]
Sample Output2: "cab"

Notes:

Here input is given such that it is possible to determine order uniquely. But in interview you should clarify these things with interviewer. Like if we are given words = ["z" "bc"] then we can only conclude that 'z' will come before 'b', but nothing about the order of 'c'!  
'''

import collections

def is_matching(word1, word2):
    i = 0
    j = 0
    while i < len(word1) and j < len(word2):
        if word1[i] != word2[j]:
            return word1[i], word2[j]
        i += 1
        j += 1
    return None, None

def create_graph(words):
    graph = collections.defaultdict(set)
    for i in range(1, len(words)):
        first, second = is_matching(words[i-1], words[i])
        if first != None and second != None:
            graph[first].add(second)
    return graph
    
def dfs(node, visited, graph,res):
    if node in visited:
        return
    visited.add(node)
    for child in graph.get(node, []):
        dfs(child, visited, graph, res)
    res.append(node)
    
def topological_sort(graph):
    visited = set()
    res = []
    for node in graph:
        if node in visited:
            continue
        dfs(node, visited, graph, res)
    return res[::-1]

def find_order(words):
    if not words:
        return ''
    if len(set(words)) == 1:
        return words[0][0]
        
    graph = create_graph(words)
    res = topological_sort(graph)
    return ''.join(res)

if __name__ == "__main__":
    words_cnt = 0
    words_cnt = int(input())
    words_i = 0
    words = []
    while words_i < words_cnt:
        try:
            words_item = str(input())
        except:
            words_item = None
        words.append(words_item)
        words_i += 1


    res = find_order(words);
	print res
