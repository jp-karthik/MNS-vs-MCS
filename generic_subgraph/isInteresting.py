from mns import MNS
from mcs import MCS

def isInteresting(v, e, edges):
    mns = MNS(v, e, edges)
    mcs = MCS(v, e, edges)
    mns.performAllPossible()
    mcs.performAllPossible()
    if (mns.getSize() == mcs.getSize()):
        return False
    else:
        return True