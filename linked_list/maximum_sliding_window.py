'''
Maximum In Sliding Window

Problem Statement:
------------------
An integer array named arr is given to you. Size of arr is n and assume that it is very large.

There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. You have to find maximum number in the window each time. 

Input Format:
-------------
There are two arguments in input. First is an integer array arr. Second is the window width w.

Output Format:
--------------
Return an array, where i-th number of the returned array contains the maximum number from arr[i] to arr[i+w-1].

Constraints:
------------
1 <= n <= 10^5
-2 * 10^9 <= arr[i] <= 2 * 10^9
1 <= w <= n

Sample Test Case:
-----------------
Sample Input:
arr = [1 3 -1 -3 5 3 6 7]
w = 3

Sample Output:
[3, 3, 5, 5, 6, 7]

Explanation:
Window Position -> Max
1) [1 3 -1] -3 5 3 6 7 -> 3
2) 1 [3 -1 -3] 5 3 6 7 -> 3
3) 1 3 [-1 -3 5] 3 6 7 -> 5
4) 1 3 -1 [-3 5 3] 6 7 -> 5
5) 1 3 -1 -3 [5 3 6] 7 -> 6
6) 1 3 -1 -3 5 [3 6 7] -> 7

'''

def max_in_sliding_window(arr, w):
    
    maximum = max(arr[0:w])
    output = [maximum]
    for i in range(w,len(arr)):
        out = arr[i-w]
        if out == maximum:
            maximum = max(arr[i-w+1:i+1])
        else:
            new = arr[i]
            if new > maximum:
                maximum = new
        output.append(maximum)
        
    return output

arr = [1, 3, -1, -3, 5, 3, 6, 7]
w = 3
print max_in_sliding_window(arr, w)

'''
# max in sliding window: brute force
def max_in_sliding_window(arr, w):
    i = 0
    l = []
    while i+w <= len(arr):
        max_val = max(arr[i:i+w])
        l.append(max_val)
        i += 1
    return l
'''
