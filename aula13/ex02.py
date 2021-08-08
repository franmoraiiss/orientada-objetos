import tkinter as tk


class GUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.label = tk.Label(self.janela, text="Hello world")

        self.label.pack()
        self.janela.mainloop()


def main():
    GUI()


main()
