'''
Run length Encoding:

Problem Statement:
------------------
Simple version of the problem: Compress a string (only has alphabet characters), with basic encoding, where you simply count the number of repeated characters. Then also write a routine to decompress it.
e.g.
Input: "AAAAA" 
Output: "5A"

Input: "BAAAB"
Output: "B3AB"

Input: "ABAB"
Output: "ABAB" [We are not concerned about characters repeating in groups]

Assume that a given character will not repeat more than 127 times.

Solution: Compression solution to this is very simple. It pretty much needs one loop. Decompression is equally simple. Let us know if that is not clear.

Important twists to the problem: 
--------------------------------
* String can have any character from the basic ASCII set (ASCII values 0 to 127). i.e. it can now include numbers.

* Compressed length must not exceed original length. It can be same or less.


Solution hint: 
--------------
Given that you cannot have numbers in your solution, can you use something else? Can you make use of higher order ASCII values?

Test cases are given for compression of 2nd (twisted) case. 

Note:
https://leetcode.com/problems/string-compression/

'''

def RLE(strinput):
	pass
