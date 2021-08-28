import math
def main():
    a=float(input("Da el valor de a: "))
    b=float(input("Da el valor de b: "))
    c=float(input("Da el valor de c: "))
    
    if a==0 and b==0:
        print("No tiene solucion")
    elif a==0 and b!=0:
        x=((-1)*(c))/b
        print(x)
    else:
        if (b**2-4*a*c)<0:
            print("Raices complejas")
        elif (b**2-4*a*c)==0:
            x=((-1)*(b))/2*a
            print(x)
        else:
            x1=((((-1)*(b))+(math.sqrt(b**2-4*a*c)))/(2*a))
            print(x1)
            x2=((((-1)*(b))-(math.sqrt(b**2-4*a*c)))/(2*a))
            print(x2)
        

main()
