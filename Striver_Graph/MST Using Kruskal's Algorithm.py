def FindParent(Node,Parent):
    if(Node == Parent[Node]):
        return Node
    Parent[Node] = FindParent(Parent[Node],Parent)
    return Parent[Node]

def Union(I,O,Parent,Rank):
    IParent = FindParent(I,Parent)
    OParent = FindParent(O,Parent)
    if(Rank[IParent] == Rank[OParent]):
        Parent[IParent] = OParent
        Rank[OParent] += 1
    elif(Rank[IParent] < Rank[OParent]):
        Parent[IParent] = OParent
    elif(Rank[OParent] < Rank[IParent]):
        Parent[OParent] = IParent

def KruskalAlgortihm(edges,n):
    edges.sort(key = lambda x:x[2])
    Parent = [i for i in range(n)]
    Rank = [0]*n
    MST = []
    for I,O,W in edges:
        IParent = FindParent(I,Parent)
        OParent = FindParent(O,Parent)
        if(IParent != OParent):
            Union(IParent,OParent,Parent,Rank)
            MST.append([I,O,W])
    return MST
    
n = 7
#edges = [[1,4,1],[1,2,2],[1,5,4],[5,4,9],[4,3,5],[4,2,3],[3,2,3],[3,6,8],[2,6,7]]
#edges = [[0,1,2],[1,2,3],[0,3,6],[3,1,8],[1,4,5],[4,2,7]]
edges = [[0,3,1],[3,4,9],[4,0,4],[3,2,5],[3,1,3],[0,1,2],[1,2,3],[2,5,8],[1,5,7]]
print(KruskalAlgortihm(edges,n))
