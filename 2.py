import csv
import os
import pandas as pd

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Entertainment, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    try:
        amount = float(amount)
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount! Please enter a numeric value.\n")

def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.\n")
    else:
        print(df.to_string(index=False), "\n")

def expense_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.\n")
    else:
        print("\nTotal Expense by Category:")
        print(df.groupby("Category")["Amount"].sum(), "\n")

def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
