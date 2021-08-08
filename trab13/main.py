import tkinter as tk

import artista
import playlist
import album
import musica


class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root

        self.root.geometry('500x500')
        self.menubar = tk.Menu(self.root)

        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar artista",
                                     command=self.controle.cadastrarArtistas)
        self.artistaMenu.add_command(label="Consultar artista",
                                     command=self.controle.consultaArtistas)

        self.albumMenu.add_command(label="Cadastrar album",
                                   command=self.controle.cadastrarAlbuns)
        self.albumMenu.add_command(label="Consultar album",
                                   command=self.controle.consultaAlbuns)

        self.playlistMenu.add_command(label="Cadastrar playlist",
                                      command=self.controle.cadastrarPlaylists)
        self.playlistMenu.add_command(label="Consultar playlist",
                                      command=self.controle.consultaPlaylists)

        self.sairMenu.add_command(label="Salvar",
                                  command=self.controle.salvaDados)

        self.menubar.add_cascade(label="Artista",
                                 menu=self.artistaMenu)
        self.menubar.add_cascade(label="Album",
                                 menu=self.albumMenu)
        self.menubar.add_cascade(label="Playlist",
                                 menu=self.playlistMenu)
        self.menubar.add_cascade(label="Sair",
                                 menu=self.sairMenu)

        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlPlaylist = playlist.CtrlPlaylist(self)
        self.ctrlMusica = musica.CtrlMusica()
        self.ctrlArtista = artista.CtrlArtista()
        self.ctrlAlbum = album.CtrlAlbum(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Playlists")

        self.root.mainloop()

    def cadastrarArtistas(self):
        self.ctrlArtista.cadastrarArtistas()

    def consultaArtistas(self):
        self.ctrlArtista.consultaArtistas()

    def cadastrarAlbuns(self):
        self.ctrlAlbum.cadastrarAlbuns()

    def consultaAlbuns(self):
        self.ctrlAlbum.consultaAlbuns()

    def cadastrarPlaylists(self):
        self.ctrlPlaylist.cadastrarPlaylists()

    def consultaPlaylists(self):
        self.ctrlPlaylist.consultaPlaylists()

    def salvaDados(self):
        self.ctrlMusica.salvaMusicas()
        self.ctrlArtista.salvaArtistas()
        self.ctrlAlbum.salvaAlbuns()
        self.ctrlPlaylist.salvaPlaylists()
        self.root.destroy()


if __name__ == '__main__':
    c = ControlePrincipal()
