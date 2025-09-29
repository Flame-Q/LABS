def transpose_matrix(matrix):
    print("Исходная матрица:")
    print_matrix(matrix)
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    
    print("Транспонированная матрица:")
    print_matrix(result)
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

matrix = []
while True:
    row_input = input("Введите матрицу (числа через пробел, строки через Enter), для завершения ввода введите пустую строку: ")
    if row_input == "":
        break

    row_input = row_input.split()
    
    row = []
    for x in row_input:
        number = int(x)
        row.append(number)
    matrix.append(row)

if matrix:
    transposed = transpose_matrix(matrix)
    
    print("Размер исходной матрицы: ", len(matrix), "x", len(matrix[0]))
    print("Размер транспонированной матрицы: ", len(transposed),"x",len(transposed[0]))
else:
    print("Матрица пустая!")