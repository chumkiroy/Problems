'''
Generate All Possible Expressions That Evaluate To The Given Target Value

Problem Statement:
------------------
You are given a string s, containing only numerical characters ('0' - '9'). You are also given a non-negative number target.

You have to put between each pair of numerical characters, one of ("", "*", "+") operators such that the expression you get will evaluate to the target value.

Putting "" (an empty string) operator between two numerical characters means, that the they are joined (e.g. 1""2 = 12). Also the join can be extended further (e.g. 1""2""3 = 123).

Precedence of the operators matters. In higher to lower precedence:

Join ("") > Multiplication ("*") > Addition ("+")

Input Format:
-------------
There are two arguments.
1) String s.
2) Long integer target. 

Output Format:
--------------
Return array of strings containing ALL possible strings that evaluate to the target value. 

You need not to worry about the order of strings in your output array. Like for s = "22" and target = 4, arrays ["2+2", "2*2"] and ["2*2", "2+2"] both will be accepted.  

Any string in the returned array should not contain any spaces. In the above example string "2+2" is expected, other strings containing any space like " 2+2", "2 + 2", "2 +2" etc. will give wrong answer. 

Constraints:
------------
1 <= |s| <= 13
s only contains numerical characters ('0' - '9').
0 <= target < 10^13
You have to return ALL possible strings that evaluate to target value.

Sample Test Cases:
------------------

Sample Input:
s = "222"
target = 24

Sample Output:
["22+2", "2+22"]

Explanation:
------------
1) 22 + 2 = 24 (Here, we put "" operator between the first two characters and then put "+" operator between the last two characters.)

2) 2 + 22 = 24 (Here, we put "+" operator between the first two characters and then put "" operator between the last two characters.)

'''

def generate_all_expressions(s, target):
    res = []
    dfs(res, s, '', 0, 0, target)
    return res
    
def dfs(res, remains, curr_str, curr, prev, target):
    if not remains:
        if curr == target:
            res.append(curr_str)
        return

    for i in range(1, len(remains)+1):
        #val = remains[:i]
        if len(curr_str) == 0:
            if not (i > 1 and remains[0]==0):
                dfs(res, remains[i:], remains[:i], int(remains[:i]), int(remains[:i]), target)
        else:
            if not (i>1 and remains[0]==0):
                dfs(res, remains[i:], curr_str+ '+' + remains[:i], curr + int(remains[:i]), int(remains[:i]), target)
                dfs(res, remains[i:], curr_str+ '*' + remains[:i], curr - prev + prev*int(remains[:i]), prev*int(remains[:i]), target)

s = "222"
target = 24

print generate_all_expressions(s, target)
