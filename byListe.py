# l =[(1,2),(1,3),(1,4),(2,5),(5,2)]
# 1,2 1,3 1,4 1,5 1,7 2,3 2,4 2,7 3,4 3,5 3,6 4,5 4,6 5,6 5,7 6,7
import collections
def nextDictFromList(list):
    nextDict = {}
    for arc in list:
        if(arc[0] in nextDict):
            nextDict[arc[0]].append(arc[1]) 
        else:
            nextDict[arc[0]] = [arc[1]]
        if arc[1] not in nextDict:
            nextDict[arc[1]] = []
    od = collections.OrderedDict(sorted(nextDict.items()))
    return od

def getPreviousFromNext(nextDict):
    prevDict = {}
    for k in nextDict:
        prevDict[k] = []
        for j in nextDict:
            if(k in nextDict[j]):
                prevDict[k].append(j)
    return prevDict


def toList(str):
    l = []
    arr = str.split(' ')
    for string_tuple in arr:
        t = tuple(string_tuple.replace(',',''))
        l.append((int(t[0]),int(t[1])))
    return l
def format(dict):
    for i in range(len(dict)):
        print(f'{i+1}\t{dict[i+1]}')
if __name__ == "__main__":
    t = input("entrer la list : ")
    res = nextDictFromList(toList(t))
    print("\nTableau des suivants")
    nextsTable = nextDictFromList(toList(t))
    format(nextsTable)
    print("\nTableau des précedent")
    prevTable = getPreviousFromNext(nextsTable)
    format(prevTable)
