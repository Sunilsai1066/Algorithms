def BFS_Traversal(AdjList):
    BFS_Result = []
    Visit = set()
    for K in AdjList.keys():
        if K not in Visit:
            Stack = [K]
            while(Stack):
                Curr = Stack.pop(0)
                Visit.add(Curr)
                BFS_Result.append(Curr)
                for V in AdjList[Curr]:
                    if V not in Visit:
                        Stack.append(V)
                        
    return BFS_Result

AdjList = {
    1:[2],
    2:[1,3,7],
    3:[2,5],
    4:[6],
    5:[3,7],
    6:[4],
    7:[2,5]}

print(BFS_Traversal(AdjList))
