import tkinter as tk

from interface.lookup import open_lookup
from interface.othertools import open_other_tools
from interface.profiler import open_profiler
from core.countries import countries

import settings


def changed_country(*args):
    settings.monpays = country.get()
    settings.codemonpays = countries[settings.monpays]


settings.init()

window = tk.Tk()
window.title("Little Brother")
window.configure(background="white")
window.geometry("300x150")

lookup = tk.Button(window, text="Lookup", command=lambda: open_lookup(window))
lookup.pack()

otherTools = tk.Button(window, text="Other Tools", command=lambda: open_other_tools(window))
otherTools.pack()

profiler = tk.Button(window, text="Profiler", command=lambda: open_profiler(window))
profiler.pack()

frame = tk.Frame(window, background="White")
frame.pack()

tk.Label(frame, text="Country:", height=2, background="White").pack(side=tk.LEFT)

country = tk.StringVar(frame)
country.set(settings.monpays)
tk.OptionMenu(frame, country, *countries.keys()).pack(side=tk.RIGHT)

country.trace("w", changed_country)

window.mainloop()
