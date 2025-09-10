import math
from collections import Counter


def calcular_media(lista):
    return sum(lista) / len(lista)


def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]


def calcular_moda(lista):
    contagem = Counter(lista)
    moda = contagem.most_common(1)[0][0]
    return moda


def calcular_desvio_padrao(lista):
    media = calcular_media(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)


def calcular_distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def main():
    print("Escolha a operação:")
    print("1 - Média")
    print("2 - Mediana")
    print("3 - Moda")
    print("4 - Desvio Padrão")
    print("5 - Distância entre dois pontos")

    opcao = input("Digite o número da opção desejada: ")

    if opcao in ['1', '2', '3', '4']:
        lista = input("Digite os números separados por espaço: ")
        numeros = list(map(float, lista.split()))

        if opcao == '1':
            print("Média:", calcular_media(numeros))
        elif opcao == '2':
            print("Mediana:", calcular_mediana(numeros))
        elif opcao == '3':
            print("Moda:", calcular_moda(numeros))
        elif opcao == '4':
            print("Desvio Padrão:", calcular_desvio_padrao(numeros))
    elif opcao == '5':
        p1 = input("Digite as coordenadas do primeiro ponto (x1 y1): ")
        p2 = input("Digite as coordenadas do segundo ponto (x2 y2): ")
        ponto1 = tuple(map(float, p1.split()))
        ponto2 = tuple(map(float, p2.split()))
        print("Distância entre os pontos:", calcular_distancia(ponto1, ponto2))
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
