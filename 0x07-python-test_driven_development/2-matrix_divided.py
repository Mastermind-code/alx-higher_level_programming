def matrix_divided(matrix, div):
    prev_len = 0
    if isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        row = matrix[i]
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if prev_len and len(row) != prev_len:
            raise TypeError("Each row of the matrix must have the same size")
        elif not prev_len:
            prev_len = len(row)

        for j in range(len(row)):
            el = row[j]
            if type(el) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            matrix[i][j] = el / div
        
        
            

            
