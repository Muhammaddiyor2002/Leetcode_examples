class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(start, num1, num2):
            if start == len(num):
                return True
            
            for end in range(start + 1, len(num) + 1):
                num3 = num[start:end]
                
                if (len(num3) > 1 and num3[0] == '0') or (len(num3) > len(num) // 2):
                    break
                
                if int(num3) == num1 + num2 and backtrack(end, num2, int(num3)):
                    return True
            
            return False
        
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                num1 = num[:i]
                num2 = num[i:j]
                
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                if backtrack(j, int(num1), int(num2)):
                    return True
        
        return False
