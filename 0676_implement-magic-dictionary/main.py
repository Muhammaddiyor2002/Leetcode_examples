class MagicDictionary:

    def __init__(self):
        self.dict = []

    def buildDict(self, dictionary):
        self.dict = dictionary

    def search(self, searchWord):
        for word in self.dict:
            if len(word) != len(searchWord):
                continue
            mismatch = 0
            for wc, sc in zip(word, searchWord):
                if wc != sc:
                    mismatch += 1
                    if mismatch > 1:
                        break
            if mismatch == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
