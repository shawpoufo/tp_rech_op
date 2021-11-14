from byListe import toList,nextDictFromList,getPreviousFromNext
from getMatric import generateMatric,printMatric
import collections
# def nextsVertecies(row):
#     return [i for i,x in enumerate(row) if x == 1]
# def previousVertecies(vertex,matrix):
#     return [i for i,r in enumerate(matrix) for j,v in enumerate(r) if v == 1 and j == vertex]

# 1,5 2,1 2,3 2,4 4,3 4,7 5,3 6,4 6,5 6,7 #sans circuit
# 1,2 2,3 2,5 3,4 3,5 4,2 5,4 6,1 6,        #avec circuit

    

# def hasCycle(matrice):
#     for i in range(len(matrice)):
#         for j in range(len(matrice)):
#             if matrice[j][i] == 1:
#                 nexts = nextsVertecies(matrice[i])
#                 previous = previousVertecies(j,matrice)
#                 allvertices = sorted(nexts+previous)
#                 unionvertices = [x[1] for x in enumerate(allvertices) if x[0] < len(allvertices) -1 and allvertices[x[0]] == allvertices[x[0]+1]]
#                 if unionvertices:
#                     print(f"suivant   de i : {i+1}{[i+1 for i in nexts]}")
#                     print(f"precedent de j : {j+1}{[i+1 for i in previous]}")
#                     print(f"circuit : {i+1, [i+1 for i in unionvertices] , j+1 , i+1}")                
#                     return True
#     return False

def hasCycle(ddp):
    levels = {}
    lvl = -1
    hasLevel = True
    while hasLevel:
        lvl += 1
        hasLevel = False
        for i,row in ddp.items():
            if not row:
                if lvl in levels:
                    levels[lvl].append(i)
                else:
                    levels[lvl] = [i]
                hasLevel = True
        
        if lvl in levels:
            for i in levels[lvl]:
                """ Supprimer les sommet qui non aucun précedent """
                del ddp[i]
                """ Supprimer les sommet qui non aucun précedent depuis
                    les listes des précedents 
                """
                for j,p in ddp.items():
                    if i in p:
                        """ p est la liste des précedent"""
                        p.remove(i)
    if ddp:
        return True
    else:
        print(f" Niveaux : {levels}")
        return False
        
        


if __name__ == "__main__":
    ls=input('Entrer la liste des arc : ')
    previous = getPreviousFromNext(nextDictFromList(toList(ls)))
    # hasCycle(previous)
    if hasCycle(previous):
        print("graph avec circuits")
    else:
        print("graph sans circuits")





