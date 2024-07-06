def findKOr(nums: list[int], k: int) -> int:
        bit = [bin(val)[2:] for val in nums]
        mb = max(len(s) for s in bit)
        
        
        for i in range(len(bit)):
            bit[i] = bit[i].zfill(mb)

        result = []
        for i in range(mb):
            count_ones = sum(1 for j in range(len(bit)) if bit[j][i] == '1')
            if count_ones >= k:
                result.append('1')
            else:
                result.append('0')
        
        return int(''.join(result), 2)
                
                        
print(findKOr([7,12,9,8,9,15], 4))