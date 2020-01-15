import tkinter as tk
from interface.searchPerson import search_person
from interface.searchUsername import search_username
from interface.searchAdress import search_adress


modes = {
    "Search Person": search_person,
    "Search Username": search_username,
    "Search Adress": search_adress,
}


def open_lookup(root, settings):
    window = tk.Toplevel(root)
    window.title("Lookup")
    window.geometry("200x400")

    for name, action in modes.items():
        tk.Button(window, text=name, command=lambda: action(window, settings)).pack()

    window.mainloop()
