# this file checks for graph which are intersting, doesn't satify p1, p2 and has triangle

import sys
import triangle.hasTriangle as T
import p1Structure.p1 as P1
import p2structure.p2 as P2

def getInput(filename) -> None:

    fp = open(filename, "r")
    numGraphs = int(fp.readline())
    
    cnt=0
    
    for i in range(numGraphs):
        s = fp.readline().strip().split(" ")

        V, E = int(s[0]), int(s[1])
        edges = []
        adjList=[[] for i in range(V)]
        
        for j in range(E): # read the edges
            t = fp.readline().strip().split(" ")
            t[0], t[1] = int(t[0]), int(t[1])
            edges.append(t)
        
        for edge in edges: # create the adjacency list
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        if P1.hasP1(V, adjList)==False and P2.hasP2(V, adjList)==False and T.hasTraingle(V, adjList)==True:
            print(i, "SUS !")
            cnt += 1

    print(cnt)

getInput(sys.argv[1])