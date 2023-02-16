class Trie(object):
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def search(self, row, col, board, parent, found):
        DIR = [(0,1), (0,-1), (1,0), (-1,0 )]

        ch = board[row][col]

        node = parent.children[ch]

        if node.word is not None:
            found.append(node.word)
            node.word = None

        board[row][col] = "#"

        for dir in DIR:
            newrow = row + dir[0]
            newcol = col + dir[1]

            if not (0 <= newrow < len(board) and  0 <= newcol < len(board[0])):
                continue

            if node.children.get(board[newrow][newcol]):
                self.search(newrow, newcol, board, node, found)

        board[row][col] = ch

        if not node.children:
            del parent.children[ch]


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])

        root = Trie()
        for word in words:
            node = root
            for ch in word:
                if node.children.get(ch):
                    node = node.children.get(ch)
                else:
                    newnode = Trie()
                    node.children[ch] = newnode
                    node = newnode

            node.word = word

        found = []
        for row in range(rows):
            for col in range(cols):
                if root.children.get(board[row][col]):
                    self.search(row, col, board, root, found)

        return found
