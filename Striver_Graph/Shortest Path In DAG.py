def ToAdList(edges,n):
    AdLis = {i:[] for i in range(n)}
    for I,O,W in edges:
        AdLis[I].append((O,W))
    return AdLis
def TopSort(AdLis):
    Res = []
    Visited = set()
    def Sort(Node,AdLis,Visited,Res):
        Visited.add(Node)
        for O,W in AdLis[Node]:
            if O not in Visited:
                Sort(O,AdLis,Visited,Res)
        Res.append(Node)
    for i in AdLis.keys():
        if i not in Visited:
            Sort(i,AdLis,Visited,Res)
    return Res

def ShortestDistance(edges,n):
    AdLis = ToAdList(edges,n)
    SortLis = TopSort(AdLis)
    DistList = [float("inf")]*n
    DistList[SortLis[-1]] = 0
    while(SortLis):
        Curr = SortLis.pop()
        CurrW = DistList[Curr]
        for O,W in AdLis[Curr]:
            if(CurrW+W < DistList[O]):
                DistList[O] = CurrW+W
    return DistList
    
n = 6
edges = [[0,1,2],[0,4,1],[1,2,3],[2,3,6],[4,2,2],[4,5,4],[5,3,1]]
print(ShortestDistance(edges,n))
