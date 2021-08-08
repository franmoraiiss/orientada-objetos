import os.path

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pickle


class Artista:

    def __init__(self, nome):
        self.__nome = nome
        self.__listaAlbuns = []
        self.__listaMusicas = []

    def getNome(self):
        return self.__nome

    def getAlbuns(self):
        return self.__listaAlbuns

    def getMusicas(self):
        return self.__listaMusicas

    def addAlbum(self, album):
        self.__listaAlbuns.append(album)

    def addMusica(self, musica):
        self.__listaMusicas.append(musica)

    def imprimir(self, artista):
        if artista.getAlbuns() == []:
            self.limiteConsulta.mostraJanela(
                'Falhou', 'O artista não tem albums.')
        else:
            str = artista.getNome() + '\n'
            for alb in artista.getAlbuns():
                str += '\nAlbum: ' + alb.getTitulo() + '\n'
                for fai in alb.getFaixas():
                    str += '  -' + fai.getTitulo() + '\n'
            self.limiteConsulta.mostraJanela('Sucesso', str)


class LimitecadastrarArtistas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Limpar")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaArtistas(tk.Toplevel):
    def __init__(self, controle, listaArtistas):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Consultar artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Pesquisar artista: ")
        self.labelNome.pack(side="left")
        self.escolhaArt = ttk.Combobox(
            self.frameNome, width=15, values=listaArtistas)
        self.escolhaArt.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterConsultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaConsultaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlArtista():
    def __init__(self):
        if os.path.getsize("artista.pickle") < 1:
            self.listaArtistas = []
        else:
            with open("artista.pickle", "rb") as f:
                self.listaArtistas = pickle.load(f)

    def salvaArtistas(self):
        if len(self.listaArtistas) != 0:
            with open("artista.pickle", "wb") as f:
                pickle.dump(self.listaArtistas, f)

    def cadastrarArtistas(self):
        self.limiteIns = LimitecadastrarArtistas(self)

    def getArtista(self, nome):
        artistaRet = None
        for artista in self.listaArtistas:
            if artista.getNome() == nome:
                artistaRet = artista
        return artistaRet

    def getListaNomeArtista(self):
        listaNome = []
        for artista in self.listaArtistas:
            listaNome.append(artista.getNome())
        return listaNome

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostraJanela(
            'Sucesso', 'Artista cadastrado!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultaArtistas(self):
        self.limiteConsulta = LimiteConsultaArtistas(
            self, self.getListaNomeArtista())

    def enterConsultaHandler(self, event):
        artista = self.getArtista(self.limiteConsulta.escolhaArt.get())
        if artista == None:
            self.limiteConsulta.mostraJanela('Falhou', 'Artista inexistente.')
        else:
            Artista.imprimir(self, artista)

    def fechaConsultaHandler(self, event):
        self.limiteConsulta.destroy()
