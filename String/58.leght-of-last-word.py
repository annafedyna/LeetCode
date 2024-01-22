import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = re.findall(r'\s*(\w+)\s*$', s, re.IGNORECASE)
        return len(a[-1])
        
        
s = Solution()
print(s.lengthOfLastWord('  Hello   World  '))