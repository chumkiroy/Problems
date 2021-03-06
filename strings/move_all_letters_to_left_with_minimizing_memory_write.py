'''
Move All Letters To Left Side With Minimizing Memory Writes

Problem Statement:
------------------
You're given a string s, which may contain alphabet letters ('a' - 'z' or 'A' - 'Z') as well as numerical characters ('0' - '9'), in random order.

Numerical characters are garbage characters and we don't care about them. 

Inside the same string, you have to make alphabet letters appear on left side, in the same order they appeared in given s.

Suppose in our architecture memory write is very expensive operation, so we have to minimize the memory write operations. As digits are garbage characters we need not to move them on the right side (Here we can save some memory writes!). Only need is that all the letters should appear on the left side. 

One example will make it more clear.

Suppose s = "1x", now if we transform it to "xx" then it will do 1 memory write, but if we transform it to "x1" then it will do 2 memory writes, so output should be "xx". ("xx" has all the letters from original string on the left side and also it minimizes the memory writes!)

Input Format:
-------------
There is only one argument denoting string s.

Output Format:
--------------
Return s after moving all the letters to left side, using minimum number of memory write operations.

Constraints:
------------
1 <= |s| <= 10^5
s will contain characters from only 'a' - 'z', 'A' - 'Z' or '0' - '9'.
Original order of letters needs to be preserved.
Numbers need not to be preserved. 
An in-place linear solution is expected.
Have to minimize the memory writes.
For languages that have immutable strings, convert the input string into a Character Array and work in-place on that array. Convert it back to the string before returning. (For the purpose of this problem, ignore the extra linear space used in that conversion, as long as you're only using constant space after conversion to character array)


Sample Test Case:
-----------------

Sample Input: "0a193zbr"
Sample Output: "azbr3zbr" 
Explanation:
In the given string letters are a, z, b and r. We can move all four letters to left side with 4 write operations and get string "azbr3zbr". For any other string it will take more than four write operations so "azbr3zbr" is the ans.

'''

def move_letters_to_left_side_with_minimizing_memory_writes(s):
    lst = list(s)
    write = 0
    i = 0
    while i < len(lst):
        if lst[i].isalpha() and i == write:
            i+=1
            write += 1
        elif lst[i].isalpha() and write < i:
            lst[write] = lst[i]
            write += 1
            i += 1
        else:
            i+= 1
    return ''.join(lst)
            
print move_letters_to_left_side_with_minimizing_memory_writes("0a193zbr")
