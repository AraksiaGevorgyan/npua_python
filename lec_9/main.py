import random
class Matrix():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                random_value = random.randint(1, 50)
                row.append(random_value)
            self.matrix.append(row)

    # def print_matrix(self):
    #     for row in self.matrix:
    #         print(row)

    def __str__(self):
        result = ''
        for row in self.matrix:
            result+=str(row)+"\n"
        return result
    
    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new=[]
            for i in range(self.rows):
                new_row = []
                for j in range(self.cols):
                    new_row.append(self.matrix[i][j] + other.matrix[i][j])
                new.append(new_row)
            new_obj = Matrix(self.rows,self.cols)
            new_obj.matrix = new       
            return new_obj
        else:
            raise ValueError("Matrices must have the same dimensions for addition")
        
    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new=[]
            for i in range(self.rows):
                new_row = []
                for j in range(self.cols):
                    new_row.append(self.matrix[i][j] - other.matrix[i][j])
                new.append(new_row)
            new_obj = Matrix(self.rows,self.cols)
            new_obj.matrix = new 
            return new_obj
        else:
            raise ValueError("Matrices must have the same dimensions for subtraction")
            

    
    def __mul__(self, other):
        if self.cols == other.rows:        
            new_matrix = []
            for i in range(self.rows):
                new_row = []
                for j in range(other.cols):
                    new_element = 0
                    for k in range(self.cols):
                        new_element += self.matrix[i][k] * other.matrix[k][j]
                    new_row.append(new_element)
                new_matrix.append(new_row)

            new_obj = Matrix(self.rows, other.cols)
            new_obj.matrix = new_matrix

            return new_obj
        else:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
       



matrix1 = Matrix(3,3)
matrix2 = Matrix(3,3)
print(matrix1)
print(matrix2)
print("Addition of 2 matrices")
matrix_add = matrix1 + matrix2
print(matrix_add)
print("Substraction of 2 matrices")
matrix_sub = matrix1 - matrix2
print(matrix_sub)
print("Multiplication of 2 matrices")
matrix_mul = matrix1*matrix2
print(matrix_mul)