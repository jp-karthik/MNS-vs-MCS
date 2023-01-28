from mns import MNS
from mcs import MCS
import sys
from isInteresting import isInteresting

def getInput():
    IPfile = sys.argv[1]
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
            print(i, "is interesting")
            cnt += 1            
    print(cnt)

getInput()

