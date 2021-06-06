class Tree:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
drink=Tree("Drink",[])
# drink.__dict__
hot=Tree("HOT",[])
# hot.__dict__
drink.children.append(hot)
# drink.__dict__
hot.children.append('tea')
hot.children.append('coffee')
hot.children.append('soup')
cold=Tree("COLD",['cola','wine'])
drink.children.append(cold)
# drink.__dict__
cold.children.append("juice")
# cold.__dict__
for i in drink.children:
    print(i.data)
    for j in i.children:
        print(j)
# hot.__dict__   
