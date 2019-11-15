import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from boltzmann_ui import Ui_MainWindow
from math import e

class boltz_teste_main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.boltz_ui = Ui_MainWindow()
        self.boltz_ui.setupUi(self)
        self.tables = QtWidgets.QTableWidget()

        #actions
        self.boltz_ui.menu_quit.triggered.connect(self.close)  # Quit from menu
        self.boltz_ui.ln_edit_nconf.returnPressed.connect(self.onpressed) #Generated tables after press enter

    def onpressed(self):
        try:
            get_nconf_int = int(self.boltz_ui.ln_edit_nconf.text())
            self.tables.resize(400, 400)
            self.tables.setRowCount(get_nconf_int + 1)   #Number of Rows
            self.tables.setColumnCount(2)            #Number of Column
            self.tables.setItem(0, 0, QtWidgets.QTableWidgetItem("Energy (KJ/mol)")) #Add a string in position 0,0
            self.tables.setItem(0, 1, QtWidgets.QTableWidgetItem("%Ci"))

            btn_table = QtWidgets.QPushButton('RUN', self.tables) #Table's button
            btn_table.move(300, 20)#position
            self.tables.show()  #show tables

            btn_table.clicked.connect(self.calcboltz)  

        except ValueError:
            csGA_QMBox = QMessageBox() 
            csGA_QMBox.setIcon(QMessageBox.Warning) 
            csGA_QMBox.setWindowTitle('Warning')
            csGA_QMBox.setText('Type a valid value.')
            csGA_QMBox.exec()

    def calcboltz(self):
        try:
            temperature_float = float(self.boltz_ui.ln_edit_temp.text())
            get_nconf_int = int(self.boltz_ui.ln_edit_nconf.text())

            beta = 1 / (temperature_float * 0.0083144621)
            #print(beta)
            denom = 0
            list_get_energy = []
            for j in range(1, get_nconf_int + 1): 
                item1 = self.tables.item(j, 0)  
                itemget = item1.text()
                list_get_energy.append(float(itemget))
                denom = denom + e**(-beta * list_get_energy[j - 1])

            for jj in range(1, get_nconf_int + 1):
                calc_boltz = (e ** (-beta * list_get_energy[jj - 1]) * 100 / denom)
                
                self.tables.setItem(jj, 1, QtWidgets.QTableWidgetItem(str(calc_boltz)))

        except AttributeError:
            csGA_QMBox = QMessageBox()
            csGA_QMBox.setIcon(QMessageBox.Warning) 
            csGA_QMBox.setWindowTitle('Warning')
            csGA_QMBox.setText('There is a blank cell.')
            csGA_QMBox.exec()

        except ValueError:
            csGA_QMBox = QMessageBox()
            csGA_QMBox.setIcon(QMessageBox.Warning) 
            csGA_QMBox.setWindowTitle('Warning')
            csGA_QMBox.setText('Type a valid value.')
            csGA_QMBox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = boltz_teste_main()
    gui.show()
    sys.exit(app.exec_())