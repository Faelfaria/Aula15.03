lista_com_duplicatas = [1, 2, 3, 4, 2, 5, 6, 7, 8, 5, 9]

lista_sem_duplicatas = []

while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0)
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
        
        print('A lista sem duplicatas é:', lista_sem_duplicatas)