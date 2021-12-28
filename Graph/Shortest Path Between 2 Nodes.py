def ShortestPath(edges,start,end):
    graph = {}
    for i in edges:
        if i[0] not in graph:
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]].append(i[1])
        if i[1] not in graph:
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]].append(i[0])
    Visit = set()
    Res = -1
    Level = -1
    Stack = [start]
    while(Stack):
        StackLen = len(Stack)
        for i in range(StackLen):
            Curr = Stack.pop(0)
            if(Curr == end): return Level+1
            if(Curr in graph and Curr not in Visit):
                Stack.extend(graph[Curr])
                Visit.add(Curr)
        Level += 1
    return Res

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
start = "w"
end = "y"
print(ShortestPath(edges,start,end))
