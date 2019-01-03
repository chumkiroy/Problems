'''
PROBLEM STATEMENT: UPSIDE DOWN

Given a binary tree where all the right nodes are leaf nodes, flip it upside down and turn it into a tree with left leaf nodes. 

Keep in mind: ALL RIGHT NODES IN ORIGINAL TREE ARE LEAF NODE.

For example, turn these:
     1
     / \ 
     2  3
   / \
   4  5
  / \
  6  7

1
/ \
2 3

 into these:
      1

     /

     2---3

   /

   4---5

  /

  6---7


1
/
2 -- 3

where 6 is the new root node for the left tree, and 2 for the right tree.

oriented correctly:
   6
 / \
7  4
    / \
  5  2
       / \
     3  1


2
/ \
3 1


Solution: https://careercup.com/question?id=6266917077647360

Custom Input Format:
--------------------
First line contains single integer denoting total no of nodes in the tree.

Seconds line contains pre-order traversal of tree (values are space separated).

For example:
------------
3
1 # #

Denotes tree like:
    1
  /   \
 null null
--------------------------------------

7
1 2 3 # # # #

Denotes tree like:
       1
      /   \
     2    null
    /  \
   3   null
  /  \
 null  null

Use the option "Show Input/Output Code " just above the code editor, to see, how input is read, tree is built, the function that you are going to complete is called and output is printed.

Note:
http://tiancao.me/Leetcode-Unlocked/LeetCode%20Locked/c1.13.html

'''

def upside_down(node):
	pass
