# #expense tracker
# import csv
# from datetime import datetime

# # File to store expense data
# EXPENSE_FILE = "expenses.csv"

# def load_expenses():
#     """
#     Load expenses from the CSV file.
#     If the file doesn't exist, return an empty list.
#     """
#     try:
#         with open(EXPENSE_FILE, mode='r', newline='', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             return list(reader)
#     except FileNotFoundError:
#         return []

# def save_expenses(expenses):
#     """
#     Save expenses to the CSV file.
#     """
#     with open(EXPENSE_FILE, mode='w', newline='', encoding='utf-8') as file:
#         fieldnames = ['date', 'category', 'amount', 'description']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(expenses)

# def add_expense(expenses):
#     """
#     Add a new expense to the list.
#     """
#     print("\n--- Add New Expense ---")
#     date = input("Enter the date (YYYY-MM-DD): ") or datetime.now().strftime("%Y-%m-%d")
#     category = input("Enter the category (e.g., Food, Transport): ")
#     amount = float(input("Enter the amount: "))
#     description = input("Enter a description (optional): ")

#     # Append the new expense to the list
#     expenses.append({
#         'date': date,
#         'category': category,
#         'amount': amount,
#         'description': description
#     })
#     print("Expense added successfully!")

# def view_expenses(expenses):
#     """
#     Display all expenses in a readable format.
#     """
#     if not expenses:
#         print("\nNo expenses found.")
#         return

#     print("\n--- All Expenses ---")
#     for idx, expense in enumerate(expenses, start=1):
#         print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
#               f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

# def filter_expenses(expenses):
#     """
#     Filter expenses by date, category, or amount range.
#     """
#     print("\n--- Filter Expenses ---")
#     print("1. Filter by Date")
#     print("2. Filter by Category")
#     print("3. Filter by Amount Range")
#     choice = input("Choose an option (1/2/3): ")

#     filtered = []
#     if choice == '1':
#         date = input("Enter the date (YYYY-MM-DD): ")
#         filtered = [e for e in expenses if e['date'] == date]
#     elif choice == '2':
#         category = input("Enter the category: ")
#         filtered = [e for e in expenses if e['category'].lower() == category.lower()]
#     elif choice == '3':
#         min_amount = float(input("Enter the minimum amount: "))
#         max_amount = float(input("Enter the maximum amount: "))
#         filtered = [e for e in expenses if min_amount <= float(e['amount']) <= max_amount]
#     else:
#         print("Invalid choice.")
#         return

#     if not filtered:
#         print("\nNo matching expenses found.")
#     else:
#         print("\n--- Filtered Expenses ---")
#         for idx, expense in enumerate(filtered, start=1):
#             print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
#                   f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

# def main():
#     """
#     Main function to run the Expense Tracker.
#     """
#     print("Welcome to the Expense Tracker!")
#     expenses = load_expenses()

#     while True:
#         print("\n--- Menu ---")
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Filter Expenses")
#         print("4. Exit")
#         choice = input("Choose an option (1/2/3/4): ")

#         if choice == '1':
#             add_expense(expenses)
#         elif choice == '2':
#             view_expenses(expenses)
#         elif choice == '3':
#             filter_expenses(expenses)
#         elif choice == '4':
#             save_expenses(expenses)
#             print("Expenses saved. Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
# def add_expense(expenses, amount, category):
#     expenses.append({"amount": amount, "category": category})

# def get_total_expenses(expenses):
#     return sum(expense["amount"] for expense in expenses)

# expenses = []

import csv
from datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk

# File to store expense data
EXPENSE_FILE = "expenses.csv"

def load_expenses():
    """
    Load expenses from the CSV file.
    If the file doesn't exist, return an empty list.
    """
    try:
        with open(EXPENSE_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)  # Return all rows as a list of dictionaries
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_expenses(expenses):
    """
    Save the current list of expenses to the CSV file.
    Overwrites the file with updated data.
    """
    with open(EXPENSE_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(expenses)  # Write all expense records

def add_expense_gui():
    """
    Add a new expense via the GUI.
    Validates input fields before adding the expense.
    """
    # Get user inputs or use default values where applicable
    date = date_entry.get() or datetime.now().strftime("%Y-%m-%d")  # Default to today's date
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()
    description = description_entry.get().strip()

    # Validate required fields
    if not category or not amount:
        messagebox.showerror("Error", "Category and Amount are required.")
        return

    # Validate that the amount is a valid number
    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a valid number.")
        return

    # Append the new expense to the global list
    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })

    # Update the GUI and clear input fields
    update_expense_list()
    clear_entries()
    messagebox.showinfo("Success", "Expense added successfully!")

