'''
Problem statement: Knight's Tour On A Chess Board

You are given a rows * cols chessboard and a knight that moves like in normal chess. 

Currently knight is at starting position denoted by start_row th row and start_col th col, and want to reach at ending position denoted by end_row th row and end_col th col.  

The goal is to calculate the minimum number of moves that the knight needs to take to get from starting position to ending position.

start_row, start_col, end_row and end_col are 0-indexed. 

Input Format:
-------------
There are six arguments. First is an integer denoting rows, second is an integer denoting cols, third is an integer denoting start_row, fourth is an integer denoting start_col, fifth is an integer denoting end_row and sixth is an integer denoting end_col.

Output Format:
--------------
Return an integer.

If it is possible to reach from starting position to ending position then return minimum number of moves that the knight needs to take to get from starting position to ending position.

If it is not possible to reach from starting position to ending position then return -1.

Constraints:
------------
1. 1 <= rows * cols <= 10^5
2. 0 <= start_row, end_row < rows
3. 0 <= start_col, end_col < cols

Sample Test Case:
-----------------

Sample Input:
	rows = 5
	cols = 5
	start_row = 0
	start_col = 0
	end_row = 4
	end_col = 1

Sample Output: 3

Explanation:
	3 moves to reach from (0, 0) to (4, 1): (0, 0) -> (1, 2) -> (3, 3) -> (4, 1). 

'''

def get_next_unit(row, col, rows, cols, board):
    unit_list = []
    directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    for r, c in directions:
        new_row = row + r
        new_col = col + c
        
        if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == 0:
            unit_list.append((new_row, new_col))
            
    return unit_list
    
def bfs(rows, cols, start_row, start_col, end_row, end_col, board):
    if start_row == end_row and start_col == end_col:
        return 0
    q1 = [(start_row, start_col)]
    q2 = []
    count = 0
    while q1 or q2:
        count += 1
        while q1:
            r,c = q1.pop()
            res = get_next_unit(r, c, rows, cols, board)
            for row, col in res:
                if row == end_row and col == end_col:
                    return count
                board[row][col] = 1
                q2.append((row, col))
        count += 1
        while q2:
            r, c =q2.pop()
            res = get_next_unit(r, c, rows, cols, board)
            for row, col in res:
                if row == end_row and col == end_col:
                    return count 
                board[row][col] = 1
                q1.append((row, col))
    return -1

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    board = [[0] * cols for _ in range(rows)]
    res = bfs(rows, cols, start_row, start_col, end_row, end_col, board)
    return res


rows = 5
cols = 5
start_row = 0
start_col = 0
end_row = 4
end_col = 1

print find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)
