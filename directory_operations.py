student = {}

while True:
    print("\n----- DICTIONARY OPERATIONS -----")
    print("1. Add item")
    print("2. Update item")
    print("3. Delete item")
    print("4. Search item")
    print("5. Display dictionary")
    print("6. Display keys")
    print("7. Display values")
    print("8. Find length")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        student[key] = value

    elif choice == 2:
        key = input("Enter key to update: ")
        if key in student:
            value = input("Enter new value: ")
            student[key] = value
        else:
            print("Key not found.")

    elif choice == 3:
        key = input("Enter key to delete: ")
        if key in student:
            del student[key]
        else:
            print("Key not found.")

    elif choice == 4:
        key = input("Enter key to search: ")
        if key in student:
            print("Value:", student[key])
        else:
            print("Key not found.")

    elif choice == 5:
        print("Dictionary:", student)

    elif choice == 6:
        print("Keys:", student.keys())

    elif choice == 7:
        print("Values:", student.values())

    elif choice == 8:
        print("Length:", len(student))

    elif choice == 9:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
