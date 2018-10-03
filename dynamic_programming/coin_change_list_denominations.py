def coin_change(amount, coins):

    def dfs(a, so_far, indx):
        if a == 0:
            output.append(so_far[:])
            return

        for i in range(indx, len(coins)):
	    c = coins[i]
	    if a >= c and dp[a] - 1 == dp[a-c]:
		so_far.append(c)
		dfs(a-c, so_far, i)
		so_far.pop()

    dp = [0] + [float('inf')] * amount
    for i in range(1, amount+1):
	for coin in coins:
	    if i >= coin:
		dp[i] = min(dp[i], 1+ dp[i-coin])
    
    if dp[-1] == float('inf'):
	return []

    output = []
    dfs(amount, [], 0)
    ans = '\n'.join([','.join([str(i) for i in row]) for row in output])
    return ans


amount = 4
coins = [1, 2, 3]
print coin_change(amount, coins)
