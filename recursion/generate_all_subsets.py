'''
Generate All Subsets Of A Set
-----------------------------

Problem Statement:
------------------
Given a set (string s containing only distinct lowercase letters ('a' - 'z')), you have to generate ALL possible subsets of it . 

Note that empty set is always a subset of any set.

Input Format:
-------------
There is only one argument denoting string s.

Output Format:
--------------
Return array of strings containing ALL possible subsets of given string.

You need not to worry about order of strings in your output array. Like for s = "a", arrays ["", "a"] and ["a", ""] both will be accepted.

Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted. 

Constraints:
------------
0 <= |s| <= 20
s only contains distinct lowercase alphabetical letters ('a' - 'z').
You have to return ALL possible subsets. 

Sample Test Cases:
------------------
Sample Input: "xy" 
Sample Output: ["", "x", "y", "xy"] 

'''

def generate_all_subsets(s):
    n = len(s)
    out = [''] * n
    res = []
    generate_subset(s, 0, out, 0, res)
    return res
    #print(len(res))
    #for l in res:
    #    print(''.join(l))
    
def generate_subset(s, i, out, j, res):
    n = len(s)
    if i == n:
        #print(to_string)
        #print(out[:j])
        res += [''.join(out[:j])]
        return
    generate_subset(s, i+1, out, j, res)
    out[j] = s[i]
    generate_subset(s, i+1, out, j+1, res)

print generate_all_subsets("xy")
