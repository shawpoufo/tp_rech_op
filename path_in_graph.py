from ast import literal_eval
from byListe import toList,nextDictFromList
from getMatric import generateMatric
def isPathInGraph(matrix,path):
    exists = True
    while len(path) > 1:
        startVertex = path[0]
        nextVertex = path[1]
        if matrix[startVertex-1][nextVertex-1] == 1:
            path.remove(startVertex)
            # isPathInGraph(matrix,path)
        else:
            exists = False
            break
    return exists
if __name__ == "__main__":
    l = toList(input("Entrer la liste des arc du graph : "))
    path =list(literal_eval(input("Entrer le chemin : ")))
    matrix = generateMatric(nextDictFromList(l))
    
    print(isPathInGraph(matrix,path))