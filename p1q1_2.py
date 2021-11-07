from ast import literal_eval
from byListe import format,getPreviousFromNext
# from p1q2 import format,getPreviousFromNext

def getNextFromMatric(matric):
    nextDict = {}
    for i in range(len(matric)):
        nextDict[i + 1] = []
        for j in range(len(matric[i])):
            if matric[i][j] == 1:
                nextDict[i + 1].append(j+1)
    return nextDict

if __name__ == "__main__":
    inp = input("entrer la matric des incidence : ")
    matric = literal_eval(inp)
    nextDict = getNextFromMatric(matric)
    print("\nTableau des suivants")
    format(nextDict)
    prevDict = getPreviousFromNext(nextDict)
    print("\nTableau des précedent")
    format(prevDict)
