"""
trie:
a tree of 26 start nodes
each node has a hashmap of all it's children
also tracks if it's a word or not (and not just a prefix)

"""


class TrieNode:
    is_word: bool = False
    child_map = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child_map:
                curr.child_map[c] = TrieNode()
            curr = curr.child_map[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.child_map:
                return False
            curr = curr.child_map[c]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.child_map:
                return False
            curr = curr.child_map[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
