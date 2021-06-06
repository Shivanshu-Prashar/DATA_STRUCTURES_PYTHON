# 1 2 3 4 0
def  insertion_sort(data):
    for f in range(len(data)):
        position=f
        while position>0 and data[position] < data[position-1]:
            data[position],data[position-1]=data[position-1],data[position]
            position=position-1
    return data

print(insertion_sort([1,5,1,0,6]))
