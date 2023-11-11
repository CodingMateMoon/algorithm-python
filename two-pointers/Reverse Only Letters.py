class Solution:
    """
    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
    """
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

    def reverseOnlyLetters_1(self, s: str) -> str:

        start_index = -1
        string_list = []
        n = len(s)
        current_index = n - 1
        for i in range (n):
            if not s[i].isalpha():
                string_list.append(s[i])
            else:
                while True:
                    if s[current_index].isalpha() or current_index < 0:
                        break
                    current_index -=1
                string_list.append(s[current_index])
                current_index -= 1
        result = ''.join(string_list)
        return result



def test_reverseWords():
    solution = Solution()
    assert solution.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert solution.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert solution.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
