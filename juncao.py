"""Programa que realiza a junção de dois arquivos com numeros em uma sequência ordenada"""


def juntar():
    """Função que realiza a junção dos arquivos"""
    with open('1.txt', 'r', encoding="utf-8") as file1, \
            open('2.txt', 'r', encoding="utf-8") as file2, \
            open('3.txt', 'w', encoding="utf-8") as file3:  # Abrindo arquivos
        file1 = file1.readlines()
        file2 = file2.readlines()
        i = 0
        while len(file1) != 0 and len(file2) != 0:
            if int(file1[i]) < int(file2[i]):  # Caso registro A < registro B
                file3.write(file1[i])
                del file1[i]
            elif int(file1[i]) == int(file2[i]):  # Caso registro A = registro B
                file3.write(file1[i])
                file3.write('\n')
                file3.write(file2[i])
                del file1[i]
                del file2[i]
            else:  # Caso registro A > registro B
                file3.write(file2[i])
                del file2[i]
        file3.write('\n')
        if len(file1) > len(file2):  # arquivo B vazio,todos os registros de A  sao copiados
            for j in enumerate(file1):
                file3.write(j[1])
        else:  # arquivo A vazio, todos os registros de B  sao copiados
            for j in enumerate(file2):
                file3.write(j[1])
    with open('3.txt', encoding="utf-8") as reader, open('3.txt', 'r+', encoding="utf-8") as writer:
        for line in reader:  # Retirando as linhas em branco do arquivo
            if line.strip():
                writer.write(line)
            writer.truncate()


juntar()
