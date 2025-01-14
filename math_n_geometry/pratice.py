class Solutions:
    def setZeroes(self, matrix):
        pair = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    pair.append([i,j])

        for p in pair:
            r,c = p
            for i in range(len(matrix)):
                matrix[i][c]=0
            for i in range(len(matrix[0])):
                matrix[r][i]=0
        return matrix
        
                   
a = Solutions()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(a.setZeroes(matrix))
