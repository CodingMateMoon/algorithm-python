# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return None

def test_groupAnagrams():
    solution = Solution()
    assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]