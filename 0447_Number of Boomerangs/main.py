class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            # Calculate the squared distance between two points
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        
        total_boomerangs = 0
        
        for i in range(len(points)):
            distances = {}  # Dictionary to store the count of distances
            
            for j in range(len(points)):
                if i == j:
                    continue  # Skip the same point
                
                d = distance(points[i], points[j])
                
                if d in distances:
                    distances[d] += 1
                else:
                    distances[d] = 1
                
            for count in distances.values():
                total_boomerangs += count * (count - 1)  # Count the boomerangs for each distance
        
        return total_boomerangs
