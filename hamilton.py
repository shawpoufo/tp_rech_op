from path_in_graph import isPathInGraph
from ast import literal_eval
from byListe import toList,nextDictFromList
from getMatric import generateMatric

if __name__ == "__main__":
    l = toList(input("Entrer la liste des arc du graph : "))
    path = list(literal_eval(input("Entrer le chemin : ")))
    pathCopy = path.copy()
    nextDict = nextDictFromList(l)
    matrix = generateMatric(nextDict)
    
    if isPathInGraph(matrix,path):
        print(set(pathCopy))
        print(set([k for k in nextDict]))
        if set(pathCopy) == set([k for k in nextDict]):
            print(True)
        else:
            print(False)
    else:
        print("ce chemin n'existe pas")
