class BST:
    def __init__(self,data):
        self.data=data
        self.LeftChild=None
        self.RightChild=None
root=BST(None)
def InsertNode(rootNode,data):
    if rootNode.data is None:
        rootNode.data=data
    elif data < rootNode.data:
        if rootNode.LeftChild is None:
            rootNode.LeftChild=BST(data)
        else:
            InsertNode(rootNode.LeftChild,data)
    elif data > rootNode.data:
        if rootNode.RightChild is None:
            rootNode.RightChild=BST(data)
        else:
            InsertNode(rootNode.RightChild,data)
while True:
    i = input("Do You Want to Insert y/n : ")
    if i=='y':
        data=int(input("Enter the element: "))
        InsertNode(root,data)
    else:
        break

def PreOrderTraversal(root):
    if not root:
        return
    print(root.data,"-->",end=" ")
    PreOrderTraversal(root.LeftChild)
    PreOrderTraversal(root.RightChild)
print("..... Binary Search Tree Traversing Using PreOrderTraversal ..... ")
PreOrderTraversal(root)

def PostOrderTraversal(root):
    if not root:
        return
    PostOrderTraversal(root.LeftChild)
    PostOrderTraversal(root.RightChild)
    print(root.data,"-->",end=" ")
print("\n..... Binary Search Tree Traversing Using PostOrderTraversal ..... ")
PostOrderTraversal(root)

# INORDER TRAVERSAL [ Left ---> Root ---> Right ]
def InOrder(root):
    if not root:
        return
    InOrder(root.LeftChild)
    print(root.data,"-->",end=" ")
    InOrder(root.RightChild)
print("\n..... Binary Search Tree Traversing Using InorderOrderTraversal ..... ")
InOrder(root)
print("/n")
