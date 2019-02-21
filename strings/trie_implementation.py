class TrieNode():
	def __init__(self):
		self.children = {}
		self.end_of_word = False

class Trie():
	def __init__(self):
		self.root = TrieNode()

	def add(self, word):
		current_node = self.root
		for c in word:
			if c not in current_node.children:
				current_node.children[c] = TrieNode()
			current_node = current_node.children[c]
		current_node.end_of_word = True

	def find_word(self, word):
		current_node = self.root
		for c in word:
			if c not in current_node.children:
				return False
			current_node = current_node.children[c]
		return current_node.end_of_word

	def _collect_words(self, node, path, output):
		if not node:
			return
		if node.end_of_word:
			output.append(''.join(path))

		for c, child in node.children.items():
			path.append(c)
			self._collect_words(child, path, output)
			path.pop()

	def start_with_prefix(self, prefix):
		current_node = self.root
		for c in prefix:
			if c not in current_node.children:
				return []
			current_node = current_node.children[c]
		
		output = []
		path = [prefix]
		self._collect_words(current_node, path, output)
		return output

	def delete_word(self, word):
		current_node = self.root
		for c in word:
			if c not in current_node.children:
				return False
			current_node = current_node.children[c]
		current_node.end_of_word = False
		return True


if __name__ == '__main__':
    trie = Trie()
    words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
    for word in words.split():
        trie.add(word)
    print "'goodbye' in trie: ", trie.find_word('goodbye')
    print trie.start_with_prefix('g')
    print trie.start_with_prefix('to')
    if trie.delete_word('too'):
    	print "deleted"
    else:
    	print "not deleted"
    print trie.start_with_prefix('to')
    if trie.delete_word('too'):
    	print "deleted"
    else:
    	print "not deleted"
    print trie.start_with_prefix('to')
