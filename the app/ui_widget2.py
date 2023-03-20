# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget2pZbkVP.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1177, 971)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stacked = QStackedWidget(self.centralwidget)
        self.stacked.setObjectName(u"stacked")
        font = QFont()
        font.setPointSize(28)
        self.stacked.setFont(font)
        self.stacked.setToolTipDuration(-1)
        self.first = QWidget()
        self.first.setObjectName(u"first")
        self.first.setStyleSheet(u"")
        self.frame = QFrame(self.first)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(580, 50, 571, 901))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.Name_in.setFont(font2)
        self.Name_in.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Name_in)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(16)
        self.label_2.setFont(font3)
        self.label_2.setMargin(0)
        self.label_2.setIndent(4)

        self.verticalLayout_2.addWidget(self.label_2)

        self.age_in = QLineEdit(self.frame)
        self.age_in.setObjectName(u"age_in")
        self.age_in.setMinimumSize(QSize(0, 0))
        self.age_in.setFont(font3)
        self.age_in.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout_2.addWidget(self.age_in)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setMargin(0)
        self.label_6.setIndent(4)

        self.verticalLayout_6.addWidget(self.label_6)

        self.phone_in = QLineEdit(self.frame)
        self.phone_in.setObjectName(u"phone_in")
        self.phone_in.setMinimumSize(QSize(0, 0))
        self.phone_in.setFont(font3)
        self.phone_in.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout_6.addWidget(self.phone_in)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setMargin(0)
        self.label_8.setIndent(4)

        self.verticalLayout_8.addWidget(self.label_8)

        self.sessions_in = QLineEdit(self.frame)
        self.sessions_in.setObjectName(u"sessions_in")
        self.sessions_in.setMinimumSize(QSize(0, 0))
        self.sessions_in.setFont(font3)
        self.sessions_in.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout_8.addWidget(self.sessions_in)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_8)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setIndent(4)

        self.verticalLayout_3.addWidget(self.label_3)

        self.Group_in = QLineEdit(self.frame)
        self.Group_in.setObjectName(u"Group_in")
        self.Group_in.setFont(font3)

        self.verticalLayout_3.addWidget(self.Group_in)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setIndent(4)

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.parent_in = QLineEdit(self.frame)
        self.parent_in.setObjectName(u"parent_in")
        self.parent_in.setFont(font3)

        self.verticalLayout_5.addWidget(self.parent_in)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_2)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setIndent(4)

        self.verticalLayout_11.addWidget(self.label_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ach_in = QLineEdit(self.frame)
        self.ach_in.setObjectName(u"ach_in")
        self.ach_in.setFont(font3)

        self.horizontalLayout_3.addWidget(self.ach_in)

        self.ach_btn = QPushButton(self.frame)
        self.ach_btn.setObjectName(u"ach_btn")
        self.ach_btn.setMinimumSize(QSize(100, 0))
        font4 = QFont()
        font4.setPointSize(12)
        self.ach_btn.setFont(font4)
        self.ach_btn.setCheckable(False)
        self.ach_btn.setChecked(False)

        self.horizontalLayout_3.addWidget(self.ach_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_11)

        self.list_viwe = QListWidget(self.frame)
        self.list_viwe.setObjectName(u"list_viwe")
        self.list_viwe.setMinimumSize(QSize(0, 150))
        self.list_viwe.setFont(font3)
        self.list_viwe.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_viwe.setLayoutMode(QListView.Batched)

        self.verticalLayout_5.addWidget(self.list_viwe)

        self.layoutWidget = QWidget(self.first)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 870, 571, 71))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.page1 = QPushButton(self.layoutWidget)
        self.page1.setObjectName(u"page1")
        self.page1.setFont(font3)

        self.horizontalLayout_4.addWidget(self.page1)

        self.save_db = QPushButton(self.layoutWidget)
        self.save_db.setObjectName(u"save_db")
        self.save_db.setFont(font3)

        self.horizontalLayout_4.addWidget(self.save_db)

        self.frame_2 = QFrame(self.first)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 40, 401, 321))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.img_labl = QLabel(self.frame_2)
        self.img_labl.setObjectName(u"img_labl")
        self.img_labl.setMaximumSize(QSize(600, 500))
        self.img_labl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.img_labl)

        self.img_btn = QPushButton(self.frame_2)
        self.img_btn.setObjectName(u"img_btn")
        self.img_btn.setFont(font3)

        self.verticalLayout_12.addWidget(self.img_btn)


        self.verticalLayout_21.addLayout(self.verticalLayout_12)

        self.bar_contanier = QFrame(self.first)
        self.bar_contanier.setObjectName(u"bar_contanier")
        self.bar_contanier.setGeometry(QRect(10, 540, 541, 281))
        self.bar_contanier.setFrameShape(QFrame.StyledPanel)
        self.bar_contanier.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.bar_contanier)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.bar_img = QLabel(self.bar_contanier)
        self.bar_img.setObjectName(u"bar_img")
        self.bar_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.bar_img)

        self.print = QPushButton(self.bar_contanier)
        self.print.setObjectName(u"print")
        self.print.setMinimumSize(QSize(200, 0))
        self.print.setMaximumSize(QSize(1082, 16777215))
        self.print.setFont(font3)
        self.print.setVisible(False)

        self.verticalLayout_22.addWidget(self.print, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.first)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, -10, 1141, 111))
        font5 = QFont()
        font5.setFamilies([u"Traditional Arabic"])
        font5.setPointSize(60)
        font5.setBold(True)
        font5.setUnderline(True)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 30)")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stacked.addWidget(self.first)
        self.second = QWidget()
        self.second.setObjectName(u"second")
        self.verticalLayout_10 = QVBoxLayout(self.second)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget = QWidget(self.second)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(1141, 100))
        self.widget.setMaximumSize(QSize(1141, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Search = QPushButton(self.widget)
        self.Search.setObjectName(u"Search")
        self.Search.setMinimumSize(QSize(136, 0))
        self.Search.setFont(font3)

        self.horizontalLayout_2.addWidget(self.Search)

        self.code = QLineEdit(self.widget)
        self.code.setObjectName(u"code")
        self.code.setFont(font3)

        self.horizontalLayout_2.addWidget(self.code)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(148, 0))
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.status_lable_3 = QLabel(self.widget)
        self.status_lable_3.setObjectName(u"status_lable_3")
        self.status_lable_3.setMinimumSize(QSize(174, 0))
        font6 = QFont()
        font6.setFamilies([u"Dubai Medium"])
        font6.setPointSize(36)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(True)
        self.status_lable_3.setFont(font6)
        self.status_lable_3.setStyleSheet(u"color:green")
        self.status_lable_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.status_lable_3)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(262, 0))
        font7 = QFont()
        font7.setFamilies([u"Dubai Medium"])
        font7.setPointSize(36)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setUnderline(True)
        self.label_11.setFont(font7)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout_10.addWidget(self.widget)

        self.main_body = QWidget(self.second)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMinimumSize(QSize(148, 0))
        font8 = QFont()
        font8.setPointSize(20)
        self.main_body.setFont(font8)
        self.gridLayout_2 = QGridLayout(self.main_body)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.main_body)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.widget_4 = QWidget(self.frame_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 20, 430, 241))
        self.widget_4.setMinimumSize(QSize(430, 210))
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.img_out = QLabel(self.widget_4)
        self.img_out.setObjectName(u"img_out")

        self.gridLayout_3.addWidget(self.img_out, 0, 0, 2, 1)

        self.widget_3 = QWidget(self.frame_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 250, 421, 481))
        self.widget_3.setMinimumSize(QSize(421, 481))
        self.verticalLayout_14 = QVBoxLayout(self.widget_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.slogan = QLabel(self.widget_3)
        self.slogan.setObjectName(u"slogan")
        self.slogan.setEnabled(True)
        font9 = QFont()
        font9.setFamilies([u"Traditional Arabic"])
        font9.setPointSize(23)
        font9.setBold(True)
        font9.setUnderline(True)
        self.slogan.setFont(font9)
        self.slogan.setToolTipDuration(-1)
        self.slogan.setLayoutDirection(Qt.LeftToRight)
        self.slogan.setStyleSheet(u"color:rgba(0, 0, 0, 30)")
        self.slogan.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.slogan)

        self.slogan_2 = QLabel(self.widget_3)
        self.slogan_2.setObjectName(u"slogan_2")
        self.slogan_2.setEnabled(True)
        self.slogan_2.setFont(font9)
        self.slogan_2.setToolTipDuration(-1)
        self.slogan_2.setLayoutDirection(Qt.LeftToRight)
        self.slogan_2.setStyleSheet(u"color:rgba(0, 0, 0, 30)")
        self.slogan_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.slogan_2)

        self.slogan_3 = QLabel(self.widget_3)
        self.slogan_3.setObjectName(u"slogan_3")
        self.slogan_3.setEnabled(True)
        self.slogan_3.setFont(font9)
        self.slogan_3.setToolTipDuration(-1)
        self.slogan_3.setLayoutDirection(Qt.LeftToRight)
        self.slogan_3.setStyleSheet(u"color:rgba(0, 0, 0, 30)")
        self.slogan_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.slogan_3)

        self.slogan_4 = QLabel(self.widget_3)
        self.slogan_4.setObjectName(u"slogan_4")
        self.slogan_4.setEnabled(True)
        self.slogan_4.setFont(font9)
        self.slogan_4.setToolTipDuration(-1)
        self.slogan_4.setLayoutDirection(Qt.LeftToRight)
        self.slogan_4.setStyleSheet(u"color:rgba(0, 0, 0, 30)")
        self.slogan_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.slogan_4)

        self.layoutWidget1 = QWidget(self.frame_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(440, 10, 661, 711))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.name_out = QLabel(self.layoutWidget1)
        self.name_out.setObjectName(u"name_out")
        self.name_out.setFont(font)
        self.name_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.name_out)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        font10 = QFont()
        font10.setFamilies([u"Segoe Script"])
        font10.setPointSize(28)
        self.label_10.setFont(font10)
        self.label_10.setIndent(9)

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout_13.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.age_out = QLabel(self.layoutWidget1)
        self.age_out.setObjectName(u"age_out")
        self.age_out.setFont(font)
        self.age_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.age_out)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font10)
        self.label_12.setIndent(9)

        self.horizontalLayout_6.addWidget(self.label_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.phone_out = QLabel(self.layoutWidget1)
        self.phone_out.setObjectName(u"phone_out")
        self.phone_out.setFont(font)
        self.phone_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.phone_out)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font10)
        self.label_14.setIndent(9)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.reNew = QPushButton(self.layoutWidget1)
        self.reNew.setObjectName(u"reNew")
        self.reNew.setMaximumSize(QSize(157, 16777215))
        font11 = QFont()
        font11.setPointSize(17)
        self.reNew.setFont(font11)

        self.horizontalLayout_8.addWidget(self.reNew)

        self.session_out = QLabel(self.layoutWidget1)
        self.session_out.setObjectName(u"session_out")
        self.session_out.setMaximumSize(QSize(225, 16777215))
        self.session_out.setFont(font)
        self.session_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.session_out)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font10)
        self.label_15.setIndent(9)

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.group_out = QLabel(self.layoutWidget1)
        self.group_out.setObjectName(u"group_out")
        self.group_out.setFont(font)
        self.group_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.group_out)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font10)
        self.label_16.setIndent(9)

        self.horizontalLayout_9.addWidget(self.label_16)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.parent_out = QLabel(self.layoutWidget1)
        self.parent_out.setObjectName(u"parent_out")
        self.parent_out.setFont(font)
        self.parent_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.parent_out)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font10)
        self.label_17.setIndent(9)

        self.horizontalLayout_10.addWidget(self.label_17)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.main_body)

        self.widget_2 = QWidget(self.second)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(1141, 54))
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.page2 = QPushButton(self.widget_2)
        self.page2.setObjectName(u"page2")
        self.page2.setMaximumSize(QSize(1139, 36))
        self.page2.setFont(font3)

        self.verticalLayout_9.addWidget(self.page2)


        self.verticalLayout_10.addWidget(self.widget_2)

        self.stacked.addWidget(self.second)

        self.gridLayout.addWidget(self.stacked, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked.setCurrentIndex(1)
        self.ach_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None))
        self.Name_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0627\u0633\u0645", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0646", None))
        self.age_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0633\u0646", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.phone_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u062d\u0635\u0635", None))
        self.sessions_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0639\u062f\u062f \u0627\u0644\u062d\u0635\u0635", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u062c\u0645\u0648\u0639\u0647", None))
        self.Group_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0645\u062c\u0645\u0648\u0639\u0647", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0638\u064a\u0641\u0647 \u0648\u0627\u0644\u064a \u0627\u0644\u0627\u0645\u0631", None))
        self.parent_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0648\u0638\u064a\u0641\u0647", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0628\u0637\u0648\u0644\u0627\u062a \u0648 \u0627\u0644\u0627\u0646\u062c\u0627\u0632\u0627\u062a", None))
        self.ach_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.page1.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b \u0639\u0646 \u0645\u0634\u062a\u0631\u0643", None))
        self.save_db.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0641\u0637", None))
        self.img_labl.setText("")
        self.img_btn.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0648\u0631\u0647 \u0627\u0644\u0645\u0634\u062a\u0631\u0643", None))
        self.bar_img.setText("")
        self.print.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0628\u0627\u0639\u0647", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nasser Swimming Acadimy", None))
        self.Search.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b \u0639\u0646 \u0645\u0634\u062a\u0631\u0643", None))
        self.status_lable_3.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0627\u0644\u0647 \u0627\u0644\u0627\u0634\u062a\u0631\u0627\u0643: ", None))
        self.img_out.setText("")
        self.slogan.setText(QCoreApplication.translate("MainWindow", u"Nasser Swimming Acadimy", None))
        self.slogan_2.setText(QCoreApplication.translate("MainWindow", u"Nasser Swimming Acadimy", None))
        self.slogan_3.setText(QCoreApplication.translate("MainWindow", u"Nasser Swimming Acadimy", None))
        self.slogan_4.setText(QCoreApplication.translate("MainWindow", u"Nasser Swimming Acadimy", None))
        self.name_out.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645:", None))
        self.age_out.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0646:", None))
        self.phone_out.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641:", None))
        self.reNew.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062c\u062f\u064a\u062f \u0627\u0644\u0627\u0634\u062a\u0631\u0627\u0643", None))
        self.session_out.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062d\u0635\u0635 \u0627\u0644\u0645\u062a\u0628\u0642\u064a\u0647:", None))
        self.group_out.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u062c\u0645\u0648\u0639\u0647:", None))
        self.parent_out.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0637\u064a\u0641\u0647 \u0648\u0644\u064a \u0627\u0644\u0627\u0645\u0631:", None))
        self.page2.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0633\u062c\u064a\u0644 \u0645\u0634\u062a\u0631\u0643 \u062c\u062f\u064a\u062f", None))
    # retranslateUi

