import func as fn
op= 0
while op !=4:
    print("1.Calcular IVA.")
    print("2.Aplicar descuento.")
    print("3.Calcular IMC.")
    print("4.Salir.")
    try:
        op= int(input("ingrese una opcion: "))
        if op>0 and op <5:
            if op==1:
                print("Calculo de iva")
                fn.iva()
            elif op==2:
                print("Aplicar descuento")
                fn.dsc()

            elif op==3:
                print("Calcular IMC")
                fn.indice()
            else:
                print("Has salido del programa con exito")
                break
        else:
            print("#"*30)
            print("ERROR:ingrese una opcion valida!!!!")
    except:
        print("ERROR:ingrese un valor numerico!!!")
