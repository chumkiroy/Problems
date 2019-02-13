def search(r, c, board, word, rows, cols, prefix):
	if r < 0 or r > rows - 1 or c < 0 or c > cols -1 or prefix not in word or board[r][c] == '-':
		return False

	if prefix == word:
		return True

	temp = board[r][c]
	board[r][c] == '-'
	
	out = search(r-1, c, board, word, rows, cols, prefix+temp) or search(r+1, c, board, word, rows, cols, prefix+temp) or search(r, c-1, board, word, rows, cols, prefix+temp) or search(r, c+1, board, word, rows, cols, prefix+temp)

	board[r][c] = temp
	return out

def boggle_search(word, board):
	rows = len(boggle)
	cols = len(boggle[0])
	for i in range(rows):
		for j in range(cols):
			if word[0] == boggle[i][j]:
				out = search(i, j, board, word, rows, cols, '')
				if out:
					break
	if out:
		return True

word = "hello"
boggle = [['a','o','l'],
		  ['d','e','l'],
		  ['g','h','i']]

'''

word = "GEEKS"
boggle = [['G','I','Z'],
          ['U','E','K'],
          ['Q','S','E']]
'''
print boggle_search(word, boggle)

