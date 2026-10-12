from curses.ascii import isdigit, isalpha


class Solution:
    def decodeString(self, s: str) -> str:
        current_stack = []
        current_str = ''
        current_number = 0

        for char in s:
            if isdigit(char):
                current_number = current_number*10 + int(char)
            if char == '[':
                current_stack.append((current_str, current_number))
                current_number = 0
                current_str = ''
            if char == ']':
                previous_str, previous_number = current_stack.pop()
                previous_str += current_str*previous_number
                current_str = previous_str
            if isalpha(char):
                current_str += char

        return current_str

if __name__ == '__main__':
    s1 = Solution()
    print(s1.decodeString('3[2[bc]]'))