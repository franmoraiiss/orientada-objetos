import os.path
import pickle


class Musica:

    def __init__(self, titulo, artista, album, nroFaixa):
        self.__nroFaixa = nroFaixa
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

        artista.addMusica(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

    def getNroFaixa(self):
        return self.__nroFaixa


class CtrlMusica():
    def __init__(self):
        if os.path.getsize("musica.pickle") > 0:
            with open("musica.pickle", "rb") as f:
                self.listaMusicas = pickle.load(f)
        else:
            self.listaMusicas = []

    def salvaMusicas(self):
        if len(self.listaMusicas) != 0:
            with open("musica.pickle", "wb") as f:
                pickle.dump(self.listaMusicas, f)

    def getMusica(self, titulo):
        musica = None
        for mus in self.listaMusicas:
            if mus.getTitulo() == titulo:
                musica = mus

        return musica
