"""
Check If The Path Exist Or Not In Undirected Graph
Time Complexity - O(e) [e = no of edges]
Space Complexity - O(n) [n = no of nodes]
"""
def DFS(edges,start,end):
    graph = {}
    for i in edges:
        if(i[0] not in graph):
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]].append(i[1])
        if(i[1] not in graph):
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]].append(i[0])
    VisitDict = {K:False for K in graph.keys()}
    Stack = [start]
    while(Stack):
        Curr = Stack.pop(0)
        if(Curr == end): return True
        elif(Curr in graph and not VisitDict[Curr]):
            Stack.extend(graph[Curr])
        VisitDict[Curr] = True
    return False
    
def BFS(edges,start,end):
    graph = {}
    for i in edges:
        if(i[0] not in graph):
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]].append(i[1])
        if(i[1] not in graph):
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]].append(i[0])
    VisitDict = {K:False for K in graph.keys()}
    Stack = [start]
    while(Stack):
        Curr = Stack.pop()
        if(Curr == end): return True
        elif(Curr in graph and not VisitDict[Curr]):
            Stack.extend(graph[Curr])
        VisitDict[Curr] = True
    return False

Edges = [["i","j"],["k","i"],["m","k"],["k","l"],["o","n"]]

Source = "j"
Destination = "m"
print("Using DFS : ",DFS(Edges,Source,Destination))
print("Using BFS : ",BFS(Edges,Source,Destination))
