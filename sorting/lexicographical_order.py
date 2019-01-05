'''
Lexicographical Order

Problem Statement:
------------------
Given a string array named arr of size N containing KEYS and VALUES separated by one space, where KEYS and VALUES can repeat. 

Your task is to find, for each unique key, the number of values with that key and the value with the highest lexicographical order (also called alphabetical order and dictionary order).

Input Format:
-------------
You will be given one string array named arr of size N containing KEYS and VALUES separated by one space, where KEYS and VALUES can repeat.

Output Format:
--------------
Return a String array with an entry for each unique key. Each entry should contain key, number of values corresponding to that key and value with the highest lexicographical order in the below format:

"<KEY>:<COUNT>,<HIGHEST_LEXICOGRAPHICAL_VALUE>"

Order of the output does not matter.

Constraints:
------------
1 <= N <= 10^4
1 <= Length(KEYS) <= 256
1 <= Length(VALUES) <= 800 

KEYS can repeat.
VALUES can repeat.
Keys and values will contain only small letters and numerics.

Sample Test Case:

Sample Input-1:
arr = [
  "key1 abcd",
  "key2 zzz",
  "key1 hello",
  "key3 world",
  "key1 hello"
]

Sample Output-1:
One possible output (you can return strings in any order):

[
  "key1:3,hello",
  "key2:1,zzz",
  "key3:1,world"
]

Sample Input-2:
arr = [
  "mark zuckerberg",
  "tim cook",
  "mark twain"
]

Sample Output-2:
One possible output (you can return strings in any order):

[
  "mark:2,zuckerberg",
  "tim:1,cook"
]

'''

key_counts = {}
key_values = {}
output = []

def add_to_key_dicts(key1, value1):
    if key1 in key_counts.keys():
        key_counts[key1] += 1
    else:
        key_counts[key1] = 1

    if key1 in key_values.keys():
        if value1 > key_values[key1]:
            key_values[key1] = value1
    else:
        key_values[key1] = value1
        
def solve(arr):
    for item in arr:
        item_split = item.split(" ")
        add_to_key_dicts(item_split[0], item_split[1])
    
    # string building
    for key2,value2 in key_counts.items():
        output_str = str(key2) + ":" + str(value2) + ","
        if key2 in key_values.keys():
            output_str = output_str + key_values[key2]

        output.append(output_str)

    return output

arr = [
  "mark zuckerberg",
  "tim cook",
  "mark twain"
]

print solve(arr)
