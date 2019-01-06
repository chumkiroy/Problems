'''
Design And Implement LRU Cache





Problem Statement:



The LRU caching scheme removes the least recently used frame, when the cache is full and a new page is referenced which is not there in the cache. 



You are given one integer named capacity, denoting the maximum size possible of the LRU cache. Also you are given three integer arrays named query_type, key and value, each having size n.



query_type[i], key[i] and value[i] together denotes one query. So there are total n queries. 



query_type contains only 0 or 1. query_type[i] = 0 means ith query is GET query and query_type[i] = 1 means ith query is SET query. key and value arrays contain only positive integers.



You have to return array containing answers for GET queries.



GET query:



For GET query only key[i] matters, do not care what is stored in value[i]. 



For each GET query append one integer in the array to be returned. Append the value of the key[i], if the key[i] exists in the cache, otherwise append -1.



SET query:



If key[i] is already present in the cache then update its value to value[i], else add key[i] with value value[i] in the cache.



Input Format:



There are four arguments in the input. First is integer named capacity. Second is integer array named query_type. Third is integer array named key. Fourth is integer array named value. 



Output Format:



Return an array containing answers for GET queries.



Constraints:



1 <= n <= 10^5
1 <= capacity <= 10^5
0 <= query_type[i] <= 1
1 <= key[i] <= 10^5
1 <= value[i] <= 10^5


Sample Test Case:



Sample Input:



capacity = 2



index      query_type      key      value

0              1                      5          11

1              1                      10         22

2              0                      5      1

3              1                      15         33

4              0                      10     1

5              1                     5          55

6              0                      5      1



(

this is same as:

query_type = [1 1 0 1 0 1 0]

key = [5 10 5 15 10 5 5]

value = [11 22 1 33 1 55 1]

)



Sample Output:



[11 -1 55]



Explanation:



Initially cache is empty.



Step 1:

SET: 5 -> 11

Noe cache contains (5 ->11).



Step 2:

SET: 10 -> 22 

Now cache contains (5 -> 11) and (10 -> 22).



Step 3:

GET: 5

Cache contains (5 ->11), so append 11 to answer. 



Step 4:

SET: 15 -> 33

Now cache contains (5 -> 11) and (15 -> 33).

Note that here (10 -> 22) is removed because 10 is the least recently used. 5 was used in the previous query! 



Step 5:

GET: 10

Cache does not contain key 10 (it was removed in previous step), so append -1 to answer.



Step 6:

SET: 5 -> 55

Now cache contains (5 -> 55) and (15 -> 33). Note that (5 -> 11) is updated to (5 -> 55).



Step 7:

GET: 5

Cache contains (5 -> 55), so append 55 to answer. 
'''
class DLL:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __hash__(self):
        return hash((self.key, self.value))

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = DLL()
        self.tail = DLL()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.bump(key)
        else:
            after_head = self.head.next
            new_node = DLL(key, value)
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = after_head
            after_head.prev = new_node
            self.map[key] = new_node
            self.size += 1
        if self.size > self.capacity:
            self.evict()

    def get(self, key):
        if key not in self.map:
            return -1
        self.bump(key)
        node = self.map[key]
        return node.value

    def bump(self, index):
        to_move = self.map.get(index)
        if not to_move or to_move == self.head.next:  # already bumped or not there
            return
        prev = to_move.prev
        next = to_move.next
        prev.next = next
        next.prev = prev
        head_points_to = self.head.next
        self.head.next = to_move
        head_points_to.prev = to_move
        to_move.prev = self.head
        to_move.next = head_points_to
        return

    def evict(self):
        elem = self.tail.prev
        key, value = elem.key, elem.value
        del self.map[key]
        before_elem = elem.prev
        before_elem.next = self.tail
        self.tail.prev = before_elem
        self.size -= 1

def implement_LRU_cache(capacity, query_type, key, value):
    lru = LRU(capacity)
    results = []
    for i in range(len(query_type)):
        if query_type[i] == 0:
            results.append(lru.get(key[i]))
        else:
            lru.set(key[i], value[i])
    return results

capacity = 2
query_type = [1, 1, 0, 1, 0, 1, 0]
key = [5, 10, 5, 15, 10, 5, 5]
value = [11, 22, 1, 33, 1, 55, 1]

print implement_LRU_cache(capacity, query_type, key, value)

'''
Another approach:(implemented)

import collections

def implement_LRU_cache(capacity, query_type, key, value):
    def get(k):
        if cache.get(k, None) == None:
            return -1
        val = cache.pop(k)
        cache[k] = val
        return val
        
    def set(k, val):
        if cache.get(k, None) == None:
            if len(cache) >= capacity:
                cache.popitem(last=False)
        else:
            cache.pop(k)
        
        cache[k] = val
            
        
    cache = collections.OrderedDict()
    ans = []
    for i in range(len(query_type)):
        if query_type[i] == 0:
            #get
            ans.append(get(key[i]))
        else:
            #set
            set(key[i], value[i])
    
    return ans
'''
