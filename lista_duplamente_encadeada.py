"""Finalidade: Sistema demostrando Lista Duplamente Encadeada.
Autor: AMANDA QUEIROZ - Matrícula: 029998000ADS000111
Autor: CLEBER BATISTA RIBEIRO - Matrícula: 029998000ADS000109
Autor: DIOGO DA SILVEIRA RIBEIRO - Matrícula: 029998000ADS000076
]Autor: MARIANE DANTAS CARDOSO - Matrícula: 029998000ADS000087
data: 10/12/2023
Versão: 0.1
Python versão: 3.10.12
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/ProjetoListaDplEncadeada
"""


def len_titulo(titulo):
    """Função para mostrar o título através da função."""
    return len(titulo)


def linha_titulo(titulo):
    """Criação de linha para formar titulo"""
    __nun_letras__ = len_titulo(titulo)
    print("*" * __nun_letras__)


def titulo_sistema(tmsg):
    """Função para mostrar o título através da função."""
    linha_titulo(tmsg)
    print(f"\n{tmsg}\n")
    linha_titulo(tmsg)


class No:
    """Classe que representa um nó em uma lista duplamente encadeada."""

    def __init__(self, novo_valor):
        """Inicializa um nó com um valor e ponteiros nulos para os
        nós anterior e próximo."""
        self.novo_valor = novo_valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        """Imprime o valor do nó."""
        print(self.novo_valor)


class ListaDuplamenteEncadeada:
    """Classe que representa uma lista duplamente encadeada."""

    def __init__(self):
        """Inicializa uma lista duplamente encadeada com ponteiros
        nulos para o primeiro e último nós."""
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia__(self):
        """Retorna True se a lista estiver vazia, False caso contrário."""
        return self.primeiro is None

    def inseri_inicio(self, new_valor):
        """
        Insere um novo nó no início da lista.

        Args:
            valor: O valor a ser inserido no novo nó.
        """
        novo = No(new_valor)
        if self.__lista_vazia__():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar_inicio(self):
        """
        Imprime todos os nós da lista, começando pelo primeiro.
        Se a lista estiver vazia, imprime uma mensagem indicando isso.
        """
        if self.__lista_vazia__():
            print("Lista está vazia!")
            return
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo


lista = ListaDuplamenteEncadeada()
titulo_sistema("Sistema demostrando Lista Duplamente Encadeada.")
while True:
    valor = input("\nInsira um número para a lista (ou 'sair' para parar): ")
    if valor.lower() == "sair":
        break
    elif valor == "":
        print("Você deve inserir um valor!")
        continue
    elif not valor.isdigit():
        print("Por favor, insira apenas números ou a palavra 'sair'.")
        continue
    lista.inseri_inicio(int(valor))

print("\nOs valores inseridos na lista são:\n")
lista.mostrar_inicio()
