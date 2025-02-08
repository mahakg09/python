def list_operations():
    my_list = []  # Initialize an empty list

    while True:
        print("Choose an operation:")
        print("1. Append an element")
        print("2. Remove an element")
        print("3. Print the list")
        print("4. Exit")

        # Input for operation choice
        choice = int(input("Enter your choice: "))

        if choice == 1:  # Append an element to the list
            element = input("Enter element to add: ")
            my_list.append(element)  # Add element to the list
            print(f"Element '{element}' added successfully.")

        elif choice == 2:  # Remove an element from the list
            element = input("Enter element to remove: ")
            if element in my_list:
                my_list.remove(element)  # Remove element from the list
                print(f"Element '{element}' removed successfully.")
            else:
                print("Element not found.")

        elif choice == 3:  # Print the list
            print("Current list:", my_list)

        elif choice == 4:  # Exit the loop
            print("Exiting the program.")
            break  # Break out of the loop to exit

        else:
            print("Invalid choice. Please try again.")

# Run the list_operations function
list_operations()
