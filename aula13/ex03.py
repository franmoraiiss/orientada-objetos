import tkinter as tk


class GUI:
    def __init__(self):
        self.janela = tk.Tk()

        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)

        self.label1 = tk.Label(self.frameTopo, text="Hello1 world")
        self.label2 = tk.Label(self.frameTopo, text="Hello2 world")
        self.label3 = tk.Label(self.frameTopo, text="Hello3 world")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4 = tk.Label(self.frameBase, text="Um")
        self.label5 = tk.Label(self.frameBase, text="Dois")
        self.label6 = tk.Label(self.frameBase, text="Tres")

        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.frameTopo.pack()
        self.frameBase.pack()

        self.janela.mainloop()


def main():
    GUI()


main()
