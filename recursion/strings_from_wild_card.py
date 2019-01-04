'''
Strings From Wild Card


Problem Statement:
------------------
You are given string s of length n, having m wildcard characters '?', where each wildcard character represent

a single character. Write a program which returns list of all possible distinct strings that can be generated by replacing each wildcard characters in s with either '0' or '1'.

Any string in returned list must not contain '?' character i.e. you have to replace all '?' with either '0' or '1'.

Input Format:
-------------
There is only one argument s, denoting input string.

Output Format:
--------------
Return a result list of distinct strings (No fix order of strings in result list is required).

Constraints:
------------
1 <= n <= 50, where n is length of s.
0 <= m <= 17, where m is number of '?' (wildcard characters) in s.

Sample Test Cases:

Sample Test Case 1:
Sample Input 1: s = "1?10"
Sample Output 1: result = ["1010", "1110"] or ["1110", "1010"].

Explanation 1:

'?' at index 1 (0 based indexing) can be replaced with either '0' or '1'. So, generated two strings replacing '?' with '0' and '1'

Sample Test Case 2:

Sample Input 2:
s = "1?0?"

Sample Output 2:
result = ["1000", "1001", "1100", "1101"] or any other list having same strings but in different order.

Explanation 2:
Input string have two '?' characters. Each one can be replaced with either '0' or '1'. So, total 2*2 strings are possible as ('?' at index 1, '?' at index 3) can be replaced with ('0','0'), ('0','1'), ('1', '0'), ('1', '1').

'''

def find_all_possibilities(s):
    n = len(s)
    return helper(s,n,0)
    
def helper(s,n,i):
    if i ==n:
        return [""]
    else:
        res=[]
        lst = helper(s,n,i+1)
        if s[i] == "?":
            for k in lst:
                res.append("0"+k)
                res.append("1"+k)
        else:
            for k in lst:
                res.append(s[i]+k)
        return res

print find_all_possibilities("1?10")
