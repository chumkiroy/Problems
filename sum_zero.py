'''
Sum Zero





Problem Statement:



Given an array of integers arr of size n, find a subarray whose sum is zero.



Input Format:



There is only one argument, arr denoting input array



Output Format:



Return an array of integer res of size 2, where res[0] and res[1] denotes start index and end index(0 based indexing)

(both inclusive) respectively of zero sum subarray, as asked in problem


Note:

If there is no such subarray, then return array res of size one and res[0] = -1
If there are multiple such subarray, then return indices of any one of them
If a matching subarray is a subarray of a larger matching subarray, then return indices of either one
If there is a number '0' in the array arr, then it counts as a valid sum zero subarray


Constraints:



1 <= n <= 10^6

-10^9 <= arr[i] <= 10^9, (i = 0,1,...,(n-1))



Sample Test Cases:



Sample Input 1:



6

5

1

2

-3

7

-4



Sample Output 1:



1

3



Explanation 1:



For given input array arr, arr[1]+arr[2]+arr[3] = 1+2+(-3) = 0. So, subarray starting from index 1 upto index 3

(0 based indexing) is sum zero subarray.

(3,5 and 1,5 are the other correct solutions)



Sample Input 2:



5

1

2

3

0

-9



Sample Output 2:



3

3



Explanation 2:



For given input array arr, arr[3] = 0. So, subarray starting from index 3 upto index 3 (0 based indexing) is sum zero

subarray.

'''

def sumZero(arr):
    d= dict()
    d[0] = -1
    s= 0
    ret = []
    for i in range(len(arr)):
        s+=arr[i]
        if s in d:
            ret.extend([d[s]+1,i])
            return ret
        d[s]=i
    return [-1]

arr = [1,2,3,0,-9]
print sumZero(arr)
