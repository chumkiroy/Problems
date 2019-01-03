'''
PROBLEM STATEMENT: Merge Two BSTs

Given two BSTs (Binary Search Trees), one with N1 number of nodes and other one with N2 number of nodes.

Your task is to merge them such that:
   - Resultant tree is height balanced.
   - Resultant tree is a BST.
   - Resultant tree contains all values from given BST-1.
   - Resultant tree contains all values from given BST-2.
   - Size of the resultant tree is N1 + N2.
   - For any value, no of occurrences in resultant tree = no of occurrences in BST-1 + no of occurrences in BST-2. (If BST-1 contains 3 nodes with value 50 and BST-2 contains 4 nodes with value 50, then resultant tree should contain exactly 7 nodes with value 50.)

Any resultant tree, satisfying all the above conditions will be considered as valid answer.

Input Format:
-------------
There are two arguments, first one is the root of the first BST with N1 number of nodes and second one is the root of the second BST with N2 number of nodes.

Output Format:
--------------
Return root of the resultant BST.

Constraints:
------------
1 <= N1, N2 <= 100000
Node value of the BSTs: 1 <= key1, key2 <= 1000000000
You are not allowed to modify the structure of the given BSTs.

Sample Test Case:
-----------------
Sample Input:

Tree-1: 
  1
   \ 
    2
     \
      3

Tree-2: 
   7
  /  \
 6   8

Sample Output:
(one possible resultant tree)
    6
   /  \
  2   7
 /  \   \
1   3   8

'''

def merge(a1, a2):
    m = len(a1)
    n = len(a2)
    i = 0
    j = 0
    a3 = []
    while i < m and j < n:
        if a1[i] <= a2[j]:
            a3.append(a1[i])
            i += 1
        else:
            a3.append(a2[j])
            j += 1
            
    if i < m:
        a3.extend(a1[i:])
    if j < n:
        a3.extend(a2[j:])
        
    return a3
    
def _storeInorder(lst, node):
    if node == None:
        return 
    _storeInorder(lst, node.left)
    lst.append(node.val)
    _storeInorder(lst, node.right)
    return lst
    
def storeInorder(node):
    lst = _storeInorder([], node)
    return lst
    
def arrToBst(arr, start, end):
    if start > end:
        return None
    mid = start + ((end-start)/2)
    node = Node(arr[mid])
    node.left = arrToBst(arr, start, mid-1)
    node.right = arrToBst(arr, mid+1, end)
    
    return node

def  mergeTrees(node1, node2):
    if not node1 and not node2:
        return None
    if not node1:
        return node2
    if not node2:
        return node1
        
    arr1 = storeInorder(node1)
    arr2 = storeInorder(node2)
    
    arr3 = merge(arr1, arr2)
    
    node = arrToBst(arr3, 0, len(arr3)-1)
    
    return node 

'''
Another approach:

class Node:
    def __init__(self, key): 
        self.key = key  
        self.left = None  
        self.right = None

def get_array(root,a):
    
    if root is None:
        return 
    get_array(root.left,a)
    a.append(root.key)
    get_array(root.right,a)

def merge(a1,a2):
    
    n1, n2 = len(a1),len(a2)
    n3 = n1+n2
    a3 = [None]*n3
    
    i = 0
    j = 0 
    k = 0
    while True:
        if i==n1 or j==n2:
            break
        
        if a1[i] < a2[j]:
            temp = a1[i]
            i += 1
        else:
            temp = a2[j]
            j += 1
        a3[k] = temp 
        k+= 1
            
    while i < n1:
        a3[k] = a1[i]
        i+= 1
        k+= 1
    
    while j < n2:
        a3[k] = a2[j]
        j+= 1
        k+= 1
        
    return a3
        
def make_btree(a,start,end):
    if start > end:
        return None
    
    mid = (start+end)/2
    root = Node(a[mid])
    
    root.left = make_btree(a,start,mid - 1)
    root.right = make_btree(a,mid+1,end)
    
    return root 
    
# Complete this function and return root of the BST
def mergeTwoBSTs(root1, root2):
    
    a1,a2 = [],[]
    get_array(root1,a1)
    get_array(root2,a2)
    a3 = merge(a1,a2)
    
    return make_btree(a3,0,len(a3)-1)
'''
