class Solution:

    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/
    # a sentence where every letter of the English alphabet appears at least once.
    def checkIfPangram(self, sentence: str) -> bool:
        isUsed = [0] * (ord('z') - ord('a') + 1)

        for i in range(len(sentence)):
            print(ord(sentence[i]))
            #isUsed[ord(sentence[i])] = True

        for i in range(isUsed):
            if isUsed[i] == False:
                return False

        return True

def test_checkIfPangram():
    solution = Solution()
    assert solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True
    assert solution.checkIfPangram("leetcode") == False
