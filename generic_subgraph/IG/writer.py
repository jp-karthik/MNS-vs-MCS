from mns import MNS
from mcs import MCS

def isInteresting(v, e, edges):
    mns = MNS(v, e, edges)
    mcs = MCS(v, e, edges)
    mns.performAllPossible()
    mcs.performAllPossible()
    if (mns.getSize() == mcs.getSize()):
        return False
    else:
        return True

def getInput():
    IPfile = "graph.txt"
    fp = open(IPfile, "r")
    numGraphs = int(fp.readline())
    cnt=0
    for i in range(numGraphs):
        s = fp.readline().strip().split(" ")
        v, e = int(s[0]), int(s[1])
        edges = []
        for j in range(e):
            t = fp.readline().strip().split(" ")
            t[0], t[1] = int(t[0]), int(t[1])
            edges.append(t)
        if isInteresting(v, e, edges):
            print(v,e)
            for e in edges:
                print(e[0], e[1])
            cnt += 1            
    print(cnt)

getInput()

