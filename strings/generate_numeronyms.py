'''
Generate Numeronyms

Problem Statement:
------------------
Given a string word of length n, generate all possible numeronyms.

What is a Numeronym?
---------------------
A numeronym is a word where a number is used to form an abbreviation.

For a given string word, a numeronym is a string with few or more contiguous letters between the first letter and last letter of word replaced with a number representing the count of letters omitted. Only one set of contiguous letters are replaced by a number.

e.g. "L10n" is called a numeronym of the word "Localization", where 10 stands for the count of letters between the first

letter 'L' and the last letter 'n' in the word.

Input Format:
-------------
Only one argument denoting input string word.

Output Format:
--------------
Return strings array containing all possible numeronyms of given string word.

You need not to worry about order of strings in your output array. For words = "aaaaa", arrays ["a2aa", "aa2a", "a3a"], ["a3a", "aa2a", "a2aa"] etc will be considered as valid answer.

In case of no possible numeronym string, return empty list.

Constraints:
------------
String will be composed of characters [a-z], [A-Z], [0-9] only.
1 <= n <= 120 where n is length of given string word.

Sample Test Case:
-----------------
Sample Input: word = "nailed"
Sample Output: ["n4d", "na3d", "n3ed", "n2led", "na2ed", "nai2d"]

Explanation:
"n4d" is abbreviated string of given string "nailed" where "aile" string letters are omitted and replaced by count of letters i.e. 4.

"na3d" is abbreviated string of given string "nailed" where "ile" string letters are omitted and replaced by count of letters i.e. 3.

Similarly for remaining generate numeronyms.

'''
def numeronyms(word):
	res = []
	n = len(word)
	for count in range(2, n-1):
		for i in range(1, n+count):
			res.append(word[:i] + str(count) + word[i+count:])

	return res

print numeronyms("aaaaa")


'''
def generateCombinations(inputString, startIndex, endIndex, isFirst, res):
    #if isFirst:
        #res.append(inputString)
        #print(inputString)
        
    startString = inputString[0:startIndex]
    middleString = inputString[startIndex: endIndex]
    endString = inputString[endIndex: len(inputString)]
    #print(startString, "-", middleString, "-", endString)
    
    rightShift = ''
    leftShift = ''
    
    for inputCounter in range(len(middleString), 1, -1):
        if inputCounter == len(middleString):
            res.append(startString + str(inputCounter) + endString)
            #print(startString + str(inputCounter) + endString)
        else:
            rightShift = middleString[0:len(middleString)-inputCounter]
            res.append(startString + rightShift + str(inputCounter)+endString)
            #print (startString + rightShift + str(inputCounter)+endString)
            
            leftShift = middleString[inputCounter: len(middleString)]
            res.append(startString + str(inputCounter) + leftShift + endString)
            #(startString + str(inputCounter) + leftShift + endString)
        
            if(endIndex-startIndex>=2):
                startIndex += 1
                endIndex -= 1
                generateCombinations(inputString, startIndex, endIndex, False, res)

def neuronyms(word):
    res = []
    generateCombinations(word, 1, len(word)-1, True, res)
    #print(res)
    return res

print neuronyms("aaaaa")
'''
