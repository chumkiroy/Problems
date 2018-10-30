'''
Knight's tour!

Problem Statement:
------------------
Given a phone keypad as shown below:
1 2 3
4 5 6
7 8 9
  0

How many different phone numbers of given length can be formed starting from the given digit? The constraint is that the movement from one digit to the next is similar to the movement of the Knight in a chess game.

For eg. if we are at 1 then the next digit can be either 6 or 8 if we are at 6 then the next digit can be 1, 7 or 0.

Repetition of digits are allowed - 1616161616 is a valid number. 
The problem requires us to just give the count of different phone numbers and not necessarily list the numbers.
Find a polynomial-time solution, based on Dynamic Programming.

Input Format:
You will be given 2 integer values, startdigit and phonenumberlength, denoting starting digit and the required length respectively.

Output Format:
Return a long integer denoting the total number of possible numbers that can be formed.

Constraints:
	0 <= startdigit <= 9
	1 <= phonenumberlength <= 30

Sample Test Case:
	Sample Input-1:
	startdigit = 1
	phonenumberlength = 2

Sample Output-1:
	2

Explanation-1:
Two possible numbers of length 2: 16, 18
'''

def knightTour(startDigit, phoneNumberLength):
	d = {0:[4,6],
		 1:[6,8],
         2:[7,9],
         3:[4,8],
         4:[0,3,9],
         5:[],
         6:[0,1,7],
         7:[2,6],
         8:[1,3],
         9:[2,4]
		}
	dp = [[0]*10 for _ in range(phoneNumberLength)]
	dp[0][startDigit] = 1
	
	for i in range(1, phoneNumberLength):
		for j in range(10):
			for to in d[j]:
				dp[i][j] += dp[i-1][to]

	ans = 0
	for i in range(10):
		ans += dp[phoneNumberLength-1][i]

	return ans

startDigit = 1
phoneNumberLength = 3
print knightTour(startDigit, phoneNumberLength)
