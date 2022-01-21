def ToAdList(edges,n):
    AdList = {i:[] for i in range(n)}
    for In,Out in edges:
        AdList[In].append(Out)
    return AdList

def TopoSort(AdList):
    Res = []
    Visit = set()
    def Sort(Node,Visit,AdList,Sort,Res):
        Visit.add(Node)
        for i in AdList[Node]:
            if i not in Visit:
                Sort(i,Visit,AdList,Sort,Res)
        Res.append(Node)
    for Node in AdList.keys():
        if Node not in Visit:
            Sort(Node,Visit,AdList,Sort,Res)
    return Res

def TransposeGraph(edges,n):
    Reverse = {i:[] for i in range(n)}
    for In,Out in edges:
        Reverse[Out].append(In)
    return Reverse
    
def SCC(GraphT):
    Res = []
    Visit = set()
    Count = 0
    def DFS(Node,Visit,GraphT,SubRes):
        Visit.add(Node)
        SubRes.append(Node)
        for i in GraphT[Node]:
            if i not in Visit:
                DFS(i,Visit,GraphT,SubRes)
                
    for i in GraphT.keys():
        if i not in Visit:
            Count += 1
            SubRes = []
            DFS(i,Visit,GraphT,SubRes)
            Res.append(SubRes)
    return Res
    
def KosarajuAlgorithm(edges,n):
    AdList = ToAdList(edges,n)
    TopSorted = TopoSort(AdList)
    GraphT = TransposeGraph(edges,n)
    SCCRes = SCC(GraphT)
    return SCCRes
    
n = 5
edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]
n = 6
edges = [[0,2],[2,1],[1,0],[2,4],[4,3],[3,5],[5,4]]
print(KosarajuAlgorithm(edges,n))
