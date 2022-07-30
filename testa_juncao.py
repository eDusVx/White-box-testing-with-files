"""Testes de caminho da junção de arquivos"""
import juncao


def teste_caminho_1():
    """testanto caminho ABCED onde os 2 arquivos estão vazios"""
    arquivo1 = []
    arquivo2 = []
    with open('1.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo1:
            file1.write(f'{item}\n')
    with open('2.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo2:
            file1.write(f'{item}\n')
    juncao.juntar()
    with open('3.txt', 'r', encoding="utf-8") as file3:
        assert file3.read().splitlines() == []


def teste_caminho_2():
    """testanto caminho ABCEFGD onde o primeiro arquivo tem 1 linha e o segundo está vazio"""
    arquivo1 = ['1']
    arquivo2 = []
    with open('1.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo1:
            file1.write(f'{item}\n')
    with open('2.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo2:
            file1.write(f'{item}\n')
    juncao.juntar()
    with open('3.txt', 'r', encoding="utf-8") as file3:
        assert file3.read().splitlines() == ['1']


def teste_caminho_3():
    """testanto caminho ABCEFID onde o primeiro arquivo está vazio e o segundo tem 1 linha"""
    arquivo1 = []
    arquivo2 = ['1']
    with open('1.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo1:
            file1.write(f'{item}\n')
    with open('2.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo2:
            file1.write(f'{item}\n')
    juncao.juntar()
    with open('3.txt', 'r', encoding="utf-8") as file3:
        assert file3.read().splitlines() == ['1']


def teste_caminho_4():
    """testanto caminho ABCEFHD onde os dois arquivos tem 1 linha e registros iguais"""
    arquivo1 = ['1']
    arquivo2 = ['1']
    with open('1.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo1:
            file1.write(f'{item}\n')
    with open('2.txt', 'w', encoding="utf-8") as file1:
        for item in arquivo2:
            file1.write(f'{item}\n')
    juncao.juntar()
    with open('3.txt', 'r', encoding="utf-8") as file3:
        assert file3.read().splitlines() == ['1','1']
