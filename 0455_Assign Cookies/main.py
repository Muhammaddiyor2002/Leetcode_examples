class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the lists of greed factors and cookie sizes
        g.sort()
        s.sort()

        content_children = 0  # Initialize the count of content children
        i, j = 0, 0  # Pointers to iterate through the lists

        while i < len(g) and j < len(s):
            # If the current cookie size is sufficient for the current child's greed, assign it
            if s[j] >= g[i]:
                content_children += 1
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie

        return content_children
