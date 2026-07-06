    *
   ***
  *****
 *******
*********
n = 5

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print stars
    for j in range(2 * i + 1):
        print("*", end="")

    print()
