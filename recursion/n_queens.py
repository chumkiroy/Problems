'''
n Queen Problem
----------------

Problem Statement:
------------------
The n queen problem is the problem of placing n chess queens on an n * n chessboard, so that no two queens attack each other.

Your task is to find ALL possible arrangements for the n queen problem.

You have to solve this problem using recursion. (There may be other ways of solving this problem, but for the purpose of this exercise, please use recursion only).

A queen can move horizontally, vertically, or diagonally.

Input Format:
-------------
There is only one argument denoting integer n.

Output Format:
--------------
Return 2-D string array of size, number of solutions * n, where length of each string is n. 

Any character in string should contain one of 'q' or '-'. Character 'q' means queen is present and character '-' means it is empty. 

(To be more clear about the output, look at the sample test case.)

Constraints:
-----------
1 <= n <= 13

Sample Test Case:
-----------------
Sample Input: 4
Sample Output:
Suppose name of the returned array is ret.
ret [0] = 
[ 
"--q-",
"q---",
"---q",
"-q--"
]

ret [1] = 
[
"-q--",
"---q",
"q---",
"--q-"
]

Explanation:
There are 2 possible solutions for 4 queen problem, hence size of ret is 2 * 4, and length of each string is 4.

ret [i] will denote ith arrangement. 
ret [i][j] will denote jth row of ith arrangement.
ret [i][j][k] will denote kth character (if it is a queen or empty cell) of jth row in ith arrangement. 

ret [0] = 
[
"-q--",
"---q",
"q---",
"--q-"
]

ret [1] = 
[ 
"--q-",
"q---",
"---q",
"-q--"
]

will also be considered as a valid answer.
'''

def find_all_arrangements(n):
    position = [i for i in range(n)]
    out = []
    nQueens(n, 0, position, out)
    #print(out)
    return nQueens_output(out)
    
def nQueens_output(out):
    output = []
    for arr in out:
        out_arr = [['-'] * len(arr) for _ in range(len(arr))]
        for r, c in enumerate(arr):
            out_arr[r][c] = 'q'
        output.append([''.join(row) for row in out_arr])
    return output

def nQueens(n, start, position, out):
    if start == n:
        out.append([x for x in position])
        return
    
    for i in range(start, n):
        swap(position, start, i)
        if is_position_valid(position, start):
            nQueens(n, start+1, position, out)
        swap(position, start, i)

def is_position_valid(position, start):
    r1 = start
    c1 = position[start]
    
    for r2, c2 in enumerate(position[:start]):
        if abs(r1-r2) == abs(c1-c2):
            return False
    return True
    
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

print find_all_arrangements(4)
