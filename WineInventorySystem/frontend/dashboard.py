import tkinter as tk

window = tk.Tk()

window.title("Wine World Delights")
window.geometry("1200x700")
window.configure(bg="#0A0A0A")




title = tk.Label(
    window,
    text="🍷 WINE WORLD DELIGHTS",
    font=("Georgia", 28, "bold"),
    bg="#0A0A0A",
    fg="#D4AF37"
)

title.pack(pady=(20, 5))

subtitle = tk.Label(
    window,
    text="Premium Wine Inventory Management System",
    font=("Segoe UI", 12),
    bg="#0A0A0A",
    fg="#A7A7A7"
)

subtitle.pack()





line = tk.Frame(
    window,
    bg="#6D071A",
    height=3
)

line.pack(fill="x", padx=150, pady=20)



stats_frame = tk.Frame(
    window,
    bg="#0A0A0A"
)

stats_frame.pack(pady=20)

# Card 1

card1 = tk.Frame(
    stats_frame,
    bg="#161616",
    width=220,
    height=120
)

card1.grid(row=0, column=0, padx=15)

card1.pack_propagate(False)

tk.Label(
    card1,
    text="🍷 Total Wines",
    bg="#161616",
    fg="#F8F5F0",
    font=("Segoe UI", 12)
).pack(pady=(15, 5))

tk.Label(
    card1,
    text="0",
    bg="#161616",
    fg="#D4AF37",
    font=("Segoe UI", 24, "bold")
).pack()

# Card 2

card2 = tk.Frame(
    stats_frame,
    bg="#161616",
    width=220,
    height=120
)

card2.grid(row=0, column=1, padx=15)

card2.pack_propagate(False)

tk.Label(
    card2,
    text="💰 Sales Today",
    bg="#161616",
    fg="#F8F5F0",
    font=("Segoe UI", 12)
).pack(pady=(15, 5))

tk.Label(
    card2,
    text="0",
    bg="#161616",
    fg="#D4AF37",
    font=("Segoe UI", 24, "bold")
).pack()

# Card 3

card3 = tk.Frame(
    stats_frame,
    bg="#161616",
    width=220,
    height=120
)

card3.grid(row=0, column=2, padx=15)

card3.pack_propagate(False)

tk.Label(
    card3,
    text="📦 Inventory",
    bg="#161616",
    fg="#F8F5F0",
    font=("Segoe UI", 12)
).pack(pady=(15, 5))

tk.Label(
    card3,
    text="0",
    bg="#161616",
    fg="#D4AF37",
    font=("Segoe UI", 24, "bold")
).pack()


buttons_frame = tk.Frame(
    window,
    bg="#0A0A0A"
)

buttons_frame.pack(pady=40)

button_style = {
    "font": ("Segoe UI", 12, "bold"),
    "bg": "#6D071A",
    "fg": "white",
    "activebackground": "#8B0000",
    "activeforeground": "white",
    "width": 22,
    "height": 2,
    "bd": 0,
    "cursor": "hand2"
}

tk.Button(
    buttons_frame,
    text="➕ Add Wine",
    **button_style
).grid(row=0, column=0, padx=15, pady=10)

tk.Button(
    buttons_frame,
    text="📦 View Inventory",
    **button_style
).grid(row=0, column=1, padx=15, pady=10)

tk.Button(
    buttons_frame,
    text="💰 Record Sale",
    **button_style
).grid(row=1, column=0, padx=15, pady=10)

tk.Button(
    buttons_frame,
    text="🗑 Delete Wine",
    **button_style
).grid(row=1, column=1, padx=15, pady=10)

window.mainloop()