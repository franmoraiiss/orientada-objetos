import os.path
import pickle

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import musica


class Album:

    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []

        artista.addAlbum(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAno(self):
        return self.__ano

    def getFaixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
        mus = musica.Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(mus)

        return mus

    def Imprimir(self, album):
        str = 'Faixas do album: ' + album.getTitulo() + '\n\n'
        for musi in album.getFaixas():
            str += '  -' + musi.getTitulo() + '\n'
        self.limiteConsulta.mostraJanela(album.getTitulo(), str)


class LimitecadastrarAlbum(tk.Toplevel):
    def __init__(self, controle, listaNomeArtista):

        tk.Toplevel.__init__(self)
        self.geometry('250x150')
        self.title("Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")

        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameArtista, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeArtista

        self.buttonCria = tk.Button(self.frameButton, text="Criar Album")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaAlbum)

        self.buttonCria = tk.Button(self.frameButton, text="Fechar")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.fechaCadastrarHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimitecadastrarMusica(tk.Toplevel):
    def __init__(self, controle, album):
        tk.Toplevel.__init__(self)
        self.geometry('200x100')
        self.title("Musica")
        self.controle = controle
        self.album = album

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Titulo: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterMusicaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaMusicaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaAlbuns(tk.Toplevel):
    def __init__(self, controle, listaAlbuns):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Consultar Album")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Escolher album: ")
        self.labelNome.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameNome, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaAlbuns

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterConsultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaConsultaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlAlbum():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if os.path.getsize("album.pickle") < 1:
            self.listaAlbuns = []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlbuns = pickle.load(f)

        self.listaCodDisc = []

        self.listaDisc = []

    def salvaAlbuns(self):
        if len(self.listaAlbuns) != 0:
            with open("album.pickle", "wb") as f:
                pickle.dump(self.listaAlbuns, f)

    def getAlbum(self, titulo):
        albumRet = None
        for album in self.listaAlbuns:
            if album.getTitulo() == titulo:
                albumRet = album

        return albumRet

    def getNomeAlbuns(self):
        listaNome = []
        for album in self.listaAlbuns:
            listaNome.append(album.getTitulo())
            print("%s" % album.getTitulo())

        return listaNome

    def cadastrarAlbuns(self):
        self.listaNomeArtista = self.ctrlPrincipal.ctrlArtista.getListaNomeArtista()
        self.limiteIns = LimitecadastrarAlbum(self, self.listaNomeArtista)

    def criaAlbum(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        ano = self.limiteIns.inputAno.get()
        artSel = self.limiteIns.escolhaCombo.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(artSel)
        if artista == None:
            self.limiteIns.mostraJanela(
                'Falhou', 'Não foi possível criar o album, selecione um artista existente.')
        else:
            album = Album(titulo, artista, ano)
            self.listaAlbuns.append(album)
            self.limiteIns.mostraJanela(
                'Sucesso', 'Adicione musicas ao album')
            self.limiteMusica = LimitecadastrarMusica(self, album)
            self.limiteIns.destroy()

    def enterMusicaHandler(self, event):
        titulo = self.limiteMusica.inputNome.get()
        musica = self.limiteMusica.album.addFaixa(titulo)
        self.ctrlPrincipal.ctrlMusica.listaMusicas.append(musica)
        self.limiteMusica.mostraJanela(
            'Sucesso', 'Musica adicionada')
        self.limiteMusica.inputNome.delete(
            0, len(self.limiteMusica.inputNome.get()))

    def fechaMusicaHandler(self, event):
        self.limiteMusica.mostraJanela('Sucesso', 'Salvo')
        self.limiteMusica.destroy()

    def consultaAlbuns(self):
        self.limiteConsulta = LimiteConsultaAlbuns(self, self.getNomeAlbuns())

    def enterConsultaHandler(self, event):
        album = self.getAlbum(self.limiteConsulta.escolhaCombo.get())
        if album == None:
            self.limiteConsulta.mostraJanela('Falhou', 'Album inexistente.')
        else:
            Album.Imprimir(self, album)

    def fechaCadastrarHandler(self, event):
        self.limiteIns.destroy()

    def fechaConsultaHandler(self, event):
        self.limiteConsulta.destroy()
