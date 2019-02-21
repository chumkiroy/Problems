class TrieNode(object):
    def __init__(self, data = None):
        self.children = {}

    def leafNode(self):
        return self.children and '$' in self.children

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.most_repeated = 0

    def add(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                node = TrieNode()
                current_node.children[c] = node
            current_node = current_node.children[c]
        current_node.children['$'] = TrieNode()

    def build_suffix_trie(self, word):
        n = len(word)
        for i in range(n-1, -1, -1):
            self.add(word[i:])

    def _helper(self, current_node, prefix):
        if not current_node:
            return 0

        dollar_count = 0
        if '$' in current_node.children:
            dollar_count += 1

        for key, node in current_node.children.items():
            count = self._helper(node, prefix+key)
            dollar_count += count
            #print "-", prefix, dollar_count

        if dollar_count > 1 and len(prefix) > 1  and dollar_count > self.most_repeated:
            self.most_repeated = dollar_count

        return dollar_count

    def get_most_repeated_substr(self):
        if not self.root:
            return 0
        self._helper(self.root, '')
        return self.most_repeated

def getMostRepeatedSubstring(word):
    trie = Trie()
    trie.build_suffix_trie(word)
    return trie.get_most_repeated_substr()

word = "ababcdcdcdcdef"
#word = "banana"  #Output = 2 - an or na
#word = "ababab" #Output = 3 - ab
print getMostRepeatedSubstring(word)

