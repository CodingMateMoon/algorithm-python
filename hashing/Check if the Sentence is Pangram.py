class Solution:

    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/
    def checkIfPangram(self, sentence: str) -> bool:
        return True

def test_checkIfPangram():
    solution = Solution()
    solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True
    solution.checkIfPangram("leetcode") == False
