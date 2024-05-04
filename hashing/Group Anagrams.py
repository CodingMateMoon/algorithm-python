# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return None

def test_groupAnagrams():
    """"
    nat, tan 동일한 알파벳으로 구성된 문자열 그룹화. e, a, t로 구성된 문자열 탐색 및 그룹화. 
    """
    solution = Solution()
    assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]