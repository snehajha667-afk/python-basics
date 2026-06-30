numbers = (10, 20, 30, 40, 50)

while True:
    print("\n----- TUPLE OPERATIONS -----")
    print("1. Display tuple")
    print("2. Find length")
    print("3. Access element")
    print("4. Count an element")
    print("5. Find index of an element")
    print("6. Check element exists")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Tuple:", numbers)

    elif choice == 2:
        print("Length:", len(numbers))

    elif choice == 3:
        index = int(input("Enter index: "))
        print("Element:", numbers[index])

    elif choice == 4:
        num = int(input("Enter element to count: "))
        print("Count:", numbers.count(num))

    elif choice == 5:
        num = int(input("Enter element to find index: "))
        if num in numbers:
            print("Index:", numbers.index(num))
        else:
            print("Element not found.")

    elif choice == 6:
        num = int(input("Enter element to search: "))
        if num in numbers:
            print("Element is present.")
        else:
            print("Element is not present.")

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
