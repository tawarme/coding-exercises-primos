class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int :

        wlength = len(beginWord)
        comb = {}

        for word in wordList:
            for i in range(wlength):
                newword = word[:i] + "*" + word[i+1:]
                
                similars = comb.get(newword, [])
                similars.append(word)
                
                comb[newword] = similars

        #print(comb)

        checked = {beginWord: True}
        q = [[beginWord, 1]]

        while q:
            word, level = q.pop(0)

            for i in range(wlength):
                newword = word[:i] + "*" + word[i+1:]

                for nei in comb.get(newword, []):
                    if nei == endWord:
                        return level + 1

                    if not checked.get(nei):
                        checked[nei] = True
                        q.append([nei, level + 1])

        return 0



