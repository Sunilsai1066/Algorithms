#https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

import heapq
class Solution:

    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        Key = [float("inf")]*V
        MST = [False]*V
        Parent = [-1]*V
        Key[0] = 0
        PriorityQueue = [(0,0)]
        heapq.heapify(PriorityQueue)
        while(PriorityQueue):
            NodeWt,NodeKey = heapq.heappop(PriorityQueue)
            MST[NodeKey] = True
            for AdNode,AdWt in adj[NodeKey]:
                if(MST[AdNode] == False):
                    if(AdWt < Key[AdNode]):
                        Key[AdNode] = AdWt
                        Parent[AdNode] = NodeKey
                        heapq.heappush(PriorityQueue,(AdWt,AdNode))
        return sum(Key)
