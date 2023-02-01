class Solution:
    def go(self, node, graph, checked):
        #print("Checking ", node)
        if checked.get(node):
            return False

        checked[node] = True

        for nei in graph[node]:
            self.go(nei, graph, checked)

    def connectedComponents(self, n, edges):
        checked = {}

        graph = {}

        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], [])
            graph[edge[0]].append(edge[1])

            graph[edge[1]] = graph.get(edge[1], [])
            graph[edge[1]].append(edge[0])

        components = 0

        for i in range(n):
            if checked.get(i):
                continue

            components += 1
            self.go(i, graph, checked)

        return components



if __name__ == "__main__":
    tests = [
                [2, 5, [[0, 1], [1, 2], [3, 4]]],
            ]

    for test in tests:
        ans = test[0]
        assert Solution().connectedComponents(*test[1:]) == ans
