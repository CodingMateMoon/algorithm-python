# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4690/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        before_element = []
        for i in range(len(s)):
            if s[i] not in before_element:
                before_element.append(s[i])
                print(f"before : {before_element} / length : {len(before_element)} / max_length : {max_length}")
                if i == len(s) - 1:
                    return max(max_length, len(before_element))
                continue
            max_length = max(max_length, len(before_element))
            before_element = []
        return max_length

def test_lengthOfLongestSubstring():
    solution = Solution()
    """
    Given a string s, find the length of the longest substring without repeating characters.
    0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
    연속된 문자로 중복 없이 가장 긴 것 구하기. 현재 커서 기준으로 다음 문자가 다를 경우 length를 증가시키고 같은 문자가 나올 경우 max(length, max_length) 저장
    """

    #The answer is "abc", with the length of 3.
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    #The answer is "b", with the length of 1.
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    #The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("aab") == 2
