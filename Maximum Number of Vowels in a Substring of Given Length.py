class Solution:

    """
    Example 1:

    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.
    Example 2:

    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.
    Example 3:

    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.
    """
    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        left = max_length = 0
        for right in range(len(s)):
            if s[right] in vowel_letters:

                max_length = max(max_length, right - left + 1)
                continue
            left = right + 1

        return max_length if max_length < k else k


if __name__ == '__main__':
    print(Solution().maxVowels("abciiidef", 3))
    print(Solution().maxVowels("aeiou", 2))
    print(Solution().maxVowels("leetcode", 3))
    print(Solution().maxVowels("weallloveyou", 7)) #4


