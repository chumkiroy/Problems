'''
Divide An Integer By Another Integer

Problem Statement:
------------------
Given two integers a and b, you have to find quotient q, when a is divided by b. 

Input/Output Format For The Function:
-------------------------------------
Input Format:

Two integers a and b.

Output Format:

A integer q, denoting quotient of a / b.

Input/Output Format For The Custom Input:
------------------------------------------
Input Format:

The first line should contain an integer, denoting a.
Second line should contain an integer, denoting b.

If a = 5 and b = 2, then input should be:
5
2

Output Format:

There will be one line, containing a integer q, denoting quotient value of a / b.

For input a = 5 and b = 2, output will be:
2

Constraints:
-------------
-10^18 <= a, b <= 10^18
b != 0
You are not allowed to use division (/) operator.
You are not allowed to use multiplication (*) operator.
You are not allowed to use mod (%) operator.

Sample Test Case:
-----------------
Sample Input: a = 5, b = 2
Sample Output: 2

Notes:
------
Here we have mentioned explicitly that b != 0, but in interview you should clarify this with the interviewer and handle the case accordingly. 

Maximum time allowed: 20 Minutes. 

'''

def divide(a, b):
    if a == 0:
        return 0
    if abs(b) == 1:
        if b > 0:
            return a
        else:
            return -a
    if abs(b) == 2:
        if b > 0:
            if a > 0:
                return abs(a) >> 1
            else:
                return -(abs(a) >> 1)
        else:
            if a > 0:
                return -(abs(a) >> 1)
            else:
                return abs(a) >> 1
    p = abs(a)
    q = abs(b)
    count = 0
    while p>0:
        p -= q
        count += 1
    if p < 0:
        count -= 1
    if ((a > 0) and (b > 0)) or ((a < 0) and (b < 0)):
        return count
    else:
        return -count

print divide(5, 2)
'''
##Another approach

def divide(dividend, divisor):
    if dividend < 0 and divisor < 0:
        sign = 1
    elif dividend < 0  or divisor < 0:
        sign = -1
    else:
        sign = 1
    D = abs(dividend)
    d = abs(divisor)
    if D == d:
        return 1*sign
    
    q = div_helper(D,d)
    return q*sign

def div_helper(D,d):
    if D < d:
        return 0
    else:
        res=0
        orig_d = d
        while D > (d<<1):
            d=d<<1
            res+=1
        rem = D - d
        return pow(2,res) + div_helper(rem,orig_d)
'''