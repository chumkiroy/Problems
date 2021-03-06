'''
Add Two Numbers

Write a function which adds two numbers a and b, represented as linked lists of size lenA and lenB respectively, and returning the sum c in form of a new linked list.

Ignoring the allocation of a new linked list, try to use constant memory when solving it.

A number is represented by a linked list, with the head of the linked list being the least significant digit. For example 125 is represented as 5->2->1, and 371 is represented as 1->7->3. Adding 5->2->1(125) and 1->7->3(371) should produce 6->9->4(496).

Input Format
There will be two arguments l_a and l_b, denoting linked lists representing numbers a and b respectively

Output Format
Return result denoting head node of resultant sum linked list.

Constraints
1<= lenA, lenB <= 100000
Numbers represented by l_a and l_b will always be non-negative.
As digits of number can be [0-9], nodes of linked list l_a and l_b will always have number [0-9].
If a or b is 0, then corresponding linked list will contain only one node having value 0. For values greater than 0, there will not be any leading zeros. Same for expected output. If answer is 0, then there must be only one node having value 0 and if answer is greater than 0, then there must not be any leading zeros.

Sample Test Cases

Sample Test Case 1
Sample Input 1
l_a = 7->5->2
l_b = 2->0->3

Sample Output 1
result = 9->5->5

Explanation 1
As l_a = 7->5->2 means number 257 and l_b = 2->0->3 means number 302. Sum of 257 and 302 is 559 so, result will represent 9->5->5.

Sample Test Case 2
Sample Input 2
l_a = 5->8->3
l_b = 9->4->1

Sample Output 2
result = 4->3->5

Explanation 2
As l_a = 5->8->3 means number 385 and l_b = 9->4->1 means number 149. Sum of 385 and 149 is 534 so, result will represent 4->3->5.

'''

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

def  addNumbers(l1, l2):
        n = 0
        a = 0
        l = None
        res = None
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        while l1 and l2:
            a = l1.val + l2.val + n
            node = LinkedListNode(int(a % 10))
            if not l:
                l = node
                res = l
            else:
                l.next = node
                l = l.next
            n = int(a / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            a = l1.val + n
            node = LinkedListNode(int(a % 10))
            l.next = node
            l = l.next
            n = int(a / 10)
            l1 = l1.next
        while l2:
            a = l2.val + n
            node = LinkedListNode(int(a % 10))
            l.next = node
            l = l.next
            n = int(a / 10)
            l2 = l2.next
        if n > 0:
                node = LinkedListNode(n)
                l.next = node
        return res
