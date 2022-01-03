def ToAdjList(edges,n):
    AdList = {i:[] for i in range(1,n+1)}
    for I,O in edges:
        AdList[I].append(O)
    return AdList
    
def CycleDetectionDirected(edges,n):
    AdList = ToAdjList(edges,n)
    Visited = [0]*(n+1)
    DFSVisit = [0]*(n+1)
    def Cycle(Node,AdList,Visited,DFSVisit):
        Visited[Node] = 1
        DFSVisit[Node] = 1
        for i in AdList[Node]:
            if(Visited[i] == 0):
                if(Cycle(i,AdList,Visited,DFSVisit) == True): return True
            elif(DFSVisit[i] == 1):
                return True
        DFSVisit[Node] = 0
    for i in AdList.keys():
        if i not in Visited:
            if(Cycle(i,AdList,Visited,DFSVisit) == True):
                return True
    return False
    
edges = [[1,2],[2,3],[3,4],[3,6],[4,5],[6,5],[7,2],[7,8],[8,9],[9,7]]
n = 9
print(CycleDetectionDirected(edges,n))
