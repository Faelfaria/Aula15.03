minha_lista = []
trocado = True
num = int(input('Quantos elementos deseja? '))

for i in range(num):
    val = float(input("Entre com o númemro: "))
    minha_lista.apped(val)
    
while trocado:
    trocado = False 
    for i in range(len(mina_lista) - 1):
        if minha_lista[i] > minha_lista[i + 1]:
            trocado = True
            minha_lista[i], minha_lista[i+1] = minha_lista[i+1], minha_lista[i]
            
print('\nOrdenando')
print(minha_lista)