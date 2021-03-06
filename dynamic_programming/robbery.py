'''
Robbery

Problem Statement:
There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal value in these houses, but he cannot steal in two adjacent houses because the owner of a stolen house will tell his two neighbors on the left and right side. What is the maximal stolen value?

For example, if there are four houses with values [6, 1, 2, 7], the maximal stolen value is 13 when the first and fourth houses are stolen.

Input Format:
You will be given an array of integer values denoting the value in each house.

Output Format:
Return an integer denoting the maximum possible robbery.

Constraints:
	1 <= length(values) <= 10^5
	1 <= values[i] <= 10^4

Sample Test Case:

Sample Input-1:
steps = [1, 2, 4, 5, 1]

Sample Output-2:
7

Explanation-2:
Steal from the second and the fourth house.
'''

def maxStolenValue(values):
	n = len(values)
	if n == 0:
		return 0
	if n == 1:
		return values[0]
	if n == 2:
		return max(values[0], values[1])

	dp = [0] * n
	dp[0] = values[0]
	dp[1] = max(values[0], values[1])

	for i in range(2, n):
		dp[i] = max(values[i] + dp[i-2], dp[i-1])

	return dp[n-1]

values = [6, 1, 2, 7]
print maxStolenValue(values) ## Steal from the first and the last house.
