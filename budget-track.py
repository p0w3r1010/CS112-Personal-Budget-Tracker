"""
This program creates a Tkinter-based personal budget tracker that allows the
user to record income and expenses and view running totals.
"""

import tkinter as tk
#root1

root = tk.Tk()
root.title("Budget Tracker M & E")

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Description:").grid(row=1, column=0)
desc_entry = tk.Entry(root)
desc_entry.grid(row=1, column=1)

tk.Button(root, text="Add Transaction").grid(row=2, column=0)
tk.Button(root, text="Quit", command=root.destroy).grid(row=2, column=1)


#open window loop
root.mainloop()