def transpose(mat: list[list[float | int]]) -> list[list]:  
    if len(mat)==0:
        return []
    num_rows=len(mat)
    num_columns=len(mat[0])
    for row in mat:
        if len(row)!=num_columns:
            raise ValueError ("Рваная матрица")
    result = []
    for i in range(num_columns):
        row = []
        for j in range(num_rows):
            row.append(mat[j][i])
        result.append(row)
    return result

if __name__=="__main__":
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1, 2], [3, 4]]))
    print(transpose([]))
    print(transpose([[1, 2], [3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    num_columns=len(mat[0])
    result=[]
    for row in mat:
        if len(row)!=num_columns:
            raise ValueError("Рваная матрица")
        result.append(sum(row))
    return result

if __name__=="__main__":
    print(row_sums([[1, 2, 3], [4, 5, 6]]))
    print(row_sums([[-1, 1], [10, -10]]))
    print(row_sums([[0, 0], [0, 0]]))
    print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    num_columns=len(mat[0])
    result=[0]*num_columns
    for row in mat:
        if len(row)!=num_columns:
            raise ValueError("Рваная матрица")
        for j in range(len(row)):
            result[j]+=row[j]
    return result

if __name__=="__main__":
    print(col_sums([[1, 2, 3], [4, 5, 6]]))
    print(col_sums([[-1, 1], [10, -10]]))
    print(col_sums([[0, 0], [0, 0]]))
    print(col_sums([[1, 2], [3]]))