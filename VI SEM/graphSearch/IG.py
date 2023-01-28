from mns import MNS
from mcs import MCS
def isInteresting(V, E, edges):
    mns = MNS(V, E, edges)
    mcs = MCS(V, E, edges)
    mns.performAllPossible()
    mcs.performAllPossible()
    if (mns.getSize() == mcs.getSize()):
        return False
    else:
        return True