import heapq
def ToAdList(edges,n):
    AdList = {i:[] for i in range(n)}
    for I,O,W in edges:
        AdList[I].append((O,W))
        AdList[O].append((I,W))
    return AdList

def PrimsAlgorithm(edges,n):
    AdList = ToAdList(edges,n)
    Key = [float("inf")]*n
    MST = [False]*n
    Parent = [-1]*n
    Key[0] = 0
    PriorityQueue = [(0,0)]
    heapq.heapify(PriorityQueue)
    while(PriorityQueue):
        NodeWt,NodeKey = heapq.heappop(PriorityQueue)
        MST[NodeKey] = True
        for AdNode,AdWt in AdList[NodeKey]:
            if(MST[AdNode] == False):
                if(AdWt < Key[AdNode]):
                    Key[AdNode] = AdWt
                    Parent[AdNode] = NodeKey
                    heapq.heappush(PriorityQueue,(AdWt,AdNode))
    
    FinalResult = []
    for i in range(1,len(Parent)):
        FinalResult.append([Parent[i],i,Key[i]])
    return FinalResult
    
n = 5
edges = [[0,1,2],[1,2,3],[0,3,6],[3,1,8],[1,4,5],[4,2,7]]
#edges = [[0,3,1],[3,4,4],[4,0,4],[3,2,5],[3,1,3],[0,1,2],[1,2,3],[2,5,8],[1,5,7]]
print(PrimsAlgorithm(edges,n))
