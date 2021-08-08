import os.path

import pickle

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Playlist:

    def __init__(self, nome):
        self.__nome = nome

        self.musicas = []

    def getNome(self):
        return self.__nome

    def Imprimir(self, playlist):
        titulo = playlist.getNome()
        str = 'Faixas \n\n'
        for mus in playlist.musicas:
            str += '  -' + mus.getTitulo() + '\n'
        self.limiteConsulta.mostraJanela(titulo, str)


class LimiteCadastrarPlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomeArtista):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Playlist")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(
            self.frameTitulo, text="Título playlist: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameArtista, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeArtista

        self.buttonBuscar = tk.Button(self.frameButton, text="Buscar")
        self.buttonBuscar.pack(side="left")
        self.buttonBuscar.bind("<Button>", controle.buscaMusica)

        self.buttonCria = tk.Button(self.frameButton, text="Criar Playlist")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class limiteMusica(tk.Toplevel):
    def __init__(self, controle, listaMusicaDoArtista):

        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Playlist")
        self.controle = controle

        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameMusica.pack()
        self.frameButton.pack()

        self.labelMusica = tk.Label(
            self.frameMusica, text="Escolha as Musicas: ")
        self.labelMusica.pack(side="left")
        self.listbox = tk.Listbox(self.frameMusica)
        self.listbox.pack(side="left")
        for musica in listaMusicaDoArtista:
            self.listbox.insert(tk.END, musica)

        self.buttonIns = tk.Button(self.frameButton, text="Cadastrar Musica")
        self.buttonIns.pack(side="left")
        self.buttonIns.bind("<Button>", controle.cadastrarMusica)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaMusicaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle, listaPlaylists):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta de Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Escolher Playlist: ")
        self.labelNome.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameNome, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaPlaylists

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.entrarConsultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaConsultaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if os.path.getsize("playlist.pickle") < 1:
            self.listaPlaylist = []
        else:
            with open("playlist.pickle", "rb") as f:
                self.listaPlaylist = pickle.load(f)

        self.listaMusicasPlaylist = []

    def salvaPlaylists(self):
        if len(self.listaPlaylist) != 0:
            with open("playlist.pickle", "wb") as f:
                pickle.dump(self.listaPlaylist, f)

    def getPlaylist(self, nome):
        playRet = None
        for play in self.listaPlaylist:
            if play.getNome() == nome:
                playRet = play
        return playRet

    def getNomePlaylist(self):
        listaNome = []
        for play in self.listaPlaylist:
            listaNome.append(play.getNome())
        return listaNome

    def getListaArtistaMusicas(self, artista):
        listaMusicas = []
        art = self.ctrlPrincipal.ctrlArtista.getArtista(artista)
        if art == None:
            return art
        else:
            for musica in art.getMusicas():
                listaMusicas.append(musica.getTitulo())
            return listaMusicas

    def cadastrarPlaylists(self):
        self.listaNomeArtista = self.ctrlPrincipal.ctrlArtista.getListaNomeArtista()
        self.limiteIns = LimiteCadastrarPlaylist(self, self.listaNomeArtista)

    def cadastrarMusica(self, event):
        musicaSel = self.limiteMusica.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlMusica.getMusica(musicaSel)
        self.listaMusicasPlaylist.append(musica)
        self.limiteMusica.listbox.delete(tk.ACTIVE)

    def fechaMusicaHandler(self, event):
        self.limiteMusica.destroy()

    def fechaHandler(self, event):
        self.limiteMusica.destroy()

    def buscaMusica(self, event):
        artista = self.limiteIns.escolhaCombo.get()
        listaMusicas = self.getListaArtistaMusicas(artista)
        if listaMusicas == None:
            self.limiteIns.mostraJanela(
                'Falha.', 'Selecione um artista existente.')
        else:
            self.limiteMusica = limiteMusica(self, listaMusicas)

    def criaPlaylist(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        playlist = Playlist(titulo)
        for musica in self.listaMusicasPlaylist:
            playlist.musicas.append(musica)
        self.listaPlaylist.append(playlist)
        self.limiteIns.mostraJanela(
            'Sucesso', 'Playlist foi criada!')
        self.listaMusicasPlaylist = []
        self.limiteIns.destroy()

    def consultaPlaylists(self):
        self.limiteConsulta = LimiteConsultaPlaylist(
            self, self.getNomePlaylist())

    def entrarConsultaHandler(self, event):
        playlist = self.getPlaylist(self.limiteConsulta.escolhaCombo.get())
        if playlist == None:
            self.limiteConsulta.mostraJanela(
                'Falha.', 'Playlist inexistente.')
        else:
            Playlist.Imprimir(self, playlist)

    def fechaConsultaHandler(self, event):
        self.limiteConsulta.destroy()
