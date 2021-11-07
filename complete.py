from byListe import toList,nextDictFromList
from getMatric import generateMatric,printMatric
def isComplet(matrice):
    for i,lign in enumerate(matrice):
        for j,v in enumerate(lign):
            if i != j and v == 0 :
                return False
    return True

if __name__=="__main__":
    print('====================== COMPLET ======================')
    ls = toList(input("Entrer la liste des arc : "))
    m = generateMatric(nextDictFromList(ls))
    if isComplet(m) :
        print('Complet')
    else:
        print("non complet")
    printMatric(m)
