'''
Find The Middle Node In A Singly Linked List

Problem Statement:
------------------
Given an integer singly linked list L, you have to find the middle node of it. L has total n no. of nodes.
If it has even number of nodes, then consider the second of the middle two nodes as the middle node.

Input/Output Format For The Function:
-------------------------------------
Input Format:
There is only one argument in input, L, denoting head node of input integer singly linked list.

Output Format:
Return the middle node of the given integer singly linked list middle.

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
The first line of input should contain an integer n, denoting total number of nodes in L. In the next n lines, ith line should contain an integer Li, denoting a value in ith node of L.

If n = 4 and L: 3 -> 7 -> 2 -> 9 -> NULL, then input should be:
4
3
7
2
9

Output Format:
There will be one line, containing an integer middle, denoting the result returned by the solution function.

For input n = 4 and L: 3 -> 7 -> 2 -> 9 -> NULL, output will be:
2

Constraints:
------------
0 <= n <= 10^5
-2 * 10^9 <= value contained in any node <= 2 * 10^9
Do it in one pass over the linked list.
If given linked list is empty then return null.

Sample Test Cases:
------------------
Sample Test Case 1:
Sample Input 1:
1 -> 2 -> 3 -> 4 -> 5 -> NULL

Sample Output 1:
Node containing value 3.


Sample Test Case 2:
Sample Input 2:
1 -> 2 -> 3 -> 4 -> NULL

Sample Output 2:
Node containing value 3.

'''

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}
def find_middle_node(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

