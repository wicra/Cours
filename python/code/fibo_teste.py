import fibo
print(fibo.fib(1000))
# affiche 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print(fibo.fib2(100))
# renvoie [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

from fibo import fib, fib2
print(fib(1000))
# affiche 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print(fib2(100))
# renvoie [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def dit_bonjour(nom: str) -> str:
    return 'Bonjour ' + nom