from tkinter import *
from tkinter import ttk

class CounterApp:

    def __init__(self, root: Tk):
        root.title("Counter App")

        mainframe = ttk.Frame(root, padding = "12 12 12 12")
        mainframe.grid(column = 0, row = 0, sticky = (N, E, W, S))
        root.columnconfigure(0, weight = 1)
        root.rowconfigure(0, weight = 1)

        self.counter = StringVar()
        self.counter.set("0")
        ttk.Label(mainframe, textvariable = self.counter).grid(column = 0, row = 0, columnspan = 2, rowspan = 2)
        ttk.Button(mainframe, text = "+", command = self.up).grid(column = 2, row = 0, sticky = (N, E, W, S))
        ttk.Button(mainframe, text = "-", command = self.down).grid(column = 2, row = 1, sticky = (N, E, W, S))

        root.bind("<Return>", self.up)
        root.bind("<BackSpace>", self.down)
        root.bind("<Escape>", lambda e: root.destroy())

        for child in mainframe.winfo_children():
            child.grid_configure(padx = 12, pady = 12)

    def up(self, *args):
        new_val = int(self.counter.get()) + 1
        self.counter.set(str(new_val))

    def down(self, *args):
        new_val = int(self.counter.get()) - 1
        self.counter.set(str(new_val))

def main():
    root = Tk()
    app = CounterApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()