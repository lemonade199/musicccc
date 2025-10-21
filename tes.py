import tkinter as tk

root = tk.Tk()
root.title("Test Tkinter")
root.geometry("300x200")
tk.Label(root, text="Kalau ini muncul, Tkinter OK ✅", font=("Arial", 12)).pack(pady=50)
root.mainloop()