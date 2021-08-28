def main():
    edad=int(input("Dime tu edad: "))
    
    if edad>=18:
        iD=str(input("¿Tienes identificación oficial? (s/n): "))
        if iD=="s":
            print("Trámite de licencia concedido")
        elif iD=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta") 
    else:
        print("No cumples requisitos")
        
main()
