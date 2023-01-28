import sys
from p1 import hasP1

def getInput() -> None:
    IPfile = sys.argv[1]
    fp = open(IPfile, "r")
    numGraphs = int(fp.readline())
    cnt=0
    for i in range(numGraphs):
        s = fp.readline().strip().split(" ")
        V, E = int(s[0]), int(s[1])
        edges = []
        adjList=[[] for i in range(V)]
        for j in range(E):
            t = fp.readline().strip().split(" ")
            t[0], t[1] = int(t[0]), int(t[1])
            edges.append(t)
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
        if hasP1(V, E, adjList, edges)==False:
            print(i, "is the black sheep")
            cnt+=1 
    print(cnt)

getInput()