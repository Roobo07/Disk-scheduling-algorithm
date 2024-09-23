#page replacement algorithm
def main():
    n=int(input("Enter the number of pages:"))
    a=list(map(int,input("Enter the page numbers: ").split()))
    no=int(input("Enter the number of frames:"))
    frame=[-1]*no
    j=0
    count=0

    print("\tRef String\tPage Frames")

    for i in range(n):
        print(f"{a[i]}\t\t",end="")
        avail=0

        for k in range(no):
            if frame[k]==a[i]:
                avail=1
        if avail==0:
            frame[j]=a[i]
            j=(j+1)%no
            count+=1
            for k in range(no):
                print(f"{frame[k]}\t",end="")
        print()

    print(f"Page Faults:{count}")

if __name__ == "__main__":
    main() 
