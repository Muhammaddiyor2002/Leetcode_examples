class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles or len(rectangles) == 0:
            return False
        
        # Initialize variables to track the boundaries and area
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        total_area = 0
        points_set = set()
        
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            
            # Update the boundaries
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            # Calculate the total area
            total_area += (x2 - x1) * (y2 - y1)
            
            # Add the four corners of each rectangle to the set
            points = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
            for point in points:
                if point in points_set:
                    points_set.remove(point)
                else:
                    points_set.add(point)
        
        # Check if the points set contains exactly the four corners
        perfect_corners = {(min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)}
        
        return points_set == perfect_corners and total_area == (max_x - min_x) * (max_y - min_y)
