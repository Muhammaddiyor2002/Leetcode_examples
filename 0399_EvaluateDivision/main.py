from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        # Step 1: Create the graph and fill it with values
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        # Step 2: DFS function to find a path from start to end
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return graph[start][neighbor] * result
            
            return -1.0

        # Step 3: Perform queries using the DFS function
        results = []
        for start, end in queries:
            visited = set()
            result = dfs(start, end, visited)
            results.append(result)

        return results
