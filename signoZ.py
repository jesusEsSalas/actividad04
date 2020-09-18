signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis",
        "Cáncer","Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
fechas = [20, 19, 20, 20, 21, 20, 21, 23, 21, 21, 21, 21]

dia = int(input("Dia de nacimiento: "))
mes = int(input("Mes de nacimiento: "))

mes = mes - 1
if dia > fechas[mes]:
    mes += 1
if mes == 12:
     mes = 0
print("Tu signo es: ", signo[mes])