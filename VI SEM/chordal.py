import sys
sys.path.append("/Users/karthikjp/Desktop/MNS-vs-MCS/VI SEM/graphSearch") # add the parent directory to the path

import graphSearch.IG as IG

# from IG import isInteresting # import the function isInteresting from IG.py

def getInput(filename):
    
    fp = open(filename, "r")

    if fp: # if the file is opened successfully

        numGraphs = int(fp.readline())
        
        cnt=0 # count the number of interesting graphs

        for i in range(numGraphs):
            s = fp.readline().strip().split(" ")

            V, E = int(s[0]), int(s[1])
            edges = []
            
            for j in range(E):
                t = fp.readline().strip().split(" ")
                t[0], t[1] = int(t[0]), int(t[1])
                edges.append(t)
            
            if E == V-1:
                print(edges)
                print("idx: ", i)
                cnt += 1

        print(cnt)

getInput(sys.argv[1])