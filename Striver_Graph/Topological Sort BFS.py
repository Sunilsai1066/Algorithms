def ToAdList(edges,n):
    AdList = {i:[] for i in range(n)}
    for I,O in edges:
        AdList[I].append(O)
    return AdList

def TopologicalSort(edges,n):
    AdList = ToAdList(edges,n)
    def ToInNode(edges,n):
        InNode = [0]*n
        for I,O in edges:
            InNode[O] += 1
        return InNode
    InNode = ToInNode(edges,n)
    Res = []
    Queue = [i for i in range(n) if(InNode[i] == 0)]
    while(Queue):
        Curr = Queue.pop(0)
        Res.append(Curr)
        for i in AdList[Curr]:
            InNode[i] -= 1
            if(InNode[i] == 0):
                Queue.append(i)
    return Res

n = 6
edges = [[5,0],[5,2],[4,0],[4,1],[3,1],[2,3]]
print(TopologicalSort(edges,n))
