import tkinter as tk
from tkinter import ttk, messagebox
from app.calculator import calc_final

def launch_app():
    root = tk.Tk()
    root.title("OFPPT Grade Calculator")
    root.geometry("400x450")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 10))
    style.configure("TEntry", font=("Segoe UI", 10))
    style.configure("TButton", font=("Segoe UI", 10, "bold"))

    fields = [
        "Note Passage",
        "Moyenne Modules",
        "Moyenne Théorie",
        "Moyenne Pratique",
        "Français",
        "Arabe",
        "Anglais"
    ]

    entries = {}

    for field in fields:
        label = ttk.Label(root, text=field)
        label.pack(pady=(10, 0))
        entry = ttk.Entry(root)
        entry.pack(pady=(0, 5), ipadx=40)
        entries[field] = entry

    result_var = tk.StringVar()

    def calculate():
        try:
            values = [float(entries[field].get()) for field in fields]
            result = calc_final(*values)
            result_var.set(f"📊 Moyenne Générale: {result:.2f} / 20")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer toutes les notes correctement.")
            result_var.set("")

    ttk.Button(root, text="Calculer la moyenne", command=calculate).pack(pady=15)
    ttk.Label(root, textvariable=result_var, font=("Segoe UI", 12, "bold")).pack(pady=10)

    root.mainloop()
