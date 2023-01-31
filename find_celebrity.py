class Solution:
    def __init__(self, graph):
        self.graph = graph
        self._ask = 0

    def knows(self, a, b):
        self._ask += 1
        return b in self.graph[a]

    def findCelebrity1(self, n):
        celeb = -1

        not_celebs = {}
        for i in range(n):
            for j in range(n):
                if i == j or (not self.knows(i, j) and self.knows(j, i)):
                    continue
                else:
                    print("NOT", i,j)
                    not_celebs[i] = True
                    break
            else:
                celeb = i
                break

        print("ASK COUNT", self._ask)
        print(celeb)
        return celeb

    def findCelebrity2(self, n):
        celeb = -1
        checkables = {}

        for i in range(n):
            checkables[i] = True

        print(checkables)

        for i in range(n):
            if checkables.get(i) is None:
                continue

            for j in checkables:
                if checkables[j] is None or i == j:
                    continue
                else:
                    if self.knows(i, j):
                        checkables[i] = None
                        break
            else:
                celeb = i
                break

        print(self._ask)

        if celeb == -1:
            return -1

        for i in range(n):
            if i == celeb:
                continue

            if not self.knows(i, celeb):
                return -1

        print(self._ask)
        return celeb

    def findCelebrity3(self, n):
        celeb = -1

        skip_to = 0
        for i in range(n):
            if i < skip_to:
                continue

            for j in range(i + 1, n):
                if self.knows(i, j):
                    skip_to = j
                    break
            else:
                celeb = i
                break

        print(self._ask)

        if celeb == -1:
            return -1

        for i in range(n):
            if i == celeb:
                continue

            if not self.knows(i, celeb):
                return -1

        print(self._ask)
        return celeb

    def findCelebrity4(self, n):
        # NOT WORKING (like video)
        celeb = -1

        skip_to = 0
        celeb_cand = 0
        for i in range(n):
            if i != celeb_cand and self.knows(celeb_cand, i):
                celeb_cand = i

        print(self._ask)

        #if celeb == -1:
        #    return -1

        for i in range(n):
            if i == celeb_cand:
                continue

            if self.knows(i, celeb_cand) or self.knows(celeb_cand,j):
                return -1

        print(self._ask)
        return celeb_cand


if __name__ == "__main__":
    tests = [
                [-1, {0:[2],1:[2],2:[],3:[2],4:[2],5:[2,4,6], 6:[2,4,5], 7:[]},8],
                [2, {0:[2],1:[2],2:[],3:[2],4:[2],5:[2,4,6], 6:[2,4,5], 7:[2]},8],
                [7, {0:[2,7],1:[2,7],2:[7],3:[2,7],4:[2,7],5:[2,4,6,7], 6:[2,4,5,7], 7:[]},8]
            ]

    for test in tests:
        ans = test[0]
        assert Solution(test[1]).findCelebrity3(*test[2:]) == ans

