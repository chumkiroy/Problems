'''
Find All Well Formed Brackets

Problem Statement:
------------------
Given positive integer n, find all well formed round brackets of length 2n.

Input Format:
-------------
There is only one argument denoting integer n.

Output Format:
-------------

Return array of strings containing all possible well formed round brackets of length 2n (Length of each string will be 2n). 

You need not to worry about the order of strings in your array. Like for n = 2, ["(())", "()()"] or ["()()", "(())"], both will be accepted.

Constraints:
------------
1 <= n <= 13
Only use round brackets. '(' and ')'.
Need to find ALL well formed brackets possible. 

Sample Test Case:
-----------------
Sample Input: 3
Sample Output:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''


def find_all_well_formed_brackets(n):
    res = []
    form_brackets(res, [], n, 0, 0)
    return res

def form_brackets(res, substring, n, openb, closeb):
    if closeb == n:
        res.append(''.join(substring))
        return
    else:
        if openb > closeb:
            form_brackets(res, substring+[')'], n, openb, closeb+1)
        if openb < n :
            form_brackets(res, substring+['('], n, openb+1, closeb)

print find_all_well_formed_brackets(3)
