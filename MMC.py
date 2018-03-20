varY=int(input('Digite um numero: '))
varX=int(input('Digite mais um numero: '))
varZ=int(input('Digite o ultimo numero: '))

if varY>varX:
    if varY>varZ:
        maior=varY
    else:
        maior=varZ
else:
    maior=varX
while True:
    if maior % varY==0 and maior % varX==0 and maior % varZ==0:
        print(maior)
        break
    else:
        maior+=1
