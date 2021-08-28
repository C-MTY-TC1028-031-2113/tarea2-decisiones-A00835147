def main():
    a=int(input("Ingresa el primer número: "))
    b=int(input("Ingresa el segundo número: "))
    c=int(input("Ingresa el tercer número: "))
    
    if a>b:
        if b<c:
            if a>c:
                print(b)
                print(c)
                print(a)
            else:
                print(b)
                print(a)
                print(c)
        else:
            print(c)
            print(b)
            print(a)
    else:
        if a<c:
            if c>b:
                print(a)
                print(b)
                print(c)
            else:
                print(a)
                print(c)
                print(b)
        else:
            print(c)
            print(a)
            print(b)
            
main()
