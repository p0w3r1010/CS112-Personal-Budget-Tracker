"""
This program creates a Tkinter-based personal budget tracker that allows the
user to record income and expenses and view running totals.
"""

import tkinter as tk
from tkinter import ttk, messagebox

#list to store all transactions
transactions = []

#add a transaction to the list and listbox
def add_transaction():
    amount_text = amount_entry.get().strip()
    desc = desc_entry.get().strip()
    category = category_var.get()
    ttype = type_var.get()

    #check if amount is entered
    if amount_text == "":
        messagebox.showerror("Error", "Please enter an amount.")
        return

    #make sure amount is a number
    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    #default description if empty
    if desc == "":
        desc = "No description"

    #store transaction as a dictionary
    transaction = {
        "amount": amount,
        "description": desc,
        "category": category,
        "type": ttype
    }
    transactions.append(transaction)

    #show transaction in the listbox
    listbox.insert(tk.END, f"{ttype} | {category} | {amount:.2f} | {desc}")

    update_totals()
    clear_fields()

#clear input fields
def clear_fields():
    amount_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    category_var.set("Food")
    type_var.set("Income")

#calculate and update totals
def update_totals():
    total_income = 0.0
    total_expenses = 0.0

    for t in transactions:
        if t["type"] == "Income":
            total_income += t["amount"]
        else:
            total_expenses += t["amount"]

    balance = total_income - total_expenses

    income_val.config(text=f"{total_income:.2f}")
    expense_val.config(text=f"{total_expenses:.2f}")
    balance_val.config(text=f"{balance:.2f}")

#delete the selected transaction
def delete_selected():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a transaction to delete.")
        return

    index = selected[0]
    del transactions[index]
    listbox.delete(index)
    update_totals()

#close the program
def quit_app():
    root.destroy()

#main window
root = tk.Tk()
root.title("Canales & Gonzalez Budget Tracker🪙")
root.configure(bg="silver")

#amount input
tk.Label(root, text="Amount:", bg="silver").grid(row=0, column=0, sticky="w")
amount_entry = tk.Entry(root, width=18)
amount_entry.grid(row=0, column=1, sticky="w")

#description input
tk.Label(root, text="Description:", bg="silver").grid(row=1, column=0, sticky="w")
desc_entry = tk.Entry(root, width=28)
desc_entry.grid(row=1, column=1, sticky="w")

#category dropdown
tk.Label(root, text="Category:", bg="silver").grid(row=2, column=0, sticky="w")
category_var = tk.StringVar(value="Food")
ttk.Combobox(
    root,
    textvariable=category_var,
    values=["Food", "Rent", "Entertainment", "Other"],
    state="readonly",
    width=16
).grid(row=2, column=1, sticky="w")

#income / expense selection
tk.Label(root, text="Type:", bg="silver").grid(row=3, column=0, sticky="w")
type_var = tk.StringVar(value="Income")
tk.Radiobutton(root, text="Income", variable=type_var, value="Income", bg="silver").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Expense", variable=type_var, value="Expense", bg="silver").grid(row=3, column=1, sticky="e")

#buttons
tk.Button(root, text="Add Transaction", command=add_transaction, bg="silver").grid(row=4, column=0)
tk.Button(root, text="Clear Fields", command=clear_fields, bg="silver").grid(row=4, column=1, sticky="w")
tk.Button(root, text="Quit", command=quit_app, bg="silver").grid(row=4, column=1, sticky="e")

#listbox to show transactions
tk.Label(root, text="Transactions:", bg="silver").grid(row=5, column=0, sticky="w")
listbox = tk.Listbox(root, width=60, height=8)
listbox.grid(row=6, column=0, columnspan=2)

#delete button
tk.Button(root, text="Delete Selected", command=delete_selected, bg="silver").grid(row=7, column=0, sticky="w")

#totals display
tk.Label(root, text="Total Income:", bg="silver").grid(row=8, column=0, sticky="w")
income_val = tk.Label(root, text="0.00", bg="silver")
income_val.grid(row=8, column=1, sticky="w")

tk.Label(root, text="Total Expenses:", bg="silver").grid(row=9, column=0, sticky="w")
expense_val = tk.Label(root, text="0.00", bg="silver")
expense_val.grid(row=9, column=1, sticky="w")

tk.Label(root, text="Balance:", bg="silver").grid(row=10, column=0, sticky="w")
balance_val = tk.Label(root, text="0.00", bg="silver")
balance_val.grid(row=10, column=1, sticky="w")

root.mainloop()