from collections import Counter
'''
Given an array of integers arr, 
return true if the number of occurrences of each value in the array is unique or 
false otherwise.
'''
def uniqueOccurrences(arr: list[int]) -> bool:
    hashmap = Counter(arr)
    set = []
    for i in hashmap.values():
        if i in set:
            return False
        else:
            set.append(i)
    return set

print(uniqueOccurrences([1,2,2]))