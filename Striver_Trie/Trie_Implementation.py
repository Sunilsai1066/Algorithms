import sys
class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.Flag = False

class Trie:
    def __init__(self):
        self.Main = Node()
        self.Root = self.Main
        self.RtCopy = self.Root
        
    def Insert(self,Word):
        self.Root = self.Main
        self.RtCopy = self.Root
        for letter in Word:
            #print(letter)
            if(self.Root.NodeLinks[ord(letter)-97] == 0):
                self.NextLink = Node()
                self.Root.NodeLinks[ord(letter)-97] = self.NextLink
                self.Root = self.Root.NodeLinks[ord(letter)-97]
                
            else:
                self.Root = self.Root.NodeLinks[ord(letter)-97]
        
        self.Root.Flag = True
        
    def Search(self,Word):
        self.Root = self.Main
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return False
        return self.Root.Flag == True
        
    
    def Startswith(self,Word):
        self.Root = self.Main
        SWith = True
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                SWith = False
                break
        return SWith


Tr = Trie()
Tr.Insert("game")
Tr.Insert("gama")
Tr.Insert("gamaded")
Tr.Insert("gamarad")
print("********Search************")
print(Tr.Search("gamas"))
Tr.Insert("gamas")
Tr.Insert("sunil")
Tr.Insert("suneel")
Tr.Insert("bhargs")
print(Tr.Search("gama"))
print(Tr.Search("gamar"))
print(Tr.Search("gamara"))
print(Tr.Search("gamarad"))
print(Tr.Search("gamarads"))
print("********Startswith************")
print(Tr.Startswith("ga"))
print(Tr.Startswith("sunil"))
print(Tr.Startswith("su"))
print(Tr.Startswith("bh"))
print(Tr.Startswith("aa"))
print(Tr.Startswith("gas"))
