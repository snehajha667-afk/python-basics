numbers = []

while True:
    print("\n----- LIST OPERATIONS -----")
    print("1. Add element")
    print("2. Insert element")
    print("3. Remove element")
    print("4. Pop last element")
    print("5. Display list")
    print("6. Sort list")
    print("7. Reverse list")
    print("8. Find length")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter element to add: "))
        numbers.append(num)

    elif choice == 2:
        pos = int(input("Enter position: "))
        num = int(input("Enter element: "))
        numbers.insert(pos, num)

    elif choice == 3:
        num = int(input("Enter element to remove: "))
        if num in numbers:
            numbers.remove(num)
        else:
            print("Element not found.")

    elif choice == 4:
        if len(numbers) > 0:
            print("Removed:", numbers.pop())
        else:
            print("List is empty.")

    elif choice == 5:
        print("List:", numbers)

    elif choice == 6:
        numbers.sort()
        print("List sorted.")

    elif choice == 7:
        numbers.reverse()
        print("List reversed.")

    elif choice == 8:
        print("Length of list:", len(numbers))

    elif choice == 9:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
