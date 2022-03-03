from regra import funcao
import os

texto = None
arquivo_alterado = None

while True:
    os.system('cls')
    texto = funcao.abrirArquivo()
    funcao.mostrarArquivo(texto)

    print('1 - modificar o arquivo')
    print('2 - selecionar outro arquivo')
    opcao = str(input('selecione uma opção: '))

    if opcao == '1':
        os.system('cls')
        break
    elif opcao == '2':
        continue

while True:
    os.system('cls')
    ramal = funcao.validarStr('insira o ramal: ')
    senha = funcao.validarStr('insira a senha: ')
    arquivo_alterado = funcao.alterar(texto, ramal, senha)
    funcao.mostrarArquivo(arquivo_alterado) 

    print('1 - arquivo alterado corretamente')
    print('2 - modificar novamente')
    opcao = str(input('selecione uma opção: '))

    if opcao == '1':
        os.system('cls')
        break
    elif opcao == '2':
        continue




    
        