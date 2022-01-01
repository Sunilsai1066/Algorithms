def BFS_Traversal(AdjList):
    BFS_Result = []
    Visit = set()
    for K in AdjList.keys():
        if K not in Visit:
            Stack = [K]
            while(Stack):
                Curr = Stack.pop()
                Visit.add(Curr)
                BFS_Result.append(Curr)
                for V in AdjList[Curr]:
                    if V not in Visit:
                        Stack.append(V)
                        Visit.add(V)
                        
    return BFS_Result

AdjList = {
    1:[2],
    2:[1,4,7],
    3:[5],
    4:[2,6],
    5:[3],
    6:[4,7],
    7:[2,6]}

print(BFS_Traversal(AdjList))
