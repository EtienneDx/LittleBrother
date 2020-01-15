import sys
import tkinter as tk
import tkinter.messagebox as messagebox

from core.searchUserName import search_username as sp


def search_username(window, settings):
    search = tk.Toplevel(window)
    search.title("Search Username")
    search.geometry("300x150")

    city = tk.StringVar()

    frame1 = tk.Frame(search, background="White")
    frame1.pack()

    tk.Label(frame1, text="Username: ").pack(side=tk.LEFT)
    name = tk.Entry(frame1)
    name.pack(side=tk.RIGHT)

    button = tk.Button(search, text="Search", command=lambda: done(search, name.get()))
    button.pack()

    search.mainloop()


def done(search, name):
    search.destroy()
    messagebox.showinfo("Searching", "Currently searching...")
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        sp(name)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
