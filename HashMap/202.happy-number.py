class Solution:
    def isHappy(self, n: int) -> bool:    
        sums = set()
        current = 0
        while current != 1:
            current = sum([int(i)*int(i) for i in str(n)])
            if current in sums:
                return False
            else:
                sums.add(current)
            n = current
        return True
            
        
s = Solution()
print(s.isHappy(19))
                