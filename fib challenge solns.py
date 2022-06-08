#Two examples of solving fibonacci, using different methods of grabbing the input - sphere isn't too picky.

#Recursive way

def fibonacci(n):
    if n < 0:
        exit()
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(input()))

#Shorter way

import sys

def fibonacci(nth):
    fib_sequence = []
    a, b = 0, 1
    for z in range(nth):
        a, b = b, a + b
        fib_sequence.append(a)
    return fib_sequence[-1]


fibs = []
for nterm in sys.stdin:
    if nterm == "\n":
        break
    else:
        print(fibonacci(int(nterm)))