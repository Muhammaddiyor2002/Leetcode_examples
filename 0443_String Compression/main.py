class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        write_index = 0  # Index to write the compressed characters
        read_index = 0  # Index to read characters from the original array

        while read_index < len(chars):
            char = chars[read_index]
            count = 1

            # Count consecutive occurrences of the current character
            while read_index + 1 < len(chars) and chars[read_index] == chars[read_index + 1]:
                read_index += 1
                count += 1

            # Write the character
            chars[write_index] = char
            write_index += 1

            # Write the count as a string
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_index] = digit
                    write_index += 1

            read_index += 1

        return write_index
