minha_lista = [17, 8, 10, 6, 2, 4]
trocado = True

while trocado #usou o while e o true kkkkk loucura o for dentro do while
    trocado = False
    for i in range(len(minha_lista)) -1):
        if minha_lista[i]> minha_lista[i + 1]:
            trocado = True #ocorreu uma troca
            minha_lista[i], minha_lista[i + 1] = minha_lista[i + 1], minha_lista[1]
print(minha_lista)
    #Se for maior troca e assim vai 
