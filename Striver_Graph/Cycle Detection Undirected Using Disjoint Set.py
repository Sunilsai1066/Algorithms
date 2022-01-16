def FindParent(NodeA,Parent):
    while(Parent[NodeA] != -1):
        NodeA = Parent[NodeA]
    return NodeA

def Union(I,O,Parent):
    IParent = FindParent(I,Parent)
    OParent = FindParent(O,Parent)
    Parent[IParent] = OParent
    
def CycleDetectionDisjoint(edges,n):
    Parent = [-1]*n
    for I,O in edges:
        IParent = FindParent(I,Parent)
        OParent = FindParent(O,Parent)
        if(IParent == OParent):
            return True
        Union(IParent,OParent,Parent)
            
    return False

n = 4
edges = [[0,1],[0,3],[2,3],[1,2]]
print(CycleDetectionDisjoint(edges,n))
