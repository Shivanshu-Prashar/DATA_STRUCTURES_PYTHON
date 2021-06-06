data=[1,2,3,4,5,6,7,8,9,10]
def bs(data,value):
    start = 0
    end = len(data)-1
    middle = int((start + end)/2)
    while not(data[middle] == value) and start <= end:
        if data[middle] > value:
            end = middle-1
        else:
            start=middle+1
        middle = int((start + end)/2)

    if data[middle] == value:
        print("found")
    else:
        print("NOT FOUND")
bs(data,9)
