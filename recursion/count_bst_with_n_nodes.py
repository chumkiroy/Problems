'''
How Many Binary Search Trees With n Nodes?

Problem Statement:
------------------
Write a function that will return the number of binary search trees that can be constructed, with n nodes.

There may be other iterative solutions, but for the purpose of this exercise, please use recursive solution.

Input Format:
-------------
There is only one argument denoting integer n.

Output Format:
--------------
Return number of binary search trees that can be constructed, with n nodes.

Constraints:
------------
1 <= n <= 16

Sample Test Cases:
------------------
Sample Input 1: 1
Sample Output 1: 1

Explanation 1:
1) root (node val = 1)

Sample Input 2: 2
Sample Output 2: 2

Explanation 2:
1) root (node val = 2), root->left (node val = 1)
2) root (node val = 1), root->right (node val = 2)

Sample Input 3: 3
Sample Output 3: 5

Explanation 3:
1) root (node val = 3), root->left (node val = 2), root->left->left (node val = 1)
2) root (node val = 3), root->left (node val = 1), root->left->right (node val = 2)
3) root (node val = 1), root->right (node val = 2), root->right->right (node val = 3)
4) root (node val = 1), root->right (node val = 3), root->right->left (node val = 2)
5) root (node val = 2), root->left (node val = 1), root->right (node val = 3)

If you keep doing this, it will form a series called Catalan numbers. One can simply lookup the formula for Catalan numbers and write code for it. But that's not how we want to do this. We want to do this by understanding the underlying recursion. The recursion is based on tree-topology only, as you can see by examples above, contents of the nodes of the tree do not matter.

'''

def how_many_BSTs(length):
    return _how_many_BSTs_with_stored_info(length, dict())
    
def _how_many_BSTs_with_stored_info(length, info):
    if info.get(length, None) != None:
        return info[length]
        
    if length == 0 or length == 1:
        info[length] = 1
        return 1
    else:
        total = 0
        for i in range(1,length+1):
            total += _how_many_BSTs_with_stored_info(i-1, info) * _how_many_BSTs_with_stored_info(length-i, info)
        info[length] = total
        return total
        
def _how_many_BSTs(length):
    if length <= 1:
        return 1
    else:
        total = 0
        for i in range(1, length+1):
            total += how_many_BSTs(i-1) * how_many_BSTs(length-i)
        return total

print how_many_BSTs(3)
