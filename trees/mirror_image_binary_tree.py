'''
PROBLEM STATEMENT: Mirror Image Of Binary Tree

You are given root node of Binary Tree T. You need to modify binary tree represented by given root node such that it will represent mirror image tree of given Binary Tree T.

Input Format:
-------------
Only argument for function, Node named root which is root node of a binary tree T.

Output Format:
--------------
Need to modify binary tree represented by given root node such that it will represent mirror image tree of that binary tree. Code written by us will have output:

If modified root node is representing mirror image of given binary tree T then binary tree represented by modified root  node will be printed.
If modified root node is not representing mirror image of given binary tree T then “Not a mirror image” along with binary tree represented by modified root node will be printed.
Here, printing binary tree represented by tree node means printing lines equal to number of vertices. Each line will have “v l r” means for vertex v, left child is vertex l and right child is vertex r.

If l or r is -1 means that child is null.

Constraints:
------------
- 1 <= n <= 100000 where n is number of nodes in binary tree.
- Indexing of vertices starting from 0.
- For each node of tree, node of tree is a vertex of binary tree and value data of that can be 0 <= data <= n-1 and data will be unique for each node.

Sample Test Case:
-----------------
Sample Input:

      0
     / \
  1      2
 / \    / \
 3  4   5 6

Sample Output:
      0
     / \
   2	 1
  / \    / \
 6   5  4   3

Explanation:

As we can easily visualise that input binary tree and output binary tree are mirror images of each other. So, If A and B are two binary tree which are mirror images of each other then taking mirror image of A would generate B and vice versa.

'''

# The function accepts root node of binary tree as parameter.
#
# Structure of TreeNode will be:
# class TreeNode(object):
#     data = -1
#     left = None
#     right = None
#
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None

def mirror_image(root):
    if root == None:
        return 
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        temp = cur_node.left
        cur_node.left = cur_node.right
        cur_node.right = temp
        
        if cur_node.left != None: 
            queue.append(cur_node.left)
        if cur_node.right != None:
            queue.append(cur_node.right)

