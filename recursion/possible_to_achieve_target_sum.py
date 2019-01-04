'''
Possible To Achieve Target Sum?

Problem Statement:
------------------
Given an array arr of size n and a target sum k. 

You have to determine, whether there exists a group of numbers (numbers need not to be contiguous and group can not be empty) in arr such that their sum equals to k.

Input Format:
-------------
There are two argument. First one is arr and second one is k.

Output Format:
--------------
Return a boolean denoting your answer.  

Constraints:
------------
1 <= n <= 18
-10^17 <= arr[i], k <= 10^17

Sample Test Cases:
------------------
Sample Input 1: arr = [2 4 8]
				k = 6

Sample Output 1: True

Explanation 1: arr[0] + arr[1] = 6


Sample Input 2: arr = [2 4 6]
				k = 5

Sample Output 2: False

Explanation 2:

There does not exists any group such that its sum equals to k.

'''

def check_if_sum_possible(arr, k):
    res = []
    out = [''] * len(arr)
    subset_sum(res, arr, 0, out, 0, [], k)
    #print('--',k)
    #print(res)
    return True if res else False
    
def subset_sum(res, inp, i, out, j, sum_so_far, k):
    if sum(sum_so_far) == k and len(sum_so_far) > 0:
        if len(out[:j]) > 0:
            res.append(out[:j])
        return
    if i == len(inp):
        return
    subset_sum(res, inp, i+1, out, j, sum_so_far, k)
    out[j] = inp[i]
    subset_sum(res, inp, i+1, out, j+1, sum_so_far + [inp[i]], k)

arr = [2, 4, 8]
k = 6

print check_if_sum_possible(arr, k)
