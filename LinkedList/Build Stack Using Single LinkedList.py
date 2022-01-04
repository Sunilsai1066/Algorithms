class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def IsNull(self):
        if(self.head == None):
            print(True)
            return
        print(False)
    def Push(self,data):
        if(self.head == None):
            self.head = Node(data)
        else:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
    def Pop(self):
        if(self.head == None):
            print("Stack Is Empty")
            return
        OutData = self.head
        self.head = self.head.next
        OutData.next = None
        print(OutData.data)
    def Top(self):
        if(self.head == None):
            print("Stack Is Empty")
            return
        print(self.head.data)
    def ViewData(self):
        Curr = self.head
        while(Curr != None):
            print(Curr.data,end=" ")
            Curr = Curr.next

St = Stack()
St.Push(10)
St.IsNull()
St.Push(11)
St.Push(12)
St.Top()
St.Pop()
St.Top()
St.ViewData()
