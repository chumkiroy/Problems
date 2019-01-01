'''
Problem Statement: Shortest Path In 2D Grid With Keys And Doors

Given a 2D grid, that represents a maze-like area. Each cell in the grid can be either land or water or door or key to some doors. 

Each type of key will only open one type of door. There can be multiple identical keys of the same type. There can also be multiple doors of the same type.

There is also a start cell and a goal cell on the land. 

You have to find the shortest path from start to the goal.

Input Format:
-------------
There is only one argument denoting the grid. 
Cells in the grid can be described as:
'#' = Water.
'.' = Land.
'a' = Key of type 'a'. All lowercase letters are keys.
'A' = Door that opens with key 'a'. All uppercase letters are doors.
'@' = Starting cell.
'+' = Ending cell (goal).

Output Format:
--------------
Return a 2D array containing the path from start to goal.

Suppose your path contains N cells, then output array should be of size N * 2, where (array[i][0], array[i][1]) describes a cell position.

Positioning of cells:
---------------------
0-indexed. 
Columns: Increasing from left to right.
Rows: Increasing from top to bottom.
There can be multiple shortest paths, so you are free to return any of them. 

Constraints:
-----------
- You can only travel on land cells, key cells and door cells, and not on water cells.
- You can travel in any of the four directions (including backwards), but not diagonally.
- It is okay to revisit a cell, if you need to (you can go backwards).
- You cannot travel thru a door, unless you have picked up the key to that door before arriving there.
- If you have picked up a certain type of key, then it can be re-used on multiple doors of same kind.
- 1 <= number of rows, number of columns <= 100
- There will be exactly one starting point and one goal.
- It is guaranteed that there exists a path from start to goal. 
- 'a' <= key <= 'j'
- 'A' <= door <= 'J'


Sample Test Case:

Sample Input:
...B
.b#.
@#+.

Sample Output:
[
  [2 0],
  [1 0],
  [1 1],
  [0 1], 
  [0 2],
  [0 3],
  [1 3],
  [2 3],
  [2 2]
]

Explanation:

In order to pass through door 'B', we first need to collect key to open that door and that is 'b'.   
'@' -> '.' -> 'b' -> '.' -> '.' -> 'B' -> '.' -> '.' -> '+' 
Here position [2 0] is '@' in the grid above, which is the starting position.

'''

from collections import deque

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] =='@':
               return r, c
    return -1,-1
    
def get_neighbour(grid,  rows, cols, row, col, keyring):
    res = []
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    for dr, dc in directions:
        new_r = dr + row
        new_c = dc + col
        if not (0 <= new_r < rows and 0 <= new_c < cols):
            continue
        cell = grid[new_r][new_c]
        if cell == '#':
            continue
        if cell in 'ABCDEFGHIJ' and ( (1 << (ord(cell) - ord('A'))) & keyring) == 0:
            continue
        if cell in 'abcdefghij':
            newkeyring = keyring | (1 << (ord(cell) - ord('a')))
        else:
            newkeyring = keyring
        res.append((new_r, new_c, newkeyring))
    return res
        
def Visited(row, col, newkeyring, visited):
    res = []
    for keyring in visited[(row, col)]:
        #print(keyring)
        if newkeyring & keyring == newkeyring:
            return True
        elif newkeyring & keyring == keyring:
            res.append(keyring)
    for r in res:
        visited[(row, col)].remove(r)
    return False

def build_path(start_row, start_col, start_keyring, end_row, end_col, end_keyring, parent):
    path = []
    while start_row != end_row or start_col != end_col or start_keyring != end_keyring:
        path.append((end_row, end_col))
        end_row, end_col, end_keyring = parent[(end_row, end_col, end_keyring)]
    path.append((start_row, start_col))
    return path[::-1]

def find_shortest_path(grid):
    q = deque()
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = find_start(grid)
    visited = {(r,c):set() for r in range(rows) for c in range(cols)}
    parent = {}
    q.append((start_row, start_col, 0))
    visited[(start_row,start_col)].add(0)
    while q:
        row, col, keyring = q.popleft()
        # end call 
        if grid[row][col] =='+':
            return build_path(start_row, start_col, 0, row, col, keyring, parent)
        for r, c, newkeyring in get_neighbour(grid,  rows, cols, row, col, keyring):
            if not Visited(r, c, newkeyring, visited):
                visited[(r, c)].add(newkeyring)
                q.append((r, c, newkeyring))
                parent[(r, c, newkeyring)] = row, col, keyring
                
    return []

grid = [['.','.','.','B'], ['.','b','#','.'], ['@','#','+','.']]
print find_shortest_path(grid)
