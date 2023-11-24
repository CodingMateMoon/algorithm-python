class Solution:
    # https://leetcode.com/problems/reverse-prefix-of-word/
    """
    시작 인덱스 left부터 abcdefd 기준 d와 일치하는 인덱스까지 스택에 데이터를 넣고 다 넣은 뒤 pop
    """
    def reversePrefix(self, word: str, ch: str) -> str:

        left = 0
        answer = [char for char in word]

        for i in range (len(word)):
            if word[i] == ch:
                temp = []
                for j in range(left, i):
                    temp.append(word[j])
                for j in range(left, i):
                    answer[j] = temp.pop()
        return ''.join(answer)
def test_reversePrefix():
    solution = Solution()
    assert solution.reversePrefix("abcdefd", "d") == "dcbaefd"
    assert solution.reversePrefix("abcd", "z") == "abcd"
