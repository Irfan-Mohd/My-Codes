def ascendingOrder(number):
    global temp
    global n
    for i in range(0,n,1):
        for j in range(i+1,n,1):
            if(number[0]==0):
                pass
            elif(number[i]>number[j]):
                temp=number[i]
                number[i]=number[j]
                number[j]=temp;
    print(number)

def descendingOrder(number):
        global temp
        global n
        for i in range(0,n,1):
            for j in range(i+1,n,1):
                if(number[j]==0):
                    pass
                elif(number[i]<number[j]):
                    temp=number[i]
                    number[i]=number[j]
                    number[j]=temp;
        print(number)

n=int(input("Enter the number of elements you want to enter: "))
number=[]
for i in range(0,n,1):
    if(i==1):
        temp=int(input("Enter {}st element: ".format(i)))
    elif(i==2):
        temp=int(input("Enter {}nd element: ".format(i)))
    elif(i==3):
        temp=int(input("Enter {}rd element: ".format(i)))
    else:
        temp=int(input("Enter {}th element: ".format(i)))
    number.append(temp)
ascendingOrder(number)

descendingOrder(number)
