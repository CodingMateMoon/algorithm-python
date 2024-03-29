class Solution:

    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/
    # a sentence where every letter of the English alphabet appears at least once.
    def checkIfPangram(self, sentence: str) -> bool:
        # Initialize seen = 0 since we start with no letter.
        seen = 0

        # Iterate over 'sentence'.
        for curr_char in sentence:
            # Map each 'curr_char' to its index using its ASCII code.
            mapped_index = ord(curr_char) - ord('a')

            # 'curr_bit' represents the bit for 'curr_char'.
            curr_bit = 1 << mapped_index

            # Use 'OR' operation since we only add its bit for once.
            seen |= curr_bit

        # Once we finish iterating, check if 'seen' contains 26 bits of 1.
        return seen == (1 << 26) - 1

    def checkIfPangram_4(self, sentence: str) -> bool:
        # Array 'seen' of size 26.
        seen = [False] * 26

        # For every letter 'currChar', we find its ASCII code,
        # and update value at the mapped index as true.
        for curr_char in sentence:
            seen[ord(curr_char) - ord('a')] = True

        # Once we finish iterating, check if 'seen' contains false.
        for status in seen:
            if not status:
                return False
        return True
    def checkIfPangram_3(self, sentence: str) -> bool:
        # Time : O(n), Space : O(1)
        # Add every letter of 'sentence' to hash set 'seen'.
        seen = set(sentence)

        # If the size of 'seen' is 26, then 'sentence' is a pangram.
        return len(seen) == 26
    def checkIfPangram_2(self, sentence: str) -> bool:
        # Time : O(n), Space : O(1)
        # We iterate over 'sentence' for 26 times, one for each letter 'curr_char'.
        for i in range(26):
            curr_char = chr(ord('a') + i)

            # If 'sentence' doesn't contain 'curr_char', it is not a pangram.
            if sentence.find(curr_char) == -1:
                return False

        # If we manage to find all 26 letters, it is a pangram.
        return True
    def checkIfPangram_1(self, sentence: str) -> bool:
        isUsed = [0] * (ord('z') - ord('a') + 1)

        for i in range(len(sentence)):
            isUsed[ord(sentence[i]) - ord('a')] = True

        for i in range(len(isUsed)):
            if isUsed[i] == False:
                return False

        return True

def test_checkIfPangram():
    solution = Solution()
    assert solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True
    assert solution.checkIfPangram("leetcode") == False
