class Solution:
    def flipLights(self, n: int, m: int) -> int:
        # if n is 0, there is no way to turn on any bulb
        if n == 0:
            return 0
        # if m is 0, there is only one way to keep the original state
        if m == 0:
            return 1
        # if n is 1, there are two ways to toggle the single bulb
        if n == 1:
            return 2
        # if n is 2, there are three ways to toggle the two bulbs
        if n == 2:
            # if m is 1, we can flip both, the first, or the second bulb
            if m == 1:
                return 3
            # if m is larger than 1, we can also flip none
            else:
                return 4
        # if n is larger than 2, there are four ways to toggle the bulbs
        if n > 2:
            # if m is 1, we can flip all, odd, even, or three bulbs
            if m == 1:
                return 4
            # if m is 2, we can flip all, odd, even, three, none, or four bulbs
            if m == 2:
                return 7
            # if m is larger than 2, we can also flip the middle bulb
            else:
                return 8
