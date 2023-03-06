class TrieNode():
    def __init__(self):
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.min = 26
        self.max = 0
        #self.mem = {}
        self.trie = TrieNode()        

    def addWord(self, word: str) -> None:
        self.min = min(self.min, len(word))
        self.max = max(self.max, len(word))


        word += "*"

        node = self.trie
        for ch in word:
            next = node.children.get(ch)

            if not next:
                next = TrieNode()
                node.children[ch] = next

            node = next

        #self.mem[word] = True

    def search(self, word: str) -> bool:
        if not (self.min <= len(word) <= self.max):
            return False

        #if self.mem.get(word, False):
        #    return True

        return self.go(self.trie, 0, word+"*")


    def go(self, node, i, word):
        if i == len(word):
            return True

        if word[i] == ".":
            for ch, child in node.children.items():
                if self.go(child, i + 1, word):
                    return True

        elif node.children.get(word[i]):
            if self.go(node.children.get(word[i]), i + 1, word):
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
