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
