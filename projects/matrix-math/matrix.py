def create(rows, cols, fill=0):
    return [[fill] * cols for _ in range(rows)]

def multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Incompatible dimensions")
    result = create(rows_a, cols_b)
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result

def transpose(m):
    return [list(row) for row in zip(*m)]

def determinant(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in m[1:]]
        det += ((-1) ** j) * m[0][j] * determinant(minor)
    return det

def display(m):
    for row in m:
        print("  " + " ".join(f"{v:>6.2f}" for v in row))

if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print("A * B =")
    display(multiply(a, b))
    print(f"\ndet(A) = {determinant(a)}")
