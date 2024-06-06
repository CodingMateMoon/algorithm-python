class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 3

def test_lengthOfLongestSubstring():
    solution = Solution()
    #The answer is "abc", with the length of 3.
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3