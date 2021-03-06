'''
Indices Of Words In Text String

Problem Statement:
------------------
You are given a text string and q words. For all q words, You need to find out all words from text string which are matching with given word.

Input Format:
-------------
Two arguments. First is text string and second is list of words.

Output Format:
--------------
Return List of q lists, where ith list contains indices of first character of all the matching words in text string, for words[i], in sorted order.

If no word found in text string for given word then have -1 as only element of answer list for that word.

Constraints:
------------
Text string and words of query can contain characters from a-z, A-Z, 0-9 and symbols from set {'$', '#', '@', '?' ,';'}. Additionally text string can contain spaces also.
Assume words in text string are single space separated. text string starts and ends with a word, not space(s). There will be no consecutive spaces in text string.
1 <= len(text) <= 1000000.
1<= q <= 100000.
Length of any word of query and text string l, 1<= l <= 10.
Every query word will be unique.
Consider indexing of character in text string from 0.
Returned list of indices must be sorted in increasing order.

Sample Test Case:
-----------------
Sample Input: 
text = "you are very very smart"
words = ["you", "are", "very", "handsome"]

Sample Output:
[
[0],
[4],
[8, 13],
[-1]
]

Explanation:
For given text string = "you are very very smart". "you" is matching with first word "you" which is starting from index 0 of text string so answer for "you" will be 0.

Similarly for "are" answer is 4.

"very" is matching with word at index 8 and 13 so answer for "very" will be 8 and 13.

"handsome" is not matching with any word so its answer is -1;

'''

def find_words(text, words):
    map1 = {}
    split_text = text.split(" ")
    i=0
    for word in split_text:
        if word in map1:
            map1[word].append(i)
        else:
            map1[word] = [i]
        i+=len(word)+1
    
    res=[]
    for word in words:
        if word in map1:
            res.append(map1[word])
        else:
            res.append([-1])
    return res

text = "you are very very smart"
words = ["you", "are", "very", "handsome"]
print find_words(text, words)
