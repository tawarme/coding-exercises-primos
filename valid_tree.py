class Solution:
    def go(self, node, source, graph, checked):
        #print("Checking ", node)
        if checked.get(node):
            return False

        checked[node] = True

        for nei in graph[node]:
            if nei == source:
                continue

            if not self.go(nei, node, graph, checked):
                return False

        return True


    def validTree(self, n, edges):
        if edges != n - 1:
            return False

        checked = {}

        graph = {}

        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], [])
            graph[edge[0]].append(edge[1])

            graph[edge[1]] = graph.get(edge[1], [])
            graph[edge[1]].append(edge[0])

        source = None
        loop_free = self.go(0, source, graph, checked)
        #print("No loops found", loop_free)
        #print(len(checked), checked)

        return loop_free and len(checked) == n



if __name__ == "__main__":
    tests = [
                [True, 5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
                [False, 4, [[0, 1], [1, 2], [2, 3], [1, 3]]],
            ]

    for test in tests:
        ans = test[0]
        assert Solution().validTree(*test[1:]) == ans
