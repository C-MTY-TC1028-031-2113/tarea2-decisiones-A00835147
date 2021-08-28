def main():
    a=float(input("Peso en kg: "))
    b=float(input("Altura en m: "))
    
    if a>0 and b>0:
        imc=a/b**2
        if imc<20:
            print("PESO BAJO")
        elif imc>=20 and imc<25:
            print("NORMAL")
        elif imc>=25 and imc<30:
            print("SOBREPESO")
        elif imc>=30 and imc<40:
            print("OBESIDAD")
        elif imc>=40:
            print("OBESIDAD MORBIDA")
    
    else:
        print("Revisa tus datos, alguno de ellos es erróneo")
    
    
main()