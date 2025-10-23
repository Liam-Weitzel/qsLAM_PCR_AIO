# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"QWidget{\n"
"	color: rgb(30, 30, 30);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(134, 210, 237, 200);\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 33, 109);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"QToolTip {\n"
"    border-left: 2px solid #00216D;\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(245, 245, 245);\n"
"	background-image: url(:/images/images/images/Erasmus_MC_logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #"
                        "00216D; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #86D2ED; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(224, 247, 247);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #00216D;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(224, 247, 247);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #00216D;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
""
                        "	border-top: 3px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(230, 242, 242);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(85, 85, 85);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(208, 235, 235);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: #00216D;\n"
"}\n"
"\n"
"/* Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: #86D2ED;\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/cil-people.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(51, 51, 51); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5p"
                        "x; }\n"
"#extraCloseColumnButton:hover { background-color: rgb(178, 223, 223); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnButton:pressed { background-color: rgb(128, 207, 207); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(224, 247, 247);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: #00216D;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Top Buttons "
                        "*/\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(224, 247, 247); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(208, 235, 235); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(235, 235, 235); }\n"
"#themeSettingsTopDetail { background-color: #86D2ED; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(245, 245, 245); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(102, 102, 102); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44p"
                        "x;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(224, 247, 247);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: #00216D;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Specific styling for R1 and R2 pair filter combo boxes */\n"
"#r1PairFilterComboBox, #r2PairFilterComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QTableWidget */\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(204, 204, 204);\n"
"	border-bottom: 1px solid rgb(220, 220, 220);\n"
"	alternate-background-color: rgb(248, 248, 248);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(220, 220, 220);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(220, 220, 220);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(134, 210, 237);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #86D2ED;\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(220, 220, 220);\n"
"    border-right: 1px solid rgb(220, 220, 220);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-colo"
                        "r: rgb(245, 245, 245);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	background-color: #01216D;\n"
"	padding: 3px;\n"
"	color: white;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(220, 220, 220);\n"
"}\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #01216D;\n"
"}\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(204, 204, 204);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #86D2ED;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid #86D2ED;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #86D2ED;\n"
"}\n"
"\n"
"/* PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #86D2ED;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScr"
                        "ollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid #86D2ED;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #86D2ED;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #01216D;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #01216D;\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    "
                        "subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border-radius: 5px;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid rgb(134, 210, 237);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(230, 230, 230);\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid rgb(134, 210, 237);\n"
"}\n"
"QRadioButton::indicator {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indi"
                        "cator:hover {\n"
"    border: 2px solid rgb(134, 210, 237);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 2px solid rgb(230, 230, 230);\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"QRadioButton::indicator:checked:hover {\n"
"    border: 2px solid rgb(134, 210, 237);\n"
"}\n"
"QCommandLinkButton {\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QCommandLinkButton:hover {\n"
"    border: 300px solid rgb(134, 210, 237);\n"
"}\n"
"/* QTabWidget Container */\n"
"QTabWidget {\n"
"    background-color: rgb(245, 245, 245);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Tab Bar */\n"
"QTabBar::tab {\n"
"    background-color: rgb(240, 240, 240);\n"
"    color: rgb(30, 30, 30);\n"
"    padding: 6px 14px;\n"
"    margin-right: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    bac"
                        "kground-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a0cdee, stop:1 #d0f0f7\n"
"    );\n"
"    color: rgb(0, 0, 0);\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(224, 247, 247);\n"
"}\n"
"\n"
"/* Tab Widget Pane (Content Area) */\n"
"QTabWidget::pane {\n"
"    border-top: 2px solid rgb(204, 204, 204);\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:disabled {\n"
"    background-color: rgb(200, 200, 200);  /* light grey for disabled tabs */\n"
"    color: rgb(120, 120, 120);             /* greyed-out text */\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(204, 204, 204);\n"
"    border-radius: 5px;\n"
"    padding: 4px 8px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"/* Hover */\n"
"QComboBox:hover {\n"
"    border: 2px solid #86D2ED;\n"
"}\n"
"\n"
"/* Focused */\n"
"QComboBo"
                        "x:focus {\n"
"    border: 2px solid #86D2ED;\n"
"}\n"
"\n"
"/* Drop-down arrow button */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid rgb(204, 204, 204);\n"
"    background-color: rgb(245, 245, 245);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"/* Arrow icon */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Drop-down button hover */\n"
"QComboBox::drop-down:hover {\n"
"    background-color: rgb(224, 247, 247);\n"
"}\n"
"\n"
"/* Popup (the list that opens) */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: #86D2ED;\n"
"    selection-color: rgb(0, 0, 0);\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QComboBox:disabled {\n"
"   "
                        " background-color: rgb(235, 235, 235);\n"
"    color: rgb(120, 120, 120);\n"
"    border: 2px solid rgb(200, 200, 200);\n"
"}\n"
"\n"
"/* QSlider */\n"
"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 6px;\n"
"    background: rgb(204, 204, 204);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background: rgb(180, 220, 240);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #00216D;\n"
"    border: none;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #6BAAD2;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(204, 204, 204);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #86D2ED;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* Vertical Slider */\n"
"QSlider::groove:vertical {\n"
"    border: none;\n"
"    width: 6px;\n"
"    background: rgb(204, 204, 204);\n"
"  "
                        "  border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::groove:vertical:hover {\n"
"    background: rgb(180, 220, 240);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #00216D;\n"
"    border: none;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: #6BAAD2;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(204, 204, 204);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #86D2ED;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* QTextBrowser - Light theme styling */\n"
"QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(30, 30, 30);\n"
"    border: 2px solid rgb(204, 204, 204);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    selection-background-color: #86D2ED;\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* QTreeWidget - Light theme styling */\n"
"QTreeWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(30, 30, 30);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 5px;\n"
"    alternate-background-color: rgb(248, 248, 248);\n"
"    selection-background-color: #86D2ED;\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    background-color: transparent;\n"
"    color: rgb(30, 30, 30);\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #86D2ED;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: rgb(224, 247, 247);\n"
"}\n"
"\n"
"/* QSplitter - Light theme styling */\n"
"QSplitter {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 3px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 3px;\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.runManagerButton = QPushButton(self.topMenu)
        self.runManagerButton.setObjectName(u"runManagerButton")
        sizePolicy.setHeightForWidth(self.runManagerButton.sizePolicy().hasHeightForWidth())
        self.runManagerButton.setSizePolicy(sizePolicy)
        self.runManagerButton.setMinimumSize(QSize(0, 45))
        self.runManagerButton.setFont(font)
        self.runManagerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runManagerButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.runManagerButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_8.addWidget(self.runManagerButton)

        self.runConfigurationButton = QPushButton(self.topMenu)
        self.runConfigurationButton.setObjectName(u"runConfigurationButton")
        sizePolicy.setHeightForWidth(self.runConfigurationButton.sizePolicy().hasHeightForWidth())
        self.runConfigurationButton.setSizePolicy(sizePolicy)
        self.runConfigurationButton.setMinimumSize(QSize(0, 45))
        self.runConfigurationButton.setFont(font)
        self.runConfigurationButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runConfigurationButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.runConfigurationButton.setStyleSheet(u"margin-left: -5px; background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.runConfigurationButton)

        self.runProgressButton = QPushButton(self.topMenu)
        self.runProgressButton.setObjectName(u"runProgressButton")
        self.runProgressButton.setMinimumSize(QSize(0, 45))
        self.runProgressButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runProgressButton.setStyleSheet(u"margin-left: -5px; background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.runProgressButton)

        self.resultsOverviewButton = QPushButton(self.topMenu)
        self.resultsOverviewButton.setObjectName(u"resultsOverviewButton")
        self.resultsOverviewButton.setMinimumSize(QSize(0, 45))
        self.resultsOverviewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resultsOverviewButton.setStyleSheet(u"margin-left: -5px; background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.resultsOverviewButton)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-double-right.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraCloseColumnButton = QPushButton(self.extraTopBg)
        self.extraCloseColumnButton.setObjectName(u"extraCloseColumnButton")
        self.extraCloseColumnButton.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnButton.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnButton.setIcon(icon)
        self.extraCloseColumnButton.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnButton, 0, 2, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.aboutText = QTextEdit(self.extraCenter)
        self.aboutText.setObjectName(u"aboutText")
        self.aboutText.setMinimumSize(QSize(222, 0))
        self.aboutText.setStyleSheet(u"background: transparent;")
        self.aboutText.setFrameShape(QFrame.Shape.NoFrame)
        self.aboutText.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.aboutText)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.moreButton = QPushButton(self.extraTopMenu)
        self.moreButton.setObjectName(u"moreButton")
        sizePolicy.setHeightForWidth(self.moreButton.sizePolicy().hasHeightForWidth())
        self.moreButton.setSizePolicy(sizePolicy)
        self.moreButton.setMinimumSize(QSize(0, 45))
        self.moreButton.setFont(font)
        self.moreButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.moreButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.moreButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.moreButton)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.currentlySelectedText = QLabel(self.leftBox)
        self.currentlySelectedText.setObjectName(u"currentlySelectedText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentlySelectedText.sizePolicy().hasHeightForWidth())
        self.currentlySelectedText.setSizePolicy(sizePolicy2)
        self.currentlySelectedText.setMaximumSize(QSize(16777215, 45))
        self.currentlySelectedText.setFont(font)
        self.currentlySelectedText.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.currentlySelectedText)

        self.currentlySelected = QLabel(self.leftBox)
        self.currentlySelected.setObjectName(u"currentlySelected")

        self.horizontalLayout_3.addWidget(self.currentlySelected)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopButton = QPushButton(self.rightButtons)
        self.settingsTopButton.setObjectName(u"settingsTopButton")
        self.settingsTopButton.setMinimumSize(QSize(28, 28))
        self.settingsTopButton.setMaximumSize(QSize(28, 28))
        self.settingsTopButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopButton.setIcon(icon1)
        self.settingsTopButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopButton)

        self.minimizeAppButton = QPushButton(self.rightButtons)
        self.minimizeAppButton.setObjectName(u"minimizeAppButton")
        self.minimizeAppButton.setMinimumSize(QSize(28, 28))
        self.minimizeAppButton.setMaximumSize(QSize(28, 28))
        self.minimizeAppButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppButton.setIcon(icon2)
        self.minimizeAppButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppButton)

        self.maximizeRestoreAppButton = QPushButton(self.rightButtons)
        self.maximizeRestoreAppButton.setObjectName(u"maximizeRestoreAppButton")
        self.maximizeRestoreAppButton.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppButton.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppButton.setFont(font3)
        self.maximizeRestoreAppButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppButton.setIcon(icon3)
        self.maximizeRestoreAppButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppButton)

        self.closeAppButton = QPushButton(self.rightButtons)
        self.closeAppButton.setObjectName(u"closeAppButton")
        self.closeAppButton.setMinimumSize(QSize(28, 28))
        self.closeAppButton.setMaximumSize(QSize(28, 28))
        self.closeAppButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppButton.setIcon(icon)
        self.closeAppButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppButton)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.runManagerTab = QWidget()
        self.runManagerTab.setObjectName(u"runManagerTab")
        self.runManagerTab.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.runManagerTab)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.runManagerTab)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setMinimumSize(QSize(0, 50))
        self.row_1.setMaximumSize(QSize(16777215, 50))
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 50))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.createRunButton = QPushButton(self.frame_content_wid_1)
        self.createRunButton.setObjectName(u"createRunButton")
        self.createRunButton.setMinimumSize(QSize(50, 30))
        self.createRunButton.setFont(font)
        self.createRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-library-add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createRunButton.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.createRunButton)

        self.selectRunButton = QPushButton(self.frame_content_wid_1)
        self.selectRunButton.setObjectName(u"selectRunButton")
        self.selectRunButton.setMinimumSize(QSize(50, 30))
        self.selectRunButton.setFont(font)
        self.selectRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.selectRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-input.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectRunButton.setIcon(icon5)

        self.horizontalLayout_9.addWidget(self.selectRunButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.refreshRunButton = QPushButton(self.frame_content_wid_1)
        self.refreshRunButton.setObjectName(u"refreshRunButton")
        self.refreshRunButton.setMinimumSize(QSize(50, 30))
        self.refreshRunButton.setFont(font)
        self.refreshRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refreshRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshRunButton.setIcon(icon6)

        self.horizontalLayout_9.addWidget(self.refreshRunButton)

        self.deleteRunButton = QPushButton(self.frame_content_wid_1)
        self.deleteRunButton.setObjectName(u"deleteRunButton")
        self.deleteRunButton.setMinimumSize(QSize(50, 30))
        self.deleteRunButton.setFont(font)
        self.deleteRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteRunButton.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.deleteRunButton)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.runManagerTab)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.runsTable = QTableWidget(self.row_2)
        if (self.runsTable.columnCount() < 4):
            self.runsTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.runsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.runsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.runsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.runsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.runsTable.setObjectName(u"runsTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.runsTable.sizePolicy().hasHeightForWidth())
        self.runsTable.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(30, 30, 30, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush3 = QBrush(QColor(30, 30, 30, 128))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.runsTable.setPalette(palette)
        self.runsTable.setFrameShape(QFrame.Shape.NoFrame)
        self.runsTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.runsTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.runsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.runsTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.runsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.runsTable.setShowGrid(True)
        self.runsTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.runsTable.setSortingEnabled(False)
        self.runsTable.horizontalHeader().setVisible(True)
        self.runsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.runsTable.horizontalHeader().setDefaultSectionSize(200)
        self.runsTable.horizontalHeader().setStretchLastSection(True)
        self.runsTable.verticalHeader().setVisible(False)
        self.runsTable.verticalHeader().setCascadingSectionResizes(False)
        self.runsTable.verticalHeader().setHighlightSections(False)
        self.runsTable.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_19.addWidget(self.runsTable)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.runManagerTab)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 70))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.importRunButton = QPushButton(self.row_3)
        self.importRunButton.setObjectName(u"importRunButton")
        self.importRunButton.setMinimumSize(QSize(50, 30))
        self.importRunButton.setFont(font)
        self.importRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.importRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-cloud-download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importRunButton.setIcon(icon8)

        self.gridLayout.addWidget(self.importRunButton, 0, 3, 1, 1)

        self.openFolderLocationButton = QPushButton(self.row_3)
        self.openFolderLocationButton.setObjectName(u"openFolderLocationButton")
        self.openFolderLocationButton.setMinimumSize(QSize(50, 30))
        self.openFolderLocationButton.setFont(font)
        self.openFolderLocationButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openFolderLocationButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openFolderLocationButton.setIcon(icon9)

        self.gridLayout.addWidget(self.openFolderLocationButton, 0, 0, 1, 1)

        self.exportRunButton = QPushButton(self.row_3)
        self.exportRunButton.setObjectName(u"exportRunButton")
        self.exportRunButton.setMinimumSize(QSize(50, 30))
        self.exportRunButton.setFont(font)
        self.exportRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exportRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportRunButton.setIcon(icon10)

        self.gridLayout.addWidget(self.exportRunButton, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.renameRunButton = QPushButton(self.row_3)
        self.renameRunButton.setObjectName(u"renameRunButton")
        self.renameRunButton.setMinimumSize(QSize(50, 30))
        self.renameRunButton.setFont(font)
        self.renameRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.renameRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-text-square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.renameRunButton.setIcon(icon11)

        self.gridLayout.addWidget(self.renameRunButton, 0, 1, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.runManagerTab)
        self.runConfigurationTab = QWidget()
        self.runConfigurationTab.setObjectName(u"runConfigurationTab")
        self.runConfigurationTab.setStyleSheet(u"")
        self.verticalLayout1 = QVBoxLayout(self.runConfigurationTab)
        self.verticalLayout1.setSpacing(10)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.verticalLayout1.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 21, 8, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 21, 6, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 21, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 21, 7, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 21, 4, 1, 1)

        self.saveButton = QPushButton(self.runConfigurationTab)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(50, 30))
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon12)

        self.gridLayout_2.addWidget(self.saveButton, 21, 9, 1, 1)

        self.r1InputButton = QPushButton(self.runConfigurationTab)
        self.r1InputButton.setObjectName(u"r1InputButton")
        self.r1InputButton.setMinimumSize(QSize(50, 30))
        self.r1InputButton.setFont(font)
        self.r1InputButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.r1InputButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.r1InputButton.setIcon(icon9)

        self.gridLayout_2.addWidget(self.r1InputButton, 0, 3, 2, 1)

        self.helpButton = QPushButton(self.runConfigurationTab)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(50, 30))
        self.helpButton.setFont(font)
        self.helpButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.helpButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-map.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpButton.setIcon(icon13)

        self.gridLayout_2.addWidget(self.helpButton, 21, 10, 1, 1)

        self.configStackedWidget = QStackedWidget(self.runConfigurationTab)
        self.configStackedWidget.setObjectName(u"configStackedWidget")
        self.docker = QWidget()
        self.docker.setObjectName(u"docker")
        self.verticalLayout2 = QVBoxLayout(self.docker)
        self.verticalLayout2.setSpacing(10)
        self.verticalLayout2.setObjectName(u"verticalLayout2")
        self.verticalLayout2.setProperty(u"leftmargin", 10)
        self.verticalLayout2.setProperty(u"topmargin", 10)
        self.verticalLayout2.setProperty(u"rightmargin", 10)
        self.verticalLayout2.setProperty(u"bottommargin", 10)
        self.row_11 = QFrame(self.docker)
        self.row_11.setObjectName(u"row_11")
        self.row_11.setMinimumSize(QSize(0, 70))
        self.row_11.setMaximumSize(QSize(16777215, 70))
        self.row_11.setProperty(u"minimumsize", QSize(0, 70))
        self.row_11.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridlayout = QGridLayout(self.row_11)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName(u"gridlayout")
        self.localRadio = QRadioButton(self.row_11)
        self.localRadio.setObjectName(u"localRadio")

        self.gridlayout.addWidget(self.localRadio, 3, 0, 1, 1)

        self.remoteRadio = QRadioButton(self.row_11)
        self.remoteRadio.setObjectName(u"remoteRadio")

        self.gridlayout.addWidget(self.remoteRadio, 3, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridlayout.addItem(self.verticalSpacer_9, 4, 0, 1, 2)

        self.dockerLabel = QLabel(self.row_11)
        self.dockerLabel.setObjectName(u"dockerLabel")

        self.gridlayout.addWidget(self.dockerLabel, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridlayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridlayout.addItem(self.verticalSpacer_16, 0, 0, 1, 2)


        self.verticalLayout2.addWidget(self.row_11)

        self.row_21 = QFrame(self.docker)
        self.row_21.setObjectName(u"row_21")
        self.row_21.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout3 = QVBoxLayout(self.row_21)
        self.verticalLayout3.setObjectName(u"verticalLayout3")
        self.dockerStackedWidget = QStackedWidget(self.row_21)
        self.dockerStackedWidget.setObjectName(u"dockerStackedWidget")
        self.local = QWidget()
        self.local.setObjectName(u"local")
        self.verticalLayout4 = QVBoxLayout(self.local)
        self.verticalLayout4.setSpacing(10)
        self.verticalLayout4.setObjectName(u"verticalLayout4")
        self.verticalLayout4.setProperty(u"leftmargin", 10)
        self.verticalLayout4.setProperty(u"topmargin", 10)
        self.verticalLayout4.setProperty(u"rightmargin", 10)
        self.verticalLayout4.setProperty(u"bottommargin", 10)
        self.grid = QFrame(self.local)
        self.grid.setObjectName(u"grid")
        self.grid.setProperty(u"minimumsize", QSize(0, 70))
        self.grid.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout1 = QGridLayout(self.grid)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.isInstalledStackedWidget = QStackedWidget(self.grid)
        self.isInstalledStackedWidget.setObjectName(u"isInstalledStackedWidget")
        self.isInstalled = QWidget()
        self.isInstalled.setObjectName(u"isInstalled")
        self.verticalLayout5 = QVBoxLayout(self.isInstalled)
        self.verticalLayout5.setSpacing(10)
        self.verticalLayout5.setObjectName(u"verticalLayout5")
        self.verticalLayout5.setProperty(u"leftmargin", 10)
        self.verticalLayout5.setProperty(u"topmargin", 10)
        self.verticalLayout5.setProperty(u"rightmargin", 10)
        self.verticalLayout5.setProperty(u"bottommargin", 10)
        self.grid1 = QFrame(self.isInstalled)
        self.grid1.setObjectName(u"grid1")
        self.grid1.setProperty(u"minimumsize", QSize(0, 70))
        self.grid1.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout2 = QGridLayout(self.grid1)
        self.gridLayout2.setSpacing(0)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.checkAgainButton_2 = QPushButton(self.grid1)
        self.checkAgainButton_2.setObjectName(u"checkAgainButton_2")
        self.checkAgainButton_2.setMinimumSize(QSize(50, 30))
        self.checkAgainButton_2.setFont(font)
        self.checkAgainButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkAgainButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.checkAgainButton_2.setIcon(icon6)

        self.gridLayout2.addWidget(self.checkAgainButton_2, 4, 5, 1, 1)

        self.dockerFoundLabel = QLabel(self.grid1)
        self.dockerFoundLabel.setObjectName(u"dockerFoundLabel")
        self.dockerFoundLabel.setStyleSheet(u"color: green; font-weight: bold;")

        self.gridLayout2.addWidget(self.dockerFoundLabel, 1, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_15, 1, 1, 1, 1)

        self.dockerSuccessIcon = QFrame(self.grid1)
        self.dockerSuccessIcon.setObjectName(u"dockerSuccessIcon")
        self.dockerSuccessIcon.setMinimumSize(QSize(20, 20))
        self.dockerSuccessIcon.setStyleSheet(u"\n"
"						    background-image: url(:/icons/images/icons/cil-smile.png);\n"
"						    background-position: center;\n"
"						    background-repeat: no-repeat;\n"
"						   ")

        self.gridLayout2.addWidget(self.dockerSuccessIcon, 1, 2, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_20, 2, 3, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_21, 0, 3, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_39, 1, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_40, 1, 5, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_41, 3, 0, 1, 2)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_38, 3, 4, 1, 2)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_32, 1, 4, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_37, 4, 4, 1, 1)

        self.dockerPathLabel_2 = QLabel(self.grid1)
        self.dockerPathLabel_2.setObjectName(u"dockerPathLabel_2")

        self.gridLayout2.addWidget(self.dockerPathLabel_2, 3, 2, 1, 2)

        self.dockerPathInput_2 = QLineEdit(self.grid1)
        self.dockerPathInput_2.setObjectName(u"dockerPathInput_2")

        self.gridLayout2.addWidget(self.dockerPathInput_2, 4, 2, 1, 2)


        self.verticalLayout5.addWidget(self.grid1)

        self.isInstalledStackedWidget.addWidget(self.isInstalled)
        self.notInstalled = QWidget()
        self.notInstalled.setObjectName(u"notInstalled")
        self.verticalLayout6 = QVBoxLayout(self.notInstalled)
        self.verticalLayout6.setSpacing(10)
        self.verticalLayout6.setObjectName(u"verticalLayout6")
        self.verticalLayout6.setProperty(u"leftmargin", 10)
        self.verticalLayout6.setProperty(u"topmargin", 10)
        self.verticalLayout6.setProperty(u"rightmargin", 10)
        self.verticalLayout6.setProperty(u"bottommargin", 10)
        self.grid2 = QFrame(self.notInstalled)
        self.grid2.setObjectName(u"grid2")
        self.grid2.setProperty(u"minimumsize", QSize(0, 70))
        self.grid2.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout3 = QGridLayout(self.grid2)
        self.gridLayout3.setSpacing(0)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.checkAgainButton = QPushButton(self.grid2)
        self.checkAgainButton.setObjectName(u"checkAgainButton")
        self.checkAgainButton.setMinimumSize(QSize(50, 30))
        self.checkAgainButton.setFont(font)
        self.checkAgainButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkAgainButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.checkAgainButton.setIcon(icon6)

        self.gridLayout3.addWidget(self.checkAgainButton, 5, 9, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout3.addItem(self.verticalSpacer_22, 2, 1, 1, 9)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout3.addItem(self.verticalSpacer_17, 6, 1, 1, 9)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout3.addItem(self.verticalSpacer_19, 0, 1, 1, 9)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout3.addItem(self.verticalSpacer_24, 8, 1, 1, 9)

        self.dockerPathInput = QLineEdit(self.grid2)
        self.dockerPathInput.setObjectName(u"dockerPathInput")

        self.gridLayout3.addWidget(self.dockerPathInput, 5, 1, 1, 5)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout3.addItem(self.verticalSpacer_23, 4, 1, 1, 9)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.horizontalSpacer_34, 1, 2, 1, 1)

        self.dockerPathLabel = QLabel(self.grid2)
        self.dockerPathLabel.setObjectName(u"dockerPathLabel")

        self.gridLayout3.addWidget(self.dockerPathLabel, 5, 0, 1, 1)

        self.dockerNotFoundLabel = QLabel(self.grid2)
        self.dockerNotFoundLabel.setObjectName(u"dockerNotFoundLabel")
        self.dockerNotFoundLabel.setStyleSheet(u"color: red; font-weight: bold;")

        self.gridLayout3.addWidget(self.dockerNotFoundLabel, 1, 4, 1, 3)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.horizontalSpacer_18, 5, 7, 1, 1)

        self.dockerErrorIcon = QFrame(self.grid2)
        self.dockerErrorIcon.setObjectName(u"dockerErrorIcon")
        self.dockerErrorIcon.setMinimumSize(QSize(20, 20))
        self.dockerErrorIcon.setStyleSheet(u"\n"
"						    background-image: url(:/icons/images/icons/cil-frown.png);\n"
"						    background-position: center;\n"
"						    background-repeat: no-repeat;\n"
"						   ")
        self.dockerErrorIcon.setFrameShape(QFrame.Shape.StyledPanel)
        self.dockerErrorIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout3.addWidget(self.dockerErrorIcon, 1, 3, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.horizontalSpacer_33, 1, 0, 1, 2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.horizontalSpacer_16, 1, 7, 1, 3)

        self.DockerNotFoundDescriptionLabel = QLabel(self.grid2)
        self.DockerNotFoundDescriptionLabel.setObjectName(u"DockerNotFoundDescriptionLabel")
        self.DockerNotFoundDescriptionLabel.setText(u"<html><body>I couldn't find a working Docker installation on your system. Docker is required to run the qsLAM_PCR pipeline locally. <a href=\"https://docs.docker.com/get-docker/\" style=\"color:#0066cc; text-decoration:none;\">Install Docker</a></body></html>")
        self.DockerNotFoundDescriptionLabel.setTextFormat(Qt.TextFormat.RichText)
        self.DockerNotFoundDescriptionLabel.setWordWrap(True)
        self.DockerNotFoundDescriptionLabel.setOpenExternalLinks(True)
        self.DockerNotFoundDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.gridLayout3.addWidget(self.DockerNotFoundDescriptionLabel, 3, 0, 1, 10)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.horizontalSpacer_17, 5, 6, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.horizontalSpacer_19, 5, 8, 1, 1)


        self.verticalLayout6.addWidget(self.grid2)

        self.isInstalledStackedWidget.addWidget(self.notInstalled)

        self.gridLayout1.addWidget(self.isInstalledStackedWidget, 0, 0, 1, 1)


        self.verticalLayout4.addWidget(self.grid)

        self.dockerStackedWidget.addWidget(self.local)
        self.remote = QWidget()
        self.remote.setObjectName(u"remote")
        self.verticalLayout7 = QVBoxLayout(self.remote)
        self.verticalLayout7.setSpacing(10)
        self.verticalLayout7.setObjectName(u"verticalLayout7")
        self.verticalLayout7.setProperty(u"leftmargin", 10)
        self.verticalLayout7.setProperty(u"topmargin", 10)
        self.verticalLayout7.setProperty(u"rightmargin", 10)
        self.verticalLayout7.setProperty(u"bottommargin", 10)
        self.grid3 = QFrame(self.remote)
        self.grid3.setObjectName(u"grid3")
        self.grid3.setProperty(u"minimumsize", QSize(0, 70))
        self.grid3.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout4 = QGridLayout(self.grid3)
        self.gridLayout4.setSpacing(0)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.httpRadio = QRadioButton(self.grid3)
        self.httpRadio.setObjectName(u"httpRadio")

        self.gridLayout4.addWidget(self.httpRadio, 7, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout4.addItem(self.verticalSpacer_13, 2, 0, 1, 8)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout4.addItem(self.verticalSpacer_15, 6, 0, 1, 8)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout4.addItem(self.verticalSpacer_12, 0, 0, 1, 8)

        self.usePublicServerButton = QCommandLinkButton(self.grid3)
        self.usePublicServerButton.setObjectName(u"usePublicServerButton")

        self.gridLayout4.addWidget(self.usePublicServerButton, 9, 0, 1, 4)

        self.portInput = QLineEdit(self.grid3)
        self.portInput.setObjectName(u"portInput")

        self.gridLayout4.addWidget(self.portInput, 3, 1, 1, 4)

        self.testConnectionButton = QPushButton(self.grid3)
        self.testConnectionButton.setObjectName(u"testConnectionButton")
        self.testConnectionButton.setMinimumSize(QSize(50, 30))
        self.testConnectionButton.setFont(font)
        self.testConnectionButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.testConnectionButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.testConnectionButton.setIcon(icon14)

        self.gridLayout4.addWidget(self.testConnectionButton, 9, 7, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout4.addItem(self.verticalSpacer_18, 8, 0, 1, 8)

        self.ipAddressLabel = QLabel(self.grid3)
        self.ipAddressLabel.setObjectName(u"ipAddressLabel")

        self.gridLayout4.addWidget(self.ipAddressLabel, 1, 0, 1, 1)

        self.authTokenLabel = QLabel(self.grid3)
        self.authTokenLabel.setObjectName(u"authTokenLabel")

        self.gridLayout4.addWidget(self.authTokenLabel, 5, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout4.addItem(self.horizontalSpacer_11, 7, 1, 1, 1)

        self.portLabel = QLabel(self.grid3)
        self.portLabel.setObjectName(u"portLabel")

        self.gridLayout4.addWidget(self.portLabel, 3, 0, 1, 1)

        self.ipAddressInput = QLineEdit(self.grid3)
        self.ipAddressInput.setObjectName(u"ipAddressInput")

        self.gridLayout4.addWidget(self.ipAddressInput, 1, 1, 1, 4)

        self.protocolLabel = QLabel(self.grid3)
        self.protocolLabel.setObjectName(u"protocolLabel")

        self.gridLayout4.addWidget(self.protocolLabel, 7, 0, 1, 1)

        self.authTokenInput = QLineEdit(self.grid3)
        self.authTokenInput.setObjectName(u"authTokenInput")

        self.gridLayout4.addWidget(self.authTokenInput, 5, 1, 1, 4)

        self.httpsRadio = QRadioButton(self.grid3)
        self.httpsRadio.setObjectName(u"httpsRadio")

        self.gridLayout4.addWidget(self.httpsRadio, 7, 4, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout4.addItem(self.verticalSpacer_14, 4, 0, 1, 8)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout4.addItem(self.horizontalSpacer_14, 7, 3, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout4.addItem(self.horizontalSpacer_13, 7, 5, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout4.addItem(self.horizontalSpacer_12, 7, 7, 1, 1)


        self.verticalLayout7.addWidget(self.grid3)

        self.dockerStackedWidget.addWidget(self.remote)

        self.verticalLayout3.addWidget(self.dockerStackedWidget)


        self.verticalLayout2.addWidget(self.row_21)

        self.configStackedWidget.addWidget(self.docker)
        self.trimming = QWidget()
        self.trimming.setObjectName(u"trimming")
        self.verticalLayout8 = QVBoxLayout(self.trimming)
        self.verticalLayout8.setSpacing(10)
        self.verticalLayout8.setObjectName(u"verticalLayout8")
        self.verticalLayout8.setProperty(u"leftmargin", 10)
        self.verticalLayout8.setProperty(u"topmargin", 10)
        self.verticalLayout8.setProperty(u"rightmargin", 10)
        self.verticalLayout8.setProperty(u"bottommargin", 10)
        self.row_5 = QFrame(self.trimming)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout9 = QVBoxLayout(self.row_5)
        self.verticalLayout9.setObjectName(u"verticalLayout9")
        self.trimmingTabs = QTabWidget(self.row_5)
        self.trimmingTabs.setObjectName(u"trimmingTabs")
        self.cutadapt = QWidget()
        self.cutadapt.setObjectName(u"cutadapt")
        self.verticalLayout10 = QVBoxLayout(self.cutadapt)
        self.verticalLayout10.setSpacing(10)
        self.verticalLayout10.setObjectName(u"verticalLayout10")
        self.verticalLayout10.setProperty(u"leftmargin", 10)
        self.verticalLayout10.setProperty(u"topmargin", 10)
        self.verticalLayout10.setProperty(u"rightmargin", 10)
        self.verticalLayout10.setProperty(u"bottommargin", 10)
        self.grid4 = QFrame(self.cutadapt)
        self.grid4.setObjectName(u"grid4")
        self.grid4.setProperty(u"minimumsize", QSize(0, 70))
        self.grid4.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout5 = QGridLayout(self.grid4)
        self.gridLayout5.setSpacing(0)
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.r1TrimLeadingInput = QLineEdit(self.grid4)
        self.r1TrimLeadingInput.setObjectName(u"r1TrimLeadingInput")

        self.gridLayout5.addWidget(self.r1TrimLeadingInput, 3, 3, 1, 1)

        self.r2TrimLeadingLabel = QLabel(self.grid4)
        self.r2TrimLeadingLabel.setObjectName(u"r2TrimLeadingLabel")

        self.gridLayout5.addWidget(self.r2TrimLeadingLabel, 3, 7, 1, 1)

        self.r2SequenceInput = QLineEdit(self.grid4)
        self.r2SequenceInput.setObjectName(u"r2SequenceInput")

        self.gridLayout5.addWidget(self.r2SequenceInput, 1, 8, 1, 1)

        self.r2MinLengthInput = QLineEdit(self.grid4)
        self.r2MinLengthInput.setObjectName(u"r2MinLengthInput")

        self.gridLayout5.addWidget(self.r2MinLengthInput, 6, 8, 1, 1)

        self.r1AnchoredLabel = QLabel(self.grid4)
        self.r1AnchoredLabel.setObjectName(u"r1AnchoredLabel")

        self.gridLayout5.addWidget(self.r1AnchoredLabel, 5, 0, 1, 1)

        self.r1MinOverlapInput = QLineEdit(self.grid4)
        self.r1MinOverlapInput.setObjectName(u"r1MinOverlapInput")

        self.gridLayout5.addWidget(self.r1MinOverlapInput, 4, 3, 1, 1)

        self.r2PairFilterLabel = QLabel(self.grid4)
        self.r2PairFilterLabel.setObjectName(u"r2PairFilterLabel")

        self.gridLayout5.addWidget(self.r2PairFilterLabel, 7, 7, 1, 1)

        self.r2AnchoredLabel = QLabel(self.grid4)
        self.r2AnchoredLabel.setObjectName(u"r2AnchoredLabel")

        self.gridLayout5.addWidget(self.r2AnchoredLabel, 5, 7, 1, 1)

        self.r1MinLengthInput = QLineEdit(self.grid4)
        self.r1MinLengthInput.setObjectName(u"r1MinLengthInput")

        self.gridLayout5.addWidget(self.r1MinLengthInput, 6, 3, 1, 1)

        self.r1AnchoredCheckbox = QCheckBox(self.grid4)
        self.r1AnchoredCheckbox.setObjectName(u"r1AnchoredCheckbox")

        self.gridLayout5.addWidget(self.r1AnchoredCheckbox, 5, 3, 1, 1)

        self.r1PairFilterLabel = QLabel(self.grid4)
        self.r1PairFilterLabel.setObjectName(u"r1PairFilterLabel")

        self.gridLayout5.addWidget(self.r1PairFilterLabel, 7, 0, 1, 1)

        self.r2MinLengthLabel = QLabel(self.grid4)
        self.r2MinLengthLabel.setObjectName(u"r2MinLengthLabel")

        self.gridLayout5.addWidget(self.r2MinLengthLabel, 6, 7, 1, 1)

        self.r2ErrorRateValueLabel = QLabel(self.grid4)
        self.r2ErrorRateValueLabel.setObjectName(u"r2ErrorRateValueLabel")

        self.gridLayout5.addWidget(self.r2ErrorRateValueLabel, 2, 9, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout5.addItem(self.horizontalSpacer_21, 1, 9, 7, 2)

        self.r1MinOverlapLabel = QLabel(self.grid4)
        self.r1MinOverlapLabel.setObjectName(u"r1MinOverlapLabel")

        self.gridLayout5.addWidget(self.r1MinOverlapLabel, 4, 0, 1, 1)

        self.r1ErrorRateSlider = QSlider(self.grid4)
        self.r1ErrorRateSlider.setObjectName(u"r1ErrorRateSlider")
        self.r1ErrorRateSlider.setValue(30)
        self.r1ErrorRateSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout5.addWidget(self.r1ErrorRateSlider, 2, 3, 1, 1)

        self.r1ErrorRateValueLabel = QLabel(self.grid4)
        self.r1ErrorRateValueLabel.setObjectName(u"r1ErrorRateValueLabel")

        self.gridLayout5.addWidget(self.r1ErrorRateValueLabel, 2, 4, 1, 1)

        self.r1MinLengthLabel = QLabel(self.grid4)
        self.r1MinLengthLabel.setObjectName(u"r1MinLengthLabel")

        self.gridLayout5.addWidget(self.r1MinLengthLabel, 6, 0, 1, 1)

        self.r2SequenceLabel = QLabel(self.grid4)
        self.r2SequenceLabel.setObjectName(u"r2SequenceLabel")

        self.gridLayout5.addWidget(self.r2SequenceLabel, 1, 7, 1, 1)

        self.useCutadaptCheckbox = QCheckBox(self.grid4)
        self.useCutadaptCheckbox.setObjectName(u"useCutadaptCheckbox")
        self.useCutadaptCheckbox.setChecked(True)

        self.gridLayout5.addWidget(self.useCutadaptCheckbox, 0, 0, 1, 11)

        self.r1SequenceLabel = QLabel(self.grid4)
        self.r1SequenceLabel.setObjectName(u"r1SequenceLabel")

        self.gridLayout5.addWidget(self.r1SequenceLabel, 1, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout5.addItem(self.horizontalSpacer_20, 1, 4, 7, 2)

        self.r2ErrorRateLabel = QLabel(self.grid4)
        self.r2ErrorRateLabel.setObjectName(u"r2ErrorRateLabel")

        self.gridLayout5.addWidget(self.r2ErrorRateLabel, 2, 7, 1, 1)

        self.r2MinOverlapInput = QLineEdit(self.grid4)
        self.r2MinOverlapInput.setObjectName(u"r2MinOverlapInput")

        self.gridLayout5.addWidget(self.r2MinOverlapInput, 4, 8, 1, 1)

        self.r2PairFilterComboBox = QComboBox(self.grid4)
        self.r2PairFilterComboBox.addItem("")
        self.r2PairFilterComboBox.addItem("")
        self.r2PairFilterComboBox.addItem("")
        self.r2PairFilterComboBox.setObjectName(u"r2PairFilterComboBox")

        self.gridLayout5.addWidget(self.r2PairFilterComboBox, 7, 8, 1, 1)

        self.r2MinOverlapLabel = QLabel(self.grid4)
        self.r2MinOverlapLabel.setObjectName(u"r2MinOverlapLabel")

        self.gridLayout5.addWidget(self.r2MinOverlapLabel, 4, 7, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout5.addItem(self.horizontalSpacer_26, 1, 6, 7, 1)

        self.r1SequenceInput = QLineEdit(self.grid4)
        self.r1SequenceInput.setObjectName(u"r1SequenceInput")

        self.gridLayout5.addWidget(self.r1SequenceInput, 1, 3, 1, 1)

        self.r2AnchoredCheckbox = QCheckBox(self.grid4)
        self.r2AnchoredCheckbox.setObjectName(u"r2AnchoredCheckbox")

        self.gridLayout5.addWidget(self.r2AnchoredCheckbox, 5, 8, 1, 1)

        self.r2ErrorRateSlider = QSlider(self.grid4)
        self.r2ErrorRateSlider.setObjectName(u"r2ErrorRateSlider")
        self.r2ErrorRateSlider.setValue(10)
        self.r2ErrorRateSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout5.addWidget(self.r2ErrorRateSlider, 2, 8, 1, 1)

        self.r1PairFilterComboBox = QComboBox(self.grid4)
        self.r1PairFilterComboBox.addItem("")
        self.r1PairFilterComboBox.addItem("")
        self.r1PairFilterComboBox.addItem("")
        self.r1PairFilterComboBox.setObjectName(u"r1PairFilterComboBox")

        self.gridLayout5.addWidget(self.r1PairFilterComboBox, 7, 3, 1, 1)

        self.r2TrimLeadingInput = QLineEdit(self.grid4)
        self.r2TrimLeadingInput.setObjectName(u"r2TrimLeadingInput")

        self.gridLayout5.addWidget(self.r2TrimLeadingInput, 3, 8, 1, 1)

        self.r1TrimLeadingLabel = QLabel(self.grid4)
        self.r1TrimLeadingLabel.setObjectName(u"r1TrimLeadingLabel")

        self.gridLayout5.addWidget(self.r1TrimLeadingLabel, 3, 0, 1, 1)

        self.r1ErrorRateLabel = QLabel(self.grid4)
        self.r1ErrorRateLabel.setObjectName(u"r1ErrorRateLabel")

        self.gridLayout5.addWidget(self.r1ErrorRateLabel, 2, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout5.addItem(self.horizontalSpacer_27, 1, 11, 7, 1)


        self.verticalLayout10.addWidget(self.grid4)

        self.trimmingTabs.addTab(self.cutadapt, "")
        self.fastp = QWidget()
        self.fastp.setObjectName(u"fastp")
        self.verticalLayout11 = QVBoxLayout(self.fastp)
        self.verticalLayout11.setSpacing(10)
        self.verticalLayout11.setObjectName(u"verticalLayout11")
        self.verticalLayout11.setProperty(u"leftmargin", 10)
        self.verticalLayout11.setProperty(u"topmargin", 10)
        self.verticalLayout11.setProperty(u"rightmargin", 10)
        self.verticalLayout11.setProperty(u"bottommargin", 10)
        self.grid5 = QFrame(self.fastp)
        self.grid5.setObjectName(u"grid5")
        self.grid5.setProperty(u"minimumsize", QSize(0, 70))
        self.grid5.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout6 = QGridLayout(self.grid5)
        self.gridLayout6.setSpacing(0)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout6.addItem(self.horizontalSpacer_22, 1, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout6.addItem(self.horizontalSpacer_23, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout6.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.label = QLabel(self.grid5)
        self.label.setObjectName(u"label")

        self.gridLayout6.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout6.addItem(self.verticalSpacer_25, 2, 1, 1, 1)


        self.verticalLayout11.addWidget(self.grid5)

        self.trimmingTabs.addTab(self.fastp, "")
        self.umi_tools = QWidget()
        self.umi_tools.setObjectName(u"umi_tools")
        self.verticalLayout12 = QVBoxLayout(self.umi_tools)
        self.verticalLayout12.setSpacing(10)
        self.verticalLayout12.setObjectName(u"verticalLayout12")
        self.verticalLayout12.setProperty(u"leftmargin", 10)
        self.verticalLayout12.setProperty(u"topmargin", 10)
        self.verticalLayout12.setProperty(u"rightmargin", 10)
        self.verticalLayout12.setProperty(u"bottommargin", 10)
        self.grid6 = QFrame(self.umi_tools)
        self.grid6.setObjectName(u"grid6")
        self.grid6.setProperty(u"minimumsize", QSize(0, 70))
        self.grid6.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout7 = QGridLayout(self.grid6)
        self.gridLayout7.setSpacing(0)
        self.gridLayout7.setObjectName(u"gridLayout7")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout7.addItem(self.horizontalSpacer_25, 1, 2, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout7.addItem(self.horizontalSpacer_24, 1, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout7.addItem(self.verticalSpacer_26, 2, 1, 1, 1)

        self.label_2 = QLabel(self.grid6)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout7.addWidget(self.label_2, 1, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout7.addItem(self.verticalSpacer_27, 0, 1, 1, 1)


        self.verticalLayout12.addWidget(self.grid6)

        self.trimmingTabs.addTab(self.umi_tools, "")

        self.verticalLayout9.addWidget(self.trimmingTabs)


        self.verticalLayout8.addWidget(self.row_5)

        self.row_4 = QFrame(self.trimming)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setProperty(u"minimumsize", QSize(0, 70))
        self.row_4.setProperty(u"maximumsize", QSize(16777215, 70))
        self.verticalLayout13 = QVBoxLayout(self.row_4)
        self.verticalLayout13.setSpacing(0)
        self.verticalLayout13.setObjectName(u"verticalLayout13")
        self.verticalLayout13.setProperty(u"leftmargin", 0)
        self.verticalLayout13.setProperty(u"topmargin", 0)
        self.verticalLayout13.setProperty(u"rightmargin", 0)
        self.verticalLayout13.setProperty(u"bottommargin", 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.readLenCheckbox = QCheckBox(self.row_4)
        self.readLenCheckbox.setObjectName(u"readLenCheckbox")
        self.readLenCheckbox.setChecked(True)

        self.gridLayout_3.addWidget(self.readLenCheckbox, 0, 5, 2, 1)

        self.qualityControlLabel = QLabel(self.row_4)
        self.qualityControlLabel.setObjectName(u"qualityControlLabel")

        self.gridLayout_3.addWidget(self.qualityControlLabel, 0, 0, 2, 1)

        self.qcAfterCheckbox = QCheckBox(self.row_4)
        self.qcAfterCheckbox.setObjectName(u"qcAfterCheckbox")
        self.qcAfterCheckbox.setChecked(True)

        self.gridLayout_3.addWidget(self.qcAfterCheckbox, 0, 3, 2, 2)

        self.qcBeforeCheckbox = QCheckBox(self.row_4)
        self.qcBeforeCheckbox.setObjectName(u"qcBeforeCheckbox")
        self.qcBeforeCheckbox.setChecked(True)

        self.gridLayout_3.addWidget(self.qcBeforeCheckbox, 0, 1, 2, 2)


        self.verticalLayout13.addLayout(self.gridLayout_3)


        self.verticalLayout8.addWidget(self.row_4)

        self.configStackedWidget.addWidget(self.trimming)
        self.read_mapping = QWidget()
        self.read_mapping.setObjectName(u"read_mapping")
        self.verticalLayout14 = QVBoxLayout(self.read_mapping)
        self.verticalLayout14.setSpacing(10)
        self.verticalLayout14.setObjectName(u"verticalLayout14")
        self.verticalLayout14.setProperty(u"leftmargin", 10)
        self.verticalLayout14.setProperty(u"topmargin", 10)
        self.verticalLayout14.setProperty(u"rightmargin", 10)
        self.verticalLayout14.setProperty(u"bottommargin", 10)
        self.row_6 = QFrame(self.read_mapping)
        self.row_6.setObjectName(u"row_6")
        self.row_6.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout15 = QVBoxLayout(self.row_6)
        self.verticalLayout15.setObjectName(u"verticalLayout15")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_29, 1, 0, 1, 1)

        self.referenceGenomeLabel = QLabel(self.row_6)
        self.referenceGenomeLabel.setObjectName(u"referenceGenomeLabel")

        self.gridLayout_4.addWidget(self.referenceGenomeLabel, 1, 1, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_28, 1, 3, 1, 1)

        self.referenceGenomeComboBox = QComboBox(self.row_6)
        self.referenceGenomeComboBox.setObjectName(u"referenceGenomeComboBox")
        self.referenceGenomeComboBox.setMinimumSize(QSize(140, 0))

        self.gridLayout_4.addWidget(self.referenceGenomeComboBox, 1, 2, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_29, 2, 0, 1, 4)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_28, 0, 0, 1, 4)


        self.verticalLayout15.addLayout(self.gridLayout_4)


        self.verticalLayout14.addWidget(self.row_6)

        self.configStackedWidget.addWidget(self.read_mapping)
        self.site_analysis = QWidget()
        self.site_analysis.setObjectName(u"site_analysis")
        self.verticalLayout16 = QVBoxLayout(self.site_analysis)
        self.verticalLayout16.setSpacing(10)
        self.verticalLayout16.setObjectName(u"verticalLayout16")
        self.verticalLayout16.setProperty(u"leftmargin", 10)
        self.verticalLayout16.setProperty(u"topmargin", 10)
        self.verticalLayout16.setProperty(u"rightmargin", 10)
        self.verticalLayout16.setProperty(u"bottommargin", 10)
        self.row_12 = QFrame(self.site_analysis)
        self.row_12.setObjectName(u"row_12")
        self.row_12.setProperty(u"minimumsize", QSize(0, 70))
        self.row_12.setProperty(u"maximumsize", QSize(16777215, 70))
        self.verticalLayout17 = QVBoxLayout(self.row_12)
        self.verticalLayout17.setSpacing(0)
        self.verticalLayout17.setObjectName(u"verticalLayout17")
        self.verticalLayout17.setProperty(u"leftmargin", 0)
        self.verticalLayout17.setProperty(u"topmargin", 0)
        self.verticalLayout17.setProperty(u"rightmargin", 0)
        self.verticalLayout17.setProperty(u"bottommargin", 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_30, 0, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_31, 1, 2, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_30, 1, 0, 1, 1)

        self.label_3 = QLabel(self.row_12)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 1, 1, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_31, 2, 1, 1, 1)


        self.verticalLayout17.addLayout(self.gridLayout_5)


        self.verticalLayout16.addWidget(self.row_12)

        self.configStackedWidget.addWidget(self.site_analysis)

        self.gridLayout_2.addWidget(self.configStackedWidget, 0, 4, 21, 7)

        self.r2InputButton = QPushButton(self.runConfigurationTab)
        self.r2InputButton.setObjectName(u"r2InputButton")
        self.r2InputButton.setMinimumSize(QSize(50, 30))
        self.r2InputButton.setFont(font)
        self.r2InputButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.r2InputButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.r2InputButton.setIcon(icon9)

        self.gridLayout_2.addWidget(self.r2InputButton, 3, 3, 1, 1)

        self.umiCheckbox = QCheckBox(self.runConfigurationTab)
        self.umiCheckbox.setObjectName(u"umiCheckbox")

        self.gridLayout_2.addWidget(self.umiCheckbox, 5, 0, 1, 2)

        self.configStepsLabel = QLabel(self.runConfigurationTab)
        self.configStepsLabel.setObjectName(u"configStepsLabel")

        self.gridLayout_2.addWidget(self.configStepsLabel, 8, 0, 1, 4)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 7, 0, 1, 4)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 6, 0, 1, 4)

        self.dockerConfig = QPushButton(self.runConfigurationTab)
        self.dockerConfig.setObjectName(u"dockerConfig")
        self.dockerConfig.setMinimumSize(QSize(50, 30))
        self.dockerConfig.setFont(font)
        self.dockerConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dockerConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-docker.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dockerConfig.setIcon(icon15)

        self.gridLayout_2.addWidget(self.dockerConfig, 9, 0, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 10, 0, 1, 4)

        self.trimmingConfig = QPushButton(self.runConfigurationTab)
        self.trimmingConfig.setObjectName(u"trimmingConfig")
        self.trimmingConfig.setMinimumSize(QSize(50, 30))
        self.trimmingConfig.setFont(font)
        self.trimmingConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.trimmingConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.trimmingConfig.setIcon(icon16)

        self.gridLayout_2.addWidget(self.trimmingConfig, 11, 0, 1, 4)

        self.readMappingConfig = QPushButton(self.runConfigurationTab)
        self.readMappingConfig.setObjectName(u"readMappingConfig")
        self.readMappingConfig.setMinimumSize(QSize(50, 30))
        self.readMappingConfig.setFont(font)
        self.readMappingConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.readMappingConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.readMappingConfig.setIcon(icon17)

        self.gridLayout_2.addWidget(self.readMappingConfig, 13, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 12, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 14, 0, 1, 4)

        self.siteAnalysisConfig = QPushButton(self.runConfigurationTab)
        self.siteAnalysisConfig.setObjectName(u"siteAnalysisConfig")
        self.siteAnalysisConfig.setMinimumSize(QSize(50, 30))
        self.siteAnalysisConfig.setFont(font)
        self.siteAnalysisConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.siteAnalysisConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/cil-terminal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.siteAnalysisConfig.setIcon(icon18)

        self.gridLayout_2.addWidget(self.siteAnalysisConfig, 15, 0, 3, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 18, 0, 3, 4)

        self.resetButton = QPushButton(self.runConfigurationTab)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(50, 30))
        self.resetButton.setFont(font)
        self.resetButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resetButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-fire.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetButton.setIcon(icon19)

        self.gridLayout_2.addWidget(self.resetButton, 21, 0, 1, 1)

        self.restoreDefaultsButton = QPushButton(self.runConfigurationTab)
        self.restoreDefaultsButton.setObjectName(u"restoreDefaultsButton")
        self.restoreDefaultsButton.setMinimumSize(QSize(50, 30))
        self.restoreDefaultsButton.setFont(font)
        self.restoreDefaultsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.restoreDefaultsButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon20 = QIcon()
        icon20.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreDefaultsButton.setIcon(icon20)

        self.gridLayout_2.addWidget(self.restoreDefaultsButton, 21, 1, 1, 3)

        self.umiInput = QLineEdit(self.runConfigurationTab)
        self.umiInput.setObjectName(u"umiInput")

        self.gridLayout_2.addWidget(self.umiInput, 5, 2, 1, 2)

        self.R1Label = QLabel(self.runConfigurationTab)
        self.R1Label.setObjectName(u"R1Label")

        self.gridLayout_2.addWidget(self.R1Label, 0, 0, 2, 1)

        self.R2Label = QLabel(self.runConfigurationTab)
        self.R2Label.setObjectName(u"R2Label")

        self.gridLayout_2.addWidget(self.R2Label, 3, 0, 1, 1)

        self.r2Input = QLineEdit(self.runConfigurationTab)
        self.r2Input.setObjectName(u"r2Input")

        self.gridLayout_2.addWidget(self.r2Input, 3, 1, 1, 2)

        self.r1Input = QLineEdit(self.runConfigurationTab)
        self.r1Input.setObjectName(u"r1Input")

        self.gridLayout_2.addWidget(self.r1Input, 0, 1, 2, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 4)


        self.verticalLayout1.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.runConfigurationTab)
        self.resultsOverviewTab = QWidget()
        self.resultsOverviewTab.setObjectName(u"resultsOverviewTab")
        self.resultsOverviewTab.setStyleSheet(u"")
        self.verticalLayout18 = QVBoxLayout(self.resultsOverviewTab)
        self.verticalLayout18.setSpacing(10)
        self.verticalLayout18.setObjectName(u"verticalLayout18")
        self.verticalLayout18.setContentsMargins(10, 10, 10, 10)
        self.resultsSplitter = QSplitter(self.resultsOverviewTab)
        self.resultsSplitter.setObjectName(u"resultsSplitter")
        self.resultsSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.leftPaneWidget = QWidget(self.resultsSplitter)
        self.leftPaneWidget.setObjectName(u"leftPaneWidget")
        self.leftPaneLayout = QVBoxLayout(self.leftPaneWidget)
        self.leftPaneLayout.setSpacing(5)
        self.leftPaneLayout.setObjectName(u"leftPaneLayout")
        self.leftPaneLayout.setContentsMargins(0, 0, 5, 0)
        self.fileTreeWidget = QTreeWidget(self.leftPaneWidget)
        self.fileTreeWidget.setObjectName(u"fileTreeWidget")
        self.fileTreeWidget.setHeaderHidden(True)

        self.leftPaneLayout.addWidget(self.fileTreeWidget)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(5)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.openFileButton = QPushButton(self.leftPaneWidget)
        self.openFileButton.setObjectName(u"openFileButton")
        self.openFileButton.setMinimumSize(QSize(50, 30))
        self.openFileButton.setFont(font)
        self.openFileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openFileButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon21 = QIcon()
        icon21.addFile(u":/icons/images/icons/cil-external-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openFileButton.setIcon(icon21)

        self.buttonLayout.addWidget(self.openFileButton)

        self.openDirectoryButton = QPushButton(self.leftPaneWidget)
        self.openDirectoryButton.setObjectName(u"openDirectoryButton")
        self.openDirectoryButton.setMinimumSize(QSize(50, 30))
        self.openDirectoryButton.setFont(font)
        self.openDirectoryButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openDirectoryButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.openDirectoryButton.setIcon(icon9)

        self.buttonLayout.addWidget(self.openDirectoryButton)


        self.leftPaneLayout.addLayout(self.buttonLayout)

        self.resultsSplitter.addWidget(self.leftPaneWidget)
        self.rightPaneWidget = QWidget(self.resultsSplitter)
        self.rightPaneWidget.setObjectName(u"rightPaneWidget")
        self.rightPaneLayout = QVBoxLayout(self.rightPaneWidget)
        self.rightPaneLayout.setSpacing(5)
        self.rightPaneLayout.setObjectName(u"rightPaneLayout")
        self.rightPaneLayout.setContentsMargins(5, 0, 0, 0)
        self.fileContentTable = QTableWidget(self.rightPaneWidget)
        self.fileContentTable.setObjectName(u"fileContentTable")
        self.fileContentTable.setAlternatingRowColors(True)
        self.fileContentTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.fileContentTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fileContentTable.setGridStyle(Qt.PenStyle.SolidLine)

        self.rightPaneLayout.addWidget(self.fileContentTable)

        self.fileStatusLabel = QLabel(self.rightPaneWidget)
        self.fileStatusLabel.setObjectName(u"fileStatusLabel")
        self.fileStatusLabel.setStyleSheet(u"color: rgb(100, 100, 100); font-style: italic;")
        self.fileStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.rightPaneLayout.addWidget(self.fileStatusLabel)

        self.resultsSplitter.addWidget(self.rightPaneWidget)

        self.verticalLayout18.addWidget(self.resultsSplitter)

        self.stackedWidget.addWidget(self.resultsOverviewTab)
        self.runProgressTab = QWidget()
        self.runProgressTab.setObjectName(u"runProgressTab")
        self.runProgressTab.setStyleSheet(u"")
        self.verticalLayout19 = QVBoxLayout(self.runProgressTab)
        self.verticalLayout19.setSpacing(10)
        self.verticalLayout19.setObjectName(u"verticalLayout19")
        self.verticalLayout19.setContentsMargins(10, 10, 10, 10)
        self.row_13 = QFrame(self.runProgressTab)
        self.row_13.setObjectName(u"row_13")
        self.row_13.setMinimumSize(QSize(0, 70))
        self.row_13.setMaximumSize(QSize(16777215, 70))
        self.row_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.row_13)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout19.addWidget(self.row_13)

        self.row_22 = QFrame(self.runProgressTab)
        self.row_22.setObjectName(u"row_22")
        self.row_22.setMinimumSize(QSize(0, 150))
        self.row_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.row_22)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.stdOut = QTextBrowser(self.row_22)
        self.stdOut.setObjectName(u"stdOut")

        self.verticalLayout_191.addWidget(self.stdOut)


        self.verticalLayout19.addWidget(self.row_22)

        self.row_31 = QFrame(self.runProgressTab)
        self.row_31.setObjectName(u"row_31")
        self.row_31.setMinimumSize(QSize(0, 50))
        self.row_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.row_31)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cleanButton = QPushButton(self.row_31)
        self.cleanButton.setObjectName(u"cleanButton")
        self.cleanButton.setMinimumSize(QSize(50, 30))
        self.cleanButton.setFont(font)
        self.cleanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cleanButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cleanButton.setIcon(icon19)

        self.horizontalLayout_6.addWidget(self.cleanButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.pauseButton = QPushButton(self.row_31)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setMinimumSize(QSize(50, 30))
        self.pauseButton.setFont(font)
        self.pauseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pauseButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon22 = QIcon()
        icon22.addFile(u":/icons/images/icons/cil-media-stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseButton.setIcon(icon22)

        self.horizontalLayout_6.addWidget(self.pauseButton)

        self.resumeButton = QPushButton(self.row_31)
        self.resumeButton.setObjectName(u"resumeButton")
        self.resumeButton.setMinimumSize(QSize(50, 30))
        self.resumeButton.setFont(font)
        self.resumeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resumeButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon23 = QIcon()
        icon23.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resumeButton.setIcon(icon23)

        self.horizontalLayout_6.addWidget(self.resumeButton)

        self.runButton = QPushButton(self.row_31)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setMinimumSize(QSize(50, 30))
        self.runButton.setFont(font)
        self.runButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.runButton.setIcon(icon23)

        self.horizontalLayout_6.addWidget(self.runButton)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_6)


        self.verticalLayout19.addWidget(self.row_31)

        self.stackedWidget.addWidget(self.runProgressTab)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.settingsLabel = QLabel(self.topMenus)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.settingsLabel.setFont(font4)
        self.settingsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.settingsLabel)

        self.restartNoticeLabel = QLabel(self.topMenus)
        self.restartNoticeLabel.setObjectName(u"restartNoticeLabel")
        self.restartNoticeLabel.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setItalic(True)
        self.restartNoticeLabel.setFont(font5)
        self.restartNoticeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.restartNoticeLabel.setStyleSheet(u"color: #888888;")

        self.verticalLayout_14.addWidget(self.restartNoticeLabel)

        self.enableCustomTitleBarLayout = QHBoxLayout()
        self.enableCustomTitleBarLayout.setObjectName(u"enableCustomTitleBarLayout")
        self.enableCustomTitleBarLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.enableCustomTitleBarLayout.addItem(self.enableCustomTitleBarLeftSpacer)

        self.enableCustomTitleBarCheckBox = QCheckBox(self.topMenus)
        self.enableCustomTitleBarCheckBox.setObjectName(u"enableCustomTitleBarCheckBox")
        self.enableCustomTitleBarCheckBox.setMinimumSize(QSize(0, 30))
        self.enableCustomTitleBarCheckBox.setFont(font)

        self.enableCustomTitleBarLayout.addWidget(self.enableCustomTitleBarCheckBox)

        self.enableCustomTitleBarRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.enableCustomTitleBarLayout.addItem(self.enableCustomTitleBarRightSpacer)


        self.verticalLayout_14.addLayout(self.enableCustomTitleBarLayout)

        self.firstStartLayout = QHBoxLayout()
        self.firstStartLayout.setObjectName(u"firstStartLayout")
        self.firstStartLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.firstStartLayout.addItem(self.firstStartLeftSpacer)

        self.firstStartCheckBox = QCheckBox(self.topMenus)
        self.firstStartCheckBox.setObjectName(u"firstStartCheckBox")
        self.firstStartCheckBox.setMinimumSize(QSize(0, 30))
        self.firstStartCheckBox.setFont(font)

        self.firstStartLayout.addWidget(self.firstStartCheckBox)

        self.firstStartRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.firstStartLayout.addItem(self.firstStartRightSpacer)


        self.verticalLayout_14.addLayout(self.firstStartLayout)

        self.line = QFrame(self.topMenus)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.emailButton = QPushButton(self.topMenus)
        self.emailButton.setObjectName(u"emailButton")
        sizePolicy.setHeightForWidth(self.emailButton.sizePolicy().hasHeightForWidth())
        self.emailButton.setSizePolicy(sizePolicy)
        self.emailButton.setMinimumSize(QSize(0, 45))
        self.emailButton.setFont(font)
        self.emailButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.emailButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.emailButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.emailButton)

        self.issueButton = QPushButton(self.topMenus)
        self.issueButton.setObjectName(u"issueButton")
        sizePolicy.setHeightForWidth(self.issueButton.sizePolicy().hasHeightForWidth())
        self.issueButton.setSizePolicy(sizePolicy)
        self.issueButton.setMinimumSize(QSize(0, 45))
        self.issueButton.setFont(font)
        self.issueButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.issueButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.issueButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-wifi-signal-off.png);")

        self.verticalLayout_14.addWidget(self.issueButton)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.umiInput, self.umiCheckbox)
        QWidget.setTabOrder(self.umiCheckbox, self.trimmingConfig)
        QWidget.setTabOrder(self.trimmingConfig, self.readMappingConfig)
        QWidget.setTabOrder(self.readMappingConfig, self.siteAnalysisConfig)
        QWidget.setTabOrder(self.siteAnalysisConfig, self.restoreDefaultsButton)
        QWidget.setTabOrder(self.restoreDefaultsButton, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.helpButton)
        QWidget.setTabOrder(self.helpButton, self.createRunButton)
        QWidget.setTabOrder(self.createRunButton, self.selectRunButton)
        QWidget.setTabOrder(self.selectRunButton, self.refreshRunButton)
        QWidget.setTabOrder(self.refreshRunButton, self.deleteRunButton)
        QWidget.setTabOrder(self.deleteRunButton, self.runsTable)
        QWidget.setTabOrder(self.runsTable, self.openFolderLocationButton)
        QWidget.setTabOrder(self.openFolderLocationButton, self.renameRunButton)
        QWidget.setTabOrder(self.renameRunButton, self.importRunButton)
        QWidget.setTabOrder(self.importRunButton, self.exportRunButton)
        QWidget.setTabOrder(self.exportRunButton, self.stdOut)
        QWidget.setTabOrder(self.stdOut, self.moreButton)
        QWidget.setTabOrder(self.moreButton, self.runManagerButton)
        QWidget.setTabOrder(self.runManagerButton, self.minimizeAppButton)
        QWidget.setTabOrder(self.minimizeAppButton, self.runConfigurationButton)
        QWidget.setTabOrder(self.runConfigurationButton, self.runProgressButton)
        QWidget.setTabOrder(self.runProgressButton, self.resultsOverviewButton)
        QWidget.setTabOrder(self.resultsOverviewButton, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnButton)
        QWidget.setTabOrder(self.extraCloseColumnButton, self.aboutText)
        QWidget.setTabOrder(self.aboutText, self.closeAppButton)
        QWidget.setTabOrder(self.closeAppButton, self.settingsTopButton)
        QWidget.setTabOrder(self.settingsTopButton, self.maximizeRestoreAppButton)
        QWidget.setTabOrder(self.maximizeRestoreAppButton, self.toggleButton)
        QWidget.setTabOrder(self.toggleButton, self.enableCustomTitleBarCheckBox)
        QWidget.setTabOrder(self.enableCustomTitleBarCheckBox, self.firstStartCheckBox)
        QWidget.setTabOrder(self.firstStartCheckBox, self.emailButton)
        QWidget.setTabOrder(self.emailButton, self.issueButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.configStackedWidget.setCurrentIndex(0)
        self.dockerStackedWidget.setCurrentIndex(0)
        self.isInstalledStackedWidget.setCurrentIndex(0)
        self.trimmingTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"qsLAM_PCR_AIO", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Erasmus MC", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.runManagerButton.setText(QCoreApplication.translate("MainWindow", u"Manage Runs", None))
        self.runConfigurationButton.setText(QCoreApplication.translate("MainWindow", u"Edit Run Configuration", None))
        self.runProgressButton.setText(QCoreApplication.translate("MainWindow", u"Run Progress", None))
        self.resultsOverviewButton.setText(QCoreApplication.translate("MainWindow", u"Results Overview", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close about", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnButton.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.aboutText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We are Erasmus MC. Every day our staff, volunteers, and students work with dedication and commitment and are passionate about everything that we stand for.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Patient care</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\">At Erasmus MC we work on top-clinical care for patients with complex care needs, rare diseases, or acute needs for care and treatment.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Education</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We work on distinctive, high-quality education that appeals to ambitious, inquisitive, and talented students and addresses the healthcare issues of tomorrow.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Research</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We also work on cutting-edge, world class international medical research that helps to understand, predict, treat, and prevent diseases and health conditions.</p"
                        ">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Valorization</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Like every university medical center, our three core tasks at Erasmus MC are: patient care, education, and research. Valorization, which is the social or economic use of knowledge gained through research, is generally regarded as a fourth core task.</p></body></html>", None))
        self.moreButton.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.currentlySelectedText.setText(QCoreApplication.translate("MainWindow", u"Currently Selected Run: ", None))
        self.currentlySelected.setText(QCoreApplication.translate("MainWindow", u"None", None))
#if QT_CONFIG(tooltip)
        self.settingsTopButton.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopButton.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppButton.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppButton.setText("")
        self.createRunButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.selectRunButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.refreshRunButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.deleteRunButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.runsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.runsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Creation Timestamp", None));
        ___qtablewidgetitem2 = self.runsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtablewidgetitem3 = self.runsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Run Timestamp", None));
        self.importRunButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.openFolderLocationButton.setText(QCoreApplication.translate("MainWindow", u"Open Folder Location", None))
        self.exportRunButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.renameRunButton.setText(QCoreApplication.translate("MainWindow", u"Rename Run", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.r1InputButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.localRadio.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.remoteRadio.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.dockerLabel.setText(QCoreApplication.translate("MainWindow", u"Do you want to run the qsLAM PCR pipeline locally or on a remote server?\n"
"You can do some trial runs on our public test server.", None))
        self.checkAgainButton_2.setText(QCoreApplication.translate("MainWindow", u"Check Again", None))
        self.dockerFoundLabel.setText(QCoreApplication.translate("MainWindow", u"Docker found! We will take it from here", None))
        self.dockerPathLabel_2.setText(QCoreApplication.translate("MainWindow", u"Do you need to change the docker path?", None))
        self.checkAgainButton.setText(QCoreApplication.translate("MainWindow", u"Check Again", None))
        self.dockerPathInput.setText(QCoreApplication.translate("MainWindow", u"docker", None))
        self.dockerPathLabel.setText(QCoreApplication.translate("MainWindow", u"Docker path: ", None))
        self.dockerNotFoundLabel.setText(QCoreApplication.translate("MainWindow", u"Docker not found on your computer!", None))
        self.httpRadio.setText(QCoreApplication.translate("MainWindow", u"Http", None))
        self.usePublicServerButton.setText(QCoreApplication.translate("MainWindow", u"Want to use our public test server instead?", None))
        self.testConnectionButton.setText(QCoreApplication.translate("MainWindow", u"Test Connection", None))
        self.ipAddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP Address: ", None))
        self.authTokenLabel.setText(QCoreApplication.translate("MainWindow", u"Authentication Token: ", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Port: ", None))
        self.protocolLabel.setText(QCoreApplication.translate("MainWindow", u"Protocol: ", None))
        self.httpsRadio.setText(QCoreApplication.translate("MainWindow", u"Https", None))
        self.r1TrimLeadingInput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r2TrimLeadingLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Trim leading: ", None))
        self.r2MinLengthInput.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.r1AnchoredLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Anchored: ", None))
        self.r1MinOverlapInput.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.r2PairFilterLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Pair filter: ", None))
        self.r2AnchoredLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Anchored: ", None))
        self.r1MinLengthInput.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.r1AnchoredCheckbox.setText("")
        self.r1PairFilterLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Pair filter: ", None))
        self.r2MinLengthLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Min length:", None))
        self.r2ErrorRateValueLabel.setText(QCoreApplication.translate("MainWindow", u" 0.1", None))
        self.r1MinOverlapLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Min overlap: ", None))
        self.r1ErrorRateValueLabel.setText(QCoreApplication.translate("MainWindow", u" 0.3", None))
        self.r1MinLengthLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Min length:", None))
        self.r2SequenceLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Sequence: ", None))
        self.useCutadaptCheckbox.setText(QCoreApplication.translate("MainWindow", u"Use Cutadapt", None))
        self.r1SequenceLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Sequence: ", None))
        self.r2ErrorRateLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Error rate: ", None))
        self.r2MinOverlapInput.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.r2PairFilterComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Both", None))
        self.r2PairFilterComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Any", None))
        self.r2PairFilterComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"First", None))

        self.r2MinOverlapLabel.setText(QCoreApplication.translate("MainWindow", u"R2 Min overlap: ", None))
        self.r2AnchoredCheckbox.setText("")
        self.r1PairFilterComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Both", None))
        self.r1PairFilterComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Any", None))
        self.r1PairFilterComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"First", None))

        self.r2TrimLeadingInput.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r1TrimLeadingLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Trim leading: ", None))
        self.r1ErrorRateLabel.setText(QCoreApplication.translate("MainWindow", u"R1 Error rate: ", None))
        self.trimmingTabs.setTabText(self.trimmingTabs.indexOf(self.cutadapt), QCoreApplication.translate("MainWindow", u"Cutadapt", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nothing to see here yet :)", None))
        self.trimmingTabs.setTabText(self.trimmingTabs.indexOf(self.fastp), QCoreApplication.translate("MainWindow", u"Fastp", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nothing to see here yet :)", None))
        self.trimmingTabs.setTabText(self.trimmingTabs.indexOf(self.umi_tools), QCoreApplication.translate("MainWindow", u"UMI Tools", None))
        self.readLenCheckbox.setText(QCoreApplication.translate("MainWindow", u"Read length\n"
"after trimming", None))
        self.qualityControlLabel.setText(QCoreApplication.translate("MainWindow", u"Quality control: ", None))
        self.qcAfterCheckbox.setText(QCoreApplication.translate("MainWindow", u"Do a quality control\n"
"check after trimming", None))
        self.qcBeforeCheckbox.setText(QCoreApplication.translate("MainWindow", u"Do a quality control\n"
"check before trimming", None))
        self.referenceGenomeLabel.setText(QCoreApplication.translate("MainWindow", u"Reference genome: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nothing to see here yet :)", None))
        self.r2InputButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.umiCheckbox.setText(QCoreApplication.translate("MainWindow", u"Unique Molecular Identifier?", None))
        self.configStepsLabel.setText(QCoreApplication.translate("MainWindow", u"Please complete all configuration steps below:", None))
        self.dockerConfig.setText(QCoreApplication.translate("MainWindow", u"Docker configuration", None))
        self.trimmingConfig.setText(QCoreApplication.translate("MainWindow", u"Adapter and primer trimming", None))
        self.readMappingConfig.setText(QCoreApplication.translate("MainWindow", u"Read mapping", None))
        self.siteAnalysisConfig.setText(QCoreApplication.translate("MainWindow", u"Site analysis", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.restoreDefaultsButton.setText(QCoreApplication.translate("MainWindow", u"Restore Defaults", None))
        self.R1Label.setText(QCoreApplication.translate("MainWindow", u"Read 1: ", None))
        self.R2Label.setText(QCoreApplication.translate("MainWindow", u"Read 2: ", None))
        ___qtreewidgetitem = self.fileTreeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open in Default App", None))
        self.openDirectoryButton.setText(QCoreApplication.translate("MainWindow", u"Open Run Directory", None))
        self.fileStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Select a file to view its contents", None))
        self.stdOut.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.cleanButton.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.resumeButton.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run Full Pipeline", None))
        self.settingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.restartNoticeLabel.setText(QCoreApplication.translate("MainWindow", u"* Restart required to apply changes", None))
        self.enableCustomTitleBarCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable Custom Title Bar", None))
        self.firstStartCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show Welcome Dialog", None))
        self.emailButton.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.issueButton.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Miro & Liam Weitzel", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

