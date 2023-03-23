# Description: Implementation of the IG algorithm
from mns import MNS
from mcs import MCS

def isInteresting(V:int, E:int, edges:list) -> bool:
    
    mns = MNS(V, E, edges) # create an instance of MNS class
    mcs = MCS(V, E, edges) # create an instance of MCS class
    
    mns.performAllPossible() # perform MNS algorithm to get all possible orderings
    mcs.performAllPossible() # perform MCS algorithm to get all possible orderings
    
    # if the number of orderings of MNS and MCS are equal, then the graph is not interesting
    if mns.getSize() == mcs.getSize(): # using is not working, instead use ==
        return False
    else:
        return True