class Singly:
    def __init__(self,v):
        self.value=v
        self.nextnode=None
x1=Singly("a@gmail.com")
x2=Singly("b@gmail.com")
x3=Singly("c@gmail.com")
x4=Singly("d@gmail.com")
x1.nextnode=x2
x2.nextnode=x3
x3.nextnode=x4

head=x1
while head is not None:
    print(head.value)
    head=head.nextnode
