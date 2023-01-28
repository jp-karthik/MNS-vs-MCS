from itertools import combinations, permutations
from isInteresting import isInteresting
import sys

def P1(v:int, g:list[list], s:list) -> bool: # check for the general subgraph condition
    # a->0,b->1,c->2,d->3,e->4,g->adjList,s->sequence
    c1 =  g[s[3]].count(s[0])>0 and g[s[1]].count(s[0])>0 and g[s[1]].count(s[2])>0 and g[s[1]].count(s[4])>0 and g[s[2]].count(s[4])>0 # all required edges
    c2 = True # no common neighbour between a and b
    c3 = True # no common neighbour between a and c
    c4 = True # no common neighbour between a and e
    c5 = not (g[s[2]].count(s[0])>0 and g[s[4]].count(s[0])>0) # (a,c) and (a,e) is not in E(G)
    for node in range(v):
        if g[node].count(s[0])>0 and g[node].count(s[1])>0 and node!=s[2] and node!=s[4]:
            c2 = False
        if g[node].count(s[0])>0 and g[node].count(s[2])>0 and node!=s[1]:
            c3 = False
        if g[node].count(s[0])>0 and g[node].count(s[4])>0 and node!=s[1]:
            c4 = False
    finalCnd = c1 and c2 and (c3 or c4) and c5
    return True if finalCnd else False

def checkP1(v:int, e:int, adjList, edges) -> bool: #return true if graph doesnt have p1
    if isInteresting(v, e, edges):
        vertexSet = [i for i in range(v)]
        combs = list(combinations(vertexSet, 5))
        for comb in combs:
            perms = list(permutations(comb))
            for perm in perms:
                if P1(v, adjList, perm):
                    return True
        return False
    else:
        return False
    
def hasTraingle(v, e, g: list[list]) -> bool: #return true if graph has triangle
    vertexSet = [i for i in range(v)]
    for X in combinations(vertexSet, 3):
        c1 = X[0] in g[X[1]]
        c2 = X[1] in g[X[2]]
        c3 = X[2] in g[X[0]]
        if c1 and c2 and c3:
            return True
    return False

def check(v, e, edges, g):

    if isInteresting(v, e, edges)==True:
        if checkP1(v, e, g, edges)==False and hasTraingle(v, e, g)==True:
            return True
    
    return False

def getInput():
    IPfile = sys.argv[1]
    fp = open(IPfile, "r")
    numGraphs = int(fp.readline())
    cnt=0
    for i in range(numGraphs):
        s = fp.readline().strip().split(" ")
        v, e = int(s[0]), int(s[1])
        edges = []
        adjList=[[] for i in range(v)]
        for j in range(e):
            t = fp.readline().strip().split(" ")
            t[0], t[1] = int(t[0]), int(t[1])
            edges.append(t)
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
        if check(v, e, edges, adjList)==True:
            print("alert")       
            cnt += 1
        else:
            print(i)
    print(cnt)  
getInput()

