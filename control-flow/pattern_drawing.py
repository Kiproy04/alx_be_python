pattern_size = int(input("Enter the size of the pattern: "))
row_number = 0
while row_number < pattern_size:
    for _ in range(pattern_size):
        print("*", end="")
    print()
    row_number = row_number + 1   

