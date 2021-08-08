import tkinter as tk


class GUI:
    def __init__(self):
        self.janela = tk.Tk()

        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)

        self.botao1 = tk.Button(
            self.janela, text="Botão 1", command=self.processaB1)
        self.botao2 = tk.Button(
            self.janela, text="Botão 2", command=self.processaB2)

        self.botao1.pack()
        self.botao2.pack()

        self.label = tk.Label(self.janela, text="Escolha...")
        self.label.pack()

        self.janela.mainloop()

    def processaB1(self):
        self.label.configure(text="Botão 1")

    def processaB2(self):
        self.label.configure(text="Botão 2")


def main():
    GUI()


main()
