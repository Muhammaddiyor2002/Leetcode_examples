class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort the people in descending order of height and ascending order of k value
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []

        # Insert people into the queue based on their k value
        for p in people:
            result.insert(p[1], p)

        return result
