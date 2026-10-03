import json
import os
# ===== EXPENSE TRACKER =====
FILE_NAME = "expenses.json"

# ===== LOAD EXPENSES =====
def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

    return []


# ===== SAVE EXPENSES =====
def save_expenses():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError:
        print("Error: Could not save expenses.")


# ===== ADD EXPENSE =====
def add_expense():
    print("\n===== ADD EXPENSE =====")

    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty!")
        return

    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    category = input("Enter category: ").strip()

    if not category:
        category = "Other"

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


# ===== VIEW EXPENSES =====
def view_expenses():
    print("\n===== EXPENSE LIST =====")

    if not expenses:
        print("No expenses found!")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} "
            f"- ₹{expense['amount']:.2f} "
            f"- {expense['category']}"
        )


# ===== TOTAL EXPENSE =====
def total_expense():
    print("\n===== TOTAL EXPENSE =====")

    if not expenses:
        print("No expenses found!")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total Expense: ₹{total:.2f}")


# ===== UPDATE EXPENSE =====
def update_expense():
    print("\n===== UPDATE EXPENSE =====")

    if not expenses:
        print("No expenses found!")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to update: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense = expenses[number - 1]

    print("\nPress Enter to keep the existing value.")

    new_name = input(f"Expense name [{expense['name']}]: ").strip()

    if new_name:
        expense["name"] = new_name

    while True:
        new_amount = input(
            f"Amount [{expense['amount']:.2f}]: "
        ).strip()

        if new_amount == "":
            break

        try:
            new_amount = float(new_amount)

            if new_amount <= 0:
                print("Amount must be greater than 0.")
                continue

            expense["amount"] = new_amount
            break

        except ValueError:
            print("Please enter a valid amount.")

    new_category = input(
        f"Category [{expense['category']}]: "
    ).strip()

    if new_category:
        expense["category"] = new_category

    save_expenses()

    print("Expense updated successfully!")


# ===== DELETE EXPENSE =====
def delete_expense():
    print("\n===== DELETE EXPENSE =====")

    if not expenses:
        print("No expenses found!")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    removed_expense = expenses.pop(number - 1)

    save_expenses()

    print(
        f"'{removed_expense['name']}' "
        "deleted successfully!"
    )


# ===== CATEGORY SUMMARY =====
def category_summary():
    print("\n===== CATEGORY SUMMARY =====")

    if not expenses:
        print("No expenses found!")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        categories[category] = categories.get(category, 0) + amount

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# ===== MAIN PROGRAM =====

expenses = load_expenses()

print("===================================")
print("       EXPENSE TRACKER")
print("===================================")

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Category Summary")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        category_summary()

    elif choice == "7":
        print("\nThank you for using Expense Tracker!")
        print("Your expenses have been saved.")
        break

    else:
        print("Invalid choice! Please select 1-7.")
