matriz = []
lista =[]
linhas = int(input())
colunas = int(input())
for i in range(linhas):
    for j in range(colunas):
        lista.append(int(input()))
    matriz.append(lista)
    lista = []
mtrz = []
linhas = int(input())
colunas = int(input())
for i in range(linhas):
    for j in range(colunas):
        lista.append(int(input()))
    mtrz.append(lista)
    lista = []
print(matriz)
print(mtrz)
matrizm = []
for i in range(linhas):
    for j in range(colunas):
        lista.append(matriz[i][j] * mtrz[i][j])
    matrizm.append(lista)
    lista = []
        
print(matrizm)