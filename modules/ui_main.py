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
    QCommandLinkButton, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
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
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
""
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
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
""
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
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBa"
                        "r::down-arrow:vertical {\n"
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
"QRadioButton::indicator:hover {\n"
"    border: 2px solid rgb(134, 210, 237);\n"
"}\n"
"QRadioB"
                        "utton::indicator:checked {\n"
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

        self.runAnalysisButton = QPushButton(self.topMenu)
        self.runAnalysisButton.setObjectName(u"runAnalysisButton")
        self.runAnalysisButton.setMinimumSize(QSize(0, 45))
        self.runAnalysisButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runAnalysisButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.runAnalysisButton)


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
        self.saveButton = QPushButton(self.runConfigurationTab)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(50, 30))
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon12)

        self.gridLayout_2.addWidget(self.saveButton, 24, 7, 1, 1)

        self.umiInput = QLineEdit(self.runConfigurationTab)
        self.umiInput.setObjectName(u"umiInput")

        self.gridLayout_2.addWidget(self.umiInput, 6, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 13, 0, 1, 2)

        self.trimmingConfig = QPushButton(self.runConfigurationTab)
        self.trimmingConfig.setObjectName(u"trimmingConfig")
        self.trimmingConfig.setMinimumSize(QSize(50, 30))
        self.trimmingConfig.setFont(font)
        self.trimmingConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.trimmingConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.trimmingConfig.setIcon(icon13)

        self.gridLayout_2.addWidget(self.trimmingConfig, 12, 0, 1, 2)

        self.restoreDefaultsButton = QPushButton(self.runConfigurationTab)
        self.restoreDefaultsButton.setObjectName(u"restoreDefaultsButton")
        self.restoreDefaultsButton.setMinimumSize(QSize(50, 30))
        self.restoreDefaultsButton.setFont(font)
        self.restoreDefaultsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.restoreDefaultsButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreDefaultsButton.setIcon(icon14)

        self.gridLayout_2.addWidget(self.restoreDefaultsButton, 24, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 2)

        self.R2Label = QLabel(self.runConfigurationTab)
        self.R2Label.setObjectName(u"R2Label")

        self.gridLayout_2.addWidget(self.R2Label, 4, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 24, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 7, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 17, 0, 1, 2)

        self.R2Input = QLineEdit(self.runConfigurationTab)
        self.R2Input.setObjectName(u"R2Input")

        self.gridLayout_2.addWidget(self.R2Input, 4, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 15, 0, 1, 2)

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

        self.verticalLayout4.addWidget(self.grid)

        self.dockerStackedWidget.addWidget(self.local)
        self.remote = QWidget()
        self.remote.setObjectName(u"remote")
        self.verticalLayout5 = QVBoxLayout(self.remote)
        self.verticalLayout5.setSpacing(10)
        self.verticalLayout5.setObjectName(u"verticalLayout5")
        self.verticalLayout5.setProperty(u"leftmargin", 10)
        self.verticalLayout5.setProperty(u"topmargin", 10)
        self.verticalLayout5.setProperty(u"rightmargin", 10)
        self.verticalLayout5.setProperty(u"bottommargin", 10)
        self.grid1 = QFrame(self.remote)
        self.grid1.setObjectName(u"grid1")
        self.grid1.setProperty(u"minimumsize", QSize(0, 70))
        self.grid1.setProperty(u"maximumsize", QSize(16777215, 70))
        self.gridLayout2 = QGridLayout(self.grid1)
        self.gridLayout2.setSpacing(0)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.radioButton = QRadioButton(self.grid1)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout2.addWidget(self.radioButton, 7, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_13, 7, 5, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_13, 2, 0, 1, 8)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_15, 6, 0, 1, 8)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_12, 0, 0, 1, 8)

        self.commandLinkButton = QCommandLinkButton(self.grid1)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout2.addWidget(self.commandLinkButton, 9, 0, 1, 4)

        self.lineEdit_2 = QLineEdit(self.grid1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout2.addWidget(self.lineEdit_2, 3, 1, 1, 4)

        self.pushButton = QPushButton(self.grid1)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout2.addWidget(self.pushButton, 9, 7, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_18, 8, 0, 1, 8)

        self.label = QLabel(self.grid1)
        self.label.setObjectName(u"label")

        self.gridLayout2.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.grid1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout2.addWidget(self.label_3, 5, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_11, 7, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_12, 7, 7, 1, 1)

        self.label_2 = QLabel(self.grid1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout2.addWidget(self.label_2, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.grid1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout2.addWidget(self.lineEdit_3, 1, 1, 1, 4)

        self.label_5 = QLabel(self.grid1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout2.addWidget(self.label_5, 7, 0, 1, 1)

        self.lineEdit = QLineEdit(self.grid1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout2.addWidget(self.lineEdit, 5, 1, 1, 4)

        self.radioButton_2 = QRadioButton(self.grid1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout2.addWidget(self.radioButton_2, 7, 4, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.verticalSpacer_14, 4, 0, 1, 8)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.horizontalSpacer_14, 7, 3, 1, 1)


        self.verticalLayout5.addWidget(self.grid1)

        self.dockerStackedWidget.addWidget(self.remote)

        self.verticalLayout3.addWidget(self.dockerStackedWidget)


        self.verticalLayout2.addWidget(self.row_21)

        self.configStackedWidget.addWidget(self.docker)
        self.trimming = QWidget()
        self.trimming.setObjectName(u"trimming")
        self.verticalLayout6 = QVBoxLayout(self.trimming)
        self.verticalLayout6.setSpacing(10)
        self.verticalLayout6.setObjectName(u"verticalLayout6")
        self.verticalLayout6.setProperty(u"leftmargin", 10)
        self.verticalLayout6.setProperty(u"topmargin", 10)
        self.verticalLayout6.setProperty(u"rightmargin", 10)
        self.verticalLayout6.setProperty(u"bottommargin", 10)
        self.row_12 = QFrame(self.trimming)
        self.row_12.setObjectName(u"row_12")
        self.row_12.setProperty(u"minimumsize", QSize(0, 70))
        self.row_12.setProperty(u"maximumsize", QSize(16777215, 70))
        self.verticalLayout7 = QVBoxLayout(self.row_12)
        self.verticalLayout7.setSpacing(0)
        self.verticalLayout7.setObjectName(u"verticalLayout7")
        self.verticalLayout7.setProperty(u"leftmargin", 0)
        self.verticalLayout7.setProperty(u"topmargin", 0)
        self.verticalLayout7.setProperty(u"rightmargin", 0)
        self.verticalLayout7.setProperty(u"bottommargin", 0)

        self.verticalLayout6.addWidget(self.row_12)

        self.row_22 = QFrame(self.trimming)
        self.row_22.setObjectName(u"row_22")
        self.row_22.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout8 = QVBoxLayout(self.row_22)
        self.verticalLayout8.setObjectName(u"verticalLayout8")

        self.verticalLayout6.addWidget(self.row_22)

        self.row_31 = QFrame(self.trimming)
        self.row_31.setObjectName(u"row_31")
        self.row_31.setProperty(u"minimumsize", QSize(0, 50))
        self.horizontalLayout1 = QVBoxLayout(self.row_31)
        self.horizontalLayout1.setSpacing(0)
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalLayout1.setProperty(u"leftmargin", 0)
        self.horizontalLayout1.setProperty(u"topmargin", 0)
        self.horizontalLayout1.setProperty(u"rightmargin", 0)
        self.horizontalLayout1.setProperty(u"bottommargin", 0)

        self.verticalLayout6.addWidget(self.row_31)

        self.configStackedWidget.addWidget(self.trimming)
        self.ref_genome = QWidget()
        self.ref_genome.setObjectName(u"ref_genome")
        self.verticalLayout9 = QVBoxLayout(self.ref_genome)
        self.verticalLayout9.setSpacing(10)
        self.verticalLayout9.setObjectName(u"verticalLayout9")
        self.verticalLayout9.setProperty(u"leftmargin", 10)
        self.verticalLayout9.setProperty(u"topmargin", 10)
        self.verticalLayout9.setProperty(u"rightmargin", 10)
        self.verticalLayout9.setProperty(u"bottommargin", 10)
        self.row_13 = QFrame(self.ref_genome)
        self.row_13.setObjectName(u"row_13")
        self.row_13.setProperty(u"minimumsize", QSize(0, 70))
        self.row_13.setProperty(u"maximumsize", QSize(16777215, 70))
        self.verticalLayout10 = QVBoxLayout(self.row_13)
        self.verticalLayout10.setSpacing(0)
        self.verticalLayout10.setObjectName(u"verticalLayout10")
        self.verticalLayout10.setProperty(u"leftmargin", 0)
        self.verticalLayout10.setProperty(u"topmargin", 0)
        self.verticalLayout10.setProperty(u"rightmargin", 0)
        self.verticalLayout10.setProperty(u"bottommargin", 0)

        self.verticalLayout9.addWidget(self.row_13)

        self.row_23 = QFrame(self.ref_genome)
        self.row_23.setObjectName(u"row_23")
        self.row_23.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout11 = QVBoxLayout(self.row_23)
        self.verticalLayout11.setObjectName(u"verticalLayout11")

        self.verticalLayout9.addWidget(self.row_23)

        self.row_32 = QFrame(self.ref_genome)
        self.row_32.setObjectName(u"row_32")
        self.row_32.setProperty(u"minimumsize", QSize(0, 50))
        self.horizontalLayout2 = QVBoxLayout(self.row_32)
        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalLayout2.setProperty(u"leftmargin", 0)
        self.horizontalLayout2.setProperty(u"topmargin", 0)
        self.horizontalLayout2.setProperty(u"rightmargin", 0)
        self.horizontalLayout2.setProperty(u"bottommargin", 0)

        self.verticalLayout9.addWidget(self.row_32)

        self.configStackedWidget.addWidget(self.ref_genome)
        self.read_mapping = QWidget()
        self.read_mapping.setObjectName(u"read_mapping")
        self.verticalLayout12 = QVBoxLayout(self.read_mapping)
        self.verticalLayout12.setSpacing(10)
        self.verticalLayout12.setObjectName(u"verticalLayout12")
        self.verticalLayout12.setProperty(u"leftmargin", 10)
        self.verticalLayout12.setProperty(u"topmargin", 10)
        self.verticalLayout12.setProperty(u"rightmargin", 10)
        self.verticalLayout12.setProperty(u"bottommargin", 10)
        self.row_14 = QFrame(self.read_mapping)
        self.row_14.setObjectName(u"row_14")
        self.row_14.setProperty(u"minimumsize", QSize(0, 70))
        self.row_14.setProperty(u"maximumsize", QSize(16777215, 70))
        self.verticalLayout13 = QVBoxLayout(self.row_14)
        self.verticalLayout13.setSpacing(0)
        self.verticalLayout13.setObjectName(u"verticalLayout13")
        self.verticalLayout13.setProperty(u"leftmargin", 0)
        self.verticalLayout13.setProperty(u"topmargin", 0)
        self.verticalLayout13.setProperty(u"rightmargin", 0)
        self.verticalLayout13.setProperty(u"bottommargin", 0)

        self.verticalLayout12.addWidget(self.row_14)

        self.row_24 = QFrame(self.read_mapping)
        self.row_24.setObjectName(u"row_24")
        self.row_24.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout14 = QVBoxLayout(self.row_24)
        self.verticalLayout14.setObjectName(u"verticalLayout14")

        self.verticalLayout12.addWidget(self.row_24)

        self.row_33 = QFrame(self.read_mapping)
        self.row_33.setObjectName(u"row_33")
        self.row_33.setProperty(u"minimumsize", QSize(0, 50))
        self.horizontalLayout3 = QVBoxLayout(self.row_33)
        self.horizontalLayout3.setSpacing(0)
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.horizontalLayout3.setProperty(u"leftmargin", 0)
        self.horizontalLayout3.setProperty(u"topmargin", 0)
        self.horizontalLayout3.setProperty(u"rightmargin", 0)
        self.horizontalLayout3.setProperty(u"bottommargin", 0)

        self.verticalLayout12.addWidget(self.row_33)

        self.configStackedWidget.addWidget(self.read_mapping)
        self.site_analysis = QWidget()
        self.site_analysis.setObjectName(u"site_analysis")
        self.verticalLayout15 = QVBoxLayout(self.site_analysis)
        self.verticalLayout15.setSpacing(10)
        self.verticalLayout15.setObjectName(u"verticalLayout15")
        self.verticalLayout15.setProperty(u"leftmargin", 10)
        self.verticalLayout15.setProperty(u"topmargin", 10)
        self.verticalLayout15.setProperty(u"rightmargin", 10)
        self.verticalLayout15.setProperty(u"bottommargin", 10)
        self.row_15 = QFrame(self.site_analysis)
        self.row_15.setObjectName(u"row_15")
        self.row_15.setProperty(u"minimumsize", QSize(0, 70))
        self.row_15.setProperty(u"maximumsize", QSize(16777215, 70))
        self.verticalLayout16 = QVBoxLayout(self.row_15)
        self.verticalLayout16.setSpacing(0)
        self.verticalLayout16.setObjectName(u"verticalLayout16")
        self.verticalLayout16.setProperty(u"leftmargin", 0)
        self.verticalLayout16.setProperty(u"topmargin", 0)
        self.verticalLayout16.setProperty(u"rightmargin", 0)
        self.verticalLayout16.setProperty(u"bottommargin", 0)

        self.verticalLayout15.addWidget(self.row_15)

        self.row_25 = QFrame(self.site_analysis)
        self.row_25.setObjectName(u"row_25")
        self.row_25.setProperty(u"minimumsize", QSize(0, 150))
        self.verticalLayout17 = QVBoxLayout(self.row_25)
        self.verticalLayout17.setObjectName(u"verticalLayout17")

        self.verticalLayout15.addWidget(self.row_25)

        self.row_34 = QFrame(self.site_analysis)
        self.row_34.setObjectName(u"row_34")
        self.row_34.setProperty(u"minimumsize", QSize(0, 50))
        self.horizontalLayout4 = QVBoxLayout(self.row_34)
        self.horizontalLayout4.setSpacing(0)
        self.horizontalLayout4.setObjectName(u"horizontalLayout4")
        self.horizontalLayout4.setProperty(u"leftmargin", 0)
        self.horizontalLayout4.setProperty(u"topmargin", 0)
        self.horizontalLayout4.setProperty(u"rightmargin", 0)
        self.horizontalLayout4.setProperty(u"bottommargin", 0)

        self.verticalLayout15.addWidget(self.row_34)

        self.configStackedWidget.addWidget(self.site_analysis)

        self.gridLayout_2.addWidget(self.configStackedWidget, 0, 2, 24, 7)

        self.readMappingConfig = QPushButton(self.runConfigurationTab)
        self.readMappingConfig.setObjectName(u"readMappingConfig")
        self.readMappingConfig.setMinimumSize(QSize(50, 30))
        self.readMappingConfig.setFont(font)
        self.readMappingConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.readMappingConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.readMappingConfig.setIcon(icon9)

        self.gridLayout_2.addWidget(self.readMappingConfig, 16, 0, 1, 2)

        self.umiCheckbox = QCheckBox(self.runConfigurationTab)
        self.umiCheckbox.setObjectName(u"umiCheckbox")

        self.gridLayout_2.addWidget(self.umiCheckbox, 6, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 24, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 24, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 24, 5, 1, 1)

        self.configStepsLabel = QLabel(self.runConfigurationTab)
        self.configStepsLabel.setObjectName(u"configStepsLabel")

        self.gridLayout_2.addWidget(self.configStepsLabel, 9, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 0, 1, 2)

        self.dockerConfig = QPushButton(self.runConfigurationTab)
        self.dockerConfig.setObjectName(u"dockerConfig")
        self.dockerConfig.setMinimumSize(QSize(50, 30))
        self.dockerConfig.setFont(font)
        self.dockerConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dockerConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-docker.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dockerConfig.setIcon(icon15)

        self.gridLayout_2.addWidget(self.dockerConfig, 10, 0, 1, 2)

        self.resetButton = QPushButton(self.runConfigurationTab)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(50, 30))
        self.resetButton.setFont(font)
        self.resetButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resetButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-fire.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetButton.setIcon(icon16)

        self.gridLayout_2.addWidget(self.resetButton, 24, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 24, 3, 1, 1)

        self.helpButton = QPushButton(self.runConfigurationTab)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(50, 30))
        self.helpButton.setFont(font)
        self.helpButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.helpButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-map.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpButton.setIcon(icon17)

        self.gridLayout_2.addWidget(self.helpButton, 24, 8, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 8, 0, 1, 2)

        self.R1Input = QLineEdit(self.runConfigurationTab)
        self.R1Input.setObjectName(u"R1Input")

        self.gridLayout_2.addWidget(self.R1Input, 0, 1, 3, 1)

        self.refGenomeConfig = QPushButton(self.runConfigurationTab)
        self.refGenomeConfig.setObjectName(u"refGenomeConfig")
        self.refGenomeConfig.setMinimumSize(QSize(50, 30))
        self.refGenomeConfig.setFont(font)
        self.refGenomeConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refGenomeConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.refGenomeConfig.setIcon(icon9)

        self.gridLayout_2.addWidget(self.refGenomeConfig, 14, 0, 1, 2)

        self.siteAnalysisConfig = QPushButton(self.runConfigurationTab)
        self.siteAnalysisConfig.setObjectName(u"siteAnalysisConfig")
        self.siteAnalysisConfig.setMinimumSize(QSize(50, 30))
        self.siteAnalysisConfig.setFont(font)
        self.siteAnalysisConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.siteAnalysisConfig.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.siteAnalysisConfig.setIcon(icon9)

        self.gridLayout_2.addWidget(self.siteAnalysisConfig, 18, 0, 3, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 11, 0, 1, 2)

        self.R1Label = QLabel(self.runConfigurationTab)
        self.R1Label.setObjectName(u"R1Label")

        self.gridLayout_2.addWidget(self.R1Label, 0, 0, 3, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 21, 0, 1, 2)


        self.verticalLayout1.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.runConfigurationTab)
        self.runAnalysisTab = QWidget()
        self.runAnalysisTab.setObjectName(u"runAnalysisTab")
        self.runAnalysisTab.setStyleSheet(u"")
        self.verticalLayout18 = QVBoxLayout(self.runAnalysisTab)
        self.verticalLayout18.setSpacing(10)
        self.verticalLayout18.setObjectName(u"verticalLayout18")
        self.verticalLayout18.setContentsMargins(10, 10, 10, 10)
        self.row_16 = QFrame(self.runAnalysisTab)
        self.row_16.setObjectName(u"row_16")
        self.row_16.setMinimumSize(QSize(0, 50))
        self.row_16.setMaximumSize(QSize(16777215, 50))
        self.row_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.row_16)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout18.addWidget(self.row_16)

        self.row_26 = QFrame(self.runAnalysisTab)
        self.row_26.setObjectName(u"row_26")
        self.row_26.setMinimumSize(QSize(0, 150))
        self.row_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.row_26)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.label_4 = QLabel(self.row_26)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_191.addWidget(self.label_4)


        self.verticalLayout18.addWidget(self.row_26)

        self.row_35 = QFrame(self.runAnalysisTab)
        self.row_35.setObjectName(u"row_35")
        self.row_35.setMinimumSize(QSize(0, 70))
        self.row_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.row_35)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout18.addWidget(self.row_35)

        self.stackedWidget.addWidget(self.runAnalysisTab)
        self.runProgressTab = QWidget()
        self.runProgressTab.setObjectName(u"runProgressTab")
        self.runProgressTab.setStyleSheet(u"")
        self.verticalLayout19 = QVBoxLayout(self.runProgressTab)
        self.verticalLayout19.setSpacing(10)
        self.verticalLayout19.setObjectName(u"verticalLayout19")
        self.verticalLayout19.setContentsMargins(10, 10, 10, 10)
        self.row_17 = QFrame(self.runProgressTab)
        self.row_17.setObjectName(u"row_17")
        self.row_17.setMinimumSize(QSize(0, 70))
        self.row_17.setMaximumSize(QSize(16777215, 70))
        self.row_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.row_17)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout19.addWidget(self.row_17)

        self.row_27 = QFrame(self.runProgressTab)
        self.row_27.setObjectName(u"row_27")
        self.row_27.setMinimumSize(QSize(0, 150))
        self.row_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.row_27)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.stdOut = QTextBrowser(self.row_27)
        self.stdOut.setObjectName(u"stdOut")

        self.verticalLayout_192.addWidget(self.stdOut)


        self.verticalLayout19.addWidget(self.row_27)

        self.row_36 = QFrame(self.runProgressTab)
        self.row_36.setObjectName(u"row_36")
        self.row_36.setMinimumSize(QSize(0, 50))
        self.row_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.row_36)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cleanButton = QPushButton(self.row_36)
        self.cleanButton.setObjectName(u"cleanButton")
        self.cleanButton.setMinimumSize(QSize(50, 30))
        self.cleanButton.setFont(font)
        self.cleanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cleanButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cleanButton.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.cleanButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.pauseButton = QPushButton(self.row_36)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setMinimumSize(QSize(50, 30))
        self.pauseButton.setFont(font)
        self.pauseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pauseButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/cil-media-stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseButton.setIcon(icon18)

        self.horizontalLayout_6.addWidget(self.pauseButton)

        self.resumeButton = QPushButton(self.row_36)
        self.resumeButton.setObjectName(u"resumeButton")
        self.resumeButton.setMinimumSize(QSize(50, 30))
        self.resumeButton.setFont(font)
        self.resumeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resumeButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resumeButton.setIcon(icon19)

        self.horizontalLayout_6.addWidget(self.resumeButton)

        self.runButton = QPushButton(self.row_36)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setMinimumSize(QSize(50, 30))
        self.runButton.setFont(font)
        self.runButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.runButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.runButton.setIcon(icon19)

        self.horizontalLayout_6.addWidget(self.runButton)


        self.horizontalLayout_122.addLayout(self.horizontalLayout_6)


        self.verticalLayout19.addWidget(self.row_36)

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
        QWidget.setTabOrder(self.R1Input, self.R2Input)
        QWidget.setTabOrder(self.R2Input, self.umiInput)
        QWidget.setTabOrder(self.umiInput, self.umiCheckbox)
        QWidget.setTabOrder(self.umiCheckbox, self.trimmingConfig)
        QWidget.setTabOrder(self.trimmingConfig, self.refGenomeConfig)
        QWidget.setTabOrder(self.refGenomeConfig, self.readMappingConfig)
        QWidget.setTabOrder(self.readMappingConfig, self.siteAnalysisConfig)
        QWidget.setTabOrder(self.siteAnalysisConfig, self.resetButton)
        QWidget.setTabOrder(self.resetButton, self.restoreDefaultsButton)
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
        QWidget.setTabOrder(self.runProgressButton, self.runAnalysisButton)
        QWidget.setTabOrder(self.runAnalysisButton, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnButton)
        QWidget.setTabOrder(self.extraCloseColumnButton, self.aboutText)
        QWidget.setTabOrder(self.aboutText, self.closeAppButton)
        QWidget.setTabOrder(self.closeAppButton, self.settingsTopButton)
        QWidget.setTabOrder(self.settingsTopButton, self.maximizeRestoreAppButton)
        QWidget.setTabOrder(self.maximizeRestoreAppButton, self.toggleButton)
        QWidget.setTabOrder(self.toggleButton, self.messageButton)
        QWidget.setTabOrder(self.messageButton, self.printButton)
        QWidget.setTabOrder(self.printButton, self.logoutButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.configStackedWidget.setCurrentIndex(0)
        self.dockerStackedWidget.setCurrentIndex(1)


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
        self.runAnalysisButton.setText(QCoreApplication.translate("MainWindow", u"Analyze Runs", None))
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
        self.trimmingConfig.setText(QCoreApplication.translate("MainWindow", u"Adapter and primer trimming", None))
        self.restoreDefaultsButton.setText(QCoreApplication.translate("MainWindow", u"Restore Defaults", None))
        self.R2Label.setText(QCoreApplication.translate("MainWindow", u"Read 2", None))
        self.localRadio.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.remoteRadio.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.dockerLabel.setText(QCoreApplication.translate("MainWindow", u"Do you want to run the qsLAM PCR pipeline locally or on a remote server? You can do some trial runs on our public test server.", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Http", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Want to use our public test server instead?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Test Connection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Authentication Token", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Https", None))
        self.readMappingConfig.setText(QCoreApplication.translate("MainWindow", u"Read mapping", None))
        self.umiCheckbox.setText(QCoreApplication.translate("MainWindow", u"Unique Molecular Identifier?", None))
        self.configStepsLabel.setText(QCoreApplication.translate("MainWindow", u"Please complete all configuration steps below:", None))
        self.dockerConfig.setText(QCoreApplication.translate("MainWindow", u"Docker configuration", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.refGenomeConfig.setText(QCoreApplication.translate("MainWindow", u"Reference genome", None))
        self.siteAnalysisConfig.setText(QCoreApplication.translate("MainWindow", u"Site analysis", None))
        self.R1Label.setText(QCoreApplication.translate("MainWindow", u"Read 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Charts here and stuff after run is complete...", None))
        self.stdOut.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
                        " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . "
                        ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
                        " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . "
                        ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
                        " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . "
                        ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
                        " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</p></body></html>", None))
        self.cleanButton.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.resumeButton.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run Full Pipeline", None))
        self.messageButton.setText(QCoreApplication.translate("MainWindow", u"Not sure yet", None))
        self.printButton.setText(QCoreApplication.translate("MainWindow", u"What this is", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"For", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Miro & Liam Weitzel", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

