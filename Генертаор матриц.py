import random

outFile = open('Матрицы100.txt', 'w', encoding='utf8')
for i in range(100):
    print('#', 3, file=outFile)
    for j in range(3):
        for k in range(4):
            print(random.uniform(0, 100), file=outFile, end=' ')
        print(file=outFile)
outFile.close()