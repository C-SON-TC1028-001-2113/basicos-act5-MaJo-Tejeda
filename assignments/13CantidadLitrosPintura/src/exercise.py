import math
def main():
    #escribe tu código abajo de esta línea
a = float(input('Area a pintar en metros: '))
b = float(input('Rendimiento m2/L: '))
c = a/b 
math.ceil(c)
print(c)


if __name__ == '__main__':
    main()
