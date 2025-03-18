# Rotate the image
# Tags: N48, Blind75, Math & Geometry, Medium   

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # Transpose and Reverse : 
    # 1.Transpose the matrix: Convert rows into columns
    # 2.Reverse each row: This completes the 90-degree rotation
        
    n = len(matrix)
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix)) 
# Output : [[7,4,1],[8,5,2],[9,6,3]]


        