def main():
    n = int(input("Enter the number of files: "))

    b = [0] * n
    sb = [0] * n
    t = [0] * n
    c = [[0 for _ in range(20)] for _ in range(n)]

    for i in range(n):
        print(f"Enter the number of blocks occupied by file {i + 1}: ", end='')
        b[i] = int(input())
       
        print(f"Enter the starting block of file {i + 1}: ", end='')
        sb[i] = int(input())

        t[i] = sb[i]

        for j in range(b[i]):
            c[i][j] = sb[i]
            sb[i] += 1

    print("Filename\tStart block\tLength")
    for i in range(n):
        print(f"{i + 1}\t\t{t[i]}\t\t{b[i]}")

    x = int(input("Enter file number to search: "))

    if 1 <= x <= n:
        print(f"File name is: {x}")
        print(f"Length is: {b[x - 1]}")
        print("Blocks occupied:", end=' ')
        for i in range(b[x - 1]):
            print(c[x - 1][i], end=' ')
        print()
    else:
        print("Invalid file number")

if __name__ == "__main__":
    main() 
