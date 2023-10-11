class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate the number of tests a single pig can perform before dying
        tests_per_pig = minutesToTest // minutesToDie + 1
        
        # Calculate the minimum number of pigs needed to test all the buckets
        pigs_required = 0
        while tests_per_pig ** pigs_required < buckets:
            pigs_required += 1
        
        return pigs_required
