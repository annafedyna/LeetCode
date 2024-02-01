def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    return [True if child + extraCandies >= max(candies) else False for child in candies]