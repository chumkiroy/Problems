'''
Reverse Given Linked List In Groups Of k

Problem Statement:
------------------
Given an integer singly linked list L, of size n, and an integer k, you have to reverse every k nodes of the linked list.

There are two cases possible:
1) When n % k = 0: There will be n / k  groups of size k. So, you have to reverse n / k  groups of size k.
2) When n % k != 0: Considering first (floor(n / k) * k) nodes, there will be floor(n / k) groups of size k and one group made of last few nodes of size n % k. So, you have to reverse

floor(n / k) groups of size k and one group of size n % k.
(Looking at sample test cases will make it more clear.)

Input/Output Format For The Function:
-------------------------------------
Input Format:
There are two arguments in input. First is an integer singly linked list L and second is an integer k.

Output Format:
Return resultant linked list resL, after reversing L in groups of k, as asked in problem statement.  

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
The first line of input should contain an integer n, denoting size of input linked list L. In next n lines, ith line should contain an integer Li, denoting value in ith node of L. In the next line, there should be an integer k, denoting the size of group as explained in problem statement section.

If n = 6, L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL and k = 3, then input should be:
6
1
2
3
4
5
6
3



Output Format:
There will be n lines, where ith line contains value of ith node of resL. Here, resL is the resultant linked list returned by the solution function.

For input n = 6, L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL and k = 3, output will be:
3
2
1
6
5
4

Constraints:
----------------
1 <= n <= 100000
-2 * 10^9 <= value stored in any node <= 2 * 10^9
1 <= k <= n
Solve it with constant extra space.

Sample Test Case:
-----------------
Sample Test Case 1:
Sample Input 1:
list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
k: 3

Sample Output 1:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> NULL

Explanation 1:
n = 6, k = 3 hence n % k = 0. So there are n / k = 6 / 3 = 2 groups of size k = 3.
Groups to be reversed are (1 -> 2 -> 3) and (4 -> 5 -> 6).


Sample Test Case 2:

Sample Input 2:
list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
k: 3

Sample Output 2:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7-> NULL

Explanation 2:
n = 8, k = 3 hence n % k != 0, so there are floor(n / k) = floor(8 / 3) = 2 groups of size k = 3 and one group of size n % k = 8 % 3 = 2.

Groups to be reversed are (1 -> 2 -> 3), (4 -> 5 -> 6) and (7 -> 8).

Notes:
Suggested time: 40 minutes.

'''

'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
# reverse the list and returns new head.
def reverse(head):
    cur = head
    prev = None

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    
    return prev # new head !
    
def reverse_linked_list_in_groups_of_k(head, k):
    
    cur = head
    exit = False
    prev = None
    
    while not exit:
        cur_head = cur
        pos = 1
        # find the list of size k
        while cur and pos != k:
            cur = cur.next
            pos += 1

        # check if we should exit after revsering current group?
        if cur == None or cur.next == None or pos != k:
            exit = True
        
        # terminate the current group and save the starting point of next group
        if cur != None and cur.next != None:
            temp = cur.next
            cur.next = None # set this to None make linked list of size k
            cur = temp # this will be head of next group of k nodes !
        
        new_head = reverse(cur_head)
        if not prev:
            head = new_head # update the head of new of the list
        
        if prev:
            prev.next = new_head # make the connection !
    
        prev = cur_head # cur_head would be now tail of the reversed list
                    
    return head

