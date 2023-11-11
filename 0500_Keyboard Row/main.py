class Solution:
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        result = []

        for word in words:
            lowercase_word = word.lower()
            in_row = None

            for row in rows:
                if lowercase_word[0] in row:
                    in_row = row
                    break

            if all(letter in in_row for letter in lowercase_word):
                result.append(word)

        return result
