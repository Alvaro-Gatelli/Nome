print('~'*15+'Azulejos'+15*'~')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
AP=float(input('Qual a Altura da parede em metros?: '))
LP=float(input('Qual a Largura da parede em metros?: '))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
AA=float(input("Qual a Altura do Azulejo em metros?: "))
AL=float(input('Qual a Largura do Azulejo em metros?: '))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print('São necessarios:',(AP*LP)/(AA*AL),'Azulejos')
print('~'*38)