class Solution:
    def constructRectangle(self, area: int):
        if area == 0:
            return [0, 0]

        # Start with the square root of the area as the initial width
        width = int(area ** 0.5)

        # Increment the width while checking if it divides the area
        while area % width != 0:
            width -= 1

        # Calculate the corresponding length
        length = area // width

        return [length, width]
