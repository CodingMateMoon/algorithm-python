class Solution:
    # https://leetcode.com/problems/get-equal-substrings-within-budget/description/
    """
    1 <= s.length <= 105
    t.length == s.length
    0 <= maxCost <= 106
    s and t consist of only lowercase English letters.
    """
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = max_length = total_cost = 0
        length = len(s)
        s_array = [char for char in s]
        t_array = [char for char in t]
        
        for right in range(length):
            total_cost += ord(t_array[right]) - ord(s_array[right])
            if (total_cost) <= maxCost:
                max_length = max(max_length, right - left + 1)
                continue
            while(total_cost > maxCost):
                total_cost -= ord(t_array[left]) - ord(s_array[left])
                left += 1

        return max_length





def test_equalSubstring():
    solution = Solution()
    """
    a + 1 = b
    b + 1 = c
    c + 1 = d
    => max_length of a substring = 3
    
    a + 2 = c
    b + 2 = d
    maxCost = 3
    => max_length of a substring = 1
    """
    assert solution.equalSubstring("abcd", "bcdf", 3) == 3
    assert solution.equalSubstring("abcd", "cdef", 3) == 1
    assert solution.equalSubstring("abcd", "acde", 0) == 1
    assert solution.equalSubstring("krrgw", "zjxss", 19) == 2
