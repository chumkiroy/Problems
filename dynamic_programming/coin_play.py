def coin_max_profit(coins):
	n = len(coins)
	dp = [[0]*n for _ in range(n)]

	for i in range(n):
        	dp[i][i] = coins[i]

	for i in range(n-1, -1, -1):
		for j in range(i, n):
			if i==j:
				dp[i][j] = coins[i]
				continue
			o1 = dp[i+2][j] if i < n-2 else float('inf')
			o2 = dp[i+1][j-1] if i < n-1 and j > 0 else float('inf')
			o3 = dp[i][j-2] if j < n-2 else float('inf')
			
			dp[i][j] = max( coins[i] + min(o1, o2), coins[j] + min(o2, o3))
			print dp[i][j]
        #print dp
	return dp[0][n-1]

v = [5,3,7,10] #[3,9,1,2] #[8, 15, 3, 7]
print coin_max_profit(v)
