'''
Find The Next Palindromic Number

Problem Statement:
------------------
Given a number n, you have to find next palindromic number pal. To be precise, you have to find an integer pal, which is smallest palindromic number, greater than n.

Input/Output Format For The Function:
-------------------------------------
Input Format:
There is only one argument denoting integer n.

Output Format:
Return the required number pal.

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
There should be only one line, containing an integer n.
If n = 5, then input should be: 5

Output Format:
There will be one line, containing resultant integer pal.

For input n = 5, output will be: 6

Constraints:
------------
0 <= n <= 2147483647

Sample Test Cases:
------------------
Sample Test Case 1:

Sample Input 1:
5

Sample Output 1:
6

Explanation 1:
6 is a palindromic number, and bigger than 5. There is no palindromic number less than 6 and bigger than 5.


Sample Test Case 2:

Sample Input 2:
10

Sample Output 2:
11

Notes:
------
Suggested time: 30 minutes.

'''

def getNumDigits(n):
  digits = []
  while (n > 0):
    digits.insert(0,n % 10)
    n = n // 10 
  return digits

def inc(digits, i, j):
  while (digits[j] == 9):
    digits[j] = 0
    j-=1
  digits[j] +=1 
  return
    
def doSolve(digits, i, j):
  if i >= j:
    return
  
  if digits[i] == digits[j]:
    doSolve(digits, i+1, j-1)
  if digits[j] > digits[i]:
    inc(digits, i, j-1)
    digits[j] = digits[i]
    doSolve(digits, i+1, j-1)
  if digits[j] < digits[i]:
    digits[j] = digits[i]
    doSolve(digits, i+1, j-1)

def next_palindrome(n):
  n+=1
  digits = getNumDigits(n)
  doSolve(digits, 0, len(digits)-1)
  return int("".join(str(e) for e in digits))

print next_palindrome(13)
'''
def get_num_of_digits(n):
    dg = 0
    
    if n == 0: # handle special case !
        return 1

    while n:
        n //= 10
        dg += 1
    
    return dg

def next_palindrome(n):

    #Approach:
    #0. Increment the number by 1 so we start with the larger number.
    #1. First count the number of digits in the number
    #2. Now have 2 pointers, one starting from the MSD (Most Significant Digit) and other from LSD (Least Significant Digit). 
    #3. Compare numbers pointed by MSD and LSD pointers. There can be 2 cases:
    #   1. If MSD number is greater than LSD then update LSD with MSD digit and continue.
    #    2. If the MSM number is lesser than LSD then increment the next left digit of the LSD, set the LSD to 0 and re-run through the number !
    #    keep forming the new number with processed MSD and LSD.
    #    End the loop when LSD pointer is less than or equal to MSD pointer.
    
    n = n + 1 # Increment the number by 1 !
    dg = get_num_of_digits(n)
    
    new_num = 0
    l = dg - 1
    r = 0
    cur_l = l
    n_tmp = n

    while l >= r:
        # handle single digit case
        if l == r:
            return new_num + n_tmp * pow(10, l)
        
        r_num = n_tmp % 10
        l_num = n_tmp // pow(10, cur_l)
        
        if l_num != r_num:
            if l_num > r_num:
                r_num = l_num
            else:
                n_tmp = n + pow(10, r + 1) - r_num * pow(10, r)
                #print("n_tmp {}".format(n_tmp))
                dg = get_num_of_digits(n_tmp)
                n = n_tmp 
                l = dg - 1
                r = 0
                cur_l = l
                new_num = 0
                continue
    
        new_num += r_num * pow(10, r)
        new_num += l_num * pow(10, l)
        #print("new_num {}".format(new_num))
    
        n_tmp = n_tmp % pow(10, cur_l)
        n_tmp = n_tmp // 10
        cur_l -= 2
        l -= 1
        r += 1
        
    return new_num
'''
