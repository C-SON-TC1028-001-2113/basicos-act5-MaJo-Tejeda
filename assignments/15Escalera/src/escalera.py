import math
def main():
    #escribe tu código abajo de esta línea
h = float(input('Altura de la casa: '))
a = int(input('Angulo en grados: ')) 

largo = h / math.sin(a) 

print('Largo de la escalera: ' + str(largo))
    
if __name__ == '__main__':
    main()
