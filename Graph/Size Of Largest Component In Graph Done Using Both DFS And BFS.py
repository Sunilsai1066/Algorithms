def ConnectedComponentsCountDFS(edges):
    VisitDict = {K:False for K in edges.keys()}
    Max = 0
    for K in edges.keys():
        if(not VisitDict[K]):
            Stack = [K]
            Count = 0
            while(Stack):
                Curr = Stack.pop()
                if(not VisitDict[Curr]):
                    Count += 1
                    Stack.extend(edges[Curr])
                    VisitDict[Curr] = True
            if(Count > Max):Max = Count
    return Max
    
def ConnectedComponentsCountBFS(edges):
    VisitDict = {K:False for K in edges.keys()}
    Max = 0
    for K in edges.keys():
        if(not VisitDict[K]):
            Stack = [K]
            Count = 0
            while(Stack):
                Curr = Stack.pop(0)
                if(not VisitDict[Curr]):
                    Count += 1
                    Stack.extend(edges[Curr])
                    VisitDict[Curr] = True
            if(Count > Max):Max = Count
    return Max

edges = {
    0 : [8,1,5],
    1 : [0],
    5 : [0,8],
    8 : [0,5],
    2 : [3,4],
    3 : [2,4],
    4 : [3,2],
    11 : [12],
    12 : [11]
}

print(ConnectedComponentsCountDFS(edges))
print(ConnectedComponentsCountBFS(edges))