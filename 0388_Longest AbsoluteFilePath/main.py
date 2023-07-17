class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length = 0
        path_length = {0: 0}  # Dictionary to store the length of each level
        
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                # Current item is a file
                max_length = max(max_length, path_length[depth] + len(name))
            else:
                # Current item is a directory
                path_length[depth + 1] = path_length[depth] + len(name) + 1  # Add 1 for the directory separator
        
        return max_length
