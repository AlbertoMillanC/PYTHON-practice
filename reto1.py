antena_a = 44600
antena_b = 51800
antena_c = 9600
antena_d = 15300
antena_e = 13900
antena_instalada= 36900

area_instalada_actual=float(input("Ingrese el area a  instalar en mts:  "))
if area_instalada_actual == 0:
        print("error en los datos")
    
    
resultado=(area_instalada_actual/antena_instalada)
resultado=(int(resultado))
    

print(f"el número a antenas a instalar es: {resultado}")





