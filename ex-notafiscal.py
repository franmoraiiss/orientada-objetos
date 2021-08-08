import random


class Produto():
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    def getCodigo(self):
        return self.__codigo

    def getDescricao(self):
        return self.__descricao

    def getValor(self):
        return self.__valor


class NotaFiscal():
    def __init__(self, nroNF, nomeCliente, itensNF):
        self.__nroNF = nroNF
        self.__nomeCliente = nomeCliente
        self.__itensNF = itensNF

    def __str__(self):
        text = '\n-> NFE: {}\n-> Cliente: {}\n-> Produtos: {}\n-> Valor: R${:.2f}\n'.format(
            self.getNroNF(), self.getNomeCliente(), self.getListaProdutos(), self.calculaValor())
        return text

    def getNroNF(self):
        return self.__nroNF

    def getNomeCliente(self):
        return self.__nomeCliente

    def getItensNF(self):
        return self.__itensNF

    def getListaProdutos(self):
        descricao = []
        itemQtd = []
        text = ''

        for item in self.getItensNF():
            descricao.append(item[0])
            itemQtd.append(item[1])

        for i in range(len(descricao)):
            text = text + '\n\n-> Item: {}\n-> Quantidade: {}\n-> Valor: R${:.2f}\n'.format(
                descricao[i].getDescricao(), itemQtd[i], descricao[i].getValor())

        return text

    def calculaValor(self):
        total = 0
        for item in self.getItensNF():
            total = total + item[0].getValor() * item[1]

        return total


class NenhumProdutoNoEstoque(Exception):
    pass


class NenhumProduto(Exception):
    pass


if __name__ == '__main__':
    random.seed(42)

    nroNF = 100

    Estoque = {}

    produtos = [
        Produto(101, 'Violão 1', 200),
        Produto(102, 'Violão 2', 110),
        Produto(103, 'Violão 3', 140),
        Produto(104, 'Violão 4', 190),
        Produto(105, 'Violão 5', 195),
        Produto(106, 'Violão 6', 100)
    ]

    for produto in produtos:
        Estoque[produto.getCodigo()] = random.randint(0, 11)

    pedidos = [
        ['Marcio', ((produtos[1], 1), (produtos[2], 2), (produtos[3], 3))],
        ['Marcinho', ((Produto(107, 'Violão X', 150), 10),
                      (produtos[2], 1))],
        ['Marcia', ((produtos[4], 4), (produtos[5], 5), (produtos[0], 6))],
    ]

    print("ESTOQUE -> %s" % Estoque)

    for pedido in pedidos:
        produtosNF = []
        for item in pedido[1]:
            itemCodigo = item[0].getCodigo()
            itemQtd = item[1]

            try:
                if itemCodigo not in Estoque:
                    raise NenhumProduto()
                if itemQtd > Estoque[itemCodigo]:
                    raise NenhumProdutoNoEstoque()
            except NenhumProdutoNoEstoque:
                print('Produto {} não está em estoque.'.format(
                    item[0].getDescricao()))
            except NenhumProduto:
                print('Não temos {}.'.format(
                    item[0].getDescricao()))
            else:
                Estoque[itemCodigo] = Estoque[itemCodigo] - itemQtd
                produtosNF.append(item)

        if(len(produtosNF) > 0):
            nroNF = nroNF + 1
            Nfe = NotaFiscal(nroNF, pedido[0], produtosNF)
            print(Nfe)
        else:
            print(
                'Não foi criada a nota fiscal do cliente {}'.format(pedido[0]))
