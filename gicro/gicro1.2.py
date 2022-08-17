
from PyQt5.QtWidgets import QApplication, QLabel
app = QApplication([])

nomeFile = input("nome file: ")
contenutoFile = input("scrivi qui: ")

file = open(nomeFile, "w")
file.write(contenutoFile)
file.close()

label = QLabel(contenutoFile)
label.show()
app.exec()