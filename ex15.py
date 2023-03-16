banda = []
print("etapa 1:", banda)

banda.append("John Lennon")
banda.append("Paul McCartney")
banda.append("George Harrison")
print("etapa 2:", banda)

for members in range(2):
    banda.append(input("Novo membro: "))
print("etapa3:" , banda)

del banda[-1]
del banda[-1]
print("etapa 4:", banda)

banda.nsert(0, "RingoStarr")
print("etapa 5:", banda)
print("The Fab: ", len(banda))