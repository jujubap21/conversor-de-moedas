print('==================================\n||     CONVERSOR DE MOEDAS      ||\n==================================')

def conversao():
    print("1. Dolar \n2. Euro \n3. Libra \n4. Iene \n5. Yuan")
    moeda = int(input("------------------------------------------------\nDigite o número da moeda que deseja converter: "))
    print("------------------------------------------------")
    quantia_em_reais = float(input("Quantos reais você quer converter: "))
   

    if moeda == 1:
        valor_final = (quantia_em_reais / 4.90)
        print("Você converteu R${:.2f} para US${:.2f}".format(quantia_em_reais, valor_final))
    elif moeda == 2:
        valor_final = (quantia_em_reais / 5.35)
        print("Você converteu R${:.2f} para €{:.2f}".format(quantia_em_reais, valor_final))
    elif moeda == 3:
        valor_final = (quantia_em_reais / 6.12)
        print("Você converteu R${:.2f} para £{:.2f}".format(quantia_em_reais, valor_final))
    elif moeda == 4:
        valor_final = (quantia_em_reais / 0.033)
        print("Você converteu R${:.2f} para ¥{:.2f}".format(quantia_em_reais, valor_final))
    elif moeda == 5:
        valor_final = (quantia_em_reais / 0.68)
        print("Você converteu R${:.2f} para ¥{:.2f}".format(quantia_em_reais, valor_final))

conversao()

while True:
    converter_novamente = str(input("Desejar fazer uma nova conversão? \nDigite 'sim' ou 'não': "))

    if converter_novamente == 'sim':
        conversao()
    elif converter_novamente == 'não':
        break
    else:
        print("Digite 'sim' ou 'não'.")

