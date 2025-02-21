import json
import os

# Define a class for finance entries
class FinanceEntry:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

# Define the file to store data
DATA_FILE = "finance_data.json"

def load_data():
    """Load finance data from file if it exists."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(entries):
    """Save finance data to file."""
    with open(DATA_FILE, "w") as file:
        json.dump([entry.to_dict() for entry in entries], file, indent=4)

def add_entry(entries):
    """Add a new finance entry."""
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")
    entry = FinanceEntry(category, amount, description)
    entries.append(entry)
    save_data(entries)
    print("Entry added successfully!")

def view_entries(entries):
    """Display all finance entries."""
    if not entries:
        print("No entries found.")
        return
    for index, entry in enumerate(entries, start=1):
        print(f"{index}. Category: {entry.category}, Amount: ${entry.amount}, Description: {entry.description}")

def edit_entry(entries):
    """Edit an existing finance entry."""
    view_entries(entries)
    try:
        index = int(input("Enter entry number to edit: ")) - 1
        if 0 <= index < len(entries):
            entries[index].category = input("Enter new category: ")
            entries[index].amount = float(input("Enter new amount: "))
            entries[index].description = input("Enter new description: ")
            save_data(entries)
            print("Entry updated successfully!")
        else:
            print("Invalid entry number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

def delete_entry(entries):
    """Delete a finance entry."""
    view_entries(entries)
    try:
        index = int(input("Enter entry number to delete: ")) - 1
        if 0 <= index < len(entries):
            del entries[index]
            save_data(entries)
            print("Entry deleted successfully!")
        else:
            print("Invalid entry number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

def main():
    """Main program loop."""
    entries = [FinanceEntry(**entry) for entry in load_data()]
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Edit Entry")
        print("4. Delete Entry")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            edit_entry(entries)
        elif choice == "4":
            delete_entry(entries)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
