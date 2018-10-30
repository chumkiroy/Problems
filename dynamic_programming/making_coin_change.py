'''
Problem Statement:
You are given n types of coin denominations of values v(1) < v(2) < ... < v(n) (all integers). Give an algorithm which makes change for an amount of money C with as few coins as possible. 
* Assume there are multiple coins of every denomination. 
* Assume v(1) = 1, (i.e. there is always a combination that leads to C).
* There may be multiple ways of reaching C. We want a solution that leads to the method using least number of coins.
* Input: C and Denominations Array

In order to solve the problem you should try to:
1. Find the minimum number of coins needed (a correct, but inefficient recursive solution).
2. Optimize the solution with DP or caching.
3. Adjust the solution of part 2 so that instead of finding the minimum number of coins, find which coins those are.
4. Adjust the solution of part 3 to output all such combinations. (Hint: You'll need to do recursion on the DP table.)

REF:
Solution with explanation: https://discuss.leetcode.com/topic/35720/easy-to-understand-recursive-dp-solution-using-java-with-explanations

More efficient solution  : https://discuss.leetcode.com/topic/32475/c-o-n-amount-time-o-amount-space-dp-solution/4
'''

def coinChange(amount, denominations):
	def dfs(amt, so_far, indx):
		if amt == 0:
			out.append(so_far[:])
			return

		for i in range(indx, len(denominations)):
			coin = denominations[i]
			if amt >= coin and dp[amt] == 1 + dp[amt - coin]:
				so_far.append(coin)
				dfs(amt-coin, so_far, i)
				so_far.pop()

	dp = [0] + [float('inf')] * amount
	for i in range(1, amount+1):
		for coin in denominations:
			if i >= coin:
				dp[i] = min(dp[i], 1 + dp[i-coin])

	if dp[-1] == float('inf'):
		return []

	print 'Total combinations:' , dp[-1]

	out = []
	dfs(amount, [], 0)
	output = '\n'.join([','.join([str(i) for i in row]) for row in out])
	print output

denominations = [1,2,3]
amount = 4
coinChange(amount, denominations)
