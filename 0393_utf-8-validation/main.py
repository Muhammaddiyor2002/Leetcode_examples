class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(num):
            if num & 0x80 == 0x00:
                return 1
            elif num & 0xE0 == 0xC0:
                return 2
            elif num & 0xF0 == 0xE0:
                return 3
            elif num & 0xF8 == 0xF0:
                return 4
            else:
                return 0

        i = 0
        while i < len(data):
            num_bytes = get_num_bytes(data[i])
            if num_bytes == 0:
                return False
            if i + num_bytes > len(data):
                return False
            for j in range(1, num_bytes):
                if data[i + j] & 0xC0 != 0x80:
                    return False
            i += num_bytes
        
        return True
