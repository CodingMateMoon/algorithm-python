class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for element in magazine:
            for i in ransomNote:
                if element == i:
                    
            


if __name__ == '__main__':

    Solution().canConstruct("aa", "aab")