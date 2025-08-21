# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingnxZcz.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"QWidget{\n"
"       color: rgb(30, 30, 30);\n"
"       font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"       color: #ffffff;\n"
"       background-color: rgba(134, 210, 237, 200);\n"
"       border: 1px solid rgb(204, 204, 204);\n"
"       background-image: none;\n"
"       background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"       border: none;\n"
"       border-left: 2px solid rgb(0, 33, 109);\n"
"       text-align: left;\n"
"       padding-left: 8px;\n"
"       margin: 0px;\n"
"}\n"
"QToolTip {\n"
"    border-left: 2px solid #00216D;\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {       \n"
"       background-color: rgb(255, 255, 255);\n"
"       border: 1px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#leftMenuBg {  \n"
"       background-color: rgb(245, 245, 245);\n"
"}\n"
"#topLogo {\n"
"       background-color: rgb(245, 245, 245);\n"
"       background-image: url(:/images/images/images/Erasmus_MC_logo.png);\n"
"       background-position: centered;\n"
"       background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #"
                        "00216D; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #86D2ED; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {        \n"
"       background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"       border: none;\n"
"       border-left: 22px solid transparent;\n"
"       background-color: transparent;\n"
"       text-align: left;\n"
"       padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"       background-color: rgb(224, 247, 247);\n"
"}\n"
"#topMenu .QPushButton:pressed {        \n"
"       background-color: #00216D;\n"
"       color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {     \n"
"       background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"       border: none;\n"
"       border-left: 20px solid transparent;\n"
"       background-color:transparent;\n"
"       text-align: left;\n"
"       padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"       background-color: rgb(224, 247, 247);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {     \n"
"       background-color: #00216D;\n"
"       color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
""
                        "       border-top: 3px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"       background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"       border: none;\n"
"       border-left: 20px solid transparent;\n"
"       background-color: rgb(230, 242, 242);\n"
"       text-align: left;\n"
"       padding-left: 44px;\n"
"       color: rgb(85, 85, 85);\n"
"}\n"
"#toggleButton:hover {\n"
"       background-color: rgb(208, 235, 235);\n"
"}\n"
"#toggleButton:pressed {\n"
"       background-color: #00216D;\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* Extra Tab */\n"
"#extraLeftBox {        \n"
"       background-color: rgb(235, 235, 235);\n"
"}\n"
"#extraTopBg{   \n"
"       background-color: #86D2ED;\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"       background-position: center;\n"
"       background-repeat: no-repeat;\n"
"       background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(51, 51, 51); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { back"
                        "ground-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(178, 223, 223); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(128, 207, 207); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"       border-top: 3px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"       border: none;\n"
"       border-left: 22px solid transparent;\n"
"       background-color:transparent;\n"
"       text-align: left;\n"
"       padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"       background-color: rgb(224, 247, 247);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {   \n"
"       background-color: #00216D;\n"
"       color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Content App */\n"
"#contentTopBg{ \n"
"       background-color: rgb(245, 245, 245);\n"
"}\n"
"#contentBottom{\n"
"       border-t"
                        "op: 3px solid rgb(204, 204, 204);\n"
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
"#contentSettings .QPushButton {        \n"
"       background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"       border: none;\n"
"       border-left: 22px solid transparent;\n"
"       background-"
                        "color:transparent;\n"
"       text-align: left;\n"
"       padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"       background-color: rgb(224, 247, 247);\n"
"}\n"
"#contentSettings .QPushButton:pressed {        \n"
"       background-color: #00216D;\n"
"       color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QTableWidget */\n"
"QTableWidget { \n"
"       background-color: transparent;\n"
"       padding: 10px;\n"
"       border-radius: 5px;\n"
"       gridline-color: rgb(204, 204, 204);\n"
"       border-bottom: 1px solid rgb(220, 220, 220);\n"
"}\n"
"QTableWidget::item{\n"
"       border-color: rgb(220, 220, 220);\n"
"       padding-left: 5px;\n"
"       padding-right: 5px;\n"
"       gridline-color: rgb(220, 220, 220);\n"
"}\n"
"QTableWidget::item:selected{\n"
"       background-color: rgb(134, 210, 237);\n"
"       color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView::section{\n"
"       background-color: #86D2ED;\n"
"       max-width: 30px;\n"
"       border: 1px solid rgb(204, 204, 204);\n"
"       border-style: none;\n"
"    border-bottom: 1px solid rgb(220, 220, 220);\n"
"    border-right: 1px solid rgb(220, 220, 220);\n"
""
                        "}\n"
"QTableWidget::horizontalHeader {       \n"
"       background-color: rgb(245, 245, 245);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"       background-color: #01216D;\n"
"       padding: 3px;\n"
"       color: white;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(220, 220, 220);\n"
"}\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"       background-color: rgb(255, 255, 255);\n"
"       border-radius: 5px;\n"
"       border: 2px solid rgb(204, 204, 204);\n"
"       padding-left: 10px;\n"
"       selection-color: rgb(255, 255, 255);\n"
"       selection-background-color: #86D2ED;\n"
"}\n"
"QLineEdit:hover {\n"
"       border: 2px solid #86D2ED;\n"
"}\n"
"QLineEdit:focus {\n"
"       border: 2px solid #86D2ED;\n"
"}\n"
"\n"
"/* PlainTextEdit */\n"
"QPlainTextEdit {\n"
"       background-color: rgb(255, 255, 255);\n"
"       border-radius: 5px;\n"
"       padding: 10px;\n"
"       selection-color: rgb(255, 255, 255);\n"
"       selection-background-color: #86D2ED;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {"
                        "\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"       border: 2px solid #86D2ED;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"       border: 2px solid #86D2ED;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"       border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #01216D;\n"
"    min-width: 25px;\n"
"       border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    width: 20px;\n"
"       border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 170, 170);\n"
"    width: 20px;\n"
"       border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-ar"
                        "row:horizontal, QScrollBar::down-arrow:horizontal\n"
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
"    subcontrol-origin"
                        ": margin;\n"
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
"QRadioButton::indicator:hover {\n"
""
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
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.btn_projectManager = QPushButton(self.topMenu)
        self.btn_projectManager.setObjectName(u"btn_projectManager")
        sizePolicy.setHeightForWidth(self.btn_projectManager.sizePolicy().hasHeightForWidth())
        self.btn_projectManager.setSizePolicy(sizePolicy)
        self.btn_projectManager.setMinimumSize(QSize(0, 45))
        self.btn_projectManager.setFont(font)
        self.btn_projectManager.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_projectManager.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_projectManager.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_8.addWidget(self.btn_projectManager)

        self.btn_setupView = QPushButton(self.topMenu)
        self.btn_setupView.setObjectName(u"btn_setupView")
        sizePolicy.setHeightForWidth(self.btn_setupView.sizePolicy().hasHeightForWidth())
        self.btn_setupView.setSizePolicy(sizePolicy)
        self.btn_setupView.setMinimumSize(QSize(0, 45))
        self.btn_setupView.setFont(font)
        self.btn_setupView.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setupView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_setupView.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_setupView)

        self.btn_runView = QPushButton(self.topMenu)
        self.btn_runView.setObjectName(u"btn_runView")
        self.btn_runView.setMinimumSize(QSize(0, 45))
        self.btn_runView.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_runView.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.btn_runView)

        self.btn_analysisView = QPushButton(self.topMenu)
        self.btn_analysisView.setObjectName(u"btn_analysisView")
        self.btn_analysisView.setMinimumSize(QSize(0, 45))
        self.btn_analysisView.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analysisView.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.btn_analysisView)


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
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

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
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_about = QPushButton(self.extraTopMenu)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy)
        self.btn_about.setMinimumSize(QSize(0, 45))
        self.btn_about.setFont(font)
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_about.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_about.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_about)


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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
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
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


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
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
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
        self.createButton = QCommandLinkButton(self.frame_content_wid_1)
        self.createButton.setObjectName(u"createButton")

        self.horizontalLayout_9.addWidget(self.createButton)

        self.deleteButton = QCommandLinkButton(self.frame_content_wid_1)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout_9.addWidget(self.deleteButton)

        self.exportButton = QCommandLinkButton(self.frame_content_wid_1)
        self.exportButton.setObjectName(u"exportButton")

        self.horizontalLayout_9.addWidget(self.exportButton)


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
        if (self.runsTable.rowCount() < 23):
            self.runsTable.setRowCount(23)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setUnderline(False)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setBackground(QColor(0, 33, 109));
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
        self.runsTable.setVerticalHeaderItem(22, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.runsTable.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.runsTable.setItem(0, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.runsTable.setItem(0, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.runsTable.setItem(0, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.runsTable.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.runsTable.setItem(1, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.runsTable.setItem(1, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.runsTable.setItem(1, 3, __qtablewidgetitem34)
        self.runsTable.setObjectName(u"runsTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.runsTable.sizePolicy().hasHeightForWidth())
        self.runsTable.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
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
        self.importRunButton.setMinimumSize(QSize(150, 30))
        self.importRunButton.setFont(font)
        self.importRunButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.importRunButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importRunButton.setIcon(icon4)

        self.gridLayout.addWidget(self.importRunButton, 1, 2, 1, 1)

        self.importRunInput = QLineEdit(self.row_3)
        self.importRunInput.setObjectName(u"importRunInput")
        self.importRunInput.setMinimumSize(QSize(0, 30))
        self.importRunInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.importRunInput, 1, 0, 1, 1)

        self.importRunLabel = QLabel(self.row_3)
        self.importRunLabel.setObjectName(u"importRunLabel")

        self.gridLayout.addWidget(self.importRunLabel, 0, 0, 1, 1)


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
        self.row_11.setMinimumSize(QSize(0, 80))
        self.row_11.setMaximumSize(QSize(16777215, 80))
        self.row_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.row_11)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_2 = QLineEdit(self.row_11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.label = QLabel(self.row_11)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.row_11)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.row_11)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 0, 1, 2)


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
        self.referenceGenomeInput = QLineEdit(self.maxSize_2)
        self.referenceGenomeInput.setObjectName(u"referenceGenomeInput")

        self.gridLayout_4.addWidget(self.referenceGenomeInput, 5, 1, 1, 1)

        self.forwardReadLabel = QLabel(self.maxSize_2)
        self.forwardReadLabel.setObjectName(u"forwardReadLabel")

        self.gridLayout_4.addWidget(self.forwardReadLabel, 1, 0, 1, 1)

        self.backwardReadLabel = QLabel(self.maxSize_2)
        self.backwardReadLabel.setObjectName(u"backwardReadLabel")

        self.gridLayout_4.addWidget(self.backwardReadLabel, 3, 0, 1, 1)

        self.forwardReadInput = QLineEdit(self.maxSize_2)
        self.forwardReadInput.setObjectName(u"forwardReadInput")

        self.gridLayout_4.addWidget(self.forwardReadInput, 1, 1, 1, 1)

        self.backwardReadInput = QLineEdit(self.maxSize_2)
        self.backwardReadInput.setObjectName(u"backwardReadInput")

        self.gridLayout_4.addWidget(self.backwardReadInput, 3, 1, 1, 1)

        self.referenceGenomeLabel = QLabel(self.maxSize_2)
        self.referenceGenomeLabel.setObjectName(u"referenceGenomeLabel")

        self.gridLayout_4.addWidget(self.referenceGenomeLabel, 5, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 6, 0, 1, 2)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 4, 0, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 2, 0, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.referenceGenomeInput_2 = QLineEdit(self.maxSize)
        self.referenceGenomeInput_2.setObjectName(u"referenceGenomeInput_2")

        self.gridLayout_5.addWidget(self.referenceGenomeInput_2, 9, 1, 1, 3)

        self.portNumberInput = QLineEdit(self.maxSize)
        self.portNumberInput.setObjectName(u"portNumberInput")

        self.gridLayout_5.addWidget(self.portNumberInput, 1, 3, 1, 1)

        self.backwardReadInput_2 = QLineEdit(self.maxSize)
        self.backwardReadInput_2.setObjectName(u"backwardReadInput_2")

        self.gridLayout_5.addWidget(self.backwardReadInput_2, 7, 1, 1, 3)

        self.portNumberLabel = QLabel(self.maxSize)
        self.portNumberLabel.setObjectName(u"portNumberLabel")

        self.gridLayout_5.addWidget(self.portNumberLabel, 1, 2, 1, 1)

        self.backwardReadLabel_2 = QLabel(self.maxSize)
        self.backwardReadLabel_2.setObjectName(u"backwardReadLabel_2")

        self.gridLayout_5.addWidget(self.backwardReadLabel_2, 7, 0, 1, 1)

        self.ipAddressLabel = QLabel(self.maxSize)
        self.ipAddressLabel.setObjectName(u"ipAddressLabel")

        self.gridLayout_5.addWidget(self.ipAddressLabel, 1, 0, 1, 1)

        self.dontSendData = QCheckBox(self.maxSize)
        self.dontSendData.setObjectName(u"dontSendData")

        self.gridLayout_5.addWidget(self.dontSendData, 3, 0, 1, 4)

        self.forwardReadInput_2 = QLineEdit(self.maxSize)
        self.forwardReadInput_2.setObjectName(u"forwardReadInput_2")

        self.gridLayout_5.addWidget(self.forwardReadInput_2, 5, 1, 1, 3)

        self.forwardReadLabel_2 = QLabel(self.maxSize)
        self.forwardReadLabel_2.setObjectName(u"forwardReadLabel_2")

        self.gridLayout_5.addWidget(self.forwardReadLabel_2, 5, 0, 1, 1)

        self.referenceGenomeLabel_2 = QLabel(self.maxSize)
        self.referenceGenomeLabel_2.setObjectName(u"referenceGenomeLabel_2")

        self.gridLayout_5.addWidget(self.referenceGenomeLabel_2, 9, 0, 1, 1)

        self.ipAddressInput = QLineEdit(self.maxSize)
        self.ipAddressInput.setObjectName(u"ipAddressInput")

        self.gridLayout_5.addWidget(self.ipAddressInput, 1, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 10, 0, 1, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 8, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 6, 0, 1, 4)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 4, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 1, 4)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 0, 0, 1, 4)


        self.verticalLayout_193.addLayout(self.gridLayout_5)


        self.verticalLayout3.addWidget(self.maxSize)

        self.stackedWidget_2.addWidget(self.remoteDocker)

        self.gridLayout_3.addWidget(self.stackedWidget_2, 2, 0, 1, 3)

        self.label_3 = QLabel(self.row_21)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_21)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout_3.addWidget(self.commandLinkButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.radioButton = QRadioButton(self.row_21)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 1, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.row_21)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout_191.addLayout(self.gridLayout_3)


        self.verticalLayout1.addWidget(self.row_21)

        self.row_31 = QFrame(self.setupView)
        self.row_31.setObjectName(u"row_31")
        self.row_31.setMinimumSize(QSize(0, 25))
        self.row_31.setMaximumSize(QSize(16777215, 25))
        self.row_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.row_31)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.buttonBox = QDialogButtonBox(self.row_31)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Help|QDialogButtonBox.StandardButton.Reset|QDialogButtonBox.StandardButton.RestoreDefaults|QDialogButtonBox.StandardButton.Save)

        self.horizontalLayout_121.addWidget(self.buttonBox)


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
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


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
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
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

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"qsLAM_PCR_AIO", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Erasmus MC", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_projectManager.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_setupView.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_runView.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_analysisView.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">lorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum "
                        "lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsumlorem ipsum lorem ipsum</p></body></html>", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Compile lentiviral vector integration sites from sequencing pipeline", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Create new run", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete run", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export run", None))
        ___qtablewidgetitem = self.runsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.runsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Creation Timestamp", None));
        ___qtablewidgetitem2 = self.runsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtablewidgetitem3 = self.runsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Run Timestamp", None));
        ___qtablewidgetitem4 = self.runsTable.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Column headers", None));
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
        ___qtablewidgetitem26 = self.runsTable.verticalHeaderItem(22)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.runsTable.isSortingEnabled()
        self.runsTable.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.runsTable.item(0, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem28 = self.runsTable.item(0, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Creation Timestamp", None));
        ___qtablewidgetitem29 = self.runsTable.item(0, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtablewidgetitem30 = self.runsTable.item(0, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Last Run Timestamp", None));
        ___qtablewidgetitem31 = self.runsTable.item(1, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem32 = self.runsTable.item(1, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem33 = self.runsTable.item(1, 2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem34 = self.runsTable.item(1, 3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"test", None));
        self.runsTable.setSortingEnabled(__sortingEnabled)

        self.importRunButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.importRunInput.setText("")
        self.importRunInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.importRunLabel.setText(QCoreApplication.translate("MainWindow", u"Import run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LTR Primer Sequence", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Adapter Sequence", None))
        self.forwardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Forward read", None))
        self.backwardReadLabel.setText(QCoreApplication.translate("MainWindow", u"Backward read", None))
        self.referenceGenomeLabel.setText(QCoreApplication.translate("MainWindow", u"Reference genome\n"
"(Leave blank for H19)", None))
        self.portNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.backwardReadLabel_2.setText(QCoreApplication.translate("MainWindow", u"Backward read", None))
        self.ipAddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP address", None))
        self.dontSendData.setText(QCoreApplication.translate("MainWindow", u"Don't send input data to remote server. I already have the input data mounted correctly in the docker container", None))
        self.forwardReadLabel_2.setText(QCoreApplication.translate("MainWindow", u"Forward read", None))
        self.referenceGenomeLabel_2.setText(QCoreApplication.translate("MainWindow", u"Reference genome\n"
"(Leave blank for H19)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  Docker setup", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Not sure what to pick?", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Charts here and stuff after run is complete...", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run!", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Not sure yet", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"What this is", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"For", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Miro & Liam Weitzel", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi
