import sys
import threading
import tkinter as tk
import tkinter.messagebox as messagebox

from core.searchAdresse import search_adress as sp


def search_adress(window, settings):
    search = tk.Toplevel(window)
    search.title("Search Adress")
    search.geometry("300x150")

    frame1 = tk.Frame(search, background="White")
    frame1.pack()

    tk.Label(frame1, text="Adress: ").pack(side=tk.LEFT)
    adress = tk.Entry(frame1)
    adress.pack(side=tk.RIGHT)

    button = tk.Button(search, text="Search", command=lambda: done(search, settings.codemonpays, adress.get()))
    button.pack()

    search.mainloop()


def done(search, code, adress):
    search.destroy()
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        try:
            x = threading.Thread(target=sp, args=(code, adress))
            x.start()
            messagebox.showinfo("Searching", "Currently searching...")
            x.join()
        except:
            messagebox.showinfo("Searching", "Currently searching...")
            sp(code, adress)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
