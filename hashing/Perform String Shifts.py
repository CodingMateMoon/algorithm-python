#https://leetcode.com/problems/perform-string-shifts/description/
class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        shift [direction, amount]
        :type shift: List[List[int]]
        :rtype: str
        """
        char_array = list(s)
        for direction, amount in shift:
            if direction == 0:
                shift_char = char_array[0]
                for x in range(amount):
                    for i in range(1, len(char_array)):
                        char_array[i - 1] = char_array[i]
                    char_array[len(char_array) - 1] = shift_char
            else:
                shift_char = char_array[len(char_array) - 1]
                for x in range(amount):
                    for i in range(len(char_array) - 1):
                        char_array[i] = char_array[i + 1]
                    char_array[0] = shift_char


        return ''.join(char_array)

def test_stringShift():
    solution = Solution()
    """
    direction> 0 : left, 1 : right
    amount> e.g) [0, 1]
    A left shift by 1 means remove the first character of s and append it to the end.
    Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
    [0,1] means shift to left by 1. "abc" -> "bca"
    [1,2] means shift to right by 2. "bca" -> "cab"
    """
    assert solution.stringShift("abc", [[0, 1], [1,2]]) == "cab"