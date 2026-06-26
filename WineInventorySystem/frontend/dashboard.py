import tkinter as tk
from tkinter import ttk, messagebox

from backend.wine_controller import (
    add_wine,
    get_all_wines,
    delete_wine,
    get_total_stock
)

from backend.sales_controller import (
    get_total_sales,
    get_total_revenue
)

root = tk.Tk()
root.title("Wine World Delights")
root.geometry("1400x800")
root.configure(bg="#0f0f0f")


BLACK = "#0f0f0f"
GOLD = "#D4AF37"
WINE_RED = "#722F37"
CARD = "#1b1b1b"
WHITE = "#f5f5f5"


header = tk.Frame(root, bg=BLACK)
header.pack(fill="x", pady=20)

title = tk.Label(
    header,
    text="🍷 WINE WORLD DELIGHTS",
    font=("Georgia", 28, "bold"),
    fg=GOLD,
    bg=BLACK
)

title.pack()

subtitle = tk.Label(
    header,
    text="Luxury Wine Inventory Management",
    font=("Segoe UI", 11),
    fg=WHITE,
    bg=BLACK
)

subtitle.pack()


stats_frame = tk.Frame(root, bg=BLACK)
stats_frame.pack(pady=20)


card1 = tk.Frame(
    stats_frame,
    bg=CARD,
    width=250,
    height=130,
    highlightbackground=GOLD,
    highlightthickness=2
)

card1.grid(row=0, column=0, padx=20)
card1.pack_propagate(False)

tk.Label(
    card1,
    text="TOTAL WINES",
    bg=CARD,
    fg=GOLD,
    font=("Segoe UI", 12, "bold")
).pack(pady=10)

total_wines_label = tk.Label(
    card1,
    text="0",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 30, "bold")
)
total_wines_label.pack()


card2 = tk.Frame(
    stats_frame,
    bg=CARD,
    width=250,
    height=130,
    highlightbackground=WINE_RED,
    highlightthickness=2
)

card2.grid(row=0, column=1, padx=20)
card2.pack_propagate(False)

tk.Label(
    card2,
    text="SALES TODAY",
    bg=CARD,
    fg=WINE_RED,
    font=("Segoe UI", 12, "bold")
).pack(pady=10)

total_sales_label = tk.Label(
    card2,
    text="0",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 30, "bold")
)
total_sales_label.pack()

card3 = tk.Frame(
    stats_frame,
    bg=CARD,
    width=250,
    height=130,
    highlightbackground=GOLD,
    highlightthickness=2
)

card3.grid(row=0, column=2, padx=20)
card3.pack_propagate(False)

tk.Label(
    card3,
    text="REVENUE",
    bg=CARD,
    fg=GOLD,
    font=("Segoe UI", 12, "bold")
).pack(pady=10)

revenue_label = tk.Label(
    card3,
    text="0",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 24, "bold")
)

revenue_label.pack()

form_frame = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=GOLD,
    highlightthickness=2
)

form_frame.pack(fill="x", padx=30, pady=20)

tk.Label(
    form_frame,
    text="Add New Wine",
    font=("Georgia", 18, "bold"),
    fg=GOLD,
    bg=CARD
).grid(row=0, column=0, columnspan=2, pady=15)

tk.Label(form_frame, text="Wine Name", fg=WHITE, bg=CARD).grid(row=1, column=0, padx=10, pady=10)
wine_name = tk.Entry(form_frame, width=35)
wine_name.grid(row=1, column=1)

tk.Label(form_frame, text="Description", fg=WHITE, bg=CARD).grid(row=2, column=0, padx=10, pady=10)
description = tk.Entry(form_frame, width=35)
description.grid(row=2, column=1)

tk.Label(form_frame, text="Price", fg=WHITE, bg=CARD).grid(row=3, column=0, padx=10, pady=10)
price = tk.Entry(form_frame, width=35)
price.grid(row=3, column=1)

tk.Label(form_frame, text="Quantity", fg=WHITE, bg=CARD).grid(row=4, column=0, padx=10, pady=10)
quantity = tk.Entry(form_frame, width=35)
quantity.grid(row=4, column=1)

save_btn = tk.Button(
    form_frame,
    text="🍷 SAVE WINE",
    bg=GOLD,
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=20
)

save_btn.grid(row=5, column=0, columnspan=2, pady=20)


table_frame = tk.Frame(root, bg=BLACK)
table_frame.pack(fill="both", expand=True, padx=30, pady=20)

columns = (
    "ID",
    "Name",
    "Description",
    "Price",
    "Quantity"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack(fill="both", expand=True)

def refresh_dashboard():

    total_wines_label.config(
        text=str(get_total_stock())
    )

    total_sales_label.config(
        text=str(get_total_sales())
    )

    revenue_label.config(
        text=f"KES {get_total_revenue():,.0f}"
    )

    tree.delete(*tree.get_children())

    for wine in get_all_wines():
        tree.insert("", "end", values=wine)

    root.after(3000, refresh_dashboard)
    refresh_dashboard()
root.mainloop()