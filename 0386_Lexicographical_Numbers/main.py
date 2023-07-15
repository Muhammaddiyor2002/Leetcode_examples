class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        
        for _ in range(n):
            result.append(curr)
            
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 != 9 and curr + 1 <= n:
                curr += 1
            else:
                while (curr // 10) % 10 == 9:
                    curr //= 10
                curr = curr // 10 + 1
        
        return result
