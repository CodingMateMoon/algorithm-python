class Solution:
    """
    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
    """
    def reverseOnlyLetters(self, s: str) -> str:

        start_index = -1
        string_list = []
        n = len(s)
        current_index = n - 1
        for i in range (n):
            if not s[i].isalpha():
                if current_index < start_index:
                    continue
                if start_index == -1:
                    start_index = i
                string_list.append(s[i])
            else:
                string_list.append(s[current_index])
            current_index -= 1
        result = ''.join(string_list)
        return result



def test_reverseWords():
    solution = Solution()
    assert solution.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert solution.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert solution.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
