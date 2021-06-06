class QUEUE:
    def __init__(self):
        self.items=[]
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
q1=QUEUE()
x=input("Enter the element to put in queue: ")
q1.enqueue(x)
print("Items In The Queue Are: ",q1.items)
print("Size Of The Queue is : ",q1.size())
print("Is Queue Empty: ",q1.isEmpty())
print("Removing/Dequeuing the element from queue: ", q1.dequeue())
