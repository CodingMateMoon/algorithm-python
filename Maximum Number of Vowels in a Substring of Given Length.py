import unittest

class Solution(unittest.TestCase):

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
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count

        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)

        return answer
    def maxVowels_1(self, s: str, k: int) -> int:
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        left = max_length = length = 0

        for i in range(k):
            length += int(s[i] in vowel_letters)
        max_length = length

        for right in range(k, len(s)):
            length += int(s[right] in vowel_letters)
            length -= int(s[right - k] in vowel_letters)
            max_length = max(max_length, length)

        return max_length

    def test_maxVowels(self):
        self.assertEqual(self.maxVowels("abciiidef", 3), 3)
        self.assertEqual(self.maxVowels("aeiou", 2), 2)
        self.assertEqual(self.maxVowels("leetcode", 3), 2)
        self.assertEqual(self.maxVowels("weallloveyou", 7), 4)

def test_maxVowels():
    solution = Solution()
    assert solution.maxVowels("weallloveyou", 7) == 4

if __name__ == '__main__':
    print(Solution().maxVowels("abciiidef", 3))
    print(Solution().maxVowels("aeiou", 2))
    print(Solution().maxVowels("leetcode", 3))
    print(Solution().maxVowels("weallloveyou", 7)) #4


