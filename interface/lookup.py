import tkinter as tk

from interface.employeeLookup import employee_lookup
from interface.searchPerson import search_person
from interface.searchUsername import search_username
from interface.searchAdress import search_adress
from interface.searchNumber import search_number
from interface.ipFinder import ip_finder
from interface.bssidFinder import bssid_finder
from interface.searchEmail import search_email


modes = {
    "Search Person": search_person,
    "Search Username": search_username,
    "Search Adress": search_adress,
    "Search Number": search_number,
    "Ip Finder": ip_finder,
    "BSSID Finder": bssid_finder,
    "Search Email": search_email,
    "Employee Lookup": employee_lookup,
}


def open_lookup(root, settings):
    window = tk.Toplevel(root)
    window.title("Lookup")
    window.geometry("200x400")

    for name, action in modes.items():
        reg(root, window, name, action, settings)

    window.mainloop()


def reg(root, window, name, action, settings):
    tk.Button(window, text=name, command=lambda: done(action, window, root, settings)).pack()


def done(action, window, root, settings):
    window.destroy()
    action(root, settings)
