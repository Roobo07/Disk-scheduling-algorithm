#page replacement algorithm
def main():
    n = int(input("Enter the number of pages: "))
    a = list(map(int, input("Enter the page numbers: ").split()))
    no = int(input("Enter the number of frames: "))
    
    frame = [-1] * no
    j = 0  
    count = 0  

    print("\t Ref string \t page frames")
    for i in range(n):
        print(f"{a[i]}\t", end = " ")
        avail = False

     for k in range(no):
if frame[k] == a[i]:
avail = True
break

      if not avail:
frame[j] = a[i]
j = (j + 1) % no  
count += 1



        for k in range(no):
            	if frame[k] != -1:
                		print(f"{frame[k]}\t", end = " ")
            	else:
                		print("-\t", end = " ")
        print()  
    print(f'Page fault: {count}')

if __name__ == "__main__":
    main()
