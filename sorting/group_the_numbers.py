'''
Group the numbers 

Problem Statement:
You are given an array of non-negative integers only. Group them in-place into evens and odds in such a way that all evens appear on the left side and all odds on the right side.

Input Format:
0 <= element <= 10^9
Integer array
Repeats possible.

Output Format:
Return the same integer array, with evens on left side and odds on the right side. There is no need to preserve order within odds or within evens.

Constraints:
1 <= n <= 10^5
Given array may contain duplicate numbers.
Solutions with linear time complexity and constant auxiliary space is expected.

Sample Test Case:

Sample Input: [1, 2, 3, 4]
Sample Output: [4, 2, 1, 3]

Explanation:
Order does not matter. Other valid solutions are
[2, 4, 1, 3]
[2, 4, 3, 1]
[4, 2, 3, 1]

'''

def is_even(num):
    return True if num%2 == 0 else False
    
def solve(arr):
    if len(arr) < 2:
        return arr
    i = 0
    j = len(arr)-1
    while i < j:
        if is_even(arr[i]):
            i += 1
        elif not is_even(arr[j]):
            j -= 1
        elif not is_even(arr[i]) and is_even(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return arr

print solve([1, 2, 3, 4])
