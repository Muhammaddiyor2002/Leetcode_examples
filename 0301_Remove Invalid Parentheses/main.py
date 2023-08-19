class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        def backtrack(index, left_removed, right_removed, left_count, right_count, current):
            if index == len(s):
                if left_removed == right_removed == 0 and isValid(current):
                    valid_expressions.add(current)
                return
            
            char = s[index]
            
            if char == '(' and left_removed > 0:
                backtrack(index + 1, left_removed - 1, right_removed, left_count, right_count, current)
            
            if char == ')' and right_removed > 0:
                backtrack(index + 1, left_removed, right_removed - 1, left_count, right_count, current)
            
            if char != '(' and char != ')':
                backtrack(index + 1, left_removed, right_removed, left_count, right_count, current + char)
            elif char == '(':
                backtrack(index + 1, left_removed, right_removed, left_count + 1, right_count, current + char)
            elif right_count < left_count:
                backtrack(index + 1, left_removed, right_removed, left_count, right_count + 1, current + char)
        
        valid_expressions = set()
        min_removed = float('inf')
        left_removed = 0
        right_removed = 0
        
        for char in s:
            if char == '(':
                left_removed += 1
            elif char == ')':
                if left_removed > 0:
                    left_removed -= 1
                else:
                    right_removed += 1
        
        backtrack(0, left_removed, right_removed, 0, 0, "")
        return list(valid_expressions)
