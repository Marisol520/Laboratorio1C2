"""
Bueno, elegí hacer este programa para calcular la ganancia de productos; en este caso, me basé en las verduras. 
Lo que el programa hace como bien mencioné, es calcular la ganancia. 
Por ejemplo, si compras tomates a $2 por unidad y quieres venderlos a $10 por unidad, 
la ganancia por unidad será la diferencia entre el precio de venta y el costo de compra. 
En este caso, la ganancia por unidad sería $10 - $2 = $8. Si tienes 50 tomates en existencia y los vendes todos, 
la ganancia total sería $8 (ganancia por unidad) multiplicado por 50 (cantidad en existencia), resultando en $400 de ganancia total.

Este programa permite ingresar los valores del costo de compra, precio de venta y cantidad en existencia para calcular y mostrar la ganancia total de manera sencilla y rápida.
"""




import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton, QFormLayout

class ProfitCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculadora de Ganancias')
        layout = QVBoxLayout()

        # Crear un formulario 
        form_layout = QFormLayout()

        # Crear los widgets
        self.product_combo = QComboBox()
        self.product_combo.addItems(['Libra de frijoles', 'Tomates', 'Dolar de platanos', ' Cebollas'])

        self.cost_spinbox = QSpinBox()
        self.cost_spinbox.setPrefix('$ ')
        self.cost_spinbox.setRange(0, 1000)
        self.cost_spinbox.setValue(2)  

        self.price_spinbox = QSpinBox()
        self.price_spinbox.setPrefix('$ ')
        self.price_spinbox.setRange(0, 1000)
        self.price_spinbox.setValue(3)  

        self.quantity_spinbox = QSpinBox()
        self.quantity_spinbox.setRange(0, 1000)
        self.quantity_spinbox.setValue(100)  

        self.result_label = QLabel('Ganancia total: $0.00')

        self.calculate_button = QPushButton('Calcular Ganancia')
        self.calculate_button.clicked.connect(self.calculate_profit)

        # Añadir widget
        form_layout.addRow('Selecciona Producto:', self.product_combo)
        form_layout.addRow('Costo de compra por Unidad:', self.cost_spinbox)
        form_layout.addRow('Precio de venta por Unidad:', self.price_spinbox)
        form_layout.addRow('Cantidad en existencia:', self.quantity_spinbox)
        form_layout.addWidget(self.calculate_button)
        form_layout.addWidget(self.result_label)

        layout.addLayout(form_layout)
        self.setLayout(layout)

    def calculate_profit(self):
        # Obtener los valores ingresados
        cost_per_unit = self.cost_spinbox.value()
        price_per_unit = self.price_spinbox.value()
        quantity = self.quantity_spinbox.value()

        # Calcular la ganancia
        profit_per_unit = price_per_unit - cost_per_unit

        # Calcular la ganancia total 
        total_profit = profit_per_unit * quantity

        # Mostrar la ganancia
        self.result_label.setText(f'Ganancia Total: ${total_profit:.2f}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProfitCalculator()
    ex.show()
    sys.exit(app.exec_())
