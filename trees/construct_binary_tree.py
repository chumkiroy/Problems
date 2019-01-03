'''
PROBLEM STATEMENT: Construct binary tree

Inorder traversal - Process all nodes of a binary tree by recursively processing the left subtree, then processing the root, and finally the right subtree.

Preorder traversal - Process all nodes of a binary tree by recursively processing the root, then processing the left subtree, and finally the right subtree.

Given the inorder and preorder traversal of a valid binary tree, you have to construct the binary tree.

[Interesting article to read: http://www.geeksforgeeks.org/if-you-are-given-two-traversal-sequences-can-you-construct-the-binary-tree/]

Input Format:
-------------
You are given two integer array named inorder and preorder of size n, containing positive values <= 10^5

Output Format:
--------------
Return root pointer of the constructed binary tree.

Constraints:
-----------
0 <= n <= 10^5
1 <= inorder[i], preorder[i] <= 10^5
Values stored in the binary tree are unique.

Sample Test Cases:
------------------

Sample Test Case 1:

Sample Input 1:
inorder = [2, 1, 3] and preorder = [1, 2, 3]

Sample Output 1:
  1
/ \
2 3

Explanation 1:

In this case, Binary tree will be look like as given above.

Return the pointer of root node of constructed binary tree. In this case root treenode has value '1'.

Sample Test Case 2:

Sample Input 2:
inorder = [3, 2, 1, 5, 4, 6] and preorder = [1, 2, 3, 4, 5, 6]

Sample Output 2:
    1
   / \
 2 4
 / / \
3 5    6

'''

# The function accepts INTEGER_ARRAY inorder and preorder as parameter and returns Root pointer of constructed binary tree.
# class TreeNode:
#    def __init__(self, x):
#        self.value = x
#        self.left = None
#        self.right = None
#

def constructBinaryTree(inorder, preorder):
    inorder_index = {}
    for i in range(len(inorder)):
        inorder_index[inorder[i]] = i
    return dfs(inorder, preorder, [0], 0, len(inorder)-1, inorder_index)
    
def dfs(inorder, preorder, preorder_index, inorder_start, inorder_end, inorder_index):
    if inorder_start > inorder_end:
        return
    if preorder_index[0] >= len(preorder):
        return
    
    found_index = inorder_index[preorder[preorder_index[0]]]
    
    
    root = TreeNode(preorder[preorder_index[0]])
    preorder_index[0] +=1
    root.left = dfs(inorder, preorder, preorder_index, inorder_start, found_index-1, inorder_index)
    root.right = dfs(inorder, preorder, preorder_index, found_index+1, inorder_end, inorder_index)
    
    return root


