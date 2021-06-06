def Selection_Sort(data):
    for i in range(len(data)):
        Min_value=i
        for j in range(i+1,len(data)):
            if data[Min_value] > data[j]:
                Min_value=j
        data[Min_value],data[i]=data[i],data[Min_value]
    print(data)
data=[9,4,7,6,3,1,0]
Selection_Sort(data)
