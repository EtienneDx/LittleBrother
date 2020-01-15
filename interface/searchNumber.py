import sys
import threading
import tkinter as tk
import tkinter.messagebox as messagebox

from core.searchNumber import search_number as sp


def search_number(window, settings):
    search = tk.Toplevel(window)
    search.title("Search Adress")
    search.geometry("300x150")

    city = tk.StringVar()

    frame1 = tk.Frame(search, background="White")
    frame1.pack()

    tk.Label(frame1, text="Number: ").pack(side=tk.LEFT)
    number = tk.Entry(frame1)
    number.pack(side=tk.RIGHT)

    button = tk.Button(search, text="Search", command=lambda: done(search, settings.codemonpays, number.get()))
    button.pack()

    search.mainloop()


def done(search, code, number):
    search.destroy()
    try:
        threading.Thread(target=messagebox.showinfo, args=("Searching", "Currently searching...")).start()
    except:
        messagebox.showinfo("Searching", "Currently searching...")
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        sp(code, number)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
