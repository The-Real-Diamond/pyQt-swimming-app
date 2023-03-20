# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetMplfLx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateEdit,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName(u"Main_Window")
        Main_Window.setEnabled(True)
        Main_Window.resize(1144, 904)
        Main_Window.setAnimated(True)
        self.centralwidget = QWidget(Main_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(590, 0, 551, 901))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.status_lable = QLabel(self.frame)
        self.status_lable.setObjectName(u"status_lable")
        font = QFont()
        font.setFamilies([u"Dubai Medium"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.status_lable.setFont(font)
        self.status_lable.setStyleSheet(u"color:green")
        self.status_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.status_lable)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setToolTipDuration(-1)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setIndent(4)

        self.verticalLayout.addWidget(self.label)

        self.Name_in = QLineEdit(self.frame)
        self.Name_in.setObjectName(u"Name_in")
        font2 = QFont()
        font2.setPointSize(16)
        self.Name_in.setFont(font2)
        self.Name_in.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Name_in)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setMargin(0)
        self.label_2.setIndent(4)

        self.verticalLayout_2.addWidget(self.label_2)

        self.age_in = QLineEdit(self.frame)
        self.age_in.setObjectName(u"age_in")
        self.age_in.setMinimumSize(QSize(0, 0))
        self.age_in.setFont(font2)

        self.verticalLayout_2.addWidget(self.age_in)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setIndent(4)

        self.verticalLayout_3.addWidget(self.label_3)

        self.Group_in = QLineEdit(self.frame)
        self.Group_in.setObjectName(u"Group_in")
        self.Group_in.setFont(font2)

        self.verticalLayout_3.addWidget(self.Group_in)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setIndent(4)

        self.verticalLayout_4.addWidget(self.label_4)

        self.date_in = QDateEdit(self.frame)
        self.date_in.setObjectName(u"date_in")
        font3 = QFont()
        font3.setFamilies([u"Rockwell Extra Bold"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.date_in.setFont(font3)
        self.date_in.setAlignment(Qt.AlignCenter)
        self.date_in.setReadOnly(False)
        self.date_in.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_in.setDate(QDate(2023, 1, 1))

        self.verticalLayout_4.addWidget(self.date_in)

        self.renew_bnt = QPushButton(self.frame)
        self.renew_bnt.setObjectName(u"renew_bnt")
        font4 = QFont()
        font4.setPointSize(12)
        self.renew_bnt.setFont(font4)

        self.verticalLayout_4.addWidget(self.renew_bnt)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_2)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setIndent(4)

        self.verticalLayout_11.addWidget(self.label_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ach_in = QLineEdit(self.frame)
        self.ach_in.setObjectName(u"ach_in")
        self.ach_in.setFont(font2)

        self.horizontalLayout_3.addWidget(self.ach_in)

        self.ach_btn = QPushButton(self.frame)
        self.ach_btn.setObjectName(u"ach_btn")
        self.ach_btn.setMinimumSize(QSize(100, 0))
        self.ach_btn.setFont(font4)
        self.ach_btn.setCheckable(False)
        self.ach_btn.setChecked(False)

        self.horizontalLayout_3.addWidget(self.ach_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_3 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_3)

        self.list_viwe = QListWidget(self.frame)
        self.list_viwe.setObjectName(u"list_viwe")
        self.list_viwe.setMinimumSize(QSize(0, 150))
        self.list_viwe.setFont(font2)
        self.list_viwe.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_viwe.setLayoutMode(QListView.Batched)

        self.verticalLayout_5.addWidget(self.list_viwe)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 561, 291))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 551, 271))
        self.verticalLayout_12 = QVBoxLayout(self.widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.img_labl = QLabel(self.widget)
        self.img_labl.setObjectName(u"img_labl")
        self.img_labl.setMaximumSize(QSize(600, 500))
        self.img_labl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.img_labl)

        self.img_btn = QPushButton(self.widget)
        self.img_btn.setObjectName(u"img_btn")
        self.img_btn.setFont(font2)

        self.verticalLayout_12.addWidget(self.img_btn)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(570, 0, 20, 901))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 830, 561, 71))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.save_db = QPushButton(self.widget1)
        self.save_db.setObjectName(u"save_db")
        self.save_db.setFont(font2)

        self.horizontalLayout_4.addWidget(self.save_db)

        Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Window)

        QMetaObject.connectSlotsByName(Main_Window)
    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(QCoreApplication.translate("Main_Window", u"MainWindow", None))
        self.status_lable.setText(QCoreApplication.translate("Main_Window", u"\u0645\u0633\u0645\u062a\u0631", None))
        self.label_5.setText(QCoreApplication.translate("Main_Window", u"\u062d\u0627\u0644\u0647 \u0627\u0644\u0627\u0634\u062a\u0631\u0643: ", None))
        self.label.setText(QCoreApplication.translate("Main_Window", u"\u0627\u0644\u0627\u0633\u0645", None))
        self.Name_in.setPlaceholderText(QCoreApplication.translate("Main_Window", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0627\u0633\u0645", None))
        self.label_2.setText(QCoreApplication.translate("Main_Window", u"\u0627\u0644\u0633\u0646", None))
        self.age_in.setPlaceholderText(QCoreApplication.translate("Main_Window", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0633\u0646", None))
        self.label_3.setText(QCoreApplication.translate("Main_Window", u"\u0627\u0644\u0645\u062c\u0645\u0648\u0639\u0647", None))
        self.Group_in.setPlaceholderText(QCoreApplication.translate("Main_Window", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0645\u062c\u0645\u0648\u0639\u0647", None))
        self.label_4.setText(QCoreApplication.translate("Main_Window", u"\u062a\u0627\u0631\u064a\u062e \u0627\u0646\u062a\u0647\u0627\u0621 \u0627\u0644\u0627\u0634\u062a\u0631\u0627\u0643", None))
        self.renew_bnt.setText(QCoreApplication.translate("Main_Window", u"\u0627\u0644\u062a\u062c\u062f\u064a\u062f \u0644\u0645\u062f\u0647 \u0634\u0647\u0631", None))
        self.label_13.setText(QCoreApplication.translate("Main_Window", u"\u0627\u0644\u0628\u0637\u0648\u0644\u0627\u062a \u0648 \u0627\u0644\u0627\u0646\u062c\u0627\u0632\u0627\u062a", None))
        self.ach_btn.setText(QCoreApplication.translate("Main_Window", u"Add", None))
        self.img_labl.setText("")
        self.img_btn.setText(QCoreApplication.translate("Main_Window", u"\u0635\u0648\u0631\u0647 \u0627\u0644\u0645\u0634\u062a\u0631\u0643", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main_Window", u"\u0628\u062d\u062b \u0639\u0646 \u0645\u0634\u062a\u0631\u0643", None))
        self.save_db.setText(QCoreApplication.translate("Main_Window", u"\u062d\u0641\u0637", None))
    # retranslateUi

