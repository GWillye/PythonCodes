lista = input().split()
linhas = lista[0]
colunas = lista[1]
linhas = int(linhas)
colunas = int(colunas)
print(linhas, colunas)
mat = []
            #Crio um contador e um laço para receber todos os valores e salvar eles na matriz
contador = 0
while contador < linhas:
                #Crio uma variavel para receber os valores de inicio, linha a linha
    inicio = input().split()
    cont = 0
                #Declaro um laço que vai rodar convertendo os numeros inseridos acima
    while len(inicio) > cont:
                    #Ele recebe o mesmo valor na lista 'inicio' e adiciona a ele como um numero inteiro
        inicio[cont] = int(inicio[cont])
        cont += 1
cont = 0
                #Salva o valor dessa linha na matriz
mat.append(inicio)
contador = contador + 1
            #Agora o próximo passo é fazer a descida e subida de degraus. Para isso, criei duas variaveis, que vão realizar a navegação pela matriz
lin = -1
col = 0
            #Agora criamos a matriz que vamos estar imprimindo
matriz = []
            #Criamos um laço para fazer a navegação entre as linhas e colunas. Enquanto o numero de linhas for menor ou igual ao numero de colinas, vamos descer. Se for o contrário, vamos subir até que
            #Chegue na primeira linha, para então descer de novo
while col < colunas:
    if lin < linhas - 1:
        lin = lin + 1
        matriz.append(mat[lin][col])
    else:
        lin = lin - 1
        matriz.append(mat[lin][col])
    col = col + 1
print(matriz)