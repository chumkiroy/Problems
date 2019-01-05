'''
Longest Substring With Balanced Parentheses





Problem Statement:



Given a string named brackets containing only '(' and ')'. You have to find the length of the longest sub-string that has balanced parentheses. We only need length, not the sub-string itself.



Input Format:



There is only one argument in input, denoting string named brackets.



Output Format:



Return an integer, denoting the length of the longest sub-string that has balanced parentheses.



Constraints:



1 <= |brackets| <= 10^5
Input string only contains '(' and ')' characters.


Sample Test cases:



Sample Input 1:



"((((())(((()"



Sample Output 1:



4



Explanation 1:



"(())"



Sample Input 2:



"()()()"



Sample Output:2:



6



Explanation 2:



"()()()"




'''

def find_max_length_of_matching_parentheses(brackets):
    stack = [-1]
    length = 0
    max_length = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) > 0:
                length = i - stack[-1]
                max_length = max(max_length, length)
            else:
                stack.append(i)
    return max_length

print find_max_length_of_matching_parentheses("((((())(((()")
