'''
Swap kth Nodes In Given Linked List

Problem Statement:
------------------
Given an integer singly linked list L of size n, and an integer k, you have to swap kth (1-indexed) node from the beginning, with kth node from the end.

Note that you have to swap the nodes themselves, not just the contents.

Input/Output Format For The Function:
-------------------------------------
Input Format:
There are two arguments in input. First is an integer singly linked list L and second is an integer k.

Output Format:
Return resultant linked list resL, after swapping kth nodes of L.

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
The first line of input should contain an integer n, denoting size of input linked list L. In next n lines, ith line should contain an integer Li, denoting value in ith node of L. In the next line, there should be an integer k, denoting the size of group as explained in problem statement section.

If n = 6, L: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL and k = 2, then input should be:
6
1
2
3
4
7
0
2

Output Format:
There will be n lines, where ith line contains value of ith node of resL. Here, resL is the resultant linked list returned by the solution function.

For input n = 6, L: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL and k = 2, output will be:
1
7
3
4
2
0

Constraints:
1 <= n <= 100000
-2 * 10^9 <= value stored in any node <= 2 * 10^9
1 <= k <= n
Try to access linked list nodes minimum number of times.

Sample Test Case:
-----------------
Sample Input:
list: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL
k: 2

Sample Output:  
1 -> 7 -> 3 -> 4 -> 2 -> 0 -> NULL

Notes:
------
Suggested time: 30 minutes.

'''

'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def swap_nodes(head, k):
    if not head or not head.next: return head

    start_k = end_k = head
    start_pre = end_pre = None

    #find kth and its previous node.
    while k >1:
        start_pre = start_k
        start_k = start_k.next
        k -=1
        
    #find kth last and its previous node.
    temp = start_k
    while temp.next:
        end_pre = end_k
        temp = temp.next
        end_k = end_k.next
    
    #swap
    
    if not start_pre: #head
        head = end_k
    else:
        start_pre.next = end_k
    if not end_pre:
        head = start_k
    else:
        end_pre.next = start_k
    
    temp = start_k.next
    start_k.next = end_k.next
    end_k.next = temp
    
    return head

