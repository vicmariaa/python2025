import random

participantes = ["Carlos", "Ana", "Pedro", "Beatriz"]
participantes.sort()
print("participantes ordenados", participantes)

participantes = ["Carlos", "Ana", "Pedro", "Beatriz"]
participantes.sort(reverse=True)
print("participantes ordenados", participantes)

horarios = ["15:00", "09:00", "12:00", "18:00"]
hor_ordenado = sorted(horarios)
print("Horarios ordenados", hor_ordenado)

notas = random.sample(participantes, len(participantes))
print("Participantes sorteados", notas)

notas = random.sample(horarios, len(horarios))
print("Horarios sorteados", notas)

Livros = ["A Hipótese do Amor" , "Quarta Asa" , "Desenfrados", "Assistente do Vilão" , ]
Liv_ordenado = sorted(Livros)
print("Livros ordenados", Liv_ordenado)