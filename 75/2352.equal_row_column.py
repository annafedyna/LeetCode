from collections import Counter, defaultdict
# O (n^3)
def equalPairs(grid: list[list[int]]) -> int:
    v = []
    for i in range(len(grid)):
        c = []
        for j in range(len(grid)):
            c.append(grid[j][i])
            
        for k in range(len(grid)):
            if grid[k] == c:
                v.append((k, i))
    return len(v)         

# O (n^2)
def equalPairs2(grid: list[list[int]]) -> int:
    freq = Counter(tuple(row) for row in grid)
    return sum([freq[col] for col in zip(*grid)])

print(equalPairs2([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))