# this file checks for graph which are intersting, doesn't satify p1, p2 and has triangle
import sys
import triangle.hasTriangle as T
import p1Structure.p1 as P1
import p2structure.p2 as P2
import graphSearch.IG as IG

def getInput(filename) -> None:

    fp = open(filename, "r")
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
        
        cnd = P1.hasP1(V, adjList) or P2.hasP2(V, adjList)
        
        if cnd is True:
            print(i, "Accept !")
            cnt += 1
    
    print(cnt)

getInput(sys.argv[1])