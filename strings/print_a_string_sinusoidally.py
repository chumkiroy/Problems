'''
Problem Statement: Print a string Sinusoidally

[This is just a stupid problem, that has no relation to anything else. It's there primarily because we see it on and off. It's a string puzzle disguised as a programming problem]

Also called "SnakeString". For example, the phrase "Google Worked" should be printed as follows (where ~ is the word separator):

    o     ~       k
  o  g  e  W  r   e
G     l      o      d

Note:
https://www.geeksforgeeks.org/print-string-wave-pattern/

'''

def print_string_sinusoidally(s, k):
	if k == 1:
		print s
		return

	l = len(s)
	a = [[' ' for _ in range(l)] for _ in range(l)]
	row = 0
	for col in range(l):
		a[row][col] = s[col]

		if row == k-1:
			down = False
		elif row == 0:
			down = True
		
		if down:
			row += 1
		else:
			row -= 1	

	#Print the matrix
	for r in range(k):
		for c in range(l):
			print a[r][c],
		print	

s = 'GeeksforGeeks'
k = 4

print_string_sinusoidally(s, k)
