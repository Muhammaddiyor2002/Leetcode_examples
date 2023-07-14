class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return None
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        curr = None
        start = 0
        
        for i in range(len(s)):
            if s[i] == '[':
                if curr:
                    stack.append(curr)
                curr = NestedInteger()
                start = i + 1
            elif s[i] == ']':
                num = s[start:i]
                if num:
                    curr.add(NestedInteger(int(num)))
                if stack:
                    popped = stack.pop()
                    popped.add(curr)
                    curr = popped
                start = i + 1
            elif s[i] == ',':
                if s[i-1] != ']':
                    num = s[start:i]
                    curr.add(NestedInteger(int(num)))
                start = i + 1
        
        return curr
