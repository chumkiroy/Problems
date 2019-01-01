'''
Problem Statement: String Transformation Using Given Dictionary Of Words

You are given a dictionary of words and two strings named start and stop.

How can you convert string start to string stop, by changing only one character at a time and making sure that 1) all the intermediate words are in the given dictionary of words and 2) minimum number of intermediate words are used?

Generally, dictionary does not contain duplicate values, but for the sake of this problem, assume that dictionary might have duplicate values. (Sometimes interviewer tricks the question, to see, how you will handle it.)

Input Format:
-------------
There are three arguments. First is an array of strings denoting the dictionary of words, second is a string start and third is a string stop.

Output Format:
--------------
Return an array of strings.

If transformation is possible then in returned array, first string should be start, last string should be stop and in between strings of given dictionary that you used for transformation, in the same order they are used in your transformation. Suppose name of the returned array is ans and size is ans_size, then for 1 <= i < ans_size, ans[i - 1] and ans[i] should differ at exactly one position.

If transformation is not possible then returned array should contain only one string "-1".

(If there are multiple valid transformations, you are free to return any one of them.)

Constraints:
------------
- Input strings contain only lower case alphabetical letters.
- Length of input strings are same.
- Input strings need not to be unique.
- 2 <= total number of characters in input strings <= 10^5
- start and stop strings need not to be present in given dictionary. 

Sample Test Case:
-----------------
Sample Input: words = ["cat", "hat", "bad", "had"]
			  start = "bat"
			  stop = "had"

Sample Output: ["bat", "bad", "had"] or "bat", "hat", "had"]

Explanation:
From "bat" change character 't' to 'd', so new string will be "bad".
From "bad" change character 'b' to 'h', so new string will be "had".
or
From "bat" change character 'b' to 'h', so new string will be "hat".
From "hat" change character 't' to 'd', so new string will be "had".

'''

from collections import deque

def get_neighbour(string, words):
    res = []
    if len(words) > 26:
        for char in 'abcdefghijklmnopqrstuvwxyz':
            for i in range(len(string)):
                new_string = string[:i] + char + string[i+1:]
                if new_string in words:
                    res.append(new_string)
    else:
        for word in words:
            diff = 0
            for i in range(len(string)):
                if word[i] != string[i]:
                    diff += 1
                if diff > 1: 
                    break
            if diff == 1:
                res.append(word)
    
    return res

def string_transformation(words, start, stop):
    #print(words)
    #print(start)
    #print(stop)
    words = set(words)
    words.add(stop)
    visited = set()
    parent = {start: None}
    found = False
    que = deque([start])

    while que:
        cur_word = que.popleft()
        for neighbour in get_neighbour(cur_word, words):
            #print('-',neighbour)
            if neighbour == stop:
                found = True
                parent[neighbour] = cur_word
                break
            if neighbour not in visited:
                visited.add(neighbour)
                que.append(neighbour)
                parent[neighbour] = cur_word
            if found:
                break
            
    end = parent.get(stop)
    #print('parent', parent)
    if not end:
        return ['-1']
    path = [stop]
    while end:
        path.append(end)
        if end == start:
            break
        end = parent[end]
    #print('output')  
    return path[::-1] if path else ['-1']

words = ["cat", "hat", "bad", "had"]
start = 'bat'
stop = 'had'
print string_transformation(words, start, stop)
