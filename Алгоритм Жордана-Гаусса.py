import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sla

inFile = open('Матрицы100.txt', 'r', encoding='utf8')
x = []
order = []
n = 0
A = []
for line in inFile:
    line = line.split()
    if line[0] == '#':
        A = []
        x = []
        n = int(line[1])
        order = np.arange(n)
    else:
        line = list(map(float, line))
        A.append(line)
        if len(A) == n:
            A = np.array(A)
            for i in range(n):
                notzeroind = i
                maxelem = 0
                for j in range(i, n):
                    if abs(A[order[j]][i]) > maxelem:
                        maxelem = abs(A[order[j]][i])
                        notzeroind = j
                if notzeroind != i:
                    order[i], order[notzeroind] = order[notzeroind], order[i]
                A[order[i]] = A[order[i]] / A[order[i]][i]
                for j in range(n):
                    if j != i:
                        A[order[j]] = A[order[j]] - (A[order[i]] * A[order[j]][i])
            for i in range(n):
                x.append(A[order[i]][n])
            x = np.array(x)
            print(x)
inFile.close()