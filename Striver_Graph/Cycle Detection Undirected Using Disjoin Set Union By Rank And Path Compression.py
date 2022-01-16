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

def CycleDetectionDisjoint(edges,n):
    Parent = [i for i in range(n)]
    Rank = [0]*n
    for I,O in edges:
        IParent = FindParent(I,Parent)
        OParent = FindParent(O,Parent)
        if(IParent == OParent):
            return True
        Union(IParent,OParent,Parent,Rank)
    return False
    
n = 5
edges = [[0,1],[2,3],[1,2],[0,4],[4,3]]
#edges = [[0,1],[2,3],[1,2],[0,4]]
print(CycleDetectionDisjoint(edges,n))
