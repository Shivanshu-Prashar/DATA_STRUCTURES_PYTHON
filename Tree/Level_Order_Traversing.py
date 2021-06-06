class Tree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
t=Tree("test")
q=Queue()
N1=Tree("N1")
N2=Tree("N2")
N3=Tree("N3")
N4=Tree("N4")
N5=Tree("N5")
N6=Tree("N6")
N7=Tree("N7")
N8=Tree("N8")
N9=Tree("N9")

N1.leftchild=N2
N1.rightchild=N3

N2.leftchild=N4
N2.rightchild=N5

N4.leftchild=N8
N4.rightchild=N9

N3.leftchild=N6
N3.rightchild=N7

def LevelOrder(root):
    if root is None:
        return "No Node"
    q.enqueue(N1)
    while q.size()!=0:
        p=q.dequeue()
        print(p.data,"-->",end=" ")
        if p.leftchild is not None:
            q.enqueue(p.leftchild)
        if p.rightchild is not None:
            q.enqueue(p.rightchild)

LevelOrder(N1)
print("\n")


