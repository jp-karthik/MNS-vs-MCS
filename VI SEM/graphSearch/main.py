import sys
from IG import isInteresting

def getInput(filename):
    fp = open(filename, "r")
    if fp:
        numGraphs = int(fp.readline())
        cnt=0
        for i in range(numGraphs):
            s = fp.readline().strip().split(" ")
            V, E = int(s[0]), int(s[1])
            edges = []
            for j in range(E):
                t = fp.readline().strip().split(" ")
                t[0], t[1] = int(t[0]), int(t[1])
                edges.append(t)
            if isInteresting(V, E, edges):
                print(i, "is interesting")
                cnt += 1            
        print(cnt)

getInput(sys.argv[1])