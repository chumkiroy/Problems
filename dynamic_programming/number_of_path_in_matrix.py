'''
Problem statement: numbers of path in a matrix

Consider a maze mapped to a matrix with an upper left corner at coordinates (row, column) = (0, 0). Any movement must be in increasing row or column direction. You must determine the number of distinct paths through the maze. You will always start at position (0, 0), the top left, and end up at (max(row), max(column)), the bottom right.

As an example, consider the following diagram where '1' indicates an open cell and '0' indicates blocked. You can only travel through open cells, so no path can go through the cell at (0, 2). There are two distinct paths to the goal.
<>
There are two possible paths from cell (0, 0) to cell (1, 3) in this matrix.


Function Description

Complete the function numberOfPaths in the editor below. The function must return the number of paths through the matrix, modulo (10^9 + 7).

[By doing a modulo, we get around overflow. By doing it with a prime number, we maximize chances of uniform distribution of remainders. By doing it with a large prime like 10^9 + 7, we minimize chances of repeats altogether]


numberOfPaths has the following parameter(s):

2D array of integers a.


Constraints

1 <= n, m <= 1000
Each cell in matrix a contains either a 0 or a 1.
 

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the number of rows in matrix a.

The next line contains an integer m, the number of columns in matrix a.

The next n lines each contain space separated m integer values, for row a[i] where 0 <= i < n.



Sample Case 0

Sample Input 0

3
4
1 1 1 1
1 1 1 1
1 1 1 1
Sample Output 0

10
Explanation 0

There are 10 possible paths from cell (0, 0) to cell (2, 3).


Sample Case 1

Sample Input 1

2
2
1 1
0 1
Sample Output 1

1
Explanation 1

Sample Case 0

There is 1 possible path from cell (0, 0) to cell (1, 1).

'''

def numberOfPaths(a):
    if not a or len(a) == 0:
        return 0
        
    m = len(a)
    n = len(a[0])
    
    if a[0][0] == 0 or a[m-1][n-1] == 0:
        return 0
        
    dp = [ [0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for i in range(1, m):
        if a[i][0] == 1:
            dp[i][0] = dp[i-1][0]
            
    for i in range(1, n):
        if a[0][i] == 1:
            dp[0][i] = dp[0][i-1]
            
    for i in range(1,m):
        for j in range(1,n):
            if a[i][j] == 1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1]

a = [[1,1,1,1], [1,1,1,1], [1,1,1,1]]
print numberOfPaths(a)
