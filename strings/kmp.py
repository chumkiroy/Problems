'''
KMP

Problem Statement:
-------------------
Given a text string t of length n and a pattern string p of length m, return start indices of all occurrences of p in t.

You have to answer q such queries.

Input/Output Format For The Function:
-------------------------------------
Input Format:
There are two arguments, t and p, denoting text string and pattern string respectively.

Output Format:
Return an array of integer pos[], where pos[i] is the start index of ith occurrence of p in t(0-based indexing).

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
The first line should contain a string t, denoting text string. Next line should contain an integer q, denoting no. of queries to be answered. In the next q lines, ith line contains a string pi, denoting pattern string for ith query, i=(1,2,...,q).
If
t = "Ourbusinessisourbusinessnoneofyourbusiness",
q = 3,
p in 1st query = "business",
p in 2nd query = "our",
p in 3rd query = "daisy",
then input should be:
Ourbusinessisourbusinessnoneofyourbusiness
3
business
our
daisy


Output Format:
Output will be printed in the sequence of queries asked. So, output of 1st query will be printed first, followed by output of 2nd query and so on, upto output of qth query.

For ith query, let say length of resultant array posi[] is leni.

Then, for ith query, there will be leni lines, where jth line of these leni lines contains a number posi[j], denoting number at jth index of posi.

So, in total, no. of lines will be = (len1 + len2 + len3 + - - + lenq)


For input:
t = "Ourbusinessisourbusinessnoneofyourbusiness",
q = 3,
p in 1st query = "business",
p in 2nd query = "our",
p in 3rd query = "daisy",
output will be:
3
16
34
13
31
-1

Note:
If there is no occurrence of p in t, then return array pos of size one with pos[0] = -1.

If there are multiple occurrences of p in t, then return an array of start indices(sorted in increasing order).

Constraints:
------------
1 <= q <= 5
1 <= n <= 2*10^5
1 <= m <= 2*10^5
t and p may contain lower case characters, upper case characters and numeric characters.

Sample Test Cases:
------------------
Sample Input 1:
t = "Ourbusinessisourbusinessnoneofyourbusiness"
q = 3 (t will be same for all 3 queries)
p in 1st query = "business"
p in 2nd query = "our"
p in 3rd query = "daisy"

Sample Output 1:
4
20
43
16
39
-1

Sample Input 2:
t = "IfyouthinkyouthinktoomuchthenyoumightbewrongThinkaboutit"
q = 4 (t will be same for all 4 queries)
p in 1st query = "aaaa"
p in 2nd query = "think"
p in 3rd query = "you"
p in 4th query = "be"


Sample Output 2:
7
17
3
13
37
47

'''

def KMP(s, p):
    n = len(s)
    m = len(p)
    if n < m:
        return [-1]
    prefix = [0 for x in range(m)]
    build_prefix(prefix,p)
    #print("prefix",prefix)
    res = []
    i=0
    j = 0
    while i < n:
        while j < m and i < n:
            if s[i] == p[j]:
                i+=1
                j+=1
            else:
                if j == 0: # mismatch at first itself, then increment i too as no need to check again
                    i+=1
                else: # if j ==0, then j = prefix[-1] which is last idx in python! remember this
                    j = prefix[j-1]
                # if j becomes 0 here, it is ok no need to increment i because j was something else before becoming 0
        if j == m:
            j = prefix[j-1]
            res.append(i-m) # i remains same as it already points to unexamined index
    
    if len(res) == 0:
        return [-1]
    return res
    
def build_prefix(prefix,p):
	m = len(p)
	i = 0
	for j in range(1, m):
		if p[j] == p[i]:
			i += 1
			j += 1
		else:
			if i == 0:
				lps[j] = 0
				j += 1
			else:
				i = lps[i-1]
	   '''
    m = len(p)
    for j in range(1,m):
        if p[j] == p[prefix[j-1]]:
            prefix[j] = prefix[j-1]+1
        elif p[j] == p[0]:
            prefix[j] = 1
    '''


s = "Ourbusinessisourbusinessnoneofyourbusiness"
p = "business"

print KMP(s, p)
