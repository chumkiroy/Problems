'''
Zip Given Linked List From Ends

Problem Statement:
------------------
Given an integer singly linked list, zip it from its two ends. (Looking at the sample test case will make it more clear.)

You have to do it in-place i.e. in the same linked list, with using only constant extra space. 

Input Format:
-------------
There is only one argument in input, denoting integer singly linked list.

Output Format:
---------------
Return zipped linked list.

Constraints:
------------
0 <= size of linked list <= 100000 
-2 * 10^9 <= value stored in any node <= 2 * 10^9

Sample Test Case:
-----------------
Sample Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

Sample Output:
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL

(Other modification to try yourself for practice: zip two separate lists and unzip them back into original lists. i.e. unzip(zip(L1, L2)) should return L1 and L2.)

'''

'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def zip_given_linked_list(head):
    if not head:
        return None
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second = slow.next
    slow.next = None
    second_rev = reverse_list(second)
    first = head
    while first and second_rev:
        first_next = first.next
        second_rev_next = second_rev.next
        first.next = second_rev
        second_rev.next = first_next
        first = first_next
        second_rev = second_rev_next
    return head
    
    
def reverse_list(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

