import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox, QDialog, QLineEdit,
    QListView, QTableView, QTreeView, QListWidget, QTableWidget,
    QTreeWidget, QTreeWidgetItem, QTableWidgetItem, QDataWidgetMapper
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QModelIndex

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Demo Completo de Widgets y Modelos")
        self.setGeometry(100, 100, 1000, 700)
        
        # --- 1. CONFIGURACIÓN DEL MODELO PARA VISTAS (List View, Table View, Tree View) ---
        self.table_model = QStandardItemModel(4, 2)
        self.table_model.setHorizontalHeaderLabels(["ID", "Artículo"])
        for i, item in enumerate(["Manzana", "Pera", "Naranja", "Uva"]):
            self.table_model.setItem(i, 0, QStandardItem(str(i + 1)))
            self.table_model.setItem(i, 1, QStandardItem(item))
            
        self.list_model = QStandardItemModel(self.table_model.rowCount(), 1)
        for row in range(self.table_model.rowCount()):
            self.list_model.setItem(row, 0, self.table_model.item(row, 1).clone())


        # ----------------------------------------------------
        # 2. CREACIÓN DE WIDGETS Y VISTAS
        # ----------------------------------------------------
        
        # WIDGETS DE EDICIÓN Y DATA EDIT
        self.edit_label = QLabel("Editar Artículo (Data Edit):")
        self.edit_field = QLineEdit()
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.table_model)
        # Mapea el campo de edición a la columna 1 (Artículo)
        self.mapper.addMapping(self.edit_field, 1)
        self.mapper.setCurrentIndex(0) # Muestra la primera fila
        
        # PUSH BUTTON & MANEJO DE EVENTOS
        self.alert_button = QPushButton("Mostrar Aviso (QMessageBox)")
        self.alert_button.clicked.connect(self.show_message_box)
        
        self.dialog_button = QPushButton("Mostrar Diálogo (QDialog)")
        self.dialog_button.clicked.connect(self.show_custom_dialog)

        # LIST WIDGET
        self.list_widget = QListWidget()
        self.list_widget.addItem("Elemento A")
        self.list_widget.addItem("Elemento B")
        self.list_widget.itemClicked.connect(self.handle_widget_event)
        
        # TREE WIDGET
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(1)
        self.tree_widget.setHeaderLabels(["Carpetas"])
        parent = QTreeWidgetItem(self.tree_widget, ["Raíz"])
        QTreeWidgetItem(parent, ["Sub Carpeta 1"])
        QTreeWidgetItem(parent, ["Sub Carpeta 2"])
        
        # TABLE WIDGET
        self.table_widget = QTableWidget(2, 3) # 2 filas, 3 columnas
        self.table_widget.setHorizontalHeaderLabels(["Col 1", "Col 2", "Col 3"])
        self.table_widget.setItem(0, 0, QTableWidgetItem("Dato 1"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Dato 2"))

        # VISTAS MODEL/VIEW
        self.list_view = QListView()
        self.list_view.setModel(self.list_model)
        
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.table_model) # Usamos el mismo modelo para simplicidad

        # ----------------------------------------------------
        # 3. DISEÑO DE LAYOUT
        # ----------------------------------------------------
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        
        # Zona de Control (Buttons y Data Edit)
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.edit_label)
        control_layout.addWidget(self.edit_field)
        control_layout.addWidget(self.alert_button)
        control_layout.addWidget(self.dialog_button)
        
        main_layout.addLayout(control_layout)
        
        # Contenedor para Widgets
        widgets_label = QLabel("--- Widgets (List, Table, Tree) y Data Edit ---")
        widgets_container = QHBoxLayout()
        widgets_container.addWidget(self.list_widget)
        widgets_container.addWidget(self.table_widget)
        widgets_container.addWidget(self.tree_widget)
        
        main_layout.addWidget(widgets_label)
        main_layout.addLayout(widgets_container)
        
        # Contenedor para Vistas (Model/View)
        views_label = QLabel("--- Vistas (List View, Table View, Tree View) ---")
        views_container = QHBoxLayout()
        views_container.addWidget(self.list_view)
        views_container.addWidget(self.table_view)
        views_container.addWidget(self.tree_view)
        
        main_layout.addWidget(views_label)
        main_layout.addLayout(views_container)
        
        self.setCentralWidget(main_widget)

    # ----------------------------------------------------
    # 4. MANEJO DE EVENTOS
    # ----------------------------------------------------
    
    def show_message_box(self):
        """Manejo de eventos con QMessageBox (Ventana de Aviso Simple)."""
        QMessageBox.information(
            self,
            "Aviso de Evento",
            "Has pulsado el botón. Este es un QMessageBox."
        )

    def show_custom_dialog(self):
        """Manejo de eventos con QDialog (Ventana de Aviso Personalizada)."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Diálogo Personalizado")
        dialog.setGeometry(200, 200, 300, 100)
        
        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel("¡Hola! Esta es una ventana QDialog."))
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(ok_button)
        
        dialog.exec_()
        
    def handle_widget_event(self, item):
        """Manejo de eventos para el List Widget."""
        QMessageBox.warning(
            self,
            "Evento de Widget",
            f"Has seleccionado el elemento: {item.text()}"
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())