'''
Minimum Element In A Sorted And Rotated Array

Problem Statement:
------------------
You are given a sorted array arr which is rotated by unknown pivot k. You need to find minimum element from given array using fastest possible way which uses only constant space.

Input Format:
-------------
Only argument for function, integer array named arr.

Output Format:
-------------
Return integer which is minimum element in given array.

Constraints:
------------
1 <= n <= 10^5 where n is number elements in given array.

Every element of array will be unique.

For every element arr[i],

-10^9 <= arr[i] <= 10^9 where 0 <= i <= (n-1)

Sample Test Case:
-----------------
Sample Input: arr = [ 4, 5, 6, 7, 8, 1, 2, 3]
Sample Output: 1

Explanation:
For given arr = [ 4, 5, 6, 7, 8, 1, 2, 3] which is sorted in ascending order and right rotated by pivot 5 has minimum value as 1 at index 5.

'''

# The function accepts INTEGER ARRAY as parameter.
# Return INTEGER.
#
def find_minimum(arr):
    #order = findorder(arr) # 1 = asc, -1= desc
    val1 = find_min1(arr,0,len(arr)-1)
    val2 = find_min2(arr,0,len(arr)-1)
    if val1==None:
        return val2
    if val2 == None:
        return val1
    return min(val1,val2)

def find_min1(arr,st,ed):
    if st == ed:
        return arr[st]
    if ed-st==1:
        return min(arr[st],arr[ed])
    mid = st + (ed-st)//2
    
    # one half will definitely be in order
    if arr[st] < arr[mid]: # 1st half in order
    
        if arr[mid] < arr[ed]: # perfect non-rotated ascending order
            return arr[st]
            
        else: 
			# go right, 2nd half out of order and arr[ed]<arr[mid] this means right half definitely has element smaller
            # exclude mid as u definitely know right has smaller element
            return find_min1(arr,mid+1,ed)
            
    elif arr[mid] < arr[ed]: 
		# 2nd half in order, 1st half not in order
        # include mid as u dont know if mid itself is smallest 
        return find_min1(arr,st,mid) # go left, probably a smaller element in left side

def find_min2(arr,st,ed):
    
    if st == ed:
        return arr[st]
    if ed-st==1:
        return min(arr[st],arr[ed])
    mid = st + (ed-st)//2
    
    # one part will definitely be in order
    if arr[st] > arr[mid]: # 1st half in order
        if arr[mid] > arr[ed]: # perfect non-rotated descending order
            return arr[ed]
        else:
            return find_min2(arr,mid,ed) 
			# go right, 2nd half out of order and arr[ed]>arr[mid] 
			# this means right half probably has element smaller, 
			# include mid as mid itself maybe smallest
            
    elif arr[mid] > arr[ed]: 
		# this means 2nd part is in desc order. if it is, then we 
		# already checked for arr[st]>arr[mid] in first if loop. 
		# If that is not true then it means that there are elemnst 
		# lower than this part to left. If there were higher, 
		# then the first if loop would have been true
        return find_min2(arr,st,mid-1) # go left

arr = [ 4, 5, 6, 7, 8, 1, 2, 3]
print find_minimum(arr)

'''
def find_min_helper(arr, st, end, min_sofar):
    
    if st == end:
        return min(arr[st], min_sofar)
    if st > end:
        return min_sofar
    
    mid_idx = st + (end - st) // 2 # use // for floor division
    mid = arr[mid_idx]
    
    if mid < min_sofar:
        min_sofar = mid
    
    if mid_idx - 1 > 0:
        left_min = min(arr[st], arr[mid_idx - 1])
    else:
        left_min = arr[st]
    
    if mid_idx + 1 < len(arr):
        right_min = min(arr[mid_idx + 1], arr[end])
    else:
        right_min = arr[end]
    
    if left_min < right_min and left_min < min_sofar:
        return find_min_helper(arr, st, mid_idx - 1, min_sofar)
    elif right_min < left_min and right_min < min_sofar:
        return find_min_helper(arr, mid_idx + 1, end, min_sofar)
    else:
        return min_sofar

def  find_minimum(arr):
    return find_min_helper(arr, 0, len(arr) - 1, float('inf'))
'''
