'''
You are given an n x n integer matrix grid
Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
'''


def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    res = []
    row = []
    max_val = 0

    for i in range(len(grid)-2):
        for c in range(len(grid)-2):
            for j in range(3):
                for g in range(3):
                    if grid[j+i][g+c] > max_val:
                        max_val = grid[j+i][g+c]
            row.append(max_val)
            max_val = 0
        
        res.append(row)
        row = []
    
    return res


print(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))

# [[9,9],[8,6]]
