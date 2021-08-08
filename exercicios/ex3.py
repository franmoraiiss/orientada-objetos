# Exercício 3
# Leia uma data no passado e informe em qual dia da semana
# essa data caiu

from datetime import datetime

myDate = input("Informe a data no formato (dd/mm/yyyy): ")
convertedDate = datetime.strptime(myDate, "%d/%m/%Y")

dateDayName = convertedDate.strftime("%A")

print(str(dateDayName))
