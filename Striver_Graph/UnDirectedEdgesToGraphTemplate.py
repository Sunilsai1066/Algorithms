def ToGraph(edges):
    graph = {}
    for I,O in edges:
        if I not in graph:
            graph[I] = [O]
        else:
            graph[I].append(O)
        if O not in graph:
            graph[O] = [I]
        else:
            graph[O].append(I)
    return graph
    
edges = [[1,2],[2,4],[3,5],[5,10],[5,6],[6,7],[7,8],[10,9],[9,8],[8,11]]
print(ToGraph(edges))
