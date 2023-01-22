# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_code2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon

from ui.ui_element import MyLabel
from ui.ui_texts import TITLE, WIN_TITLE, BULLETIN_BOARD, PIC_PATH, GITHUB_URL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1158, 651)
        MainWindow.setMinimumSize(QtCore.QSize(1158, 651))
        MainWindow.setMaximumSize(QtCore.QSize(1158, 651))

        MainWindow.setWindowIcon(QIcon("favicon.ico"))
        # 添加ico

        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 420, 541, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 521, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.xiaZaiKaoShiXinXiProgressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.xiaZaiKaoShiXinXiProgressBar.setProperty("value", 0)
        self.xiaZaiKaoShiXinXiProgressBar.setTextVisible(False)
        self.xiaZaiKaoShiXinXiProgressBar.setObjectName("xiaZaiKaoShiXinXiProgressBar")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.xiaZaiKaoShiXinXiProgressBar)
        self.xiaZaiZhuanYeXinXiProgressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.xiaZaiZhuanYeXinXiProgressBar.setProperty("value", 0)
        self.xiaZaiZhuanYeXinXiProgressBar.setTextVisible(False)
        self.xiaZaiZhuanYeXinXiProgressBar.setObjectName("xiaZaiZhuanYeXinXiProgressBar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.xiaZaiZhuanYeXinXiProgressBar)
        self.xiaZaiYuanXiaoXinXiProgressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.xiaZaiYuanXiaoXinXiProgressBar.setProperty("value", 0)
        self.xiaZaiYuanXiaoXinXiProgressBar.setTextVisible(False)
        self.xiaZaiYuanXiaoXinXiProgressBar.setObjectName("xiaZaiYuanXiaoXinXiProgressBar")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xiaZaiYuanXiaoXinXiProgressBar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dangQianRenWuLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dangQianRenWuLable.setFont(font)
        self.dangQianRenWuLable.setObjectName("dangQianRenWuLable")
        self.horizontalLayout_2.addWidget(self.dangQianRenWuLable)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.quXiaoXiaZaiBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.quXiaoXiaZaiBtn.setObjectName("quXiaoXiaZaiBtn")
        self.horizontalLayout_2.addWidget(self.quXiaoXiaZaiBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 420, 601, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 571, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_3)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.shanChuXuanZhongBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.shanChuXuanZhongBtn.setObjectName("shanChuXuanZhongBtn")
        self.horizontalLayout_3.addWidget(self.shanChuXuanZhongBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        # self.shangChuanWenDangBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        # self.shangChuanWenDangBtn.setObjectName("shangChuanWenDangBtn")
        # self.horizontalLayout_3.addWidget(self.shangChuanWenDangBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)

        self.daShangBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.daShangBtn.setObjectName("daShang")
        self.horizontalLayout_3.addWidget(self.daShangBtn)
        self.daShangBtn.setText("💴打赏")

        self.daoChuSheZhi = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.daoChuSheZhi.setObjectName("daoChuSheZhi")
        self.horizontalLayout_3.addWidget(self.daoChuSheZhi)

        self.daoChu = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.daoChu.setObjectName("daoChu")
        self.horizontalLayout_3.addWidget(self.daoChu)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(740, 72, 411, 344))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")

        self.gongGaoText = QtWidgets.QLabel(self.groupBox)
        self.gongGaoText.setGeometry(QtCore.QRect(10, 20, 391, 311))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gongGaoText.setWordWrap(True)
        self.gongGaoText.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # 可被鼠标选择复制
        self.gongGaoText.setFont(font)
        self.gongGaoText.setObjectName("gongGaoText")

        self.gongGaoText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 80, 731, 336))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 360, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 341, 171))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.xueWeiLeiBieBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.xueWeiLeiBieBox.setObjectName("xueWeiLeiBieBox")
        self.xueWeiLeiBieBox.addItem("")
        self.xueWeiLeiBieBox.addItem("")
        self.xueWeiLeiBieBox.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xueWeiLeiBieBox)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.menLeiLeiBieBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.menLeiLeiBieBox.setObjectName("menLeiLeiBieBox")
        self.menLeiLeiBieBox.addItem("")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.menLeiLeiBieBox)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        self.xueKeLeiBieBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.xueKeLeiBieBox.setObjectName("xueKeLeiBieBox")
        self.xueKeLeiBieBox.addItem("")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.xueKeLeiBieBox)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem11 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        spacerItem12 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem13 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        spacerItem14 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem15 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        spacerItem16 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.formLayout_3.setLayout(5, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_13)

        self.biXuanZhuText = QtWidgets.QLabel(self.groupBox_4)
        self.biXuanZhuText.setWordWrap(True)
        self.biXuanZhuText.setGeometry(QtCore.QRect(10, 200, 341, 61))
        self.biXuanZhuText.setObjectName("biXuanZhuText")
        self.biXuanZhuText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(360, 10, 371, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_6)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem17)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem18 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        spacerItem19 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem19)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_7)
        self.zhuanYeMingChengBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zhuanYeMingChengBox.setFont(font)
        self.zhuanYeMingChengBox.setObjectName("zhuanYeMingChengBox")
        self.zhuanYeMingChengBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zhuanYeMingChengBox)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem20)
        self.xueXIFangShiBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xueXIFangShiBox.setFont(font)
        self.xueXIFangShiBox.setObjectName("xueXIFangShiBox")

        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.xueXIFangShiBox)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem21)
        self.yuanXiaoJianSheJiHuaBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yuanXiaoJianSheJiHuaBox.setFont(font)
        self.yuanXiaoJianSheJiHuaBox.setObjectName("yuanXiaoJianSheJiHuaBox")

        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.yuanXiaoJianSheJiHuaBox)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem22)
        self.yuanXiaoQuYuBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yuanXiaoQuYuBox.setFont(font)
        self.yuanXiaoQuYuBox.setObjectName("yuanXiaoQuYuBox")

        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.yuanXiaoQuYuBox)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem23)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem24)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        spacerItem25 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem25)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem26 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem26)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem27 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem27)
        self.formLayout_2.setLayout(6, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem28 = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem28)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem29 = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem29)
        self.formLayout_2.setLayout(8, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_8)

        self.keXuanZhuText = QtWidgets.QLabel(self.groupBox_6)
        self.keXuanZhuText.setWordWrap(True)
        self.keXuanZhuText.setGeometry(QtCore.QRect(10, 200, 351, 61))
        self.keXuanZhuText.setObjectName("keXuanZhuText")
        self.keXuanZhuText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(280, 290, 171, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.kaiShiXiaZaiBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.kaiShiXiaZaiBtn.setObjectName("kaiShiXiaZaiBtn")
        self.horizontalLayout_4.addWidget(self.kaiShiXiaZaiBtn)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 731, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem30)
        self.biaoTiLable = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.biaoTiLable.setFont(font)
        self.biaoTiLable.setObjectName("biaoTiLable")
        self.horizontalLayout.addWidget(self.biaoTiLable)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem31)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(740, 4, 411, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem32)

        self.gitHublabel = MyLabel(self.horizontalLayoutWidget_3)
        self.gitHublabel.setUrl(GITHUB_URL)
        self.gitHublabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gitHublabel.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.gitHublabel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", WIN_TITLE))
        self.groupBox_2.setTitle(_translate("MainWindow", "下载进度"))
        self.label_2.setText(_translate("MainWindow", "下载院校信息"))
        self.label_3.setText(_translate("MainWindow", "下载专业信息"))
        self.label_4.setText(_translate("MainWindow", "下载考试信息"))
        self.xiaZaiKaoShiXinXiProgressBar.setFormat(_translate("MainWindow", "%p%"))
        self.dangQianRenWuLable.setText(_translate("MainWindow", "当前下载任务"))
        self.quXiaoXiaZaiBtn.setText(_translate("MainWindow", "取消"))
        self.groupBox_3.setTitle(_translate("MainWindow", "已完成"))
        self.shanChuXuanZhongBtn.setText(_translate("MainWindow", "删除选中"))
        # self.shangChuanWenDangBtn.setText(_translate("MainWindow", "上传文档"))
        self.daoChu.setText(_translate("MainWindow", "导出"))
        self.daoChuSheZhi.setText(_translate("MainWindow", "导出设置"))
        self.groupBox.setTitle(_translate("MainWindow", "Tips"))
        self.gongGaoText.setText("%s" % BULLETIN_BOARD)
        self.groupBox_4.setTitle(_translate("MainWindow", "必选"))
        self.xueWeiLeiBieBox.setItemText(0, _translate("MainWindow", "请选择"))
        self.xueWeiLeiBieBox.setItemText(1, _translate("MainWindow", "专业学位"))
        self.xueWeiLeiBieBox.setItemText(2, _translate("MainWindow", "学术学位"))
        self.menLeiLeiBieBox.setItemText(0, _translate("MainWindow", "请选择"))
        self.xueKeLeiBieBox.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_11.setText(_translate("MainWindow", "学位类别"))
        self.label_13.setText(_translate("MainWindow", "门类类别"))
        self.label_12.setText(_translate("MainWindow", "学科类别"))
        self.biXuanZhuText.setText("注：你必须选择这些选项，具体可参考研招网对专业领域的选项")
        self.groupBox_6.setTitle(_translate("MainWindow", "可选"))
        self.label_9.setText(_translate("MainWindow", "专业名称"))
        self.zhuanYeMingChengBox.setItemText(0, _translate("MainWindow", "不做选择"))
        self.label_14.setText(_translate("MainWindow", "学习方式"))
        self.label_7.setText(_translate("MainWindow", "院校建设计划"))
        self.label_8.setText(_translate("MainWindow", "院校区域"))
        self.keXuanZhuText.setText(
            "注： 普通院校 将会 排除 211、985和双一流院校")
        self.kaiShiXiaZaiBtn.setText(_translate("MainWindow", "开始下载"))
        self.biaoTiLable.setText(_translate("MainWindow", TITLE))
        self.gitHublabel.setText(_translate("MainWindow", "Star"))
        self.gitHublabel.setPixmap(QPixmap(PIC_PATH))
        self.gitHublabel.setCursor(Qt.PointingHandCursor)
        self.gitHublabel.setScaledContents(True)
