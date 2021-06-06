data=[10,5,2,4,3,7,6,8,9,1]
''' MAIN LOGIC'''
def Bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data)-1 - i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                
            else:
                pass
    return data
d = Bubble_sort(data)
print(d)
