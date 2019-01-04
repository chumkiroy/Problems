'''
Given two sequences, find the longest subsequence present in both of them. (Not just the length, but the actual string)

The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences). It differs from problems of finding common substrings: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the diff utility, and has applications in bioinformatics. It is also widely used by revision control systems such as Git for reconciling multiple changes made to a revision-controlled collection of files. (Source Wikipedia).

For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length 'n' has 2^n different possible subsequences.

LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Return empty string if there is no such common subsequence.

NOTE:
http://www.geeksforgeeks.org/printing-longest-common-subsequence/

'''

def longestCommonSubsequence(a,b):
	if not a or not b or len(a) == 0 or len(b) == 0:
		return 0

	m = len(a)
	n = len(b)
	word = []
	dp = [[0]*(n+1) for _ in range(m+1)]

	for i in range(1, m+1):
		for j in range(1, n+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
				word.append(a[i-1])
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	indx = dp[m][n]
	subseq = []
	i = m
	j = n
	
	while i > 0 and j > 0:
		if a[i-1] == b[j-1]:
			subseq.append(a[i-1])
			i -= 1
			j -= 1
			indx -= 1
		elif dp[i-1][j] > dp[i][j-1]:
			i -= 1
		else:
			j -= 1
	
	return subseq[::-1]

a = 'abcdaf'
b = 'acbcf'

print longestCommonSubsequence(a,b)
