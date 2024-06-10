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
    연속된 문자로 가장 긴 것 구하기. 현재 커서 기준으로 다음 문자가 다를 경우 length를 증가시키고 같은 문자가 나올 경우 max(length, max_length) 저장
    """

    #The answer is "abc", with the length of 3.
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    #The answer is "b", with the length of 1.
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    #The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
