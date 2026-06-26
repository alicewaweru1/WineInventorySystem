import tkinter as tk
from tkinter import ttk, messagebox


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

tk.Label(
    card1,
    text="0",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 30, "bold")
).pack()


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

tk.Label(
    card2,
    text="0",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 30, "bold")
).pack()