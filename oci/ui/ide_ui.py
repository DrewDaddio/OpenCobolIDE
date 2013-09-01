# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ide.ui'
#
# Created: Sun Sep  1 15:56:40 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_6 = QtGui.QGridLayout(self.page)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.QHomeWidget = QHomeWidget(self.page)
        self.QHomeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.QHomeWidget.setProperty("icon", icon)
        self.QHomeWidget.setObjectName("QHomeWidget")
        self.gridLayout_6.addWidget(self.QHomeWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidgetEditors = QCodeEditTabWidget(self.page_2)
        self.tabWidgetEditors.setObjectName("tabWidgetEditors")
        self.gridLayout_2.addWidget(self.tabWidgetEditors, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarFile = QtGui.QToolBar(MainWindow)
        self.toolBarFile.setObjectName("toolBarFile")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFile)
        self.toolBarCode = QtGui.QToolBar(MainWindow)
        self.toolBarCode.setObjectName("toolBarCode")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCode)
        self.dockWidgetLogs = QtGui.QDockWidget(MainWindow)
        self.dockWidgetLogs.setObjectName("dockWidgetLogs")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidgetLogs = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetLogs.setObjectName("tabWidgetLogs")
        self.tabCompiler = QtGui.QWidget()
        self.tabCompiler.setObjectName("tabCompiler")
        self.gridLayout_4 = QtGui.QGridLayout(self.tabCompiler)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.errorsTable = QErrorsTable(self.tabCompiler)
        self.errorsTable.setMinimumSize(QtCore.QSize(0, 0))
        self.errorsTable.setObjectName("errorsTable")
        self.errorsTable.setColumnCount(5)
        self.errorsTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.errorsTable, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ide-icons/rc/applications-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidgetLogs.addTab(self.tabCompiler, icon1, "")
        self.tabProgramOutput = QtGui.QWidget()
        self.tabProgramOutput.setObjectName("tabProgramOutput")
        self.gridLayout_5 = QtGui.QGridLayout(self.tabProgramOutput)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.consoleOutput = QInteractiveConsole(self.tabProgramOutput)
        self.consoleOutput.setObjectName("consoleOutput")
        self.gridLayout_5.addWidget(self.consoleOutput, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ide-icons/rc/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidgetLogs.addTab(self.tabProgramOutput, icon2, "")
        self.gridLayout_3.addWidget(self.tabWidgetLogs, 0, 0, 1, 1)
        self.dockWidgetLogs.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetLogs)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent_files = QtGui.QMenu(self.menuFile)
        self.menuRecent_files.setObjectName("menuRecent_files")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.mnuActiveEditor = QtGui.QMenu(self.menuEdit)
        self.mnuActiveEditor.setObjectName("mnuActiveEditor")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QtGui.QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuDock_panels = QtGui.QMenu(self.menuView)
        self.menuDock_panels.setObjectName("menuDock_panels")
        self.menuCobol = QtGui.QMenu(self.menuBar)
        self.menuCobol.setObjectName("menuCobol")
        self.menuProgramType = QtGui.QMenu(self.menuCobol)
        self.menuProgramType.setObjectName("menuProgramType")
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.dockWidgetNavPanel = QtGui.QDockWidget(MainWindow)
        self.dockWidgetNavPanel.setObjectName("dockWidgetNavPanel")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_7 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_7.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.twNavigation = QtGui.QTreeWidget(self.dockWidgetContents_2)
        self.twNavigation.setObjectName("twNavigation")
        self.twNavigation.headerItem().setText(0, "1")
        self.twNavigation.header().setVisible(False)
        self.gridLayout_7.addWidget(self.twNavigation, 0, 0, 1, 1)
        self.dockWidgetNavPanel.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetNavPanel)
        self.actionQuit = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ide-icons/rc/system-log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCompile = QtGui.QAction(MainWindow)
        self.actionCompile.setIcon(icon1)
        self.actionCompile.setIconVisibleInMenu(True)
        self.actionCompile.setObjectName("actionCompile")
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setIcon(icon2)
        self.actionRun.setIconVisibleInMenu(True)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon5)
        self.actionSaveAs.setIconVisibleInMenu(True)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ide-icons/rc/view-fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullscreen.setIcon(icon6)
        self.actionFullscreen.setIconVisibleInMenu(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionNew = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon7)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon8)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("rc/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon9)
        self.actionClear.setIconVisibleInMenu(True)
        self.actionClear.setObjectName("actionClear")
        self.aShowFilesToolbar = QtGui.QAction(MainWindow)
        self.aShowFilesToolbar.setCheckable(True)
        self.aShowFilesToolbar.setObjectName("aShowFilesToolbar")
        self.aShowCodeToolbar = QtGui.QAction(MainWindow)
        self.aShowCodeToolbar.setCheckable(True)
        self.aShowCodeToolbar.setObjectName("aShowCodeToolbar")
        self.aShowLogsWin = QtGui.QAction(MainWindow)
        self.aShowLogsWin.setCheckable(True)
        self.aShowLogsWin.setObjectName("aShowLogsWin")
        self.aShowNavWin = QtGui.QAction(MainWindow)
        self.aShowNavWin.setCheckable(True)
        self.aShowNavWin.setObjectName("aShowNavWin")
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/ide-icons/rc/Preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon10)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon11)
        self.actionHelp.setObjectName("actionHelp")
        self.actionProgram = QtGui.QAction(MainWindow)
        self.actionProgram.setCheckable(True)
        self.actionProgram.setChecked(True)
        self.actionProgram.setObjectName("actionProgram")
        self.actionSubprogram = QtGui.QAction(MainWindow)
        self.actionSubprogram.setCheckable(True)
        self.actionSubprogram.setObjectName("actionSubprogram")
        self.toolBarFile.addAction(self.actionNew)
        self.toolBarFile.addAction(self.actionOpen)
        self.toolBarFile.addSeparator()
        self.toolBarFile.addAction(self.actionSave)
        self.toolBarFile.addAction(self.actionSaveAs)
        self.toolBarCode.addAction(self.actionCompile)
        self.toolBarCode.addAction(self.actionRun)
        self.menuRecent_files.addSeparator()
        self.menuRecent_files.addAction(self.actionClear)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuRecent_files.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.mnuActiveEditor.addSeparator()
        self.menuEdit.addAction(self.mnuActiveEditor.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuToolbars.addAction(self.aShowFilesToolbar)
        self.menuToolbars.addAction(self.aShowCodeToolbar)
        self.menuDock_panels.addAction(self.aShowLogsWin)
        self.menuDock_panels.addAction(self.aShowNavWin)
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addAction(self.menuDock_panels.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFullscreen)
        self.menuProgramType.addAction(self.actionProgram)
        self.menuProgramType.addAction(self.actionSubprogram)
        self.menuCobol.addAction(self.menuProgramType.menuAction())
        self.menuCobol.addSeparator()
        self.menuCobol.addAction(self.actionCompile)
        self.menuCobol.addAction(self.actionRun)
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCobol.menuAction())
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidgetLogs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenCobolIDE", None, QtGui.QApplication.UnicodeUTF8))
        self.QHomeWidget.setProperty("title", QtGui.QApplication.translate("MainWindow", "Welcome to OpenCobolIDE", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBarFile.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Toolbar File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBarCode.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Toolbar Code", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetLogs.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabCompiler), QtGui.QApplication.translate("MainWindow", "Compiler", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLogs.setTabToolTip(self.tabWidgetLogs.indexOf(self.tabCompiler), QtGui.QApplication.translate("MainWindow", "Show compiler log", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabProgramOutput), QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRecent_files.setTitle(QtGui.QApplication.translate("MainWindow", "Recent files", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuActiveEditor.setTitle(QtGui.QApplication.translate("MainWindow", "Active editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuToolbars.setTitle(QtGui.QApplication.translate("MainWindow", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDock_panels.setTitle(QtGui.QApplication.translate("MainWindow", "Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCobol.setTitle(QtGui.QApplication.translate("MainWindow", "Cobol", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProgramType.setTitle(QtGui.QApplication.translate("MainWindow", "Program type", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetNavPanel.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit application (Ctrl+Q)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompile.setText(QtGui.QApplication.translate("MainWindow", "Compile", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompile.setToolTip(QtGui.QApplication.translate("MainWindow", "Compile the current file (F8)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompile.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setToolTip(QtGui.QApplication.translate("MainWindow", "Run the current file (F5)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About OpenCobolIDE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setToolTip(QtGui.QApplication.translate("MainWindow", "About OpenCobol IDE (F1)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("MainWindow", "Save current file (Ctrl+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save current file as (Ctrl+Shift+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setText(QtGui.QApplication.translate("MainWindow", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setToolTip(QtGui.QApplication.translate("MainWindow", "Toggle fullscreen (F12)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setShortcut(QtGui.QApplication.translate("MainWindow", "F11", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("MainWindow", "New file (Ctrl+N)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setToolTip(QtGui.QApplication.translate("MainWindow", "Open a file (Ctrl+O)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear list of recent files", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowFilesToolbar.setText(QtGui.QApplication.translate("MainWindow", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowFilesToolbar.setToolTip(QtGui.QApplication.translate("MainWindow", "Show/Hide the files toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowCodeToolbar.setText(QtGui.QApplication.translate("MainWindow", "Code", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowCodeToolbar.setToolTip(QtGui.QApplication.translate("MainWindow", "Show/Hide code toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowLogsWin.setText(QtGui.QApplication.translate("MainWindow", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowLogsWin.setToolTip(QtGui.QApplication.translate("MainWindow", "Show/Hide logs window", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowLogsWin.setShortcut(QtGui.QApplication.translate("MainWindow", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowNavWin.setText(QtGui.QApplication.translate("MainWindow", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowNavWin.setToolTip(QtGui.QApplication.translate("MainWindow", "Show/Hide navigation panel", None, QtGui.QApplication.UnicodeUTF8))
        self.aShowNavWin.setShortcut(QtGui.QApplication.translate("MainWindow", "F10", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setToolTip(QtGui.QApplication.translate("MainWindow", "Edit the application settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProgram.setText(QtGui.QApplication.translate("MainWindow", "Executable", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSubprogram.setText(QtGui.QApplication.translate("MainWindow", "Module", None, QtGui.QApplication.UnicodeUTF8))

from pyqode.widgets import QErrorsTable, QInteractiveConsole, QCodeEditTabWidget, QHomeWidget
from . import ide_rc