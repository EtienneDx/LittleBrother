import sys
import threading
import tkinter as tk
import tkinter.messagebox as messagebox

from core.employee_lookup import emp_lookup as sp


def employee_lookup(window, settings):
    search = tk.Toplevel(window)
    search.title("Employee lookup")
    search.geometry("300x150")

    frame1 = tk.Frame(search, background="White")
    frame1.pack()
    frame2 = tk.Frame(search, background="White")
    frame2.pack()

    tk.Label(frame1, text="Enterprise: ").pack(side=tk.LEFT)
    name = tk.Entry(frame1)
    name.pack(side=tk.RIGHT)

    tk.Label(frame2, text="City: ").pack(side=tk.LEFT)
    city = tk.Entry(frame2)
    city.pack(side=tk.RIGHT)

    button = tk.Button(search, text="Search", command=lambda: done(search, name.get(), city.get()))
    button.pack()

    search.mainloop()


def done(search, name, city):
    search.destroy()
    try:
        threading.Thread(target=messagebox.showinfo, args=("Searching", "Currently searching...")).start()
    except:
        messagebox.showinfo("Searching", "Currently searching...")
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        sp(name, city)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
