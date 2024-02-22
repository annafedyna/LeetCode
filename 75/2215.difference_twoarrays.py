'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
'''

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    n1 = set(nums1)
    n2 = set(nums2)
    return [[i for i in n1 if i not in n2],[j for j in n2 if j not in n1]]

print(findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))