# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'futures_algo_dev.ui'
#
# Created: Fri Dec 26 00:54:09 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(821, 554)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_backtest_setup_run = QtGui.QWidget()
        self.tab_backtest_setup_run.setObjectName(_fromUtf8("tab_backtest_setup_run"))
        self.frame = QtGui.QFrame(self.tab_backtest_setup_run)
        self.frame.setGeometry(QtCore.QRect(20, 20, 251, 241))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.comboBox_instrument = QtGui.QComboBox(self.frame)
        self.comboBox_instrument.setGeometry(QtCore.QRect(10, 50, 51, 31))
        self.comboBox_instrument.setObjectName(_fromUtf8("comboBox_instrument"))
        self.comboBox_instrument.addItem(_fromUtf8(""))
        self.comboBox_instrument.addItem(_fromUtf8(""))
        self.comboBox_instrument.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox_range = QtGui.QSpinBox(self.frame)
        self.spinBox_range.setGeometry(QtCore.QRect(10, 110, 51, 31))
        self.spinBox_range.setProperty("value", 10)
        self.spinBox_range.setObjectName(_fromUtf8("spinBox_range"))
        self.dateEdit_start_date = QtGui.QDateEdit(self.frame)
        self.dateEdit_start_date.setGeometry(QtCore.QRect(120, 50, 121, 31))
        self.dateEdit_start_date.setCalendarPopup(True)
        self.dateEdit_start_date.setDate(QtCore.QDate(2013, 9, 10))
        self.dateEdit_start_date.setObjectName(_fromUtf8("dateEdit_start_date"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 30, 81, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(120, 90, 81, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dateEdit_end_date = QtGui.QDateEdit(self.frame)
        self.dateEdit_end_date.setGeometry(QtCore.QRect(120, 110, 121, 31))
        self.dateEdit_end_date.setCalendarPopup(True)
        self.dateEdit_end_date.setDate(QtCore.QDate(2014, 11, 30))
        self.dateEdit_end_date.setObjectName(_fromUtf8("dateEdit_end_date"))
        self.checkBox_optimize = QtGui.QCheckBox(self.frame)
        self.checkBox_optimize.setGeometry(QtCore.QRect(10, 150, 97, 22))
        self.checkBox_optimize.setChecked(False)
        self.checkBox_optimize.setObjectName(_fromUtf8("checkBox_optimize"))
        self.checkBox_log_intrabar_data = QtGui.QCheckBox(self.frame)
        self.checkBox_log_intrabar_data.setGeometry(QtCore.QRect(10, 170, 151, 22))
        self.checkBox_log_intrabar_data.setChecked(False)
        self.checkBox_log_intrabar_data.setObjectName(_fromUtf8("checkBox_log_intrabar_data"))
        self.checkBox_write_trade_data = QtGui.QCheckBox(self.frame)
        self.checkBox_write_trade_data.setGeometry(QtCore.QRect(10, 190, 151, 22))
        self.checkBox_write_trade_data.setObjectName(_fromUtf8("checkBox_write_trade_data"))
        self.checkBox_write_bar_data = QtGui.QCheckBox(self.frame)
        self.checkBox_write_bar_data.setGeometry(QtCore.QRect(10, 210, 151, 22))
        self.checkBox_write_bar_data.setObjectName(_fromUtf8("checkBox_write_bar_data"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 16, 251, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_2 = QtGui.QFrame(self.tab_backtest_setup_run)
        self.frame_2.setGeometry(QtCore.QRect(20, 280, 251, 121))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton_run_backtest = QtGui.QPushButton(self.frame_2)
        self.pushButton_run_backtest.setGeometry(QtCore.QRect(10, 10, 231, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_run_backtest.sizePolicy().hasHeightForWidth())
        self.pushButton_run_backtest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.pushButton_run_backtest.setFont(font)
        self.pushButton_run_backtest.setObjectName(_fromUtf8("pushButton_run_backtest"))
        self.progressBar_backtest = QtGui.QProgressBar(self.frame_2)
        self.progressBar_backtest.setGeometry(QtCore.QRect(10, 70, 231, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.progressBar_backtest.setFont(font)
        self.progressBar_backtest.setProperty("value", 0)
        self.progressBar_backtest.setObjectName(_fromUtf8("progressBar_backtest"))
        self.label_time_remaining = QtGui.QLabel(self.frame_2)
        self.label_time_remaining.setGeometry(QtCore.QRect(10, 90, 221, 20))
        self.label_time_remaining.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_time_remaining.setObjectName(_fromUtf8("label_time_remaining"))
        self.tabWidget.addTab(self.tab_backtest_setup_run, _fromUtf8(""))
        self.tab_backtest_view = QtGui.QWidget()
        self.tab_backtest_view.setObjectName(_fromUtf8("tab_backtest_view"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_backtest_view)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_view_date = QtGui.QLabel(self.tab_backtest_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_view_date.sizePolicy().hasHeightForWidth())
        self.label_view_date.setSizePolicy(sizePolicy)
        self.label_view_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_view_date.setObjectName(_fromUtf8("label_view_date"))
        self.verticalLayout_2.addWidget(self.label_view_date)
        self.mpl = MplWidget(self.tab_backtest_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.verticalLayout_2.addWidget(self.mpl)
        self.horizontalScrollBar_range_bar = QtGui.QScrollBar(self.tab_backtest_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_range_bar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_range_bar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_range_bar.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.horizontalScrollBar_range_bar.setFont(font)
        self.horizontalScrollBar_range_bar.setProperty("value", 99)
        self.horizontalScrollBar_range_bar.setSliderPosition(99)
        self.horizontalScrollBar_range_bar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_range_bar.setInvertedAppearance(False)
        self.horizontalScrollBar_range_bar.setInvertedControls(True)
        self.horizontalScrollBar_range_bar.setObjectName(_fromUtf8("horizontalScrollBar_range_bar"))
        self.verticalLayout_2.addWidget(self.horizontalScrollBar_range_bar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_backtest_view, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSetup_Run = QtGui.QAction(MainWindow)
        self.actionSetup_Run.setObjectName(_fromUtf8("actionSetup_Run"))
        self.actionView = QtGui.QAction(MainWindow)
        self.actionView.setObjectName(_fromUtf8("actionView"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Futures Algorithm Development", None))
        self.comboBox_instrument.setItemText(0, _translate("MainWindow", "GC", None))
        self.comboBox_instrument.setItemText(1, _translate("MainWindow", "CL", None))
        self.comboBox_instrument.setItemText(2, _translate("MainWindow", "ZB", None))
        self.label.setText(_translate("MainWindow", "Instrument", None))
        self.label_3.setText(_translate("MainWindow", "Range", None))
        self.dateEdit_start_date.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy", None))
        self.label_4.setText(_translate("MainWindow", "Start Date", None))
        self.label_5.setText(_translate("MainWindow", "End Date", None))
        self.dateEdit_end_date.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy", None))
        self.checkBox_optimize.setText(_translate("MainWindow", "Optimize", None))
        self.checkBox_log_intrabar_data.setText(_translate("MainWindow", "Log intra-bar data", None))
        self.checkBox_write_trade_data.setText(_translate("MainWindow", "Write trade data", None))
        self.checkBox_write_bar_data.setText(_translate("MainWindow", "Write bar data", None))
        self.label_2.setText(_translate("MainWindow", "Backtest Setup", None))
        self.pushButton_run_backtest.setText(_translate("MainWindow", "RUN BACKTEST", None))
        self.label_time_remaining.setText(_translate("MainWindow", "Time Remaining: 0:00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_backtest_setup_run), _translate("MainWindow", "Setup/Run", None))
        self.label_view_date.setText(_translate("MainWindow", "DATE     ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_backtest_view), _translate("MainWindow", "View", None))
        self.actionSetup_Run.setText(_translate("MainWindow", "Setup/Run", None))
        self.actionView.setText(_translate("MainWindow", "View", None))

from mplwidget import MplWidget
