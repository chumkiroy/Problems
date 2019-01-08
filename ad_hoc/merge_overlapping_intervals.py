'''
Merge Overlapping Intervals

Problem Statement:
------------------
Given an array of time intervals(in any order) inputArray of size n, merge all overlapping intervals into one and output the resulting array,
such that no two intervals in result array are overlapping. In other words, result array should contain only mutually exclusive intervals.
(In this problem, you should consider all the intervals as closed intervals. i.e. endpoints of intervals are inclusive.) 

Input Format:
-------------
There is only one argument: inputArray, denoting input array of time intervals,
where inputArray is 2D array of n*2 size, denoting inputArray[i][0] as start point of ith interval, and inputArray[i][1] as end point of ith interval

Output Format:
--------------
Return an array of time intervals outputArray, denoting the required array of merged time intervals,
where outputArray is 2D array of n*2 size, denoting outputArray[i][0] as start point of ith interval, and outputArray[i][1] as end point of ith interval
(order of intervals in outputArray doesn't matter)

Constraints:
------------
1 <= n <= 105
-109 <= inputArray[0][i], inputArray[1][i] <= 109,  i=0, 1, ..., (n-1)
inputArray[0][i] <= inputArray[1][i], i=0, 1, ..., (n-1)

Sample Test Cases:
------------------
Sample Input 1:
4
2
1 3
5 7
2 4
6 8

Sample Output 1:
1 4
5 8

Explanation 1:
The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1,4}.
Similarly {5,7} and {6,8} should be merged and become {5,8}.


Sample Input 2:
7
2
100 154
13 47
1 5
2 9
7 11
51 51
47 50

Sample Output 2:
1 11
13 50
51 51
100 154

Explanation 2:
The intervals {1,5} and {2,9} overlap with each other, so they should be merged and become {1,9}.
Also, {1,9} and {7,11} overlap with each other, so they should be merged and become {1,11}
Similarly, The intervals {13,47} and {47,50} should be merged and become {13,50}.
Intervals {51,51} and {100,154} are kept as it is as they are not overlapping with any other intervals.

'''

def getMergedIntervals(inputArray):
    sorted_intervals = sort_intervals(inputArray)
    return merge_intervals(sorted_intervals)
    
def merge_intervals(sorted_intervals):
    res = []
    start_ival = 0
    while start_ival < len(sorted_intervals):
        cur_ival = start_ival+1
        if cur_ival == len(sorted_intervals) or sorted_intervals[cur_ival][0] > sorted_intervals[start_ival][1]:
            res.append(sorted_intervals[start_ival])
        else:
            ends = [sorted_intervals[start_ival][1]]
            while cur_ival < len(sorted_intervals) and sorted_intervals[cur_ival][0] <= max(ends):
                ends.append(sorted_intervals[cur_ival][1])
                cur_ival += 1
        
            res.append([sorted_intervals[start_ival][0], max(ends)])
        start_ival = cur_ival
    return res

def sort_intervals(inputArray):
    return sorted(inputArray, key=sort_start)
    
def sort_start(interval):
    return interval[0]

inputArray = [[1,3], [5,7], [2,4], [6,8]]
print getMergedIntervals(inputArray)
    
'''
def getMergedIntervals(inputArray):
    #print(inputArray)
    iA = sorted(inputArray, key=lambda x: x[0])
    #print(iA)
    results = []
    
    min_ = iA[0][0]
    max_ = iA[0][1]
    for x,y in iA[1:]:
        if x <= max_ or x <= min_:
            max_ = max(max_, y)
        else:
            results.append((min_, max_))
            min_ = x
            max_ = y
    
    if not results or results[-1] != (min_, max_):
        results.append((min_, max_))
    return results
'''
