def options():
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View your tasks")
    print("4. Exit program")

def decide():
    items = []
    while True:  # loops the menu when we are finished to continue adding or removing
        add_or_remove = int(input("Please type 1, 2, 3 or 4: "))

        if add_or_remove == 1:  # if 1 display add task msg
            for i in range(4):
                add_item = input(f"Item number {i + 1}, what item would you like to add: ")
                items.append(add_item)
                print(f"You now have: {items}")

        elif add_or_remove == 2:
            for n in range(4):
                remove_item = input("What item would you like to remove? ")
                items.remove(remove_item)
                print(items)

        elif add_or_remove == 3:
            print(items)

        elif add_or_remove == 4:
            print("Goodbye")
            exit()

