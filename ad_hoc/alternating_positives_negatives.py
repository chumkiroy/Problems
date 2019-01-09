'''
Alternating Positives and Negatives

Problem Statement:
------------------
Given an array named array of size n, that contains both positive and negative numbers. Rearrange the array elements so that positive and negative numbers appear alternatively in the output. The order in which the positive elements appear should be maintained. Similarly, the order in which the negative elements appear should also be maintained.

Number of positive and negative integers may not be equal and extra positives or negatives have to appear in the end of the array.

Input Format:
-------------
There is only one argument in input, denoting integer array named array.

Output Format:
--------------
Return an integer array with alternate positive and negative numbers with order maintained.

Constraints:
------------
1 <= n <= 500000
-2 * 10^9 <= array[i] <= 2 * 10^9
Consider 0 as a positive integer for this particular question.
Start the array with the positive integer unless all the integers in the input array are negative.

Sample Test Case:

Sample Input: array = [2 3 -4 -9 -1 -7 1 -5 -6]

Sample Output: [2 -4 3 -9 1 -1 -7 -5 -6]

Explanation:
Order of positive integers in the input array is [2 3 1] which is similar to order of positive integers in the output array.

Order of negative integers in the input array is [-4 -9 -1 -7 -5 -6] which is similar to order of negative integers in the output array.

The output array starts with a positive integer and keeps alternating with negative integers until all positive integers are exhausted. Rest of the output array is filled with leftover negative integers.

'''

def alternating_positives_and_negatives(array):
    if len(array) < 2:
        return array
        
    res = []
    pos = 0
    neg = 0
    idx = len(array)
    for i in range(len(array)):
        while pos < len(array) and array[pos] < 0:
            pos += 1
        while neg < len(array) and array[neg] >= 0:
            neg += 1
        
        if pos == len(array):
            res.append(array[neg])
            neg += 1
        elif neg == len(array):
            res.append(array[pos])
            pos += 1
        else:
            if i % 2 == 0 and pos < len(array):
                res.append(array[pos])
                pos += 1
            elif i % 2 == 1 and neg < len(array):
                res.append(array[neg])
                neg += 1
    
    
    return res

array = [2, 3, -4, -9, -1, -7, 1, -5, -6]
print alternating_positives_and_negatives(array)
