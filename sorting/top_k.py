'''
Top K

Problem Statement:

You are given an array of integers which is analogous to a continuous stream of input. Find K largest elements from a given stream of numbers. By definition, we don't know the size of the input stream. Hence produce K largest elements seen so far, at any given time. For repeated numbers, return them only once.

If there are less than K unique elements, return all of them.

Note:
Represent input stream as an array. Don't rely on its size.
Feel free to use built-in functions if you need a specific data-structure.

Input Format:
Integer array
Repeats are possible
Input may or may not be sorted

Output Format:
Return an integer array containing K largest elements. If there are less than K unique elements, return all of them. If there are duplicates, return only one instance.
Order of output does not matter.


Constraints:
1 <= N <= 10^5
1 <= K <= 10^5

Given array may contain duplicate numbers.

Sample Test Case:

Sample Input-1:
arr = [1, 5, 4, 4, 2]; k = 2

Sample Output-1:
[4, 5]

Sample Input-2:
arr = [1, 5, 1, 5, 1]; k = 3

Sample Output-2:
[5, 1]

'''

'''
 * Complete the function below.
 * Please store the size of the int array to be returned in result_size pointer. For example,
 * int a[3] = {1, 2, 3};
 * *result_size = 3;
 * return a;
 * 
'''

import heapq

def topK(arr, k):
    lst = list(set(arr))
    heap = []
    for i in range(k):
        if i < len(lst):
            heapq.heappush(heap, lst[i])

    for i in range(k,len(arr)):
        if i < len(lst):
            heapq.heappushpop(heap,lst[i])

    return heap

print topK([1,5,1,5,1], 3)
