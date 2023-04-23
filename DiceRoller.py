from PyQt5 import QtCore, QtGui, QtWidgets
import random
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QLineEdit, QLabel, QCheckBox, QDockWidget, QMainWindow
import sys
from PyQt5.QtCore import Qt


def dieRoll(numSides, numRolls, mod):
    total = 0
    for i in range(numRolls):
        total += random.randint(1, numSides)
    total += mod
    return total


def makeDie(input):
    if (input.find('+') != -1):
        sides = int(input[input.find('d')+1:input.find('+')])
        rolls = int(input[0:input.find('d')])
        mod = int(input[input.find('+')+1:len(input)])
    elif (input.find('-') != -1):
        sides = int(input[input.find('d')+1:input.find('-')])
        rolls = int(input[0:input.find('d')])
        mod = -int(input[input.find('-')+1])
    else:
        sides = int(input[input.find('d')+1:])
        rolls = int(input[0:input.find('d')])
        mod = 0
    return dieRoll(sides, rolls, mod)


def makeDieAdv(input):
    return max(makeDie(input), makeDie(input))


def makeDieDis(input):
    return min(makeDie(input), makeDie(input))


def rollDice():
    if advantage.isChecked():
        QMessageBox.about(window, 'Result', str(makeDieAdv(input.text())))
    elif disadvantage.isChecked():
        QMessageBox.about(window, 'Result', str(makeDieDis(input.text())))
    else:
        QMessageBox.about(window, 'Result', str(makeDie(input.text())))


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Dice Roller')
window.setGeometry(100, 100, 100, 200)
window.move(60, 15)


widget = QDockWidget(window)
widget.move(10, 10)

window.addDockWidget(Qt.LeftDockWidgetArea, widget)


input = QLineEdit(widget)
input.move(10, 40)


button = QPushButton('Roll', widget)
button.move(10, 70)

button.clicked.connect(rollDice)

advantage = QCheckBox('Advantage', widget)
advantage.move(10, 100)

disadvantage = QCheckBox('Disadvantage', widget)
disadvantage.move(10, 130)


window.show()
if __name__ == '__main__':
    # print(makeDie('2d6+3'))
    sys.exit(app.exec_())
