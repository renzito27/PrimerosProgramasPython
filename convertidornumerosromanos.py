print("Programa para convertir a números romanos")

na = int(input("Valor arábigo a convertir"))

if na >0 and na < 4000:

    r = ""

    while na > 0:
        if na >= 1000:
            na -= 1000
            r += "M"
        elif na >= 900:
            na -= 900
            r += "CM"
        elif na >= 500:
            na -= 500
            r += "D"
        elif na >= 400:
            na -= 400
            r += "CD"
        elif na >= 100:
            na -= 100
            r += "C"
        elif na >= 90:
            na -= 90
            r += "XC"
        elif na >= 50:
            na -= 50
            r += "L"
        elif na >= 40:
            na -= 40
            r += "XL"
        elif na >= 10:
            na -= 10
            r += "X"
        elif na >= 9:
            na -= 9
            r += "IX"    
        elif na >= 5:
            na -= 5
            r += "V"
        elif na >= 4:
            na -= 4
            r += "IV"    
        else: 
            na -= 1
            r += "I"    
            
    print("el número romano es" , r)
else:    
    print("Dato no válido")
