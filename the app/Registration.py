from PySide6 import QtWidgets, QtCore
import sqlite3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QtWidgets.QLabel()
        self.setCentralWidget(self.label)

        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        self.search_button.setFixedSize(100, 30)
        self.statusBar().addPermanentWidget(self.search_button)

        self.id_line_edit = QtWidgets.QLineEdit()
        self.statusBar().addPermanentWidget(self.id_line_edit)

    def search(self):
        id = self.id_line_edit.text()
        data = self.get_data_from_database(id)
        if data:
            # Here's where you can modify the data before it's displayed
            modified_data = "ID: {}\nName: {}\nAge: {}".format(data[0], data[1], data[2])
            self.label.setText(modified_data)
        else:
            self.label.setText("No data found.")

    def get_data_from_database(self, id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        data = cursor.fetchone()
        conn.close()
        return data

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
