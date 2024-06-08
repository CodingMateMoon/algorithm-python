# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4690/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 3

def test_lengthOfLongestSubstring():
    solution = Solution()
    """
    Given a string s, find the length of the longest substring without repeating characters.
    0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
    """

    #The answer is "abc", with the length of 3.
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    #The answer is "b", with the length of 1.
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
