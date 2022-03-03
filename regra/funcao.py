from operator import truediv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import time
import os

arquivo = None

def abrirArquivo():

    Tk().withdraw()

    try:
        arquivo = askopenfilename(filetypes=(("Text files", "*.xml"),))
        with open(arquivo, encoding='UTF-8') as arquivo:
            return str(arquivo.read())

    except (FileNotFoundError):
        print("Nenhum arquivo selecionado")
        time.sleep(6)
        os.system('cls')


def mostrarArquivo(arquivo):
    print('---------- arquivo ----------')
    print(arquivo)
    print('-----------------------------')


def alterar(arquivo, ramal, senha):
    if arquivo is None:
        print(f'não tem nenhum arquivo para ser alterado')
    else:
        if(ramal is not None and senha is not None):
                arquivoFinal = trocarTexto(arquivo, '<featureLabel>', '</featureLabel>',
                                            ramal)
                arquivoFinal = trocarTexto(
                        arquivoFinal, '<name>', '</name>', ramal)
                arquivoFinal = trocarTexto(arquivoFinal, '<displayName>', '</displayName>',
                                            ramal)
                arquivoFinal = trocarTexto(arquivoFinal, '<authName>', '</authName>',
                                            ramal)
                arquivoFinal = trocarTexto(arquivoFinal, '<contact>', '</contact>',
                                            ramal)
                arquivoFinal = trocarTexto(arquivoFinal, '<authPassword>', '</authPassword>',
                                            senha)   
                print('alterado documento')
                time.sleep(2)
                os.system('cls')
                return arquivoFinal

def salvar(arquivo_url, texto_modificado):

    try:
        arquivo = asksaveasfile(defaultextension= '.xml').name

        with open(arquivo, mode='w', encoding="UTF-8") as xml:
            xml.write(texto_modificado)
    except(AttributeError):
        print('nem arquivo selecionado para ser salvo')

    if arquivo_url == arquivo:
        os.remove(arquivo_url)


def posicaoInicial(texto, argumento, inicioBloco=None, finalBloco=None):
    return texto.index(argumento, inicioBloco, finalBloco)


def posicaoFinal(texto, argumento, inicioBloco=None, finalBloco=None):
    return texto.index(argumento, inicioBloco, finalBloco) + len(argumento)


def textoCompleta(texto, argumentoInicial, argunmentoFinal, inicioBloco, finalBloco):
    return texto[posicaoInicial(texto, argumentoInicial, inicioBloco, finalBloco): 
    posicaoFinal(texto, argunmentoFinal, inicioBloco, finalBloco)]


def valorTexto(texto, argumentoInicial, argunmentoFinal):
    return texto[posicaoFinal(texto, argumentoInicial): 
    posicaoInicial(texto, argunmentoFinal)]


def trocarTexto(texto, argumentoInicial, argunmentoFinal, novoValor,):
    inicioBloco = posicaoInicial(texto, '<proxy>')
    finalBloco = posicaoFinal(texto, '</authPassword>')
    argumento = textoCompleta(texto, argumentoInicial, argunmentoFinal, inicioBloco, finalBloco)

    if argumento is not None:
        valor = valorTexto(argumento, argumentoInicial, argunmentoFinal)
        argumentoNovo = argumento.replace(valor, novoValor)
        return texto.replace(argumento, argumentoNovo)
        
 
def validarStr(textoInput):
    while True:
        texto = input(textoInput).strip()

        if texto == '':
                continue
        else:
            return texto