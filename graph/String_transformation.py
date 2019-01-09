'''
Problem Statement: String Transformation Using Given Dictionary Of Words

You are given a dictionary of words and two strings named start and stop.

How can you convert string start to string stop, by changing only one character at a time and making sure that 1) all the intermediate words are in the given dictionary of words and 2) minimum number of intermediate words are used?

Generally, dictionary does not contain duplicate values, but for the sake of this problem, assume that dictionary might have duplicate values. (Sometimes interviewer tricks the question, to see, how you will handle it.)

Input Format:
-------------
There are three arguments. First is an array of strings denoting the dictionary of words, second is a string start and third is a string stop.

Output Format:
--------------
Return an array of strings.

If transformation is possible then in returned array, first string should be start, last string should be stop and in between strings of given dictionary that you used for transformation, in the same order they are used in your transformation. Suppose name of the returned array is ans and size is ans_size, then for 1 <= i < ans_size, ans[i - 1] and ans[i] should differ at exactly one position.

If transformation is not possible then returned array should contain only one string "-1".

(If there are multiple valid transformations, you are free to return any one of them.)

Constraints:
------------
- Input strings contain only lower case alphabetical letters.
- Length of input strings are same.
- Input strings need not to be unique.
- 2 <= total number of characters in input strings <= 10^5
- start and stop strings need not to be present in given dictionary. 

Sample Test Case:
-----------------
Sample Input: words = ["cat", "hat", "bad", "had"]
			  start = "bat"
			  stop = "had"

Sample Output: ["bat", "bad", "had"] or "bat", "hat", "had"]

Explanation:
From "bat" change character 't' to 'd', so new string will be "bad".
From "bad" change character 'b' to 'h', so new string will be "had".
or
From "bat" change character 'b' to 'h', so new string will be "hat".
From "hat" change character 't' to 'd', so new string will be "had".

'''

from collections import deque

def get_neighbour(string, words):
    res = []
    if len(words) > 26:
        for char in 'abcdefghijklmnopqrstuvwxyz':
            for i in range(len(string)):
                new_string = string[:i] + char + string[i+1:]
                if new_string in words:
                    res.append(new_string)
    else:
        for word in words:
            diff = 0
            for i in range(len(string)):
                if word[i] != string[i]:
                    diff += 1
                if diff > 1: 
                    break
            if diff == 1:
                res.append(word)
    
    return res

def string_transformation(words, start, stop):
    #print(words)
    #print(start)
    #print(stop)
    words = set(words)
    words.add(stop)
    visited = set()
    parent = {start: None}
    found = False
    que = deque([start])

    while que:
        cur_word = que.popleft()
        for neighbour in get_neighbour(cur_word, words):
            #print('-',neighbour)
            if neighbour == stop:
                found = True
                parent[neighbour] = cur_word
                break
            if neighbour not in visited:
                visited.add(neighbour)
                que.append(neighbour)
                parent[neighbour] = cur_word
            if found:
                break
            
    end = parent.get(stop)
    #print('parent', parent)
    if not end:
        return ['-1']
    path = [stop]
    while end:
        path.append(end)
        if end == start:
            break
        end = parent[end]
    #print('output')  
    return path[::-1] if path else ['-1']

words = ["cat", "hat", "bad", "had"]
start = 'bat'
stop = 'had'
print string_transformation(words, start, stop)

'''
# Alternative solution:

from collections import deque

def string_transformation(words, start, stop):
    if len(words) < len(start):
        return string_transformation_small_n(words, start, stop)
    else:
        return string_transformation_small_k(words, start, stop)

def string_transformation_small_k(words, start, stop):
    char_sets = []
    for letter in start:
        char_sets.append(set())
    words.extend([start, stop])
    word_dictionary = set()
    for word in words:
        word_dictionary.add(word)
        for i in range(len(word)):
            char_sets[i].add(word[i])
    parent_map = {}
    if start != stop:
        parent_map[start] = None
    queue = deque([])
    queue.append(start)
    end = None
    while queue:
        current_word = queue.popleft()
        charArr = list(current_word)
        for i in range(len(charArr)):
            if end is not None:
                break
            for letter in char_sets[i]:
                if letter != charArr[i]:
                    charArr[i] = letter
                    next_word = "".join(charArr)
                    if next_word in word_dictionary and next_word not in parent_map:
                        queue.append(next_word)
                        parent_map[next_word] = current_word
                    if next_word == stop:
                        end = next_word
                        break
                    charArr[i] = current_word[i]
    path = []
    seen = set()
    current = end
    while current is not None:
        path.append(current)
        if current in seen:
            break
        seen.add(current)
        current = parent_map[current]
    path.reverse()
    if path:
        return path
    return ["-1"]


def string_transformation_small_n(words, start, stop):
    word_dictionary = {start:set(), stop:set()}
    for word in words:
        # add each word to the dictionary
        word_dictionary[word] = set()
    for a in word_dictionary:
        for b in word_dictionary:
            if a != b:
                if one_away(a,b):
                    word_dictionary[a].add(b)
    # do me some BFS
    parent_map = {}
    queue = deque([])
    queue.append(start)
    end = None
    if start != stop:
        parent_map = {start: None}
    while queue:
        current_word = queue.popleft()
        for neighbor in word_dictionary[current_word]:
            if neighbor not in parent_map:
                parent_map[neighbor] = current_word
                if neighbor == stop:
                    end = neighbor
                queue.append(neighbor)
    path = []
    seen = set()
    current = end
    while current is not None:
        path.append(current)
        if current in seen:
            break
        seen.add(current)
        current = parent_map[current]
    path.reverse()
    if path:
        return path
    return ["-1"]


def one_away(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return False
    return True


if __name__ == "__main__":
    f = sys.stdout

    words_size = int(input())

    words = []
    for _ in range(words_size):
        words_item = input()
        words.append(words_item)


    start = input()

    stop = input()

    res = string_transformation(words, start, stop)

    f.write('\n'.join(res))
    f.write('\n')
    f.close()
'''