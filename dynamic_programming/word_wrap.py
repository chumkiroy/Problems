'''
Word Wrap

Given a sequence of words, and a limit on the number of characters that can be put in one line (line width). Put line breaks in the given sequence such that the lines are printed neatly. Assume that the length of each word is smaller than the line width.

The word processors like MS Word do task of placing line breaks. The idea is to have balanced lines. In other words, not have few lines with lots of extra spaces and some lines with small amount of extra spaces.

The extra spaces includes spaces put at the end of every line.  
The problem is to minimize the following total cost.

 Cost of a line = (Number of extra spaces in the line)^3
 Total Cost = Sum of costs for all lines
Please note that the total cost function is not sum of extra spaces, but sum of cubes of extra spaces. The idea behind this cost function is to balance the spaces among lines. For example, consider the following two arrangement of same set of words:

1) There are 3 lines. One line has 3 extra spaces and all other lines have 0 extra spaces. Total extra spaces = 3 + 0 + 0 = 3. Total cost = 3*3*3 + 0*0*0 + 0*0*0 = 27.

2) There are 3 lines. Each of the 3 lines has one extra space. Total extra spaces = 1 + 1 + 1 = 3. Total cost = 1*1*1 + 1*1*1 + 1*1*1 = 3.

Total extra spaces are 3 in both scenarios, but second arrangement should be preferred because extra spaces are balanced in all three lines. The cost function with cubic sum serves the purpose because the value of total cost in second scenario is less.

Note:
Problem and Solution: http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/ [The problem statement here is a bit flawed, but the code and explanation is resonable]

(Variation: https://leetcode.com/problems/text-justification/)

LeetCode is the greedy approach used in old MS word and DP one with cubic badness is used in Latex.

'''

# A Dynamic programming solution for Word Wrap Problem
# A utility function to print the solution
# l[] represents lengths of different words in input sequence. For example,
# l[] = {3, 2, 2, 5} is for a sentence like aaa bb cc ddddd. n is size of
# l[] and M is line width (maximum no. of characters that can fit in a line)

INF = 2147483647

def printSolution(p, n):
	k = 0
	if p[n] == 1:
		k = 1
	else:
		k = printSolution(p, p[n] - 1) + 1
	print 'Line number ', k, ': From word no. ',p[n], 'to ', n
	return k

def solveWordWrap (l, n, M):
	# For simplicity, 1 extra space is used in all below arrays
	# extras[i][j] will have number of extra spaces if words from i to j are put in a single line
	extras = [[0 for i in range(n + 1)] for i in range(n + 1)]

	# lc[i][j] will have cost of a line which has words from i to j
	lc = [[0 for i in range(n + 1)] for i in range(n + 1)]

	# c[i] will have total cost of optimal arrangement of words from 1 to i
	c = [0 for i in range(n + 1)]

	# p[] is used to print the solution.
	p = [0 for i in range(n + 1)]

	# calculate extra spaces in a single line. The value extra[i][j] indicates
	# extra spaces if words from word number i to j are placed in a single line
	for i in range(n + 1):
		extras[i][i] = M - l[i - 1]
		for j in range(i + 1, n + 1):
			extras[i][j] = (extras[i][j - 1] - l[j - 1] - 1)

	# Calculate line cost corresponding to the above calculated extra
	# spaces. The value lc[i][j] indicates cost of putting words from word number
	# i to j in a single line
	for i in range(n + 1):
		for j in range(i, n + 1):
			if extras[i][j] < 0: lc[i][j] = INF; 
			elif j == n and extras[i][j] >= 0:
				lc[i][j] = 0
			else:
				lc[i][j] = (extras[i][j] * extras[i][j])

	# Calculate minimum cost and find minimum cost arrangement. The value
	# c[j] indicates optimized cost to arrange words from word number 1 to j.
	c[0] = 0
	for j in range(1, n + 1):
		c[j] = INF
	for i in range(1, j + 1):
		if (c[i - 1] != INF and lc[i][j] != INF and ((c[i - 1] + lc[i][j]) < c[j])):
			c[j] = c[i-1] + lc[i][j]
			p[j] = i
	printSolution(p, n) 
			
# Driver Code 
l = [3, 2, 2, 5] 
n = len(l) 
M = 6 
solveWordWrap(l, n, M) 
