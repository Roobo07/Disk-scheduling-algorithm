def main():

    queue = []

    n = int(input("Enter the max range of disk: "))

    size = int(input("Enter the size of queue request: "))

    print("Enter the queue of disk positions to be read:")

    for i in range(size):
        queue.append(int(input()))

    head = int(input("Enter the initial head position: "))
    queue.insert(0, head)

    seek = 0

    for j in range(size):
        diff = abs(queue[j + 1] - queue[j])
        seek += diff
        print(f"Disk head moves from {queue[j]} to {queue[j + 1]} with seek {diff}")

    print(f"Total seek time is {seek}")

    avg = seek / float(size)
    print(f"Average seek time is {avg}")

if __name__ == "__main__":
    main() 
