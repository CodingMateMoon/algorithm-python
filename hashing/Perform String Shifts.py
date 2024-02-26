# https://leetcode.com/problems/perform-string-shifts/description/
class Solution(object):
    def stringShift(self, s, shift):
        # Add up the left shifts and right shifts.
        overall_shifts = [0, 0]
        for direction, amount in shift:
            overall_shifts[direction] += amount
        left_shifts, right_shifts = overall_shifts

        # Determine which shift (if any) to perform.
        if left_shifts > right_shifts:
            left_shifts = (left_shifts - right_shifts) % len(s)
            s = s[left_shifts:] + s[:left_shifts]
        else:
            right_shifts = (right_shifts - left_shifts) % len(s)
            s = s[-right_shifts:] + s[:-right_shifts]

        return s
    def stringShift_3(self, s, shift):
        for direction, amount in shift:
            amount %= len(s)
            if direction == 0:
                # Move necessary amount of characters from start to end
                s = s[amount:] + s[:amount]
            else:
                # Move necessary amount of characters from end to start
                s = s[-amount:] + s[:-amount]
        return s
    def stringShift_2(self, s, shift):
        for direction, amount in shift:

            if direction == 0:
                print(f"{s} : {amount} : {s[amount:]} : {s[:amount]}")
                s = s[amount:] + s[:amount]
                continue
            right_index = len(s) - amount
            s = s[right_index:] + s[:right_index]

        return s

    def stringShift_1(self, s, shift):
        """
        :type s: str
        shift [direction, amount]
        :type shift: List[List[int]]
        :rtype: str
        """
        char_array = list(s)
        for direction, amount in shift:
            if direction == 0:
                for x in range(amount):
                    shift_char = char_array[0]
                    for i in range(1, len(char_array)):
                        char_array[i - 1] = char_array[i]
                    char_array[len(char_array) - 1] = shift_char
            else:
                for x in range(amount):
                    shift_char = char_array[len(char_array) - 1]
                    for i in range(len(char_array) - 2, -1, -1):
                        char_array[i + 1] = char_array[i]
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
    assert solution.stringShift("abc", [[0, 1], [1, 2]]) == "cab"
    assert solution.stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]) == "efgabcd"
