# Declaramos una variable 
calificacion = input("Introduce tu calificación de la AZ-900")

calificacion = int(calificacion)
# Preguntamos si la calificación es menor a 700
if calificacion < 700 : 
    print("veeees, por no estudiar") # Si es menor a 700, muestra esto 
elif calificacion > 1000 :
    print("MIENTES, no puedes sacar más de 1000")
else : # Si no se cumple el if anterior, pasa a esta linea 
    print("felicidades, pasa por tu certificad") # se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
    edad = input ("Introduce tu edad: ")
    edad = int (edad)

    if edad >= 18 and edad <= 100 :
        print("Bienvenido al mamitas")
    elif edad > 100 :
        print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
    elif edad < 0 :
        print("Ni que fueras viajero del tiempo")
    else : 
        print("No te puedas llevar esos cigarros")