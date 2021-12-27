def DFS(graph,Source):
    Stack = [Source]
    Res = []
    while(Stack):
        Curr = Stack.pop()
        Res.append(Curr)
        for neighbour in graph[Curr]:
            Stack.append(neighbour)
    return Res

def BFS(graph,Source):
    Stack = [Source]
    Res = []
    while(Stack):
        Curr = Stack.pop(0)
        Res.append(Curr)
        for neighbour in graph[Curr]:
            Stack.append(neighbour)
    return Res
    
graph = {
    "a" : ["c","b"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : []
}

Source = "a"
print("DFS : ",DFS(graph,Source))
print("BFS : ",BFS(graph,Source))
