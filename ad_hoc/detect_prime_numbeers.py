'''
Detect Prime Numbers

Problem Statement:
------------------
Given an integer array a of size N. For each integer in a we have to check if it is a prime number or not.

Input/Output Format For The Function:
-------------------------------------
Input Format:

There is only one argument denoting integer array a.

Output Format:

Return a string res of size N, where ith character of string contains '1' if a[i] is a prime number else it should contain '0'. (1 is neither a prime nor a composite number, hence according to the previous statement, it should go in else part, i.e. ith character should contain '0', when a[i] = 1.)

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:

The first line should contain a number N, denoting the number of elements in the array a. In next N lines, ith line should contain a number a[i], denoting ith element in a.

If N = 4 and a = [6, 2, 5, 8], then input should be:

4
6
2
5
8

Output Format:

There will be one line, containing a resultant string res.

For input N = 4 and a = [6, 2, 5, 8], output will be:

0110

Constraints:
--------------
1 <= a[i] <= 4 * 10^6
1 <= N <= 3 * 10^5

Sample Test Case:
------------------
Sample Input: [6, 2, 5, 8]
Sample Output: 0110

Explanation:

6 is not a prime number. (6 = 2 * 3)
2 is a prime number.
5 is a prime number.
8 is not a prime number. (8 = 2 * 4)

Notes:
Maximum time allowed: 20 Minutes.

'''

import math
def detect_primes(a):
    largest = max(a)
    n = [True]*(largest+1)
    
    n[0]= n[1] = False
    
    
    for i in range(2,int(math.sqrt(largest+1))):
        #for j in range(2,i):
        #    if n[i]== True:
        #        if j%i == 0 :n[j]=False
        if n[i]==True:
            for j in range(i*i,largest+1,i):
                n[j]=False
            
    res = []
    for i in a:
        if n[i] : res.append('1')
        else:  res.append('0')   
    
    return ''.join(res)
    
print detect_primes([6,2,5,8])
'''
#faster approach
def detect_primes(a):
    largest = max(a)
    prime = [True]*(largest+1)
    
    prime[0]= prime[1] = False
    
    
    for i in range(2,int(math.sqrt(largest+1))):
        if prime[i]==True:
            for j in range(i*i,largest+1,i):
                prime[j]=False
            
    res = []
    for i in a:
        if prime[i] : res.append('1')
        else:  res.append('0')   
    
    return ''.join(res)
'''