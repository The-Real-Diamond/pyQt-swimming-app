import sys
import sqlite3
from barcode import Code128
from barcode.writer import ImageWriter
import random
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtPrintSupport import QPrintDialog , QPrinter
from PySide6.QtGui import QPixmap , QIntValidator , QIcon
from qt_material import apply_stylesheet
from ui_widget2 import Ui_MainWindow

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        Id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        phone_number TEXT NOT NULL,
        sessionsNumber INTEGER NOT NULL,
        GroupType TEXT NOT NULL,
        parentName TEXT NOT NULL,
        path TEXT NOT NULL
    )
''')


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.ach_btn.clicked.connect(self.add_achivment)
        self.ui.img_btn.clicked.connect(self.add_image)
        self.ui.save_db.clicked.connect(self.bar)
        self.ui.page1.clicked.connect(lambda:self.ui.stacked.setCurrentIndex(1))
        self.ui.page2.clicked.connect(lambda:self.ui.stacked.setCurrentIndex(0))
        self.ui.Search.clicked.connect(self.track)
        self.ui.reNew.clicked.connect(self.renew)
        self.ui.print.clicked.connect(self.print)
        self.v = QIntValidator(self.ui.age_in)
        self.v.setTop(100)
        self.v.setBottom(0)
        self.ui.age_in.setValidator(self.v)
        
        

        self.setWindowTitle("Nasser Swimming")
        self.setWindowIcon(QIcon('logo.jpg'))
    def add_achivment(self):
        text = self.ui.ach_in.text()
        self.ui.list_viwe.addItem(text)
        self.ui.ach_in.clear()
    
    def add_image(self):
        global fname
        fname= QFileDialog.getOpenFileName(self, 'openfile' , 'C:\\backup\\swimming' , 'All Files (*)')
        self.pixmap = QPixmap(fname[0])
        self.ui.img_labl.setPixmap(self.pixmap.scaledToWidth(self.ui.img_labl.width()))
    def track(self):
        id = self.ui.code.text()
        cursor.execute("SELECT sessionsNumber FROM data WHERE id=?", (id,))
        q= cursor.fetchone()
        if q:
            cursor.execute("UPDATE data SET sessionsNumber =? WHERE ID = ?;" , (q[0] -1 , id,))
            conn.commit()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Not Found")
            dlg.setText("رقم المسلسل غير وجود")
            dlg.exec()
        
        cursor.execute("SELECT * FROM data WHERE id=?", (id,))
        result = cursor.fetchone()
        if result:
            self.ui.name_out.setText(result[1])
            self.ui.age_out.setText(str(result[2]))
            self.ui.phone_out.setText(result[3])
            self.ui.session_out.setText(str(result[4]))
            self.ui.group_out.setText(result[5])
            self.ui.parent_out.setText(result[6])
            self.ui.img_out.setPixmap(QPixmap(result[7]).scaledToHeight(self.ui.img_out.height()))
            if result[4]<=0:
                self.ui.status_lable_3.setStyleSheet('color:red;')
                self.ui.status_lable_3.setText('منتهي')
            else:
                self.ui.status_lable_3.setStyleSheet('color:green;')
                self.ui.status_lable_3.setText('مستمر')


    def bar(self):
        b = random.randint(0,1000000)
        code = Code128(f"{b}", writer=ImageWriter())
        code.save(f"{self.ui.Name_in.text()}")
        self.ui.bar_img.setPixmap(QPixmap(f"{self.ui.Name_in.text()}"))
        Id=b
        name=self.ui.Name_in.text()
        age = self.ui.age_in.text()
        phone= self.ui.phone_in.text()
        sessions = self.ui.sessions_in.text()
        group = self.ui.Group_in.text()
        parent = self.ui.parent_in.text()
        path = fname[0]

        self.ui.print.setVisible(True)

        cursor.execute("INSERT INTO data (Id, name, age, phone_number, sessionsNumber, GroupType, parentName, path) VALUES (?,?,?,?,?,?,?,?)", (Id,name, age, phone, sessions, group , parent ,path))
        conn.commit()
        name=self.ui.Name_in.setText('')
        age = self.ui.age_in.setText('')
        phone= self.ui.phone_in.setText('')
        sessions = self.ui.sessions_in.setText('')
        group = self.ui.Group_in.setText('')
        parent = self.ui.parent_in.setText('')
    def renew(self):
        id = self.ui.code.text()
        if id:
            cursor.execute("UPDATE data SET sessionsNumber =? WHERE ID = ?;" , (8 , id,))
            conn.commit()
            self.ui.session_out.setText('8')
            self.ui.status_lable_3.setStyleSheet('color:green;')
            self.ui.status_lable_3.setText('مستمر')
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Not Found")
            dlg.setText("رقم المسلسل غير وجود")
            dlg.exec()

    def print(self):
        printer = QPrinter()
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.ui.img_labl.print_(printer)




        


        



extra = {


    # Font
    'font_family': 'Dubai Medium',
    'font_size': '20px',
    'font_weigt': '700',
    'line_height':'13px',
}

app = QApplication(sys.argv)
w= MainWindow()
apply_stylesheet(app, theme='light_blue.xml' , invert_secondary=True, extra=extra)
w.show()
app.exec()