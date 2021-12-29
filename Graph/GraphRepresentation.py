# Adjacency Matrix
def CreateAdjMatrix(N, E, edges):
    AdMat = [[0 for j in range(N)] for i in range(N)]
    for i in edges:
        R, C = i
        AdMat[R - 1][C - 1] = 1
        AdMat[C - 1][R - 1] = 1
    return AdMat


def AdjList(N, E, edges) -> dict:
    graph = {K: [] for K in range(N + 1)}
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    return graph


N = 5
E = 7
edges = [
    [1, 2],
    [2, 3],
    [2, 4],
    [4, 3],
    [3, 5],
    [5, 1],
    [1, 3]
]

print("Adjacency Matrix")
print(CreateAdjMatrix(N, E, edges))
print("Adjacency List")
print(AdjList(N, E, edges))
