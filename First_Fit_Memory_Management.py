def first_fit (blockSize,request,m,n,allocated):

     frag = 0
     for i in range(n):
         print(blockSize)
         for j in range(m):
             if blockSize[j]>=request[i]:
                 allocated[i] = j
                 blockSize[j] -= request[i]
                 break

     for i in range(n):
         if allocated[i] == -1:
             for i in range(m):
                 frag += blockSize[i]
             break
     return frag


if __name__ == "__main__":
    blockSize = [50,200,70,115,15]
    Request=[100,10,35,15,23,6,25,55,88,40]
    m=len(blockSize)
    n=len(Request)
    allocated = [-1]*n
    frag = first_fit(blockSize,request,m,n,allocated)
    allocated = [x+1 for x in allocated]
    for i in range(n):
        if allocated[i]!=0:
            print("Process "+str(i+1)+" is allocated in memory block: "+str(allocated[i]))
        else:
            print("Process " + str(i + 1) + " is not allocated")


    if frag != 0:
        print("The External Fragmentation is: %d"%frag)
    else:
        print("There is not External Fragmentation")



