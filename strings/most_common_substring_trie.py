class TrieNode(object):
    def __init__(self, data = None):
        self.children = {}

    def leafNode(self):
        return self.children and '$' in self.children

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.longest = ""

    def add(self, word, end):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                node = TrieNode()
                current_node.children[c] = node
            current_node = current_node.children[c]
        current_node.children[end] = TrieNode()

    def build_suffix_trie(self, word, end):
        n = len(word)
        for i in range(n-1, -1, -1):
            self.add(word[i:], end)

    def _helper(self, current_node, prefix):
        if not current_node:
            return 0

        dollar_count = 0
        hash_count = 0
        if '$' in current_node.children:
            dollar_count += 1
        if '#' in current_node.children:
			hash_count += 1

        for key, node in current_node.children.items():
            d_count, h_count = self._helper(node, prefix+key)
            dollar_count += d_count
            hash_count += h_count
            if (dollar_count > 0 and hash_count > 0) and dollar_count == hash_count and len(prefix) > len(self.longest):
            	self.longest = prefix

        return dollar_count, hash_count

    def get_longest_repeated_substr(self):
        if not self.root:
            return 0
        self._helper(self.root, '')
        return self.longest

def getLongestRepeatedSubstring(word1, word2):
    trie = Trie()
    trie.build_suffix_trie(word1, '$')
    trie.build_suffix_trie(word2, '#')
    return trie.get_longest_repeated_substr()

word1 = "geeksforgeeks"
word2 = "geeksquiz"
print getLongestRepeatedSubstring(word1, word2)

# Output: geeks
