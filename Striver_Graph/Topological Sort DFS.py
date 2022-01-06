def ToAdjList(edges,n):
    AdList = {i:[] for i in range(n)}
    for I,O in edges:
        AdList[I].append(O)
    return AdList
    
def TopologicalSort(edges,n):
    AdList = ToAdjList(edges,n)
    Visited = set()
    Stack = []
    def TopSort(Node,AdList,Visited,Stack):
        Visited.add(Node)
        for i in AdList[Node]:
            if i not in Visited:
                TopSort(i,AdList,Visited,Stack)
        Stack.insert(0,Node)
    for i in AdList.keys():
        if i not in Visited:
            TopSort(i,AdList,Visited,Stack)
    return Stack
    
edges = [[2,3],[3,1],[4,0],[4,1],[5,0],[5,2]]
n = 6
print(TopologicalSort(edges,n))
