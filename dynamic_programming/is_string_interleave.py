'''
Strings Interleave

Problem Statement:

You're given three strings a, b and i. Write a function that checks whether i is an interleaving of a and b.

String i is said to be interleaving string a and b, if:
len(i) = len(a) + len(b).
i only contains characters present in a or b.
i contains all characters of a. From a, any character a[index] should be added exactly once in i.
i contains all characters of b. From b, any character b[index] should be added exactly once in i.
Order of all characters in individual strings (a and b) is preserved.


Input Format:
You will be given three strings a, b and i.
Strings can contain
Small alphabets - a-z
Large alphabets - A-Z
Numbers - 0-9

Output Format:
Return a boolean if i is an interleaving of a and b.

Constraints:
0 <= len(a), len(b) <= 1000
0 <= len(i) <= 2000


Sample Test Case:

Sample Input-1:
a = "123"
b = "456"
i = "123456"

Sample Output-1:
True

Sample Input-2:
a = "AAB"
b = "AAC"
i = "AAAABC"

Sample Output-2:
True

Sample Input-3:
i = "AAABAC"

Sample Output-3:
True

'''

def isInterleaved(s1, s2, s3):
	l1 = len(s1)
	l2 = len(s2)
	
	T = [[False] * (l2+1) for _ in range(l1+1)]

	for i in range(len(T)):
		for j in range(len(T[0])):
			l = i+j-1
			if i==0 and j==0:
				T[i][j] = True
			elif i == 0:
				if s3[l] == s2[j-1]:
					T[i][j] = T[i][j-1]
			elif j == 0:
				if s3[l] == s1[i-1]:
					T[i][j] = T[i-1][j]
			else:
				if s3[l] == s1[i-1]:
					T[i][j] = T[i-1][j]
				elif s3[l] == s2[j-1]:
					T[i][j] = T[i][j-1]
				else:
					T[i][j] = False
	return T[l1][l2]

str1 = 'AAB'#'XXYM'
str2 = 'AAC'#'XXZT'
str3 = 'AAAABC'#'XXXZXYTM'

print isInterleaved(str1, str2, str3)
