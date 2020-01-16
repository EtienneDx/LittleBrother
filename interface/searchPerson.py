import sys
import threading
import tkinter as tk
import tkinter.messagebox as messagebox

from core.searchPersonne import search_person as sp


def search_person(window, settings):
    search = tk.Toplevel(window)
    search.title("Search Person")
    search.geometry("300x150")

    frame1 = tk.Frame(search, background="White")
    frame1.pack()
    frame2 = tk.Frame(search, background="White")
    frame2.pack()

    tk.Label(frame1, text="Name: ").pack(side=tk.LEFT)
    name = tk.Entry(frame1)
    name.pack(side=tk.RIGHT)

    tk.Label(frame2, text="City: ").pack(side=tk.LEFT)
    city = tk.Entry(frame2)
    city.pack(side=tk.RIGHT)

    button = tk.Button(search, text="Search", command=lambda: done(search, settings.codemonpays, name.get(), city.get()))
    button.pack()

    search.mainloop()


def done(search, code, name, city):
    search.destroy()
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        try:
            x = threading.Thread(target=sp, args=(code, name, city))
            x.start()
            messagebox.showinfo("Searching", "Currently searching...")
            x.join()
        except:
            messagebox.showinfo("Searching", "Currently searching...")
            sp(code, name, city)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
