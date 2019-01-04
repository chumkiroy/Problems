'''
Balanced Partition

(This is an extension and generalization of SumZero problem)

Partition an array into two partitions, such that sum of two partitions is the same.
* Assume that the sum of all elements in the array is even. 
* Numbers can be positive or negative, viz non-zero integers
* Numbers can repeat.
* If there are multiple such partitions possible, then print any one.
* When you print, try to preserve the order of elements when you print them.

e.g. Input: 4, 1, -5, 6, -11, 3
	 Output: 4, 6, -11 and 1, -5, 3 (Both sum to -1)

NOTE:
https://leetcode.com/problems/partition-equal-subset-sum/

Solution (when elements are non-negative): http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/

Solution (when elements are non-zero): Generate every possible subsets and check.
'''

def findPartition(arr, n):
	sum = 0
	for i in range(n):
		sum += arr[i]
	if sum % 2 != 0:
		return False

	dp = [[False]*(n+1) for _ in range((sum/2)+1)]
	print n, dp
	'''
	for i in range(n+1):
		dp[0][i] = True
	for i in range(1,(sum/2)+1):
		dp[i][0] = False

	for i in range(1, (sum/2)+1):
		for j in range(1, n+1):
			dp[i][j] = dp[i][j-1]
			if i >= arr[j-1]:
				dp[i][j] = dp[i][j] or dp[i - arr[j-1]][j-1]

	## For printing the dp table
	for i in range((sum/2)+1):
		for j in range(n+1):
			print dp[i][j],
		print 

	return dp[sum/2][n]
	'''
	return 0
#arr = [3,1,1,2,2,1]
arr = [4, 1, -5, 6, -11, 3]
n = len(arr)
if findPartition(arr, n) == True:
	print "can be divided into two subsets of equal sum"
else:
	print "can not be divided into two subsets of equal sum"
