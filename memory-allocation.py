#Memory Allocation Algorithm
def firstFit(blockSize,m,processSize,n):
    allocation=[-1]*n
   
    for i in range(n):
        for j in range(m):
            if blockSize[j]>=processSize[i]:
                allocation[i]=j
                blockSize[j]-=processSize[i]
                break
    print("Process No. Process Size Block no.")
    for i in range(n):
        print("",i+1," ",processSize[i]," ",end="")
        if allocation[i]!= -1:
            print(allocation[i]+1)
        else:
            print("Not Allocated")
           
if __name__=='__main__':
    m=int(input("Enter the number of memory blocks:"))
    blockSize=[]
    for i in range(m):
        size=int(input(f"Enter size of memory block{i+1}:"))
        blockSize.append(size)

    n=int(input("Enter the number of processes:"))
    processSize=[]
    for i in range(n):
        size=int(input(f"Enter size of process{i+1}:"))
        processSize.append(size)

    firstFit(blockSize,m,processSize,n) 
