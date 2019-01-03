'''
PROBLEM STATEMENT: Balanced BST From A Sorted Array

Given a sorted array a of size N containing distinct integers. You have to build a balanced binary search tree of a. 

A binary search tree is balanced if for each node it holds that the number of nodes in the left subtree and the number of nodes in the right subtree differ by at most 1.

Input Format:
-------------
There is only one argument denoting array a. 

Output Format:
--------------
You have to return the root of the balanced BST that you created. 

There can be multiple balanced BST for given input. So, you are free to return any of the valid one.

Only thing you have to consider is that it is a valid balanced BST of a.

Consider a = [1, 2] then:
1) 1 is the root of the tree and 2 is 1's right child. 
2) 2 is the root of the tree and 1 is 2's left child.

Both of them will be considered as correct answer. 

Constraints:
------------
a is sorted.
a contains distinct integers.
-2 * 10^9 <= a[i] <= 2 * 20^9 
1 <= N <= 10^5

Sample Test Case:
-----------------
Sample Input: a = [8 10 12 15 16 20 25]
Sample Output:
Root of the Balanced BST where:
15 is the root node.
10 is 15's left child.
20 is 15's right child.
8 is 10's left child.
12 is 10's right child.
16 is 20's left child.
25 is 20's right child.

Explanation:
------------
For each node, number of nodes in left subtree and number of nodes in right subtree are same (differ by 0) and also it is a BST. Hence it is a balanced BST.   

'''

def build_balanced_bst(a):
	if not a:
        return None
        
    mid = int(len(a) / 2)
    node = TreeNode(a[mid])
    node.left_ptr = build_balanced_bst(a[:mid])
    node.right_ptr = build_balanced_bst(a[mid+1:])
    return node

'''

Another approach:

def do_build(a, s, e):
  if (e < s):
    return None
  if (s == e):
    return TreeNode(a[s])
  mid = (s + e) // 2
  root = TreeNode(a[mid])
  root.left_ptr = do_build(a, s, mid - 1)
  root.right_ptr = do_build(a, mid+1, e)
  return root

def build_balanced_bst(a):
  return do_build(a, 0, len(a)-1)

'''
