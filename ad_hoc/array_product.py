'''
Array Product

Problem Statement:
------------------
Given an array of numbers nums of size n, find an array of numbers products of size n, such that products[i] is the product of all numbers nums[j], where j != i.

Input/Output Format For The Function:
-------------------------------------
Input Format:
There is only one argument: nums, denoting input array.

Output Format:
Return an array of numbers products, denoting the required product array.

Input/Output Format For The Custom Input:
-----------------------------------------
Input Format:
The first line of the input should contain a single integer n denoting the size of input array.
In the next n lines, each line should contain a number Ai, denoting ith number of the input array A, (1<=i<=N).
If n = 5 and nums = [1, 2, 3, 4, 5], then input should be:
5
1
2
3
4
5

Output Format:
There will be n lines, each line containing a number Pi, denoting ith number of the resultant product array P.
For input n = 5 and nums = [1, 2, 3, 4, 5], output will be:
120
60
40
30
24

Constraints:
------------
You can't use division anywhere in solution
2 <= n <= 100000
-2147483648 <= nums[i] <= 2147483647, i=1,2,3,...,n
-2147483648 <= products[i] <= 2147483647, i=1,2,3,...,n

Notes:
------
Usage of resultant products array will not be considered as extra space used.
Without using division is the key constraint to remember.

Sample Test Cases:
------------------
Sample Input 1:
5
1
2
3
4
5

Sample Output 1:
120
60
40
30
24

Explaination 1:

Resultant Product array products = [products[1], products[2], products[3], products[4], products[5]]
               = [(nums[2]*nums[3]*nums[4]*nums[5]), (nums[1]*nums[3]*nums[4]*nums[5]), (nums[1]*nums[2]*nums[4]*nums[5]), (nums[1]*nums[2]*nums[3]*nums[5]), (nums[1]*nums[2]*nums[3]*nums[4])]
               = [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
               = [120, 60, 40, 30, 24]

Sample Input 2:
3
4
9
10

Sample Output 2:
90
40
36

Explaination 2:

Resultant Product array products = [products[1], products[2], products[3]]
                         = [(nums[2]*nums[3]), (nums[1]*nums[3]), (nums[1]*nums[2])]
                         = [(9*10), (4*10), (4*9)]
                         = [90, 40, 36] 

Suggestions:
Suggested time: 20 minutes.

'''
def get_p1(p1, nums, n):

    p1[0] = nums[0]

    for i in range(1, n):

        p1[i] = p1[i-1] * nums[i]


    return p1


def get_p2(p2, nums, n):

    p2[n-1] = nums[n-1]

    for i in reversed(range(n-1)):

        p2[i] = p2[i+1] * nums[i]

    return p2



def getProductArray(nums):

    n =  len(nums)

    p = [None] * n

    p1 = [None] * n

    p2 = [None] * n


    
get_p1(p1, nums, n)

    get_p2(p2, nums, n)


    
p[0] = p2[1]

    p[n-1] = p1[n-2]


    for i in range(1, (n-1)):

        p[i] = p1[i-1] * p2[i+1]

    return p

nums = [3, 4, 9, 10]
print getProductArray(nums)