print('~'*20+'Conversão de dolar'+15*'~')

#│=Dinheiro para ser transformado de real para dolar
#↓
dinheiro=float(input("Digite quanto dinheiro você quer converter em doalres: "))

print('De:',dinheiro,'R$ Para:',dinheiro/100*33,'$')

#│=Dinheiro para ser transformado de dolar para real
#↓
pergunta=input('Você Deseja converter de dolares para reais?s/n: ')
if pergunta == 's':
    dinheiro2=float(input('Digite uma quantia em dolares que você queira converter para reais: '))
    print('De:',dinheiro2,'$ Para:',dinheiro2/100*330)
else:
    print('Seu saldo é de:',dinheiro)

print('~'*20+'Conversão de dolar'+15*'~')