import heapq

class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        projects = [(Capital[i], Profits[i]) for i in range(len(Profits))]
        projects.sort(key=lambda x: x[0])  # Sort projects by capital

        available_projects = []  # Max heap for available projects
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= W:
                # Add projects that can be started with the current capital
                heapq.heappush(available_projects, -projects[i][1])
                i += 1

            if available_projects:
                # Select the project with the maximum profit
                W -= heapq.heappop(available_projects)
            else:
                break

        return W
