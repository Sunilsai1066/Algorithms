def NegativeWtCycle(edges,NegCycleArr):
    for In,Out,Wt in edges:
        if((NegCycleArr[In]+Wt) < NegCycleArr[Out]):
            NegCycleArr[Out] = NegCycleArr[In]+Wt
    return NegCycleArr

def CheckDistances(Dist,CycleDist):
    Len = len(Dist)
    for i in range(Len):
        if(Dist[i] != CycleDist[i]):
            return True
    return False
    
def BellmanFordAlgorithm(edges,n):
    DistArr = [float('inf')]*n
    DistArr[0] = 0
    for i in range(n-1):
        for In,Out,Wt in edges:
            if((DistArr[In]+Wt) < DistArr[Out]):
                DistArr[Out] = DistArr[In]+Wt
    NegCycleArr = NegativeWtCycle(edges,DistArr[:])
    print("Negative Cycle In Graph : ",CheckDistances(DistArr,NegCycleArr))
    return "Final Distance Array",DistArr
    
#n = 6
#edges = [[0,1,5],[1,2,-2],[2,4,3],[1,5,-3],[5,3,1],[3,2,6],[3,4,-2]]
n = 4
edges = [[0,1,1],[1,2,-1],[2,3,-1],[3,0,-1]]
print(*BellmanFordAlgorithm(edges,n))
