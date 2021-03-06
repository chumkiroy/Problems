'''
Reverse The Ordering Of Words In A String

Problem Statement: 
------------------
Given a string s containing a set of words, transform it such that the words appear in the reverse order. Words are separated only by one or more spaces. (See sample test cases for further clarifications.)

Input Format:
-------------
There is only one argument denoting string s.

Output Format:
--------------
Return a string containing your answer.

Constraints:
------------
1 <= |s| <= 10^5
s will contain characters only from lowercase alphabetical letters, uppercase alphabetical letters, space or punctuation marks.
More specifically s will be made from " .,?!':;-aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ". (s will be made from characters inside "".)
Punctuation mark is part of the word.
Usage of inbuilt string functions isn't allowed.
An in-place linear solution is expected.
For languages that have immutable strings, convert the input string into a Character Array and work in-place on that array. Convert it back to the string before returning. (For the purpose of this problem, ignore the extra linear space used in that conversion, as long as you're only using constant space after conversion to character array.)


Sample Test Cases:
------------------

Sample Input 1: "I will do it."
Sample Output 1: "it. do will I"

Sample Input 2: "  word1  word2 " 
(Note: there are 3 spaces in the beginning, 2 spaces between the words and 1 space at the end.)
Sample Output 2: " word2  word1   " 
(Note: there is 1 space in the beginning, 2 spaces between the words and 3 spaces at the end.)

Sample Input 3: "word1, word2;" 
Sample Output 3: "word2; word1,"

[This is a very old interview question, which Google used last year as one of their qualifier questions in Google CodeJam)

'''

def reverse_ordering_of_words(s):
    arr = s.split(' ')
    rev_str = ''
    for i in range(len(arr)-1,-1,-1):
        rev_str+=arr[i]+' '
    return rev_str[:-1]

print reverse_ordering_of_words("word1, word2;")
