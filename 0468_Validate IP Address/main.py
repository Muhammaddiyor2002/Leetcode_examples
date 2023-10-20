class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (len(part) > 1 and part[0] == '0'):
                    return False
            return True

        def isIPv6(s):
            parts = s.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in "0123456789ABCDEFabcdef" for c in part):
                    return False
            return True

        if '.' in IP and isIPv4(IP):
            return "IPv4"
        elif ':' in IP and isIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
