class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        '''
        Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) 
        and bottom right coordinate is (row2,col2).
        '''
        for i in range(row1, row2+1):
            for j in range(col1,col2+1):
                self.rectangle[i][j] = newValue
        return 
    
    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(obj.updateSubrectangle(0, 0, 3, 2, 5))
param_2 = obj.getValue(0,2)