class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def IsNull(self):
        print(self.head == None)
    def Push(self,data):
        if(self.head == None):
            self.head = Node(data)
        else:
            Curr = self.head
            Prev = None
            while(Curr):
                Prev = Curr
                Curr = Curr.next
            Prev.next = Node(data)
    def Pop(self):
        if(self.head == None):
            print("Queue Is Empty")
            return
        Prevhead = self.head
        self.head = self.head.next
        Prevhead.next = None
        print(Prevhead.data)
    def Bottom(self):
        if(self.head == None):
            print("Queue Is Empty")
            return
        print(self.head.data)
    def Top(self):
        Prev = None
        if(self.head == None):
            print("Queue Is Empty")
            return
        Curr = self.head
        while(Curr != None):
            Prev = Curr.data
            Curr = Curr.next
        print(Prev)
    def ViewData(self):
        if(self.head == None):
            print("Queue Is Empty")
            return
        Curr = self.head
        while(Curr != None):
            print(Curr.data,end=" ")
            Curr = Curr.next
        print()

q = Queue()
q.IsNull()
q.Top()
q.Push(10)
q.Push(12)
q.Push(14)
q.Push(16)
q.IsNull()
q.ViewData()
q.Pop()
q.ViewData()
q.Top()
q.Bottom()
q.Pop()
q.ViewData()
