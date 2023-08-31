class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 10
        for c in s:
            if c == 'z':
                count[0] += 1
            elif c == 'w':
                count[2] += 1
            elif c == 'x':
                count[6] += 1
            elif c == 's':
                count[7] += 1
            elif c == 'g':
                count[8] += 1
            elif c == 'u':
                count[4] += 1
            elif c == 'f':
                count[5] += 1
            elif c == 'h':
                count[3] += 1
            elif c == 'i':
                count[9] += 1
            elif c == 'o':
                count[1] += 1
        
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] -= count[8] + count[6] + count[5]
        count[1] -= count[0] + count[2] + count[4]
        
        result = []
        for i in range(10):
            result.extend([str(i)] * count[i])
            
        return ''.join(result)