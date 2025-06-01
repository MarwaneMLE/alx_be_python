#!/usr/bin/env python3

n = int(input("Enter the size of the pattern: "))
if n > 0:
    row = 1
    while row <= n:
        for col in range(n):
            print("*", end="")
        print()
        row += 1
else:
    print("Please enter positive number!!!")
