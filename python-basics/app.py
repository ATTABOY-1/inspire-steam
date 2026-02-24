from tkinter import *

def hello():
    print("Hello from Alvin!")

root = Tk()
root.geometry("600x600")

frame_1 = Frame(root)
frame_1.pack()

button_1 = Button(frame_1, text="Say Hello", command=hello)
button_1.pack()

root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# -------------------------------
# Product Database (Sample Items)
# -------------------------------
products = {
    "Milk": 2.50,
    "Bread": 1.80,
    "Eggs": 3.00,
    "Rice (1kg)": 4.20,
    "Sugar (1kg)": 3.50,
    "Apples (1kg)": 2.80,
    "Chicken (1kg)": 6.50
}

cart = []

# -------------------------------
# Functions
# -------------------------------

def add_to_cart():
    product_name = product_var.get()
    quantity = qty_var.get()

    if product_name == "" or quantity == "":
        messagebox.showwarning("Warning", "Please select product and quantity")
        return

    quantity = int(quantity)
    price = products[product_name]
    total_price = price * quantity

    cart.append((product_name, quantity, price, total_price))

    cart_tree.insert("", "end", values=(product_name, quantity, f"${price:.2f}", f"${total_price:.2f}"))

    update_total()


def remove_item():
    selected_item = cart_tree.selection()
    if not selected_item:
        return

    index = cart_tree.index(selected_item)
    cart_tree.delete(selected_item)
    cart.pop(index)
    update_total()


def clear_cart():
    cart.clear()
    for item in cart_tree.get_children():
        cart_tree.delete(item)
    update_total()


def update_total():
    total = sum(item[3] for item in cart)
    total_label.config(text=f"Total: ${total:.2f}")


def generate_receipt():
    if not cart:
        messagebox.showwarning("Warning", "Cart is empty!")
        return

    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")

    receipt_text = tk.Text(receipt_window, width=50, height=25)
    receipt_text.pack()

    receipt_text.insert(tk.END, "      SUPERMARKET RECEIPT\n")
    receipt_text.insert(tk.END, "---------------------------------------\n")
    receipt_text.insert(tk.END, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    receipt_text.insert(tk.END, "---------------------------------------\n")

    for item in cart:
        receipt_text.insert(
            tk.END,
            f"{item[0]} x{item[1]} = ${item[3]:.2f}\n"
        )

    receipt_text.insert(tk.END, "---------------------------------------\n")
    total = sum(item[3] for item in cart)
    receipt_text.insert(tk.END, f"TOTAL: ${total:.2f}\n")
    receipt_text.insert(tk.END, "---------------------------------------\n")
    receipt_text.insert(tk.END, "      Thank You For Shopping!\n")

    receipt_text.config(state="disabled")


# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Supermarket POS System")
root.geometry("750x500")
root.configure(bg="#f4f4f4")

# -------------------------------
# Product Selection Frame
# -------------------------------
frame_top = tk.Frame(root, bg="#f4f4f4")
frame_top.pack(pady=10)

tk.Label(frame_top, text="Select Product:", bg="#f4f4f4").grid(row=0, column=0, padx=5)

product_var = tk.StringVar()
product_dropdown = ttk.Combobox(frame_top, textvariable=product_var)
product_dropdown["values"] = list(products.keys())
product_dropdown.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Quantity:", bg="#f4f4f4").grid(row=0, column=2, padx=5)

qty_var = tk.StringVar()
qty_entry = tk.Entry(frame_top, textvariable=qty_var, width=5)
qty_entry.grid(row=0, column=3, padx=5)

tk.Button(frame_top, text="Add to Cart", command=add_to_cart, bg="#4CAF50", fg="white").grid(row=0, column=4, padx=10)

# -------------------------------
# Cart Table
# -------------------------------
columns = ("Product", "Quantity", "Unit Price", "Total Price")

cart_tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    cart_tree.heading(col, text=col)
    cart_tree.column(col, anchor="center", width=150)

cart_tree.pack(pady=20)

# -------------------------------
# Bottom Controls
# -------------------------------
frame_bottom = tk.Frame(root, bg="#f4f4f4")
frame_bottom.pack()

total_label = tk.Label(frame_bottom, text="Total: $0.00", font=("Arial", 14, "bold"), bg="#f4f4f4")
total_label.grid(row=0, column=0, padx=20)

tk.Button(frame_bottom, text="Remove Selected", command=remove_item, bg="#f44336", fg="white").grid(row=0, column=1, padx=10)

tk.Button(frame_bottom, text="Clear Cart", command=clear_cart, bg="#FF9800", fg="white").grid(row=0, column=2, padx=10)

tk.Button(frame_bottom, text="Generate Receipt", command=generate_receipt, bg="#2196F3", fg="white").grid(row=0, column=3, padx=10)

# -------------------------------
# Run Application
# -------------------------------
root.mainloop()