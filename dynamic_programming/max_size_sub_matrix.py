'''
Largest sub-square matrix with all 1s

Problem Statement:
This problem is yet to be reviewed, hence might contain minor typos, but still good enough to start practicing!

Given a 2D matrix mat of integers with n rows and m columns. All the elements in the matrix mat are either 0 or 1. Your task is to determine the largest sub-square size of the matrix that contains only 1s.

Input Format:
First and second parameter of the largest_sub_square_matrix function, is n and m, depicting the number of rows and columns in the matrix. The third and last parameter of the function is the 2D matrix mat.

Output Format:
Return an integer denoting the largest size of sub-square matrix that contains only 1s in the input 2D matrix.

Constraints:
1 <= n,m <= 1000
0 <= elements in matrix <= 1

Sample Test Case:

Sample Input:
mat = [ [1,0,0] , [0,1,1] , [0,1,1] ]
n = 3
m = 3

Sample Output:
2

Explanation:
The given matrix is represented below:
1 0 0
0 1 1
0 1 1
Here, we can easily infer that the 1s in bold form a sub-square matrix and is of the largest size(2*2) in the matrix such that all the elements in the sub-matrix are 1. Hence, the answer is 2.

'''

'''
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
Given this matrix:
   0  1  1  0  1 
   1  1  0  1  0 
   0  1  1  1  0
   1  1  1  1  0
   1  1  1  1  1
   0  0  0  0  0
The maximum square sub-matrix with all set bits is
    1  1  1
    1  1  1
    1  1  1
Please hard-code your test-cases. That will give you more flexibility in input and output. For the output for example, you can either print the matrix, or simply return the top left and bottom corner index values - your choice.

(It's debatable whether the solution to this problem can strictly be categorized as a DP solution. Nevertheless, this is an important problem to solve and it's challenging!)

Ref: http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
'''

def get_sub_matrix(m):
	r = len(m)
	c = len(m[0])

	dp = [[0] * c for _ in range(r)]
	max_val = 0
	max_r = 0
	max_c = 0

	for i in range(c):
		dp[0][i] = m[0][i]

	for i in range(r):
		dp[i][0] = m[i][0]

	for i in range(1,r):
		for j in range(1,c):
			if m[i][j] == 1:
				dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
				if max_val < dp[i][j]:
					max_val = dp[i][j]
					max_r = i
					max_c = j
			else:
				dp[i][j] = 0
	print max_val, 'r=', max_r, 'c=', max_c

	'''
	for i in range(max_i, max_i - max_of_s, -1): 
        for j in range(max_j, max_j - max_of_s, -1): 
            print (M[i][j]
	'''
	for i in range(max_r-max_val+1, max_r+1):
		for j in range(max_c-max_val+1, max_c+1):
			print m[i][j], ' ',
		print
	return dp

m = [[0,1,1,0,1],[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,0],[1,1,1,1,1],[0,0,0,0,0]]
get_sub_matrix(m)
