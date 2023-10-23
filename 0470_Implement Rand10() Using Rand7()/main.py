class Solution:
    def rand10(self):
        while True:
            # Generate a random number in the range 1 to 49 using rand7()
            num = (rand7() - 1) * 7 + rand7()
            
            # Reject numbers greater than 40 to ensure a uniform distribution
            if num <= 40:
                return 1 + (num - 1) % 10
