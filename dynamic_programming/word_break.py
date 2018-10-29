'''
Word Break

Problem Statement: 
You are given a dictionary set dictionary that contains dictionaryCount distinct words and another string txt. Your task is to segment the txt string in such a way that all the segments occur in a continuous manner in the original txt string and all these segments (or words) exists in our dictionary set dictionary. 

Same word from the dictionary can be used multiple times when splitting the given string. 

Input Format:
First parameter of the function that is to be implemented is an integer dictionaryCount denoting, the number of words in our dictionary. Second parameter is a vector(array) of strings dictionary, denoting the list of words in our dictionary and the last parameter is a string txt, denoting the text string that is to be segmented.

Output Format:

Return array of strings containing all different possible segmentation arrangements for the txt string.

Constraints:
1 <= dictionaryCount <= 500
1 <= |txt| <= 19
1<= lengths of words in dictionary <= 19
All the characters in txt and words in dictionary are lower case English alphabets.

Sample Test Case:
7
jim
cook
jimcook
is
awe
some
awesome
jimcookisawesome

Sample Output:

jim cook is awe some 
jim cook is awesome 
jimcook is awe some 
jimcook is awesome
'''
def doesWordBreak(word, dict):
    n = len(word)
    dp = [True] + [False for _ in range(n)]

    for i in range(1, n+1):
	for w in dict:
	    if w == word[i-len(w):i] and dp[i-len(w)]:
		dp[i] = True
    return dp[-1]

def dfs(word, dict, path, res):
	if doesWordBreak(word, dict):
		if len(word) == 0:
			res.append(path)
			return
		for i in range(1, len(word)+1):
			if word[:i] in dict:
				dfs(word[i:], dict, path+' '+word[:i], res)

def wordBreak(word, dict):
	res = []
	dfs(word, dict, '', res)
	return res    

#word = 'catsanddog'
#dict = ['cat', 'cats', 'and', 'sand', 'dog']
word = 'jimcookisawesome'
dict = ['jim', 'cook', 'jimcook', 'is', 'awe', 'some', 'awesome']

print wordBreak(word, dict)
