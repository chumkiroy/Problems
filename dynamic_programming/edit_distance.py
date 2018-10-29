'''
Levenshtein Distance

Problem Statement:

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character

e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3

kitten - sitten (substitution of s for k)
sitten - sittin (substitution of i for e)
sittin - sitting (insertion of g at the end)

Input Format:
You will be given two strings strWord1 and strWord2, containing lower case alphabets from a to z.

Output Format:
Return an integer denoting the edit distance between two strings.

Constraints:
1 <= length(strWord1), length(strWord2) <= 1000

Sample Test Case:
	Sample Input-1:
		cat
		bat
	Sample Output-1:
		1
	Explanation-1:
		1: Replace c with b.

	Sample Input-2:
		qwe
		q
	Sample Output-2:
		2
	Explanation-2:
		1: Add w
		2: Add e
'''

def editDistance(word1, word2):
	if not word1 and len(word2) > 0:
		return len(word2)
	if not word2 and len(word1) > 0:
		return len(word1)

	l1 = len(word1)
	l2 = len(word2)

	dp = [[0]*(l2+1) for _ in range(l1+1)]

	for i in range(len(dp)):
		dp[i][0] = i
	for i in range(len(dp[0])):
		dp[0][i] = i

	for i in range(1, l1+1):
		for j in range(1, l2+1):
			if word1[i-1] == word2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
	return dp[l1][l2]

word1 = 'abc'
word2 = 'def'

print editDistance(word1, word2)


