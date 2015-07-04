from PyQt4.QtGui import *
from PyQt4.QtCore import *
from bmi_gui import Ui_MainWindow

class MyMainGui(QMainWindow, Ui_MainWindow):

    # extend constructors of QMainWindow and Ui_mainWindow
    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)

        app.setStyle(QStyleFactory.create('Plastique'))

        self.pushButton_cal_bmi_kg_m.clicked.connect(self.calculate_bmi_metric_system)
        self.pushButton_cal_bmi_lb_ft.clicked.connect(self.calculate_bmi_imperial_system)

    def calculate_bmi_metric_system(self):
        """Calculate BMI in Metric system"""

        weight_str = self.lineEdit_weight_in_kg.text()
        height_str = self.lineEdit_height_in_m.text()

        if weight_str =='' or height_str == '':
            return
        else:
            try:
                weight_in_kg = float(weight_str)
                height_in_m = float(height_str)
            except:
                # Display an error if input is invalid
                QMessageBox.warning(self, 'Error!', 'Inputs must be valid numbers.')
                return

            bmi = weight_in_kg/(height_in_m ** 2)
            bmi = '{0:.2f}'.format(bmi)
            self.lineEdit_bmi_meteric.setText(bmi)

    def calculate_bmi_imperial_system(self):
        """Calculates BMI in Imperial system"""

        weight_str = self.lineEdit_weight_in_lb.text()
        height_str = self.lineEdit_height_in_inches.text()

        if weight_str =='' or height_str == '':
            return
        else:
            try:
                weight_in_lb = float(weight_str)
                height_in_ft = float(height_str)
            except:
                QMessageBox.warning(self, 'Error!', 'Inputs must be valid numbers.')
                return

            bmi = (weight_in_lb * 703)/(height_in_ft ** 2)
            bmi = '{0:.2f}'.format(bmi)
            self.lineEdit_bmi_imperial.setText(bmi)


if __name__ == "__main__":
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())