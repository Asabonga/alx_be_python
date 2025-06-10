import os

FILE_NAME = "shopping_list.txt"

def load_list():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            items = [line.strip() for line in f.readlines()]
        return items
    return []

def save_list(shopping_list):
    with open(FILE_NAME, "w") as f:
        for item in shopping_list:
            f.write(item + "\n")

def main():
    shopping_list = load_list()

    while True:
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            save_list(shopping_list)
            print(f"'{item}' added.")
        elif choice == "2":
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                save_list(shopping_list)
                print(f"'{item}' removed.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == "3":
            if shopping_list:
                print("Shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
def main():
    print("Hello from shopping_list_manager!")
    # Add your shopping list code here

if __name__ == "__main__":
    main()

