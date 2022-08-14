ano = int(input("Digite o ano de interesse: "))
import calendar

if calendar.isleap(ano):
    print("o ano é bissexto")
else:
    print("o ano não é bissexto")
