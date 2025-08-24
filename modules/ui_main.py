# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
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
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
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
"#extraCloseColumnButton { back"
                        "ground-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
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
"	bo"
                        "rder-top: 3px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
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
"	backg"
                        "round-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(224, 247, 247);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: #00216D;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(204, 204, 204);\n"
"	border-bottom: 1px solid rgb(220, 220, 220);\n"
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
"    border-right: 1px solid rgb(220, 220, "
                        "220);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(245, 245, 245);\n"
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
"QPlainTextEdit  QScrollBar:ho"
                        "rizontal {\n"
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
"QScroll"
                        "Bar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
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
"    subcont"
                        "rol-origin: margin;\n"
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
"QRadioButton::indicator:h"
                        "over {\n"
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
        self.projectManagerButton = QPushButton(self.topMenu)
        self.projectManagerButton.setObjectName(u"projectManagerButton")
        sizePolicy.setHeightForWidth(self.projectManagerButton.sizePolicy().hasHeightForWidth())
        self.projectManagerButton.setSizePolicy(sizePolicy)
        self.projectManagerButton.setMinimumSize(QSize(0, 45))
        self.projectManagerButton.setFont(font)
        self.projectManagerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.projectManagerButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.projectManagerButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_8.addWidget(self.projectManagerButton)

        self.setupViewButton = QPushButton(self.topMenu)
        self.setupViewButton.setObjectName(u"setupViewButton")
        sizePolicy.setHeightForWidth(self.setupViewButton.sizePolicy().hasHeightForWidth())
        self.setupViewButton.setSizePolicy(sizePolicy)
        self.setupViewButton.setMinimumSize(QSize(0, 45))
        self.setupViewButton.setFont(font)
        self.setupViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setupViewButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.setupViewButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.setupViewButton)

        self.runViewButton = QPushButton(self.topMenu)
        self.runViewButton.setObjectName(u"runViewButton")
        self.runViewButton.setMinimumSize(QSize(0, 45))
        self.runViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runViewButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.runViewButton)

        self.analysisViewButton = QPushButton(self.topMenu)
        self.analysisViewButton.setObjectName(u"analysisViewButton")
        self.analysisViewButton.setMinimumSize(QSize(0, 45))
        self.analysisViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.analysisViewButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.analysisViewButton)


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
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


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
        self.projectManager = QWidget()
        self.projectManager.setObjectName(u"projectManager")
        self.projectManager.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.projectManager)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.projectManager)
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

        self.label_5 = QLabel(self.frame_content_wid_1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_content_wid_1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

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

        self.row_2 = QFrame(self.projectManager)
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
        if (self.runsTable.rowCount() < 22):
            self.runsTable.setRowCount(22)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(16, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(17, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(18, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(19, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(20, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.runsTable.setVerticalHeaderItem(21, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.runsTable.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.runsTable.setItem(0, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.runsTable.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.runsTable.setItem(0, 3, __qtablewidgetitem29)
        self.runsTable.setObjectName(u"runsTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.runsTable.sizePolicy().hasHeightForWidth())
        self.runsTable.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
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
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush)
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

        self.row_3 = QFrame(self.projectManager)
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

        self.gridLayout.addWidget(self.importRunButton, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.exportRunButton = QPushButton(self.row_3)
        self.exportRunButton.setObjectName(u"exportRunButton")
        self.exportRunButton.setMinimumSize(QSize(50, 30))
        self.exportRunButton.setFont(font)
        self.exportRunButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exportRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportRunButton.setIcon(icon9)

        self.gridLayout.addWidget(self.exportRunButton, 0, 4, 1, 1)

        self.openFolderLocationButton = QPushButton(self.row_3)
        self.openFolderLocationButton.setObjectName(u"openFolderLocationButton")
        self.openFolderLocationButton.setMinimumSize(QSize(50, 30))
        self.openFolderLocationButton.setFont(font)
        self.openFolderLocationButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.openFolderLocationButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openFolderLocationButton.setIcon(icon10)

        self.gridLayout.addWidget(self.openFolderLocationButton, 0, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.projectManager)
        self.setupView = QWidget()
        self.setupView.setObjectName(u"setupView")
        self.setupView.setStyleSheet(u"")
        self.verticalLayout1 = QVBoxLayout(self.setupView)
        self.verticalLayout1.setSpacing(10)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.verticalLayout1.setContentsMargins(10, 10, 10, 10)
        self.row_11 = QFrame(self.setupView)
        self.row_11.setObjectName(u"row_11")
        self.row_11.setMinimumSize(QSize(0, 120))
        self.row_11.setMaximumSize(QSize(16777215, 120))
        self.row_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.row_11)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.nameRunLabel = QLabel(self.row_11)
        self.nameRunLabel.setObjectName(u"nameRunLabel")

        self.gridLayout_2.addWidget(self.nameRunLabel, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 0, 1, 2)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_14, 6, 0, 1, 2)

        self.nameRunInput = QLineEdit(self.row_11)
        self.nameRunInput.setObjectName(u"nameRunInput")

        self.gridLayout_2.addWidget(self.nameRunInput, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.adapterSequenceLabel = QLabel(self.row_11)
        self.adapterSequenceLabel.setObjectName(u"adapterSequenceLabel")

        self.gridLayout_2.addWidget(self.adapterSequenceLabel, 3, 0, 1, 1)

        self.ltrPrimerSequenceLabel = QLabel(self.row_11)
        self.ltrPrimerSequenceLabel.setObjectName(u"ltrPrimerSequenceLabel")

        self.gridLayout_2.addWidget(self.ltrPrimerSequenceLabel, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.adapterSequenceInput = QLineEdit(self.row_11)
        self.adapterSequenceInput.setObjectName(u"adapterSequenceInput")

        self.gridLayout_2.addWidget(self.adapterSequenceInput, 3, 1, 1, 1)

        self.ltrPrimerSequenceInput = QLineEdit(self.row_11)
        self.ltrPrimerSequenceInput.setObjectName(u"ltrPrimerSequenceInput")

        self.gridLayout_2.addWidget(self.ltrPrimerSequenceInput, 5, 1, 1, 1)


        self.verticalLayout_161.addLayout(self.gridLayout_2)


        self.verticalLayout1.addWidget(self.row_11)

        self.row_21 = QFrame(self.setupView)
        self.row_21.setObjectName(u"row_21")
        self.row_21.setMinimumSize(QSize(0, 150))
        self.row_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.row_21)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget_2 = QStackedWidget(self.row_21)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background: transparent;")
        self.localDocker = QWidget()
        self.localDocker.setObjectName(u"localDocker")
        self.localDocker.setStyleSheet(u"")
        self.verticalLayout2 = QVBoxLayout(self.localDocker)
        self.verticalLayout2.setSpacing(10)
        self.verticalLayout2.setObjectName(u"verticalLayout2")
        self.verticalLayout2.setContentsMargins(10, 10, 10, 10)
        self.maxSize_2 = QFrame(self.localDocker)
        self.maxSize_2.setObjectName(u"maxSize_2")
        self.maxSize_2.setMinimumSize(QSize(0, 150))
        self.maxSize_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.maxSize_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.maxSize_2)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.localReferenceGenomeInput = QLineEdit(self.maxSize_2)
        self.localReferenceGenomeInput.setObjectName(u"localReferenceGenomeInput")

        self.gridLayout_4.addWidget(self.localReferenceGenomeInput, 5, 1, 1, 1)

        self.localForwardReadLabel = QLabel(self.maxSize_2)
        self.localForwardReadLabel.setObjectName(u"localForwardReadLabel")

        self.gridLayout_4.addWidget(self.localForwardReadLabel, 1, 0, 1, 1)

        self.localBackwardReadLabel = QLabel(self.maxSize_2)
        self.localBackwardReadLabel.setObjectName(u"localBackwardReadLabel")

        self.gridLayout_4.addWidget(self.localBackwardReadLabel, 3, 0, 1, 1)

        self.localForwardReadInput = QLineEdit(self.maxSize_2)
        self.localForwardReadInput.setObjectName(u"localForwardReadInput")

        self.gridLayout_4.addWidget(self.localForwardReadInput, 1, 1, 1, 1)

        self.localBackwardReadInput = QLineEdit(self.maxSize_2)
        self.localBackwardReadInput.setObjectName(u"localBackwardReadInput")

        self.gridLayout_4.addWidget(self.localBackwardReadInput, 3, 1, 1, 1)

        self.localReferenceGenomeLabel = QLabel(self.maxSize_2)
        self.localReferenceGenomeLabel.setObjectName(u"localReferenceGenomeLabel")

        self.gridLayout_4.addWidget(self.localReferenceGenomeLabel, 5, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 6, 0, 1, 2)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 4, 0, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 2, 0, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 0, 0, 1, 2)


        self.verticalLayout_192.addLayout(self.gridLayout_4)


        self.verticalLayout2.addWidget(self.maxSize_2)

        self.stackedWidget_2.addWidget(self.localDocker)
        self.remoteDocker = QWidget()
        self.remoteDocker.setObjectName(u"remoteDocker")
        self.remoteDocker.setStyleSheet(u"")
        self.verticalLayout3 = QVBoxLayout(self.remoteDocker)
        self.verticalLayout3.setSpacing(10)
        self.verticalLayout3.setObjectName(u"verticalLayout3")
        self.verticalLayout3.setContentsMargins(10, 10, 10, 10)
        self.maxSize = QFrame(self.remoteDocker)
        self.maxSize.setObjectName(u"maxSize")
        self.maxSize.setMinimumSize(QSize(0, 150))
        self.maxSize.setFrameShape(QFrame.Shape.StyledPanel)
        self.maxSize.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.maxSize)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.remoteReferenceGenomeInput = QLineEdit(self.maxSize)
        self.remoteReferenceGenomeInput.setObjectName(u"remoteReferenceGenomeInput")

        self.gridLayout_5.addWidget(self.remoteReferenceGenomeInput, 9, 1, 1, 3)

        self.remotePortNumberInput = QLineEdit(self.maxSize)
        self.remotePortNumberInput.setObjectName(u"remotePortNumberInput")

        self.gridLayout_5.addWidget(self.remotePortNumberInput, 1, 3, 1, 1)

        self.remoteBackwardReadInput = QLineEdit(self.maxSize)
        self.remoteBackwardReadInput.setObjectName(u"remoteBackwardReadInput")

        self.gridLayout_5.addWidget(self.remoteBackwardReadInput, 7, 1, 1, 3)

        self.remotePortNumberLabel = QLabel(self.maxSize)
        self.remotePortNumberLabel.setObjectName(u"remotePortNumberLabel")

        self.gridLayout_5.addWidget(self.remotePortNumberLabel, 1, 2, 1, 1)

        self.remoteBackwardReadLabel = QLabel(self.maxSize)
        self.remoteBackwardReadLabel.setObjectName(u"remoteBackwardReadLabel")

        self.gridLayout_5.addWidget(self.remoteBackwardReadLabel, 7, 0, 1, 1)

        self.remoteIpAddressLabel = QLabel(self.maxSize)
        self.remoteIpAddressLabel.setObjectName(u"remoteIpAddressLabel")

        self.gridLayout_5.addWidget(self.remoteIpAddressLabel, 1, 0, 1, 1)

        self.remoteDontSendDataCheckbox = QCheckBox(self.maxSize)
        self.remoteDontSendDataCheckbox.setObjectName(u"remoteDontSendDataCheckbox")

        self.gridLayout_5.addWidget(self.remoteDontSendDataCheckbox, 3, 0, 1, 4)

        self.remoteForwardReadInput = QLineEdit(self.maxSize)
        self.remoteForwardReadInput.setObjectName(u"remoteForwardReadInput")

        self.gridLayout_5.addWidget(self.remoteForwardReadInput, 5, 1, 1, 3)

        self.remoteForwardReadLabel = QLabel(self.maxSize)
        self.remoteForwardReadLabel.setObjectName(u"remoteForwardReadLabel")

        self.gridLayout_5.addWidget(self.remoteForwardReadLabel, 5, 0, 1, 1)

        self.remoteReferenceGenomeLabel = QLabel(self.maxSize)
        self.remoteReferenceGenomeLabel.setObjectName(u"remoteReferenceGenomeLabel")

        self.gridLayout_5.addWidget(self.remoteReferenceGenomeLabel, 9, 0, 1, 1)

        self.remoteIpAddressInput = QLineEdit(self.maxSize)
        self.remoteIpAddressInput.setObjectName(u"remoteIpAddressInput")

        self.gridLayout_5.addWidget(self.remoteIpAddressInput, 1, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 10, 0, 1, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 8, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 6, 0, 1, 4)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 4, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 1, 4)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 0, 0, 1, 4)


        self.verticalLayout_193.addLayout(self.gridLayout_5)


        self.verticalLayout3.addWidget(self.maxSize)

        self.stackedWidget_2.addWidget(self.remoteDocker)

        self.gridLayout_3.addWidget(self.stackedWidget_2, 2, 0, 1, 3)

        self.dockerSetupLabel = QLabel(self.row_21)
        self.dockerSetupLabel.setObjectName(u"dockerSetupLabel")

        self.gridLayout_3.addWidget(self.dockerSetupLabel, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.dockerLocalButton = QRadioButton(self.row_21)
        self.dockerLocalButton.setObjectName(u"dockerLocalButton")

        self.gridLayout_3.addWidget(self.dockerLocalButton, 1, 0, 1, 1)

        self.dockerRemoteButton = QRadioButton(self.row_21)
        self.dockerRemoteButton.setObjectName(u"dockerRemoteButton")

        self.gridLayout_3.addWidget(self.dockerRemoteButton, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.dockerGuideButton = QPushButton(self.row_21)
        self.dockerGuideButton.setObjectName(u"dockerGuideButton")
        self.dockerGuideButton.setMinimumSize(QSize(50, 30))
        self.dockerGuideButton.setFont(font)
        self.dockerGuideButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dockerGuideButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-external-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dockerGuideButton.setIcon(icon11)

        self.gridLayout_3.addWidget(self.dockerGuideButton, 0, 1, 1, 1)


        self.verticalLayout_191.addLayout(self.gridLayout_3)


        self.verticalLayout1.addWidget(self.row_21)

        self.row_31 = QFrame(self.setupView)
        self.row_31.setObjectName(u"row_31")
        self.row_31.setMinimumSize(QSize(0, 35))
        self.row_31.setMaximumSize(QSize(16777215, 35))
        self.row_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.row_31)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.resetButton = QPushButton(self.row_31)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(50, 30))
        self.resetButton.setFont(font)
        self.resetButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resetButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-fire.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetButton.setIcon(icon12)

        self.horizontalLayout_121.addWidget(self.resetButton)

        self.restoreDefaultsButton = QPushButton(self.row_31)
        self.restoreDefaultsButton.setObjectName(u"restoreDefaultsButton")
        self.restoreDefaultsButton.setMinimumSize(QSize(50, 30))
        self.restoreDefaultsButton.setFont(font)
        self.restoreDefaultsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.restoreDefaultsButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreDefaultsButton.setIcon(icon13)

        self.horizontalLayout_121.addWidget(self.restoreDefaultsButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_121.addItem(self.horizontalSpacer_6)

        self.saveButton = QPushButton(self.row_31)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(50, 30))
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon14)

        self.horizontalLayout_121.addWidget(self.saveButton)

        self.helpButton = QPushButton(self.row_31)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(50, 30))
        self.helpButton.setFont(font)
        self.helpButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.helpButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-map.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpButton.setIcon(icon15)

        self.horizontalLayout_121.addWidget(self.helpButton)


        self.verticalLayout1.addWidget(self.row_31)

        self.stackedWidget.addWidget(self.setupView)
        self.analysisView = QWidget()
        self.analysisView.setObjectName(u"analysisView")
        self.analysisView.setStyleSheet(u"")
        self.verticalLayout4 = QVBoxLayout(self.analysisView)
        self.verticalLayout4.setSpacing(10)
        self.verticalLayout4.setObjectName(u"verticalLayout4")
        self.verticalLayout4.setContentsMargins(10, 10, 10, 10)
        self.row_12 = QFrame(self.analysisView)
        self.row_12.setObjectName(u"row_12")
        self.row_12.setMinimumSize(QSize(0, 50))
        self.row_12.setMaximumSize(QSize(16777215, 50))
        self.row_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.row_12)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout4.addWidget(self.row_12)

        self.row_22 = QFrame(self.analysisView)
        self.row_22.setObjectName(u"row_22")
        self.row_22.setMinimumSize(QSize(0, 150))
        self.row_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.row_22)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.label_4 = QLabel(self.row_22)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_194.addWidget(self.label_4)


        self.verticalLayout4.addWidget(self.row_22)

        self.row_32 = QFrame(self.analysisView)
        self.row_32.setObjectName(u"row_32")
        self.row_32.setMinimumSize(QSize(0, 70))
        self.row_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.row_32)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout4.addWidget(self.row_32)

        self.stackedWidget.addWidget(self.analysisView)
        self.runView = QWidget()
        self.runView.setObjectName(u"runView")
        self.runView.setStyleSheet(u"")
        self.verticalLayout5 = QVBoxLayout(self.runView)
        self.verticalLayout5.setSpacing(10)
        self.verticalLayout5.setObjectName(u"verticalLayout5")
        self.verticalLayout5.setContentsMargins(10, 10, 10, 10)
        self.row_13 = QFrame(self.runView)
        self.row_13.setObjectName(u"row_13")
        self.row_13.setMinimumSize(QSize(0, 50))
        self.row_13.setMaximumSize(QSize(16777215, 50))
        self.row_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.row_13)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.runButton = QPushButton(self.row_13)
        self.runButton.setObjectName(u"runButton")

        self.verticalLayout_163.addWidget(self.runButton)


        self.verticalLayout5.addWidget(self.row_13)

        self.row_23 = QFrame(self.runView)
        self.row_23.setObjectName(u"row_23")
        self.row_23.setMinimumSize(QSize(0, 150))
        self.row_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.row_23)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.stdOut = QTextBrowser(self.row_23)
        self.stdOut.setObjectName(u"stdOut")

        self.verticalLayout_195.addWidget(self.stdOut)


        self.verticalLayout5.addWidget(self.row_23)

        self.row_33 = QFrame(self.runView)
        self.row_33.setObjectName(u"row_33")
        self.row_33.setMinimumSize(QSize(0, 70))
        self.row_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.row_33)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.row_33)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_123.addWidget(self.progressBar)


        self.verticalLayout5.addWidget(self.row_33)

        self.stackedWidget.addWidget(self.runView)

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
        self.messageButton = QPushButton(self.topMenus)
        self.messageButton.setObjectName(u"messageButton")
        sizePolicy.setHeightForWidth(self.messageButton.sizePolicy().hasHeightForWidth())
        self.messageButton.setSizePolicy(sizePolicy)
        self.messageButton.setMinimumSize(QSize(0, 45))
        self.messageButton.setFont(font)
        self.messageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.messageButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.messageButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.messageButton)

        self.printButton = QPushButton(self.topMenus)
        self.printButton.setObjectName(u"printButton")
        sizePolicy.setHeightForWidth(self.printButton.sizePolicy().hasHeightForWidth())
        self.printButton.setSizePolicy(sizePolicy)
        self.printButton.setMinimumSize(QSize(0, 45))
        self.printButton.setFont(font)
        self.printButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.printButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.printButton)

        self.logoutButton = QPushButton(self.topMenus)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setMinimumSize(QSize(0, 45))
        self.logoutButton.setFont(font)
        self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.logoutButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.logoutButton)


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
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
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

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"qsLAM_PCR_AIO", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Erasmus MC", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.projectManagerButton.setText(QCoreApplication.translate("MainWindow", u"Project Manager", None))
        self.setupViewButton.setText(QCoreApplication.translate("MainWindow", u"Edit Run Configuration", None))
        self.runViewButton.setText(QCoreApplication.translate("MainWindow", u"Run Progress", None))
        self.analysisViewButton.setText(QCoreApplication.translate("MainWindow", u"Analyze Run", None))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">lorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum "
                        "lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsum</p></body></html>", None))
        self.moreButton.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Compile lentiviral vector integration sites from sequencing pipeline", None))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Currently Selected Run:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
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
        ___qtablewidgetitem4 = self.runsTable.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.runsTable.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.runsTable.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.runsTable.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.runsTable.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.runsTable.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.runsTable.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.runsTable.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.runsTable.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.runsTable.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.runsTable.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.runsTable.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.runsTable.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.runsTable.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.runsTable.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.runsTable.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.runsTable.verticalHeaderItem(16)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.runsTable.verticalHeaderItem(17)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.runsTable.verticalHeaderItem(18)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.runsTable.verticalHeaderItem(19)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.runsTable.verticalHeaderItem(20)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.runsTable.verticalHeaderItem(21)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.runsTable.isSortingEnabled()
        self.runsTable.setSortingEnabled(False)
        ___qtablewidgetitem26 = self.runsTable.item(0, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem27 = self.runsTable.item(0, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem28 = self.runsTable.item(0, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem29 = self.runsTable.item(0, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"test", None));
        self.runsTable.setSortingEnabled(__sortingEnabled)

        self.importRunButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.exportRunButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.openFolderLocationButton.setText(QCoreApplication.translate("MainWindow", u"Open Folder Location", None))
        self.nameRunLabel.setText(QCoreApplication.translate("MainWindow", u"Name of this run", None))
        self.adapterSequenceLabel.setText(QCoreApplication.translate("MainWindow", u"Adapter Sequence", None))
        self.ltrPrimerSequenceLabel.setText(QCoreApplication.translate("MainWindow", u"LTR Primer Sequence", None))
        self.localForwardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Forward read", None))
        self.localBackwardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Backward read", None))
        self.localReferenceGenomeLabel.setText(QCoreApplication.translate("MainWindow", u"Reference genome\n"
"(Leave blank for H19)", None))
        self.remotePortNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.remoteBackwardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Backward read", None))
        self.remoteIpAddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP address", None))
        self.remoteDontSendDataCheckbox.setText(QCoreApplication.translate("MainWindow", u"Don't send input data to remote server. I already have the input data mounted correctly in the docker container", None))
        self.remoteForwardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Forward read", None))
        self.remoteReferenceGenomeLabel.setText(QCoreApplication.translate("MainWindow", u"Reference genome\n"
"(Leave blank for H19)", None))
        self.dockerSetupLabel.setText(QCoreApplication.translate("MainWindow", u"  Docker setup", None))
        self.dockerLocalButton.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.dockerRemoteButton.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.dockerGuideButton.setText(QCoreApplication.translate("MainWindow", u"Not sure what to pick?", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.restoreDefaultsButton.setText(QCoreApplication.translate("MainWindow", u"Restore Defaults", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Charts here and stuff after run is complete...", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run!", None))
        self.messageButton.setText(QCoreApplication.translate("MainWindow", u"Not sure yet", None))
        self.printButton.setText(QCoreApplication.translate("MainWindow", u"What this is", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"For", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Miro & Liam Weitzel", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

