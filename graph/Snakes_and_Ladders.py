'''
Problem Statement: Snakes and Ladders Matrix

Given a snake and ladder rectangular MxN board-game, find the minimum number of dice throws required to reach the final cell from the 1st cell. 

Rules are as usual: If after a dice-throw, the player reaches a cell where the ladder starts, the player has to climb up that ladder and if the player reaches a cell that has the mouth of the snake, s/he has to go down to the tail of snake.

For example, in the board given below, it will take minimum 4 throws to reach from 1 to 36. That can be done with the following sequence of throws: (1,6,4,1). There may be more such sequences of the same length viz. (4,2,6,3) etc. 

Input Format:
-------------
You will be given an integer n denoting the size of the board and an array of integer moves of length n, denoting if there is a ladder or a snake as follows:

moves[i] = -1, No ladder and no snake
moves[i] < i, Snake from i to moves[i]
moves[i] > i, Ladder from i to moves[i]
moves array has one-based indexing.

Output Format:
--------------
Return an integer denoting the minimum number of dice rolls required to reach the last cell.

Constraints:
------------
1 <= n <= 10^5
1 <= moves[i] <= n

Note:
You start at cell 1.
There is no snake at the last cell and no ladder at the first cell.
No snake starts at the top of a ladder or bottom of a snake. No ladder starts at the bottom of the snake or top of a ladder.
Return -1 if there is no possible way.


Sample Test Case:
------------------
Sample Input-1:
n = 20
moves = [-1, 19, -1, -1, -1, -1, -1, -1, 3, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1]

Sample Output-1:
2

Explanation-1:
1 --> (2~19) --> 20

'''

def minNumberOfRolls(n, moves):
    board = [i for i in range(n+1)]
    
    for i, pos in enumerate([0]+moves):
        if pos != -1:
            board[i] = pos
            
    que = [(1,0)]
    visited = set()
    visited.add(1)
    
    while que:
        pos, count = que.pop(0)
        if pos == n:
            return count
            
        for dice in range(1, 7):
            next_num = pos + dice
            if next_num <= n:
                next_pos = board[next_num]
                if next_pos not in visited:
                    visited.add(next_pos)
                    visited.add(next_num)
                    que.append((next_pos, count+1))
                    
    return -1

n = 20
moves = [-1, 19, -1, -1, -1, -1, -1, -1, 3, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1]

print minNumberOfRolls(n, moves)
