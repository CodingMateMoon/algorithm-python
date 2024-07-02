# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4690/
from collections import Counter


class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        max_length = 0
        before_element = []
        for i in range(len(s)):
            if s[i] not in before_element:
                before_element.append(s[i])
                print(f"before : {before_element} / length : {len(before_element)} / max_length : {max_length}")
                if i == len(s) - 1:
                    return max(max_length, len(before_element))
                continue
            for j in range(len(before_element)):
                if s[i] == before_element[j]:
                    for k in range(j):
                        print(f"before pop:{before_element}")
                        before_element.pop(k)
                        print(f"after pop:{before_element}")
                    before_element.append(s[i])

            max_length = max(max_length, len(before_element))

        return max_length
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        char_count = Counter()
        left = right = 0
        result = 0
        while right < len(s):
            before = s[right]
            char_count[before] += 1

            while char_count[before] > 1:
                l = s[left]
                char_count[l] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
            for i in range(left, right):
                print(f"{i}:{s[i]}")
        return right

def test_lengthOfLongestSubstring():
    solution = Solution()
    """
    Given a string s, find the length of the longest substring without repeating characters.
    0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
    연속된 문자로 중복 없이 가장 긴 것 구하기. 현재 커서 기준으로 다음 문자가 다를 경우 length를 증가시키고 같은 문자가 나올 경우 max(length, max_length) 저장
    dv 다음 d가 나오는 것처럼 이전 문자와는 다르나 그 앞에 문자가 중복해서 나오는 경우 초기화하지 않고 유지. 앞의 d를 pop 두번째부터 길이 계산. 
    """

    #The answer is "abc", with the length of 3.
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    #The answer is "b", with the length of 1.
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    #The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("aab") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3
