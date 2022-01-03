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
            
def CycleDetection(edges):
    def CycleCheck(Node,graph,Visited):
        Queue = [(Node,-1)]
        while(Queue):
            Curr,Parent = Queue.pop()
            for i in graph[Curr]:
                if i not in Visited:
                    Queue.append((i,Curr))
                    Visited.add(i)
                elif(i in Visited and i!=Parent):
                    return True
    graph = ToGraph(edges)    
    Visited = set()
    for i in graph.keys():
        if i not in Visited:
            Visited.add(i)
            if(CycleCheck(i,graph,Visited) == True):
                return True
    return False
    
edges = [[1,3],[3,4],[2,5],[5,8],[5,6],[6,7],[7,8]]
print(CycleDetection(edges))
