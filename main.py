# CHANGE MATRICES

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

def multiply(m1, m2):
    mr = [[] for i in m1]  # Resultant Matrix
    for r in m1:
        for c in range(len(m2[0])):
            sum = 0
            for i in r:
              # print(i*m2[r.index(i)][c]) #  Process
                sum += i*m2[r.index(i)][c]
            mr[m1.index(r)].append(sum)
    return mr

list = multiply(matrix1, matrix2)
print(list)
