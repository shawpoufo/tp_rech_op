from byListe import toList,nextDictFromList
from byMatric import getNextFromMatric,getPreviousFromNext
from getMatric import generateMatric
def isConnexe(matrice):
    nexts = getNextFromMatric(matrice)
    previous = getPreviousFromNext(nexts)

    for i,nextVertices in nexts.items():
        for j,prevVertices in previous.items():
            if j > i:
                if j in nextVertices:
                    break
                else:
                    allvertices = sorted(nextVertices + prevVertices)
                    unionvertices = [x[1] for x in enumerate(allvertices) if x[0] < len(allvertices) -1 and allvertices[x[0]] == allvertices[x[0]+1]]
                    if not unionvertices:
                        return False
    return True


if __name__ == "__main__":
    ls = input("Entrer la liste des arc : ") 
    if isConnexe(generateMatric(nextDictFromList(toList(ls)))):
        print('Connexe')
    else:
        print('non Connexe')

