'''
Count ways to reach the Nth stair

Problem Statement:
There are n stairs, a person standing at the bottom wants to reach the top. He can climb a certain number of steps together. For instance, the person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
Note: Solve the problem for general case i.e. for n stairs, and different kinds of steps that can be taken (e.g. instead of only 1 or 2 steps, it could be 2, 3 and 5 steps at a time)
 
Input Format:
You will be given an array of integer steps denoting the steps the person can climb.
You will be given one integer n, denoting the number of stairs.
	All steps will be unique. There are no duplicate entries.
Note: Answer is guaranteed to fit in long integer. 
Output Format:
Return an integer denoting the number of ways to reach the last staircase.
 
Constraints:
1 <= n <= 100
1 <= steps <= 10000

Sample Test Case:

Sample Input-1:
	n = 1
	steps = [1, 2]
Sample Output-1:
	1

Explanation-1:
	Only one way to reach = [{1}]

Sample Input-2:
	n = 2
	steps = [1, 2]
Sample Output-2:
	2
Explanation-2:
	Two ways to reach = [{1, 1}, {2}]

'''
def countWaysToReachNthStair(steps, n):
	dp = [0]*(n+1)
	dp[0] = 1

	for i in range(1, n+1):
		for step in steps:
			prev_step = i - step
			if prev_step >= 0:
				dp[i] += dp[prev_step]

	return dp[n]

steps = [1,2]
n = 2
print countWaysToReachNthStair(steps, n)
