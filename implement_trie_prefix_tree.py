class TrieNode:
    def __init__(self, children={}):
        self.children = children


class Trie:

    def __init__(self):
        self.trie = TrieNode({})

    def _traverse(self, word, insert):
        node = self.trie
        
        for ch in word:
            next = node.children.get(ch)

            if not next:
                if insert:
                    next = TrieNode({})
                    node.children[ch] = next
                else:
                    return None

            node = next

        return node

    def insert(self, word: str) -> None:
        word += "."

        self._traverse(word, True)
        

    def search(self, word: str) -> bool:

        node = self.startsWith(word)

        if node and node.children.get("."):
            return True

        return False
        

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix, False)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)