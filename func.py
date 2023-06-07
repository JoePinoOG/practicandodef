def iva():
    pp=int(input("ingrese el valor del producto: "))
    iv=pp*0.19
    ci= iv+pp
    print(f"el valor total con iva incluido es ${ci}")
    print(f"el valor solo del iva es ${iv}")
def dsc():
    p=int(input("ingrese el valor del producto: "))
    vdsc=int(input("ingrese el descuento a aplicar: "))
    dc=p*(vdsc/100)
    totdsc= p-dc
    print(f"el valor total con descuento aplicado es de${totdsc} ")
    print(f"el descuento es de ${dc} menos")
def indice():
    peso=int(input("ingrese su peso en kg:"))
    altura=float(input("ingrese su altura en metros: "))
    imc=peso/(altura*altura)
    
    print(f"su imc es {imc}")
    estado(imc)
def estado(imc):
    if imc< 18.5:
        print("bajo peso")
    elif 18.5< imc <24.9:
        print("Adecuado")
    elif 25< imc < 29.9:
         print("sobrepeso")
    elif 30< imc < 34.9:
         print("obesidad grado 1")
    elif 35 < imc < 39.9:
         print("obesidad grado 2")
    elif imc> 40:
         print("obesidad grado 2")