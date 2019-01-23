'''
Problem Statement: Minimum window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T.

e.g.
S = "AYZABOBECODXBANC"
T = "ABC"

Minimum window is "BANC",which contains all letters - A B and C.
* If no such window exists, then return an empty string 
* If there are multiple minimum windows of the same length, then return any one
* Characters may be repeated

Note:
https://leetcode.com/problems/minimum-window-substring/description/

'''
from collections import Counter

def  MinWindow(s, t):
	if not t or not s:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        
        l, r = 0, 0
        unique_char_in_window = 0
        window = {}
        
        ans = float('inf'), None, None
        
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in dict_t and window[char] == dict_t[char]:
                unique_char_in_window += 1
                
            while l <= r and unique_char_in_window == required:
                char = s[l]
                
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                    
                window[char] -=1
                if char in dict_t and window[char] < dict_t[char]:
                    unique_char_in_window -= 1
                
                l += 1
            
            r += 1
            
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

S = "AYZABOBECODXBANC"
T = "ABC"
print MinWindow(S, T)
