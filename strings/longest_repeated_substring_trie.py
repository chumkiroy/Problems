class TrieNode(object):
    def __init__(self, data = None):
        self.children = {}

    def leafNode(self):
        return self.children and '$' in self.children

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.longest = ""

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

        if dollar_count > 1 and len(prefix) > len(self.longest):
            self.longest = prefix

        return dollar_count

    def get_longest_repeated_substr(self):
        if not self.root:
            return 0
        self._helper(self.root, '')
        return self.longest

def getLongestRepeatedSubstring(word):
    trie = Trie()
    trie.build_suffix_trie(word)
    return trie.get_longest_repeated_substr()

word = "banana"
print getLongestRepeatedSubstring(word)

