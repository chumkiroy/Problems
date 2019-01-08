'''
Find Intersection Of Two Singly Linked Lists

Problem Statement:
------------------
Given two singly linked lists L1 and L2 containing non-negative integers. You have to find the intersection of given linked lists if any.

Intersection of two linked lists is the first common node (first node with the same address).

Input Format:
-------------
There are two arguments L1 and L2 denoting pointers to head of the linked lists.

Output Format:
--------------
If given linked lists intersects then return the value in the first node where intersection begins, else return -1.

Constraints:
------------
0 <= value stored in nodes <= 10^9
You are not allowed to modify the given linked lists.
Let N1 denote number of nodes in L1 and N2 denote number of nodes in L2. Then 0 <= N1, N2 <= 10^5. 

Sample Test Case:
-----------------
Sample Input:

1 - 2 - 3 
		\
		 - 4 - 7 - 8 - 9
		/
    5 - 6 

L1: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9 
L2: 5 -> 6 -> 4 -> 7 -> 8 -> 9

Sample Output: 4

Explanation:
L1 and L2 intersects at node containing value 4.

Notes:
Expected solution: Linear time complexity, with constant extra space.
Realize that when comparing two nodes, you should be comparing the addresses, and NOT values.

'''

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}
def find_intersection(l1, l2):
    if l1 == None or l2 == None:
        return -1
        
    h1 = l1
    h2 = l2
    
    def length(L):
        l = 0
        while L:
            l += 1
            L = L.next
        return l
    len1 = length(h1)
    len2 = length(h2)
    
    if len1 > len2:
        h1 = l2
        h2 = l1 # h2 is longer
        
    for _ in range(abs(len1-len2)):
        h2 = h2.next
        
    while h1 and h1 and h1 is not h2:
        h1 = h1.next
        h2 = h2.next
    
    if h1 == None or h2 == None:
        return -1
    return h1.val

