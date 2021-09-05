
print("inicio el programa")
#secuencia fibonacci    
def fibonacci(n):
        n = int(input("introduzca el número de la serie fibonacci hasta donde desea llegar   "))
        a = 0
        b = 1
        print(a)
        print(b)
        if n == 1:
            print(a) 
        for i in range (2, n):
            c = a + b    
            a = b
            b = c
            print( c)
fibonacci (1)
# numero par o impar
num = int(input("\n" """por favor ingrese un número y entero  """ "\n"))
residuo = num % 2
if residuo == 0:
    print("el número", num,  "es par" "\n")
else:
    print("el número",  num,  "es impar" "\n")
#numero mayor    
print("por favor ingrese 3 numeros, de uno en uno" "\n")    
num_N_1 = int(input("ingrese el primer número   "))    
num_N_2 = int(input("ingrese el segundo número  "))
num_N_3 = int(input("ingrese el tercer número   "))
if num_N_3 > num_N_2 and num_N_3 > num_N_1:
    print ("el numero mayor es", num_N_3, "\n")

elif num_N_1 > num_N_2 and num_N_1 > num_N_3:
    print("el numero mayor es",  num_N_1, "\n" )    
else:
    print("el mayor es", num_N_2, "\n")
    
print("desea terminar el programa" "\n")

#condicional para salir
while True:
    n= 0
    
    try:
        n = int(input("para salir marque 0  " "\n"))
        if n > 0:
            print("\n","ingrese 0 para salir")
        else:
            ("exit")
            break
    except TypeError:
        print()
    except ValueError:
        print()
    except NameError:
        print()        