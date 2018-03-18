print('~'*10+'Palindromos'+'~'*10)
minha_string=input('Digite uma palavra: ')

print('~'*22)

if minha_string==minha_string[::-1]:
    print(minha_string+' É um palindromo')
else:
    print(minha_string+' Não é um palindromo')
print('~'*22)
