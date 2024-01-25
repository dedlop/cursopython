"""
Iterável -> str, rangem etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue seu próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto:
texto = 'Luiz' # iterável
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break