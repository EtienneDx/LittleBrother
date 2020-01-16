import tkinter as tk

from interface.hashDecrypt import hash_decrypt

modes = {
    "Hash Decrypt": hash_decrypt,
}


def open_other_tools(root, settings):
    window = tk.Toplevel(root)
    window.title("Other tools")
    window.geometry("200x400")

    for name, action in modes.items():
        reg(root, window, name, action, settings)

    window.mainloop()


def reg(root, window, name, action, settings):
    tk.Button(window, text=name, command=lambda: done(action, window, root, settings)).pack()


def done(action, window, root, settings):
    window.destroy()
    action(root, settings)
