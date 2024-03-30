# Bookstore Inventory Management System
# Designed for Introduction to Programming using Python - High Distinction Example

def main_menu():
    print("\nBookstore Inventory System")
    print("1. Add a Book")
    print("2. List All Books")
    print("3. Search for a Book")
    print("4. Quit")
    return input("Choose an option: ")

def add_book(inventory):
    try:
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        price = float(input("Enter the price: $"))
        inventory[title] = {'Author': author, 'Price': price}
        print(f"{title} by {author} added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid price.")

def list_books(inventory):
    if inventory:
        print("\nBook Inventory:")
        for title, details in inventory.items():
            print(f"Title: {title}, Author: {details['Author']}, Price: ${details['Price']}")
    else:
        print("No books in inventory.")

def search_book(inventory):
    title = input("Enter the title of the book to search for: ")
    if title in inventory:
        book = inventory[title]
        print(f"Found: {title} by {book['Author']}, Price: ${book['Price']}")
    else:
        print("Book not found.")

def main():
    inventory = {}
    while True:
        choice = main_menu()
        if choice == '1':
            add_book(inventory)
        elif choice == '2':
            list_books(inventory)
        elif choice == '3':
            search_book(inventory)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
