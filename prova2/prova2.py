import os.path

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pickle


class CupomFiscal:

    def __init__(self, codigo, listaProdutos):
        self.__codigo = codigo

        self.__produtos = listaProdutos

    def getCodigo(self):
        return self.__codigo

    def getProdutos(self):
        return self.__produtos


class insereCupom(tk.Toplevel):
    def __init__(self, controle, listaCodDisc):

        tk.Toplevel.__init__(self)
        self.geometry('250x300')
        self.title("Criação Cupom Fiscal")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameCodigo.pack()
        self.frameDiscip.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(
            self.frameCodigo, text="Código da cupom fiscal: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.labelEst = tk.Label(
            self.frameDiscip, text="Escolha os Produtos: ")
        self.labelEst.pack(side="left")
        self.listbox = tk.Listbox(self.frameDiscip)
        self.listbox.pack(side="left")
        for dis in listaCodDisc:
            if dis != controle.listaProdutos:
                self.listbox.insert(tk.END, dis)

        self.buttonInsere = tk.Button(self.frameButton, text="Inserir Produto")
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereDisciplina)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.criaCupom)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def mostraHistorico(self):
        listaProdutos = self.ctrlPrincipal.ctrlProduto.getMatriculaProdutos()
        self.limiteHis = LimiteMostraProduto(self, listaProdutos)

    def mostraHistoricoProduto(self, event):
        produtoSel = self.limiteHis.escolhaCombo.get()
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(produtoSel)
        mostra = ''
        mostra += 'Descrição: ' + produto.getDescricao() + '\n'
        mostra += 'Código: ' + produto.getCodigo() + '\n'
        mostra += "Valor: R${}".format(produto.getValor()) + '\n'
        self.limiteLista = LimiteMostraProdutoMensagem(mostra)

    def fechaHandler(self, event):
        self.limiteIns.destroy()


class CtrlCupomFiscal():
    def __init__(self, controlePrincipal):
        self.listaProdutos = []
        self.ctrlPrincipal = controlePrincipal

        if not os.path.isfile("nf.pickle"):
            self.listaCupoms = []
        else:
            with open("nf.pickle", "rb") as f:
                self.listaCupoms = pickle.load(f)

    def salvaCupomFiscal(self):
        if len(self.listaCupoms) != 0:
            with open("nf.pickle", "wb") as f:
                pickle.dump(self.listaCupoms, f)

    def getlistaCupoms(self):
        return self.listaCupoms

    def insereCupoms(self):
        self.limiteIns = LimiteInsereCupom(self)

    def buscaCupom(self):
        lista = self.getlistaCupoms()
        listaN = []
        for element in lista:
            listaN.append(element.getCodigo())
        self.limiteIns = LimiteMostraCupom(self, listaN)

    def insereCupom(self):
        self.listaCodDisciplinas = self.ctrlPrincipal.ctrlProduto.getMatriculaProdutos()
        self.limiteIns = insereCupom(self, self.listaCodDisciplinas)

    def criaCupom(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nf = CupomFiscal(codigo, self.listaProdutos)
        self.listaCupoms.append(nf)
        self.limiteIns.mostraJanela('Sucesso', 'Cupom criado')
        self.limiteIns.destroy()

    def insereDisciplina(self, event):
        discSel = self.limiteIns.listbox.get(tk.ACTIVE)
        disciplina = self.ctrlPrincipal.ctrlProduto.getProduto(discSel)
        self.listaProdutos.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Produto inserido!')

    def getCodigosCupom(self):
        listaAno = []
        for disc in self.listaCupoms:
            listaAno.append(disc.getCodigo())
        return listaAno

    def getCupom(self, codigo):
        discRet = None
        for disc in self.listaCupoms:
            if disc.getCodigo() == codigo:
                discRet = disc
        return discRet

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(
            0, len(self.limiteIns.inputCodigo.get()))

    def fechaHandler(self, event):
        self.criaCupom(self, event)
        self.limiteIns.destroy()

    def getCupom(self, codigo):
        cupom = None

        for cp in self.getlistaCupoms():
            if codigo == cp.getCodigo():
                cupom = cp
        return cupom

    def mostraCupom(self, event):
        str = ''
        cupom = self.limiteIns.escolhaCombo.get()
        cp = self.getCupom(cupom)

        str += 'Código: ' + cp.getCodigo() + '\n'

        str += 'Itens: \n'
        for produto in cp.getProdutos():
            str += '- Código: ' + produto.getCodigo() + '- Descrição: ' + \
                produto.getDescricao() + ' - R$ {}\n'.format(produto.getValor())

        self.limiteLista = LimiteInsereCupom(str)


class LimiteInsereCupom(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x150')
        self.title("Cupom Fiscal")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(
            self.frameCodigo, text="Número Cupom fiscal: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Cria Cupom")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criaCupom)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteInsereCupom():
    def __init__(self, str):
        messagebox.showinfo('Cupom Fiscal', str)


class LimiteMostraCupom(tk.Toplevel):
    def __init__(self, controle, listaCupom):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Cupom Fiscais')
        self.controle = controle

        self.frameCupom = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCupom.pack()
        self.frameButton.pack()

        self.labelCupom = tk.Label(
            self.frameCupom, text="Escolher Cupom Fiscal: ")
        self.labelCupom.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameCupom, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCupom

        self.buttonSubmit = tk.Button(
            self.frameButton, text="Verificar Cupom Fiscal")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.mostraCupom)


