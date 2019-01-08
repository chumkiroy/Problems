'''
Find Median Of Sorted Circular Singly Linked List

Problem Statement:
------------------
Given a pointer ptr to an arbitrary node of a sorted circular singly linked list L, having n nodes, containing only even integers, you have to find the median value M of L.

When n is an even number, then the median M is average of two middle elements in a sequence of elements in L, arranged in sorted order.

Input/Output Format For The Function:
-------------------------------------
Input Format:
There is only one argument, ptr, denoting a pointer to an arbitrary node of L.

Output Format:
Return one integer denoting the median M.

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:

The first line of input should contain an integer n, denoting the number of nodes in L. In next n lines, ith line should contain an integer(even number) Li, denoting value in ith node of L.

In next line, there should be an integer x, denoting index of a node in L, address of which is referenced as a pointer ptr in problem statement section. (0-based indexing for x.)

If n = 5, L: 2 -> 4 -> 6 -> 8 -> 10 (and pointer back to first node i.e. 2) and x = 1, then input should be:
5
2
4
6
8
10
1

Output Format:

There will be one line, containing an integer M, denoting the result returned by the solution function.

For input n = 5, L: 2 -> 4 -> 6 -> 8 -> 10 (and pointer back to first node i.e. 2) and x = 1, then output will be:
6

Constraints:
------------
1 <= n <= 10^5
- 2 * 10^9 <= Li <= 2 * 10^9, i = (1,2,3,...,n)
Value contained in nodes will be even number.
(Hence when even number of elements in L, median M will be an integer. (even + even) / 2 will result in an integer value. So answer will always be integer (never float).)

Sample Test Case:
-----------------
Sample Input:
L: 2 -> 4 -> 6 -> 8 -> 10
ptr: Pointer of the node containing value 4.

Sample Output:
6

Explanation:
------------
There are 5 nodes in L hence median M will be the value of 3rd node, which is 6.

Notes:
Expected solution: Linear time complexity with constant extra space.

Maximum time allowed in interview: 20 Minutes.

Due to some HackerRank limitations currently we are providing code-stubs only in C, C++, C++ 14, C#, Java 7, Java 8, JavaScript, Python 3 and Swift.

'''

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

def find_first_big(ptr):
    ######
    if ptr.val < ptr.next.val:
        return ptr.next
    
    curr = ptr.next
    
    while curr != ptr:
        if curr.val < curr.next.val:
            return curr.next
        curr = curr.next
        
    return None

def find_smallest(ptr):
    ######
    if ptr.val > ptr.next.val:
        return ptr.next
    
    curr = ptr.next
    
    while curr != ptr:
        if curr.val > curr.next.val:
            return curr.next
        curr = curr.next
    
    return None

def is_ascending(ptr):
    if ptr.val > ptr.next.val:
        return False
    
    curr = ptr.next
    while curr.next != ptr:
        if curr.val > curr.next.val:
            return False
        curr = curr.next
        
    return True

def find_length(ptr):
    ######
    length = 1
    curr = ptr.next
    
    while curr != ptr:
        length += 1
        curr = curr.next

    return length
    
def find_median(ptr): ## starting function
    
    length = find_length(ptr)
    
    smallest = find_smallest(ptr)
    # if all elements in the list have same value, return value of any element
    if smallest == None:
        return ptr.val
    
    head = None
    # take smallest element and find if the sequence is ascending or descending?
    if is_ascending(smallest):
        head = smallest
    else:
        head = find_first_big(ptr)
    
    if length % 2 == 0:
        middle = length // 2
    else:
        middle = (length // 2) + 1
    
    i = 1
    curr = head
    while i < middle:
        i += 1
        curr = curr.next
    
    if length % 2 == 0:
        return (int)((curr.val + curr.next.val) // 2)
    else:
        return curr.val
    
def find_median_v1(ptr):
    # edge/special cases:
    if ptr.next == ptr:
        return ptr.val
    elif ptr.next.next == ptr:
        return (int)((ptr.val + ptr.next.val) / 2)

    # 2 things to find for finding the median:
    # 1. Find the head of the linked list
    # 2. Find the length of the list
    
    curr = ptr.next
    prev = ptr
    l2h_cnt = 0
    h2l_cnt = 0
    l2h = False
    h2l = False
    l2h_node = None
    h2l_node = None
    length = 0

    # -10 -> 0 -> 10
    while True:
        if curr.val > prev.val:
            l2h = True
            l2h_cnt += 1
            if h2l == True and l2h_node == None:
                l2h_node = curr
            h2l = False
        elif curr.val < prev.val:
            h2l = True
            h2l_cnt += 1
            if l2h == True and h2l_node == None:
                h2l_node = curr
            l2h = False
        else:
            #equal
            if l2h == True:
                l2h_cnt += 1
            elif h2l == True:
                h2l_cnt += 1
        
        length += 1
        
        if curr == ptr:
            break
        
        prev = curr
        curr = curr.next
            
    if l2h_cnt > h2l_cnt:
        # ascending order
        head = h2l_node
    elif h2l_cnt > l2h_cnt:
        # descending order
        head = l2h_node
    else:
        # we don't know, any order is fine?
        # choose any one which is valid
        if h2l_node != None:
            head = h2l_node
        else:
            head = l2h_node

    if not head:
        head = ptr

    #print(length)
    #print(head.val)
    
    curr = head
    if length % 2 != 0:
        middle = (length // 2) + 1
    else:
        middle = length // 2
    
    i = 1
    while i < middle:
        curr = curr.next
        i += 1
    
    if length % 2 == 0:
        #print("curr.val {} curr.next.val {}".format(curr.val, curr.next.val))
        median = (curr.val + curr.next.val) // 2
    else:
        #print("curr.val {}".format(curr.val))
        median = curr.val
    
    return int(median)

'''
# Another approach:

def find_med(head):
    slow = head
    fast = head
    prev = None
    flag = True
    
    while flag or (fast!=head and fast.next!=head):
        flag = False
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    if fast.next == head: # odd length
        return slow.val
    elif fast == head: # even length
        return (slow.val + prev.val)//2
 

def find_start_pt(ptr,order):
    curr = ptr
    if order == 1:
        while curr.val <= curr.next.val and curr.next!=ptr:
            curr = curr.next
        start = curr.next
        return start
    else:
        while curr.val >= curr.next.val and curr.next!=ptr:
            curr = curr.next
        start = curr.next
        return start
    
def find_order(ptr):
    order = 0
    curr = ptr
    asc=0
    desc=0
    
    while curr.next != ptr:
        if curr.val < curr.next.val:
            asc+=1
        elif curr.val > curr.next.val:
            desc+=1
        if asc ==2:
            return 1
        if desc == 2:
            return 0
        curr=curr.next
            
def find_median(ptr):
    order = find_order(ptr)
    # ascending = 0, descending = 1
    head = find_start_pt(ptr,order)
    return find_med(head)
'''
