import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from time import time


def Jordan_Gauss_me(A, n):
    start = time()
    x = []
    order = np.arange(n)
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
    finish = time()
    return np.array(x), finish - start


def Jordan_Gauss(A, n):
    start = time()
    x = []
    order = np.arange(n)
    for i in range(n):
        notzeroind = i
        for j in range(i, n):
            if A[order[j]][i] != 0:
                notzeroind = j
                break
        if notzeroind != i:
            order[i], order[notzeroind] = order[notzeroind], order[i]
        A[order[i]] = A[order[i]] / A[order[i]][i]
        for j in range(n):
            if j != i:
                A[order[j]] = A[order[j]] - (A[order[i]] * A[order[j]][i])
    for i in range(n):
        x.append(A[order[i]][n])
    finish = time()
    return np.array(x), finish - start


inFile = open('Матрицы100.txt', 'r', encoding='utf8')
n = 0
A = []
num = 0
df = pd.DataFrame(index=np.arange(1, 101),
                  columns=['J-G m.e. error', 'J-G error', 'J-G m.e. time', 'J-G time'])
for line in inFile:
    line = line.split()
    if line[0] == '#':
        num = num + 1
        A = []
        n = int(line[1])
    else:
        line = list(map(float, line))
        A.append(line)
        if len(A) == n:
            A = np.array(A)
            x1, df.loc[num, 'J-G m.e. time'] = Jordan_Gauss_me(A.copy(), n)
            x2, df.loc[num, 'J-G time'] = Jordan_Gauss(A.copy(), n)
            df.loc[num, 'J-G m.e. error'] = np.linalg.norm(np.dot(A[:, :n], x1) - A[:, n], np.inf)
            df.loc[num, 'J-G error'] = np.linalg.norm(np.dot(A[:, :n], x2) - A[:, n], np.inf)
df[['J-G m.e. error', 'J-G error']].plot(figsize=(7, 7))
plt.xlabel('Матрица')
plt.ylabel('Ошибка')
plt.title('Сравнение ошибок алгоритмов Жордана-Гаусса')
plt.savefig('Err1.png')
df[['J-G m.e. time', 'J-G time']].plot(figsize=(7, 7))
plt.xlabel('Матрица')
plt.ylabel('Время работы')
plt.title('Сравнение времени работы')
plt.savefig('Time.png')
plt.show()
inFile.close()
