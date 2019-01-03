'''
PROBLEM STATEMENT: Kth Smallest Element Of BST

Given a BST (binary search tree) of size N containing integer elements and an integer k. You have to find kth smallest element of given BST.

Input Format:
-------------
There are two arguments in the input. First one is the root of the BST and second one is an integer k.

Output Format:
--------------
Return an integer denoting kth smallest element of BST.

Constraints:
------------
1 <= N <= 6000
1 <= k <= N
-2 * 10^9 <= value stored in any node <= 2 * 10^9
BST need not to be balanced.
You are not allowed to alter the structure or data inside the given BST. 

Sample Test Case:
-----------------
Sample Input:

BST =
2 is the root node.
1 is 2's left child.
3 is 2's right child. 

k = 3

Sample Output: 3

Explanation:
3rd smallest element is 3.
'''

'''
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def kth_smallest_element(root, k):
    def helper(root):
        if root:
            if len(k_smallest_number) < k:
                helper(root.left_ptr)
                if len(k_smallest_number) < k:
                    k_smallest_number.append(root.val)
                    helper(root.right_ptr)
        
    k_smallest_number = []
    helper(root)
    return k_smallest_number[-1]

'''
Another appreach:

def kth_smallest_element(root, k):
    stack = []
    while root:
        stack.append(root)
        root = root.left_ptr
    p = 1
    while stack and  p <= k:
        root = stack.pop()
        p = p + 1
        rchild = root.right_ptr
        while rchild:
            stack.append(rchild)
            rchild = rchild.left_ptr
    return root.val
'''
