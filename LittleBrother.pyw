import sys

from terminaltables.ascii_table import AsciiTable
import terminaltables.other_tables as ot


if sys.platform.startswith("darwin"):
    # Needed to force ascii tables on mac os because mac encoding doesn't allow special chars used for SingleTable
    def uncache(exclude):
        """Remove package modules from cache except excluded ones.
        On next import they will be reloaded.

        Args:
            exclude (iter<str>): Sequence of module paths.
        """
        pkgs = []
        for mod in exclude:
            pkg = mod.split('.', 1)[0]
            pkgs.append(pkg)

        to_uncache = []
        for mod in sys.modules:
            if mod in exclude:
                continue

            if mod in pkgs:
                to_uncache.append(mod)
                continue

            for pkg in pkgs:
                if mod.startswith(pkg + '.'):
                    to_uncache.append(mod)
                    break

        for mod in to_uncache:
            del sys.modules[mod]


    ot.SingleTable = AsciiTable
    uncache(['terminaltables.other_tables'])

from terminaltables import SingleTable
print(SingleTable(['something']).table)


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
window.geometry("300x100")

lookup = tk.Button(window, text="Lookup", command=lambda: open_lookup(window, settings))
lookup.pack()

otherTools = tk.Button(window, text="Other Tools", command=lambda: open_other_tools(window, settings))
otherTools.pack()

# profiler = tk.Button(window, text="Profiler", command=lambda: open_profiler(window))
# profiler.pack()

frame = tk.Frame(window, background="White")
frame.pack()

tk.Label(frame, text="Country:", height=2, background="White").pack(side=tk.LEFT)

country = tk.StringVar(frame)
country.set(settings.monpays)
tk.OptionMenu(frame, country, *countries.keys()).pack(side=tk.RIGHT)

country.trace("w", changed_country)

window.mainloop()

