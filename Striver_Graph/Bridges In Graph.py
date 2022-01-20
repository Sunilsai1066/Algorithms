def ToAdList(edges,n):
    AdList = {i:[] for i in range(n)}
    for I,O in edges:
        AdList[I].append(O)
        AdList[O].append(I)
    return AdList

def DFS(Node,Parent,Vis,InTime,Low,Time,AdList):
    Vis[Node] = 1
    InTime[Node] = Low [Node] = Time
    Time += 1
    for SubNode in AdList[Node]:
        if(SubNode == Parent):
            continue
        if(Vis[SubNode] == 0):
            DFS(SubNode,Node,Vis,InTime,Low,Time,AdList)
            Low[Node] = min(Low[Node],Low[SubNode])
            if(Low[SubNode] > InTime[Node]):
                print([Node,SubNode])
        else:
            Low[Node] = min(Low[Node],InTime[SubNode])

def BridgeAlgorithm(edges,n,Source):
    AdList = ToAdList(edges,n)
    Vis = [0]*n
    InTime = [-1]*n
    Low = [-1]*n
    Time = 1
    print(AdList)
    for Node in AdList.keys():
        if(Vis[Node] == 0):
            DFS(Node,-1,Vis,InTime,Low,Time,AdList)
    
n,Source = 6,1
edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[3,0]]
BridgeAlgorithm(edges,n,Source)
