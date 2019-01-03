'''
PROBLEM STATEMENT: Populate Sibling pointers

Given a binary tree, populate nextRight pointers in each node and return the root of the tree.

* Constraint: Use only constant extra space.

e.g. Given this:
         a
       /  \
      b    c
     / \    \
    d   e    f

Turn it into this:

         a -> nil
       /  \
      b -> c -> nil
     / \    \
    d -> e -> f -> nil

Note that 'c' doesn't have both children. It only has right child. So we need to connect 'e' to 'f'.

Custom Input Format:

	First line contains single integer denoting total no of nodes in the tree.

	Seconds line contains pre-order traversal of tree (values are space separated).

For example:

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

Notes:

Suggested time: 40 minutes.

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

'''

Class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		self.right = None
		self.left = None

Class Solution:
	def populateSiblingPointers(self, root):
		if not root:
			return None

		tail = dummy = TreelinkNode(0)

		while root:
			tail.next = root.left
			if tail.next:
				tail = tail.next
			tail.next = root.right
			if tail.next:
				tail = tail.next
			root = root.next

			if not root:
				tail = dummy
				root = dummy.next

'''
Check the following solution:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37828/o1-space-on-complexity-iterative-solution

public class Solution {
    
    //based on level order traversal
    public void connect(TreeLinkNode root) {

        TreeLinkNode head = null; //head of the next level
        TreeLinkNode prev = null; //the leading node on the next level
        TreeLinkNode cur = root;  //current node of current level

        while (cur != null) {
            
            while (cur != null) { //iterate on the current level
                //left child
                if (cur.left != null) {
                    if (prev != null) {
                        prev.next = cur.left;
                    } else {
                        head = cur.left;
                    }
                    prev = cur.left;
                }
                //right child
                if (cur.right != null) {
                    if (prev != null) {
                        prev.next = cur.right;
                    } else {
                        head = cur.right;
                    }
                    prev = cur.right;
                }
                //move to next node
                cur = cur.next;
            }
            
            //move to next level
            cur = head;
            head = null;
            prev = null;
        }
        
    }
}

# O(1) space and O(n) Time complexity
'''