class LimiteMostraProduto(tk.Toplevel):
    def __init__(self, controle, listaProdutos):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produtos")
        self.controle = controle

        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameProduto.pack()
        self.frameButton.pack()

        self.labelProduto = tk.Label(
            self.frameProduto, text="Escolha Produto: ")
        self.labelProduto.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameProduto, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaProdutos

        self.buttonSubmit = tk.Button(
            self.frameButton, text="Verificar Produto")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.mostraHistoricoProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraProdutoMensagem():
    def __init__(self, str):
        messagebox.showinfo('Produto:', str)


class Produto:

    def __init__(self, descricao, codigo, valor):
        self.__descricao = descricao
        self.__codigo = codigo
        self.__valor = valor

    def getDescricao(self):
        return self.__descricao

    def getCodigo(self):
        return self.__codigo

    def getValor(self):
        return self.__valor


class LimiteInsereProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('200x300')
        self.title("Produto")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameNroMatric = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNome.pack()
        self.frameNroMatric.pack()
        self.frameValor.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Descrição: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelNroMatric = tk.Label(self.frameNroMatric, text="Código: ")
        self.labelNroMatric.pack(side="left")
        self.inputNro = tk.Entry(self.frameNroMatric, width=20)
        self.inputNro.pack(side="left")

        self.labelValor = tk.Label(self.frameValor, text="Valor Unitário: ")
        self.labelValor.pack(side="left")
        self.inputValor = tk.Entry(self.frameValor, width=20)
        self.inputValor.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Cria Produto")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criaProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraProdutos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Produtos', str)


class CtrlProduto():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

        if not os.path.isfile("produto.pickle"):
            self.listaProdutos = []
        else:
            with open("produto.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    def salvaProduto(self):
        if len(self.listaProdutos) != 0:
            with open("produto.pickle", "wb") as f:
                pickle.dump(self.listaProdutos, f)

    def getListaProdutos(self):
        return self.listaProdutos

    def insereProdutos(self):
        self.limiteIns = LimiteInsereProduto(self)

    def getProduto(self, nmr):
        discRet = None
        for produto in self.listaProdutos:
            if produto.getCodigo() == nmr:
                discRet = produto
        return discRet

    def criaProduto(self, event):
        descricao = self.limiteIns.inputNome.get()
        nro = self.limiteIns.inputNro.get()
        valor = self.limiteIns.inputValor.get()
        produto = Produto(descricao, nro, valor)
        self.listaProdutos.append(produto)
        self.limiteIns.mostraJanela('Sucesso', 'Produto criado com sucesso')
        self.limiteIns.destroy()

    def mostraProdutos(self):
        str = ''
        for produto in self.listaProdutos:
            str += 'Nome: ' + produto.getDescricao() + '\n'
            str += 'Número de Matrícula: ' + produto.getCodigo() + '\n'
            str += 'Curso: ' + produto.getCurso().getDescricao() + '\n\n'
        self.limiteLista = LimiteMostraProdutos(str)

    def getDescricaoProdutos(self):
        listaProdutos = []
        for aln in self.listaProdutos:
            listaProdutos.append(aln.getDescricao())
        return listaProdutos

    def getMatriculaProdutos(self):
        listaProdutos = []
        for produto in self.listaProdutos:
            listaProdutos.append(produto.getCodigo())
        return listaProdutos

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()


class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x350')

        self.menubar = tk.Menu(self.root)
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.historicoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.produtoMenu.add_command(label="Cadastrar produto",
                                     command=self.controle.insereProdutos)
        self.produtoMenu.add_command(label="Consultar produto",
                                     command=self.controle.MostraHistorico)
        self.menubar.add_cascade(label="Produto",
                                 menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Criar Cupom Fiscal",
                                   command=self.controle.insereCupom)
        self.cupomMenu.add_command(label="Consultar Cupom Fiscal",
                                   command=self.controle.buscaCupom)
        self.menubar.add_cascade(label="Cupom Fiscal",
                                 menu=self.cupomMenu)

        self.sairMenu.add_command(label="Salva",
                                  command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair",
                                 menu=self.sairMenu)

        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = CtrlProduto(self)
        self.ctrlCupomFiscal = CtrlCupomFiscal(self)
        self.ctrlHistorico = CtrlHistorico(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Emissão de cupom fiscal")

        self.root.mainloop()

    def insereProdutos(self):
        self.ctrlProduto.insereProdutos()

    def mostraProdutos(self):
        self.ctrlProduto.mostraProdutos()

    def insereCupoms(self):
        self.ctrlCupomFiscal.insereCupoms()

    def buscaCupom(self):
        self.ctrlCupomFiscal.buscaCupom()

    def insereCupom(self):
        self.ctrlCupomFiscal.insereCupom()

    def salvaDados(self):
        self.ctrlProduto.salvaProduto()
        self.ctrlCupomFiscal.salvaCupomFiscal()
        self.root.destroy()

    def MostraHistorico(self):
        self.ctrlHistorico.mostraHistorico()

    def insereDisciplinasHistorico(self):
        self.ctrlHistorico.insereDisciplinas()


if __name__ == '__main__':
    c = ControlePrincipal()
