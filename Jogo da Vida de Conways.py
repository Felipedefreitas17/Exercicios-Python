# Jogo da Vida de Conway
import random, time, copy
WIDTH = 10
HEIGHT = 10

# Cria uma lista de listas de celulas:
nextCells = []
for x in range(WIDTH):
    column = [] # Cria uma coluna em uma lista.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Adiciona uma célula viva.
        else:
            column.append('.') # Adiciona uma célula morta.
    nextCells.append(column) # nextCells é uma lista de colunas.

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells) # Cria uma cópia da lista principal
    
	# Imprime na tela:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Imprime cada célula.
        print() # Imprime uma nova linha ao término de cada linha.

    # Calcula o próximo ciclo com base nas células do ciclo atual:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Verifica as células vizinhas:
            leftCoord = (x - 1)
            rightCoord = (x + 1)
            aboveCoord = (y - 1)
            belowCoord = (y + 1)

            # Conta o número de vizinhos vivos:
            numNeighbors = 0
            if aboveCoord >= 0:
                if leftCoord >= 0:
                    if currentCells[leftCoord][aboveCoord] == '#':
                        numNeighbors += 1 # Celula Superior Esquerda está viva.
                if currentCells[x][aboveCoord] == '#':
                    numNeighbors += 1 # Celula Superior está viva.
                if rightCoord < 10:
                    if currentCells[rightCoord][aboveCoord] == '#':
                        numNeighbors += 1 # Celula Superior Direita está viva.
                    
            if leftCoord >= 0:
                if currentCells[leftCoord][y] == '#':
                    numNeighbors += 1 # Celula Esquerda está viva.
            if rightCoord < 10:
                if currentCells[rightCoord][y] == '#':
                    numNeighbors += 1 # Celula Direita está viva.
                    
            if belowCoord < 10:
                if leftCoord >= 0:       
                    if currentCells[leftCoord][belowCoord] == '#':
                        numNeighbors += 1 # Celula Inferior Esquerda está viva.
                if currentCells[x][belowCoord] == '#':
                    numNeighbors += 1 # Celula Inferior está viva.
                if rightCoord < 10:
                    if currentCells[rightCoord][belowCoord] == '#':
                        numNeighbors += 1 # Celula Inferior Direita está viva.

            # Anota como ficará cada célula de acordo com a regra do Jogo da Vida de Conway:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Células Vivas com 2 ou 3 vizinhos vivos permanecem vivas:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '.' and numNeighbors == 3:
                # Células Mortas com exatamente 3 vizinhos voltam a vida:
                nextCells[x][y] = '#'
            else:
                # Qualquer outra condição, a célula morre ou permanece morta:
                nextCells[x][y] = '.'
    time.sleep(1)
