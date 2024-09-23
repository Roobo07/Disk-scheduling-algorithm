def input_values():
    global max, alloc,need, avail, n,r
    print("***Banker's Algo ****")

    n=int(input("Enter the no. of Process :"))
    r=int(input("Enter the no. of resource instances: "))

    max= [[0] * r for _ in range(n)]
    alloc=[[0] * r for _ in range(n)]
    need=[[0] * r for _ in range(n)]
    avail=[0] * r

    print("Enter the max Matrix:")
    for i in range(n):
        max[i]=list(map(int,input().split()))
    print(" Enter the alloc:")
    for i in range(n):
        alloc[i]=list(map(int,input().split()))
       

    print("Enter the avail Reso:")
    avail=list(map(int,input().split()))
def show():
    print("Process\tAllocation\tMax\tAvailable")
    for i in range(n):
        print(f"P{i+1}\t",end='')
        print(*alloc[i],end='\t')
        print(*max[i],end='\t')
        if i == 0:
            print(*avail,end='')
        print()

def cal():
    finish=[0] * n
    flag=1
    safe=[]

    for i in range (n):
        for j in range(r):
            need[i][j]=max[i][j] - alloc[i][j]

    while flag:
        flag=0
        for i in range(n):
            c=0
            for j in range(r):
               
                    if finish[i] == 0 and need[i][j] <= avail[j]:
                        c += 1
                        if c == r:
                            for k in range(r):
                                avail[k] +=alloc[i][j]
                            finish[i]=1
                            flag = 1
                            safe.append(i)
                            if finish[i] == 1:
                                i = n
        print(f"P{safe[-1]}",end="->")
        c1 = sum(finish)
        if c1 == n:
            print("\n Safe State")
        else:
            print("Deadlock")
input_values()
show()
cal() 
