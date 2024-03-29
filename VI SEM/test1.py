# this file checks for graph which are intersting, doesn't satify p1 and has triangle

import sys
import triangle.hasTriangle as T
import p1Structure.p1 as P1

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
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        if T.hasTraingle(V, adjList)==True and P1.hasP1(V, adjList)==False:
            print(i, "SUS!")
            cnt += 1
            
    print(cnt)

getInput(sys.argv[1])