# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    """
    공백으로 단어를 구분하는데 각 단어마다 역순으로 정렬합니다
    start_index,
    """
    def reverseWords(self, s: str) -> str:

        start_index = 0
        string_list = []
        length = len(s)
        for i in range(length):
            if s[i] == ' ':
                for j in range(i, start_index, -1):
                    string_list.append(s[j - 1])
                string_list.append(' ')
                start_index = i + 1
            elif i == length - 1:
                for j in range(i, start_index - 1, -1):
                    string_list.append(s[j])
        result = ''.join(string_list)
        print(f"result : {result}")
        return result





    def reverseWords_1(self, s: str) -> str:

        start_index = 0
        result = ""
        for i in range(len(s)):
            if s[i] == ' ':
                for j in range(i, start_index, -1):
                    result += s[j - 1]
                result += ' '
                start_index = i + 1
        for i in range(len(s), start_index, -1):
            result += s[i - 1]
        print(f"result : {result}")
        return result





def test_reverseWords():
    solution = Solution()
    assert solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert solution.reverseWords("God Ding") == "doG gniD"

"""
    def test_maxVowels(self):
        self.assertEqual(self.maxVowels("abciiidef", 3), 3)
        self.assertEqual(self.maxVowels("aeiou", 2), 2)
        self.assertEqual(self.maxVowels("leetcode", 3), 2)
        self.assertEqual(self.maxVowels("weallloveyou", 7), 4)

def test_maxVowels():
    solution = Solution()
    assert solution.maxVowels("weallloveyou", 7) == 4
"""