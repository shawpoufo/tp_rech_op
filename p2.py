#literal_eval("[-1,0,0,0,1,0],[1,-1,0,0,0,1],[0,1,-1,0,0,0],[0,0,1,-1,0,0],[0,0,0,1,-1,-1]")
from ast import literal_eval
from p1 import format,getPreviousFromNext
# -1 : sort
#  1 : entre
#  0 : none
def nextDictFromIncidenceMatrix(matrix):
    dict = {}
    len_arcs = len(matrix[0])
    len_sommet = len(matrix)
    #loop vertical
    for i in range(len_arcs): 
        _from ,_to =0,0 
        for j in range(len_sommet): 
            if matrix[j][i] == -1 :
                _from = j
            if matrix[j][i] == 1 :
                _to = j
            
            if _from != 0 and _to != 0:
                break
                
        if _from + 1 in dict:
            dict[_from + 1].append(_to + 1)
        else:
            dict[_from + 1] = [_to + 1]
    return dict

if __name__ == "__main__":
    matric = literal_eval(input("entrer la matric : "))
    nexts = nextDictFromIncidenceMatrix(matric)
    print("Liste des suivants \n")
    format(nexts)
    print("Liste des précedent \n")
    previous = getPreviousFromNext(nexts)    
    format(previous)



