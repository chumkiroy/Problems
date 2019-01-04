'''
Palindromic Decomposition Of A String


Problem Statement:
-------------------
A palindromic decomposition of string is a decomposition of the string into sub-strings, such that all those sub-strings are valid palindromes.

Given a string s, you have to find ALL possible palindromic decompositions of it.

Input Format:
-------------
There is only one argument denoting string s.

Output Format:
--------------
Return array of string containing ALL possible palindromic decompositions of given string. 

To differentiate sub-strings in the decomposed string add '|' between them. (Look at the sample test cases for more clarity.)

You need not to worry about the order of strings in your output array. Like for s = "aa", arrays ["a|a", "aa"] and ["aa", "a|a"] both will be accepted. (Also note that string itself is also a sub-string.)

Any string in the returned array should not contain any spaces. e.g. s = "ab" then ["a|b"] is expected, ["a |b"] or ["a| b"] or ["a | b"] will give wrong answer.

Constraints:
------------
- 1 <= |s| <= 20
- s only contains lowercase letters ('a' - 'z').
- You have to return ALL possible palindromic decompositions.
- In any string in your returned array, order of characters should remain same as in given string. (i.e. for s = "ab" you should return ["a|b"] and not ["b|a"].)

Sample Test Cases:
------------------
Sample Input: "abracadabra"

Sample Output:
[
    "a|b|r|a|c|a|d|a|b|r|a",
    "a|b|r|a|c|ada|b|r|a",
    "a|b|r|aca|d|a|b|r|a"
]

'''

def generate_palindromic_decompositions(s):
    res = []
    helper(s,0,'',res)
    return res
    
def helper(s,i,d,res):
    if i==len(s)-1:
        print(d+s[i])
        #res.append(d+s[i])
        return
    if i>len(s)-1:
        print(d[:-1])
        #res.append(d[:-1])
        return
    for x in range(i+1,len(s)+1): 
        if isPalindrome(s[i:x]):
            helper(s,x,d+s[i:x]+'|',res)
    #print(x)
    
    
def isPalindrome(a):
    i=0
    j=len(a)-1
    while (j>=i):
        if a[i]!=a[j]:
            return False
        i+=1
        j-=1
    return True

string = "abracadabra"
print generate_palindromic_decompositions(string)
