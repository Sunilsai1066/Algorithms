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

def Bipartite(edges):
    graph = ToGraph(edges)
    Color = [-1 for _ in range(len(graph.keys())+1)]
    def CheckBipartate(graph,Node,Color,PrevColor):
        Color[Node] = PrevColor
        for i in graph[Node]:
            if(Color[i] == -1):
                if(CheckBipartate(graph,i,Color,1-PrevColor) == False):
                    return False
            elif(Color[i] == PrevColor):
                return False
        return True
    for i in graph.keys():
        if(Color[i] ==  -1):
            PrevColor = 0
            if(CheckBipartate(graph,i,Color,PrevColor) == False):
                return False
    return True
    
#edges = [[1,2],[2,3],[2,8],[3,4],[8,5],[4,5],[5,6],[6,7]]
#edges = [[1,2],[2,3],[3,4],[4,5],[5,8],[2,7],[7,6],[6,5]]
#edges = [[0,1],[1,2],[2,3],[3,0],[0,2]]
#edges = [[0,1],[1,2],[2,3],[3,0]]
edges = [[1,2],[1,3],[2,3]]
print(Bipartite(edges))
