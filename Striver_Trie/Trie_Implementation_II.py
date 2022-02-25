class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.Equals = 0
        self.StartWith = 0

Root = Node()
RtCopy = Root

class Trie:
    def __init__(self):
        self.Root = Root
        self.RtCopy = RtCopy

    def insert(self,word):
        self.Root = Root
        for letter in word:
            if(self.Root.NodeLinks[ord(letter)-97] == 0):
                #print("Entered None")
                self.NewLink = Node()
                self.NewLink.StartWith += 1
                self.Root.NodeLinks[ord(letter)-97] = self.NewLink
                #print(self.Root.NodeLinks[ord(letter)-97])
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                self.Root.NodeLinks[ord(letter)-97].StartWith += 1
                self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Equals += 1
        #print()
        
    def countWordsEqualTo(self,word):
        self.Root = Root
        for letter in word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return 0
        return self.Root.Equals
        
    def countWordsStartingWith(self,word):
        self.Root = Root
        for letter in word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return 0
        return self.Root.StartWith
    
    def erase(self,word):
        self.Root = Root
        for letter in word:
            self.Root.NodeLinks[ord(letter)-97].StartWith -= 1
            self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Equals -= 1

Tr = Trie()
Tr.insert("samsung")
Tr.insert("samsung")
Tr.insert("vivo")
Tr.erase("vivo")
print(Tr.countWordsEqualTo("samsung"))
print(Tr.countWordsStartingWith("vi"))
