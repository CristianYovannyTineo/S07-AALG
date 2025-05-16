
# Pida el peso maximo m que pueda llevar una mochila, luego dadas las cajas indicadas, que sus atributos son peso y soles,
#  debe hacer un metodo voraz para elegir las de menor peso con mayor valor.
#  Son cajas Unicas. Puede llevar fracciones de cajas Indicar que cajas se seleccionaron. El peso total y los soles totales.

def selecciondecajas(pesomax, cajas):
    
    valor = [c[2] / c[1] for c in cajas]

    n = len(cajas)
    for i in range(n):
        for j in range(i + 1, n):
            if valor[j] > valor[i]:
                cajas[i], cajas[j] = cajas[j], cajas[i]
                valor[i], valor[j] = valor[j], valor[i]

    pstotal = 0
    solestotales = 0
    
    print("----------------------------------------------")
    print("Cajas seleccionadas: ")
    print("----------------------------------------------")

    for num in range(n):
        nombre, peso, soles = cajas[num]
        if pesomax >= peso:
           
            print("Caja", nombre, "completa -", peso, "kg - S/", soles)
            pstotal = pstotal + peso
            solestotales = solestotales + soles
            pesomax = pesomax - peso
        else:
           
            fraccion = pesomax / peso
            pesoCargado = pesomax
            valorCargado = soles * fraccion
            print("Caja", nombre, "fracción", round(fraccion,2), "-",
                   round(pesoCargado,2), "kg - S/", round(valorCargado,2))
            pstotal = pstotal + pesoCargado
            solestotales = solestotales + valorCargado
            break

    print("-----------------------------------------------")
    print("Peso total cargado:", round(pstotal,2), "kg")
    print("Total de Soles: S/", round(solestotales,2))
    print("-----------------------------------------------")

cajas_Unicas = [["A", 10, 4],["B", 4, 3],["C", 7, 3],["D", 5, 2],
                     ["E", 3, 1],["F", 3, 2],["G", 2, 1.8],["H", 3, 3]]

print("******************************************")
pesomax = float(input("Ingrese el peso máximo de la mochila (kg): "))
selecciondecajas(pesomax, cajas_Unicas)


