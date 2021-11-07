from byListe import toList,nextDictFromList,format
""" dict : c'est le dictionaire des suivants """
def generateMatric(dict):
    matrice = initialise(len(dict))
    for k,v in dict.items():
        for c in v:
            matrice[k-1][c-1] = 1
    return matrice
def initialise(length):
    return [[0 for col in range(length)] for row in range(length)]
def printMatric(matric):
    print('  ',end='', flush=True)
    for i in range(len(matric)):
        print(f'{i+1} ',sep=' ',end='', flush=True)
    print('')
    i = 0
    for row in matric:
        i += 1
        print(f"{i} ",end='',flush=True)
        print(*row)
if __name__ == "__main__":
    graphList = toList(input("Donner la liste des arc : "))
    graphDict = nextDictFromList(graphList)
    format(graphDict)    
    print("-"*50)
    matrice = generateMatric(graphDict)
    printMatric(matrice)
