print("Programa para convertir a números romanos")

try:
    na = int(input("Valor arábigo a convertir"))

    if na >0 and na <4000:

        romanos = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        valores = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        nai = na
        r = ""
        p = 0
        while na > 0:
            
            while na < valores[p]:
                p += 1
            na -= valores[p]
            r += romanos[p]   
            
        print("el número romano es", nai,"es", r)
    else:    
        print("Dato no válido")
except Exception as e:
    print("Error en la entrada de datos\n[",e,"]")
