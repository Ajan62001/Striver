 def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set() 
        x= len(matrix[0])
        y = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])): 
                  if matrix[i][j] == 0:
                        row.add(i)
                        column.add(j)
        for i in row:
           matrix[i] = [0]*x
        for j in column:
            for r in matrix:
                r[j] = 0