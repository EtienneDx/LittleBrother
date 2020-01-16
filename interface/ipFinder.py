import sys
import threading
import tkinter as tk
import tkinter.messagebox as messagebox

from core.ipFinder import ip_finder as sp


def ip_finder(window, settings):
    search = tk.Toplevel(window)
    search.title("Ip Finder")
    search.geometry("300x150")

    frame1 = tk.Frame(search, background="White")
    frame1.pack()

    tk.Label(frame1, text="IP adress: ").pack(side=tk.LEFT)
    name = tk.Entry(frame1)
    name.pack(side=tk.RIGHT)

    button = tk.Button(search, text="Search", command=lambda: done(search, name.get()))
    button.pack()

    search.mainloop()


def done(search, name):
    search.destroy()
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        try:
            x = threading.Thread(target=sp, args=(name))
            x.start()
            messagebox.showinfo("Searching", "Currently searching...")
            x.join()
        except:
            messagebox.showinfo("Searching", "Currently searching...")
            sp(name)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
