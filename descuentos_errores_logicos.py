#Construíremos un sistema que solicite 3 datos
#La edad, si cuenta con pase premiun y total compra
#El sistema solicitará la edad, si es menor de edad, no aplica descto
#si esta entre 18 y menor a 65 años y además cuenta con 
#pase premiun, con un total de compra mayor o igual a $50.000
#aplica descuento del 20%, si compra es menor a $50.000, 
#10% descuento, si no cuenta pase premiun, 5%, sino, no tiene
#descuento
#Pero si cuenta con más de 64 años, y cuenta con pase premiun,
#tiene un 30%, en caso contrario, un 25% de descuento. 
 
 
try:
    edad = int(input("Ingrese su edad:"))
    pasePremiun = input("¿Tiene pase? (si/no)").lower()
    compra = float(input("Ingrese total de compra:"))
    if edad < 18 and edad > 100:
        print("No aplica descuento o compras por límites de edad")
    elif edad >= 18 and edad < 65:
        if pasePremiun == "si":
            if compra >= 50000:
                print("Descuento aplicado al 20%")
            else:
                print("Descuento aplicado al 10%")
        else:
            if compra < 50000:
                print("Descuento aplicado al 5%")
            else:
                print("No tiene descuento")
    elif edad > 64:
        if pasePremiun == "si":
            print("Descuento aplicado al 30%")
        else:
            print("Descuento aplicado al 25%")
except ValueError:
    print("Error, ingreso un valor incorrecto")
except TypeError:
    print("Error, ingreso un tipo de dato incorrecto")
except Exception:
    print("Error, hay un error desconocido")