import heapq
def ToAdList(edges,n):
    AdList = {i:[] for i in range(1,n+1)}
    for I,O,W in edges:
        AdList[I].append((O,W))
        AdList[O].append((I,W))
    return AdList

def DijkstraAlgorithm(edges,n,Source):
    AdList = ToAdList(edges,n)
    DistList = [float("inf")]*(n+1)
    DistList[Source] = 0
    MinHeap = [(DistList[Source],1)]
    heapq.heapify(MinHeap)
    while(MinHeap):
        Dist,Node = heapq.heappop(MinHeap)
        for AdNode,AdWt in AdList[Node]:
            if(Dist+AdWt < DistList[AdNode]):
                DistList[AdNode] = Dist+AdWt 
                heapq.heappush(MinHeap,(DistList[AdNode],AdNode))
    return DistList[1:]

n = 5
edges = [[1,2,2],[2,5,5],[1,4,1],[4,3,3],[3,2,4],[3,5,1]]
Source = 1
print(DijkstraAlgorithm(edges,n,Source))
