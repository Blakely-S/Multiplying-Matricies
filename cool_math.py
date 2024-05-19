#Inputting Matrix
Row1 = int(input("Give the number of rows:"))  
Column1 = int(input("Give the number of columns:"))  
matrix1 = [[int(input())for c in range (Column1)] for r in range(Row1)]


Row2 = int(input("Give the number of rows:"))  
Column2 = int(input("Give the number of columns:"))  
matrix2 = [[int(input())for c in range (Column2)] for r in range(Row2)]
print("first matrix: " + str(matrix2)) 
print("second matrix: " + str(matrix1))   

#Multiplying Matrix
def multiply(m1,m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    return result
print("resulting matrix" + str(multiply(matrix1,matrix2)))

