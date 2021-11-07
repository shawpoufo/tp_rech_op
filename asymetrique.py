from byListe import toList,nextDictFromList
from getMatric import generateMatric,printMatric

def isAsysmetrique(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True

if __name__ == "__main__":
    print("================== ASYMETRIQUE ==================")
    ls = input("donner la liste des arc :")
    m = generateMatric(nextDictFromList(toList(ls)))
    if isAsysmetrique(m):
        print("oui asymétrique")
    else:
        print("anti-asymétrique")
    printMatric(m)


        