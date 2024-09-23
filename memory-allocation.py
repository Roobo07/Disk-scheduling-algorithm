#Memory Allocation Algorithm
def ff(bsize, m, psize, n):
alloc = [-1] * n

for i in range(n):
for j in range(m):
      		if bsize[j] >= psize[i]:
        			alloc[i] = j
        			bsize[j] -= psize[i]
       			break

  	print("Process No. process Size Block no.")
  	for i in range(n):
    		print(" ", i+1, "   ", psize[i],"   ", end=" ")
    		if alloc[i] ! = -1:
      			print(alloc[i]+1)
    		else:
      			print("Not Allocated")

if __name__ == "__main__":
  	m = int(input("Enter the number of memory blocks:"))
  	bsize = []
  	for i in range(m):
    		size = int(input(f"Enter size of memory block {i+1}: "))
    		bsize.append(size)


  	n = int(input("Enter the number of processes:"))
  	psize = []
  	for i in range(n):
    		size = int(input(f"Enter size of process {i+1}:"))
    		psize.append(size)

  	ff(bsize, m, psize, n)
