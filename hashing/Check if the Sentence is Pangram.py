class Solution:

    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/
    # a sentence where every letter of the English alphabet appears at least once.
    def checkIfPangram(self, sentence: str) -> bool:
        isUsed = [0] * len(ord('z') - ord('a') + 1)
        
        for char in range(ord('a'), ord('z') + 1):
            print(chr(char))
        return True

def test_checkIfPangram():
    solution = Solution()
    assert solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True
    assert solution.checkIfPangram("leetcode") == False
