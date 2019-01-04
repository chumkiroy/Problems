'''
Coin Play

Problem Statement:
------------------
Consider a row of n coins of values v1, . . ., vn. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Assume full competency by both players.

Input/Output Format For The Function:
------------------------------------
Input Format : You will be given an array of integers v.
Output Format: Return an integer max, denoting the maximum possible amount of sum that you can accumulate.

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
The first line should contain an integer n, denoting no. of coins. In next n lines, ith line should contain an integer vi, denoting value of ith coin in input array v.

If n = 4 and v = [8, 15, 3, 7], then input should be:
4
8
15
3
7

Output Format:
There will be only one line, containing an integer max, denoting the maximum possible amount of sum that you can accumulate.

For input n = 4 and v = [8, 15, 3, 7], output will be:
22

Constraints:
------------
1 <= n <= 1000
1 <= v[i] <= 10^6

Sample Test Case:
-----------------
Sample Input : v = [8, 15, 3, 7]
Sample Output: 22

Explanation:

Player 1 can start two different ways: either picking 8 or picking 7. Depending on the choice s/he makes, the end reward will be different. We want to find the maximum reward the first player can collect.

1. Player 1 start by picking coin of amount 8.
Remaining v = [15, 3, 7].

Opponent will have two choices, either pick coin of value 15 or 7. Opponent will always pick 15 (to maximize his/her own amount).

Remaining v = [3, 7].

Player 1 will have two choices, either pick coin of value 3 or 7.

Player 1 will always pick 7 (to maximize his/her own amount).

Hence in this case, player 1 can get maximum amount 8 + 7 = 15.

(This is greedy strategy i.e. pick the highest at every step.)

2. Player 1 start by picking coin of amount 7.

Remaining v = [8, 15, 3].

Opponent will have two choices, either pick coin of value 8 or 3.

Opponent will pick 8 (to maximize his/her own amount). (Even if he/she picks 3, then also answer will be same, because in next turn player 1 is looking for coin of value 15.)

Remaining v = [15, 3].

Player 1 will have two choices, either pick coin of value 15 or 3.

Player 1 will always pick 15 (to maximize his/her own amount).

Hence in this case, player 1 can get maximum amount 7 + 15 = 22.


Given these two strategies, we want 22 as the answer, and not 15.

'''

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
	print dp
	return dp[0][n-1]

v = [5,3,7,10] #[3,9,1,2] #[8, 15, 3, 7]
print coin_max_profit(v)
