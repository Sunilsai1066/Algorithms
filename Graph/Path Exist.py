def DFS(graph,Source,Destination):
    Stack = [Source]
    Res = []
    while(Stack):
        Curr = Stack.pop()
        Res.append(Curr)
        if(Curr == Destination): return True
        for neighbour in graph[Curr]:
            Stack.append(neighbour)
    return False

def BFS(graph,Source,Destination):
    Stack = [Source]
    Res = []
    while(Stack):
        Curr = Stack.pop(0)
        Res.append(Curr)
        if(Curr == Destination): return True
        for neighbour in graph[Curr]:
            Stack.append(neighbour)
    return False
    
graph = {
    "f" : ["g","i"],
    "g" : ["h"],    
    "h" : [],
    "i" : ["g","k"],
    "j" : ["i"],
    "k" : []
}

Source = "f"
Destination = "i"
print("Using DFS : ",DFS(graph,Source,Destination))
print("Using BFS : ",BFS(graph,Source,Destination))
