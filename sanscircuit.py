from byListe import toList,nextDictFromList
from getMatric import generateMatric,printMatric
def nextsVertecies(row):
    return [i for i,x in enumerate(row) if x == 1]
def previousVertecies(vertex,matrix):
    return [i for i,r in enumerate(matrix) for j,v in enumerate(r) if v == 1 and j == vertex]


    

def hasCycle(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[j][i] == 1:
                nexts = nextsVertecies(matrice[i])
                previous = previousVertecies(j,matrice)
                allvertices = sorted(nexts+previous)
                unionvertices = [x[1] for x in enumerate(allvertices) if x[0] < len(allvertices) -1 and allvertices[x[0]] == allvertices[x[0]+1]]
                if unionvertices:
                    # print(nexts)
                    # print(previous)
                    # print(i, unionvertices , j , i)                
                    return True
    return False

if __name__ == "__main__":
    ls=input('Entrer la liste des arc : ')
    m = generateMatric(nextDictFromList(toList(ls)))
    printMatric(m)
    if hasCycle(m):
        print("graph avec circuits")
    else:
        print("graph sans circuits")





