'''
3 Sum

Problem Statement:

Given an array of N integers, find all triplets that sum to 0 (zero).

Triplets may or may not be consecutive numbers.
The array can include duplicate elements.
Array is not necessarily sorted.
Print output as shown. i.e. as strings, one per line, comma separated elements. See sample for clarity.
Order of elements inside the answer triplets does not matter. i.e. if your output elements are the same, but only in different order, then it's an acceptable solution.
Do not print duplicate triplets. Eg: 1,1,-2 and 1,-2,1 are duplicates.
If no such triplets are found, then print nothing.


Input Format:
-------------
Integer array
Input may or may not be sorted
Repeats possible

Output Format:
--------------
Return a String array containing all possible triplets who sum to 0. One String for one triplet.
Order of output does not matter. 

Constraints:
------------
1 <= N <= 2000
-10^3 <= element <= 10^3
Given array may contains duplicate numbers.

Sample Test Case:
-----------------

Sample Input-1:
arr = [10, 3, -4, 1, -6, 9];

Sample Output-1:
10,-4,-6
3,-4,1

Sample Input-2:
arr = [12, 34, -46];

Sample Output-2:
12,-46,34

Sample Input-3:
arr = [0, 0, 0];

Sample Output-3:
0,0,0

Sample Input-4:
arr = [-2, 2, 0 -2, 2];

Sample Output-4:
2,-2,0

'''

def findZeroSum(arr):
    res = []
    arr.sort()
    for i,n in enumerate(arr):
        if n <= 0:
            if i > 0 and arr[i] == arr[i-1]:
                continue
            l = i+1
            r = len(arr)-1
            while l < r:
                three_sum = n+arr[l]+arr[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append("{0},{1},{2}".format(n,arr[l],arr[r]))
                    l += 1
                    r -= 1
                    while l <= len(arr)-1 and arr[l] == arr[l-1]:
                        l += 1
                    while r >= 0 and arr[r]==arr[r+1]:
                        r -= 1
    return res

arr = [10, 3, -4, 1, -6, 9];
print findZeroSum(arr)
