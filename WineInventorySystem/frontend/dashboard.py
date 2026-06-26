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