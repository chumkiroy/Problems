'''
Longest Substring With Exactly Two Distinct Characters

Problem Statement:
------------------
Given a string s of length n, find the length of the longest substring ss that contains exactly two distinct characters.

There are t test cases.

Input Format:
-------------
There is only one argument s, denoting input string.
s may contain upper case alphabets, lower case alphabets and numerical values.

Output Format:
--------------
Return an integer len, denoting length of longest substring as asked in problem
(If there are no such substrings, then return 0)

Constraints:
------------
1 <= t <= 1000
1 <= n <= 10^5

Sample Test Cases:
------------------
Sample Input 1:
2
eceba
abcdef

Sample Output 1:
3
2

Explanation 1:
In first case, 'ece' is the largest substring with exactly 2 distinct characters.
In second case, 'ab' is the largest substring with exactly 2 distinct characters. Also, 'bc', 'cd', 'de', 'ef' can be

considered as substring with exactly 2 distinct characters.


Sample Input 2:
3
ababababa
e
baabcbab

Sample Output 2:
9
0
4

Explanation 2:
In first case, whole string 'ababababa' is the largest substring with exactly 2 distinct characters.
In second case, there is no substring with exactly 2 distinct characters.
In third case, 'baab' is the largest substring with exactly 2 distinct characters.

'''

def unique(d):
    uni = 0
    for k in d:
        if d[k] != 0:
            uni += 1
    return uni

def  longestSub(strText):
    start = end = 0
    window_size = 1
    ans = ''
    d = {}
    
    for l in strText:
        if d.get(l, None) == None:
            d[l] = 1
        else:
            d[l] += 1
        end += 1
           
        if unique(d) == 2:
            tmp = strText[start: end]
            if len(tmp) > len(ans):
                ans = tmp
        while unique(d) > 2:
            d[strText[start]] -= 1
            start += 1
        
    return ans

string = "eceba" # "abcdef"
ans = longestSub(string)

print "longest substring = ", ans
print "length = ", len(ans)
