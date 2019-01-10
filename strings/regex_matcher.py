'''
Regex Matcher

Problem Statement:
------------------
Given a text string containing characters only from lowercase alphabetic characters and a pattern string containing characters only from lowercase alphabetic characters and two other special characters '.' and '*'.

Your task is to implement pattern matching algorithm that returns true if pattern is matched with text otherwise returns false. The matching must be exact, not partial.

Explanation of the special characters:
--------------------------------------
1) '.' - Matches a single character from lowercase alphabetic characters.
2) '*' - Matches zero or more preceding character. It is guaranteed that '*' will have one preceding character which can be any lowercase alphabetic character or special character '.'. But '*' will never be the preceding character of '*'. (That means "**" will never occur in the pattern string.)

'.' = "a", "b", "c", ... , "z".

a* = "a","aa","aaa","aaaa",... or empty string("").

ab* = "a", "ab", "abb", "abbb", "abbbb",...

Input Format:
-------------
There are two arguments, first one is string denoting text and second one is string denoting pattern.

Output Format:
--------------
Return boolean, true if text and pattern matches exactly, otherwise return false.

Constraints:
------------
0 <= text length, pattern length <= 1000
Text string containing characters only from lowercase alphabetic characters.

Pattern string containing characters only from lowercase alphabetic characters and two other special characters '.' and '*'

In pattern string, It is guaranteed that '*' will have one preceding character which can be any lowercase alphabetic character or special character '.'. But '*' will never be the preceding character of '*'.

Sample Test Cases:
------------------
Sample Test Case 1:

Sample Input 1:
text = "abbbc" and pattern = "ab*c"

Sample Output 1:
true

Explanation 1:
Given pattern string can match:
"ac", "abc", "abbc", "abbbc", "abbbbc", ...


Sample Test Case 2:

Sample Input 2:
text = "abcdefg" and pattern = "a.c.*.*gg*"

Sample Output 2:
true

Explanation 2:
".*" in pattern can match  "", ".", "..", "...", "....", ...
"g*" in pattern can match "", "g", "gg", "ggg", "gggg", ...

Now, consider:
   '.' at position 2 as 'b',
   '.*'  at position {4,5} as "...",
   '.*' at position {6,7} as "" and
   [g*] at position {8,9} as "".
So, "a.c.*gg*" = "abc...g" where we can write "..." as "def". Hence, both matches.

Sample Test Case 3:

Sample Input 3:
text = "abc" and pattern = ".ab*.."

Sample Output 3:
false

Explanation 3:
If we take 'b*' as "" then also, length of the pattern will be 4 (".a.."). But, given text's length is only 3. Hence, they can not match.

'''

def regexMatch(s, p, i, j):
    if j == len(p):
        return i == len(s)
        
    if i > len(s):
        return False
        
    if j < len(p)-1 and p[j+1] == '*':
        return (regexMatch(s, p, i+1, j)) or (regexMatch(s, p, i, j+2))
        
    if i < len(s) and (s[i] == p[j] or p[j] == '.'):
        return regexMatch(s, p, i+1, j+1)
         
    return False
"""
def match(s, i, p, j):
    if i == len(s) or j == len(p):
        return False

    return p[j] == '.' or s[i] == p[j]

def helper(s, i, p, j):
    # Base Cases
    if j == len(p):
        return i == len(s)
    # to cover the case of "abc" ".*"
    if i > len(s):
        return False

    # 1. if second is * p[i+1]
    if j < len(p) - 1 and p[j + 1] == '*':
        # Zero means advance p[j+2]
        # one or more compare and advance if match
        return (match(s, i, p, j) and helper(s, i + 1, p, j)) or helper(s, i, p, j + 2)

    # 2. Match either same or '.'
    if match(s, i, p, j):
        return helper(s, i + 1, p, j + 1)


        # 3. No match or *
    return False
"""
def  isMatch(strText, strPattern):
    return regexMatch(strText, strPattern, 0, 0)

text = "abbbc"
pattern = "ab*c"
print isMatch(text, pattern)
