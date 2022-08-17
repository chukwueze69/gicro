from time import sleep


print("benvenuto in gicro v1")

print("ora digita il nome del file")

nomeFile = input("nome file: ")

print("ora digita il contenuto del file")

contenutoFile = input("scrivi qui: ")

file = open(nomeFile, "w")
file.write(contenutoFile)
file.close()

