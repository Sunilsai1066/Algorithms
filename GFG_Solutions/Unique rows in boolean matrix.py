#Using Trie+DFS
#User function Template for python3
class TrieNode:
    def __init__(self):
        self.NodeLinks = {}
        self.Count = 0

class Trie:
    def __init__(self):
        self.Root = TrieNode()

    def insertRow(self,Row):
        Node = self.Root
        for bit in Row:
            if(bit not in Node.NodeLinks):
                Node.NodeLinks[bit] = TrieNode()
            Node = Node.NodeLinks[bit]
        Node.Count += 1

    def printUnique(self,Row):
        Node = self.Root
        for bit in Row:
            Node = Node.NodeLinks[bit]
        if(Node.Count != 0):
            Node.Count = 0
            return True
        return False

def uniqueRow(row, col, matrix):
    Tr = Trie()
    subMat = []
    for i in range(0,len(matrix),col):
        subMat.append(matrix[i:i+col])
    FinRes = []
    for Row in subMat:
        Tr.insertRow(Row)
    for Row in subMat:
        if(Tr.printUnique(Row)):
            FinRes.append(Row)
    return FinRes


#Using Set
def uniqueRow(row, col, matrix):
    Set,Res = set(),[]
    for i in range(0,len(matrix),col):
        subMat = matrix[i:i+col]
        if(tuple(subMat) not in Set):
            Res.append(subMat)
            Set.add(tuple(subMat))
    return Res
