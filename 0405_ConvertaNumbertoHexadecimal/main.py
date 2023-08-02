class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        while num != 0 and len(result) < 8:
            # Get the last 4 bits and convert them to a hexadecimal character
            result = hex_chars[num & 15] + result
            num >>= 4
        
        return result
