'''
Merge K sorted arrays, size N each

Problem Statement:

This is a popular facebook problem. Given K sorted arrays of size N each, merge them and print the sorted output. Assume N is very large compared to K. N may not even be known. The arrays could be just sorted streams, for instance, timestamp streams.

All arrays might be sorted in increasing manner or decreasing manner. Sort all of them in the manner they appear.

Don't use inbuilt sorts or any standard sorting algorithm after simply merging the lists.

Note:
Repeats are allowed.
Negative numbers and zeros are allowed.
Assume all arrays are sorted in the same order. Preserve that sort order in output.
It is possible to find out the sort order from at least one of the arrays.

Input Format:
2-D Integer array
Repeats possible
Individual integer array is sorted

Output Format:
Return an integer array containing all elements from all individual arrays combined.

Constraints:
2 <= N <= 500
1 <= K <= 500
-10^6 <= element <= 10^6

Sample Test Case:

Sample Input-1:
K = 3, N =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Sample Output-1:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

'''

import heapq
def mergeArrays(arr):
    heap = []
    merged_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            heapq.heappush(heap, arr[i][j])
            
    for i in range(len(heap)):
        merged_arr.append(heapq.heappop(heap))
            
    return merged_arr

arr = [[1,3,5,7], [2,4,6,8], [0,9,10,11]]
print mergeArrays(arr)
