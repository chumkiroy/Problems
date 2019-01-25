'''
Find minimum number by removing k digits:
num = '3194' and k=2

output would be 14 but not 13
'''

def removeKdigits(num, k):
	"""
	:type num: str
	:type k: int
	:rtype: str
	"""
	while k > 0:
	    i = 0
	    while i < len(num)-1:
	        if num[i] > num[i+1]:
	            break
	        i += 1
	    num = num[:i] + num[i+1:]
	    k -= 1
	
	if len(num) == 0:
	    return "0"
	else:
	    return str(int(num))

print removeKdigits('3194', 2)