def update_expense_list(filtered_expenses=None):
    """
    Update the Treeview widget with the latest expenses.
    Optionally accepts a filtered list of expenses to display.
    """
    # Clear existing rows in the Treeview
    for row in expense_tree.get_children():
        expense_tree.delete(row)

    # Use the filtered list if provided; otherwise, use all expenses
    expense_data = filtered_expenses if filtered_expenses else expenses

    # Insert each expense into the Treeview
    for expense in expense_data:
        expense_tree.insert("", END, values=(
            expense['date'],
            expense['category'],
            f"${float(expense['amount']):.2f}",  # Format amount as currency
            expense['description']
        ))

def clear_entries():
    """
    Clear all input fields after adding an expense.
    """
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    amount_entry.delete(0, END)
    description_entry.delete(0, END)

def filter_expenses_gui():
    """
    Filter expenses by category using the dropdown menu.
    Displays only matching expenses in the Treeview.
    """
    category_filter = filter_category_combobox.get().strip()
    if not category_filter:
        messagebox.showerror("Error", "Please select a category to filter.")
        return

    # Filter expenses based on the selected category
    filtered = [e for e in expenses if e['category'].lower() == category_filter.lower()]
    update_expense_list(filtered)

def main():
    """
    Main function to initialize the GUI for the Expense Tracker.
    Sets up the layout, widgets, and event handlers.
    """
    global expenses, date_entry, category_entry, amount_entry, description_entry, expense_tree, filter_category_combobox

    # Load existing expenses from the file
    expenses = load_expenses()

    # Create the main application window
    root = Tk()
    root.title("Expense Tracker")
    root.geometry("800x600")

    # Title Label
    title_label = Label(root, text="Expense Tracker", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)

    # Input Frame for adding expenses
    input_frame = Frame(root)
    input_frame.pack(pady=10)

    # Date Field
    Label(input_frame, text="Date:").grid(row=0, column=0, padx=5, pady=5)
    date_entry = Entry(input_frame)
    date_entry.grid(row=0, column=1, padx=5, pady=5)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to today's date

    # Category Field
    Label(input_frame, text="Category:").grid(row=0, column=2, padx=5, pady=5)
    category_entry = Entry(input_frame)
    category_entry.grid(row=0, column=3, padx=5, pady=5)

    # Amount Field
    Label(input_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
    amount_entry = Entry(input_frame)
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    # Description Field
    Label(input_frame, text="Description:").grid(row=1, column=2, padx=5, pady=5)
    description_entry = Entry(input_frame)
    description_entry.grid(row=1, column=3, padx=5, pady=5)

    # Add Expense Button
    add_button = Button(input_frame, text="Add Expense", command=add_expense_gui)
    add_button.grid(row=2, columnspan=4, pady=10)

    # Expense List Frame
    list_frame = Frame(root)
    list_frame.pack(pady=10, fill=BOTH, expand=True)

    # Expense Treeview to display expenses in a table format
    columns = ("Date", "Category", "Amount", "Description")
    expense_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
    for col in columns:
        expense_tree.heading(col, text=col)  # Set column headers
        expense_tree.column(col, width=150)  # Set column widths
    expense_tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Scrollbar for the Treeview
    scrollbar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=expense_tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    expense_tree.configure(yscrollcommand=scrollbar.set)

    # Filter Frame for filtering expenses by category
    filter_frame = Frame(root)
    filter_frame.pack(pady=10)

    Label(filter_frame, text="Filter by Category:").pack(side=LEFT, padx=5)
    filter_category_combobox = ttk.Combobox(filter_frame, values=["Food", "Transport", "Entertainment", "Utilities"])
    filter_category_combobox.pack(side=LEFT, padx=5)
    filter_button = Button(filter_frame, text="Filter", command=filter_expenses_gui)
    filter_button.pack(side=LEFT, padx=5)

    # Display initial data in the Treeview
    update_expense_list()

    # Save expenses and exit the application
    def on_closing():
        save_expenses(expenses)  # Save data to the CSV file
        root.destroy()  # Close the application

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()