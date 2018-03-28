print('~'*20+'Conversão de dolar'+15*'~')

#│=Dinheiro para ser transformado em dolar ou vice-versa
#↓
dinheiro=float(input("Digite quanto dinheiro você quer converter em doalres: "))

#~~~~~│=Dinheiro em reais vai para dinheiro em dolar
#     ↓
print('De:',dinheiro,'R$ Para:',dinheiro/100*33,'$')

#│pergunta se você quer transformar seus dolares em reais novamente
#↓
pergunta=input('Quer re-converter o dolar para real?s/n: ')

#│=Se a resposta da pergunta for sim então o programa vai re-converter de dolar para real
#↓
if pergunta == 's':
    print('De:',dinheiro/100*33,'$ Para:',dinheiro)
else:
    print('Seu dinheiro é de:',dinheiro/100*33)
print('~'*53)
