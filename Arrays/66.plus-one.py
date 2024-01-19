class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Given a non-empty array of decimal digits representing a non-negative integer,
        increment the integer represented by the array by one.
        Parameters:
        - digits (List[int]): A list of decimal digits representing a non-negative integer.
        Returns:
        - List[int]: A new list representing the result of incrementing the input integer by one.
        """
        number = int(''.join([str(i) for i in digits]))
        number += 1
        return [int(i) for i in str(number)]
    
    
s = Solution()
print(s.plusOne([1,2,3]))
        