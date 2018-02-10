import os
import sys
import listdir
from PyQt5.QtCore import *  
from PyQt5 import QtCore, QtGui, QtWidgets
current_path="/"
names = listdir.getlist(current_path)

class Ui_Exile(object):
    def setupUi(self, Exile):
        Exile.setObjectName("Exile")
        Exile.resize(920, 600)#420, 714
        #Doco.setFixedSize(420, 714)#
	#Exile.setWindowFlags(QtCore.Qt.FramelessWindowHint)#隐藏默认窗口样式
        self.retranslateUi(Exile)
        QtCore.QMetaObject.connectSlotsByName(Exile)
        

        self.pushButton_pre = QtWidgets.QPushButton(Exile,clicked=lambda:Event.Pre(self))
        self.pushButton_pre.setGeometry(QtCore.QRect(0, 575, 25, 25))
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.pushButton_pre.setText("..")

        self.listWidget = QtWidgets.QListWidget(Exile)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 920, 575))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.verticalScrollBar().setSingleStep(1)#set step
        #self.listWidget.setAlternatingRowColors(True);
        #self.listWidget.setVisible(False)
        self.music_list()

    def retranslateUi(self, Exile):
        _translate = QtCore.QCoreApplication.translate
        Exile.setWindowTitle(_translate("Exile", "Exile"))
        #self.label_name.setText(_translate("Exile", ""))
        #self.label_time.setText(_translate("Exile", ""))

    def music_list(self):
        self.listWidget.clear()#clear list
        #print(len(names))
        for n in range(0,len(names)):
            # Create QCustomQWidget
            myItemQWidget = ItemQWidget(n,self)
            myItemQWidget.setName()
            #myItemQWidget.setPlay()
            #myItemQWidget.setEvent(self.listWidget)
            # Create QListWidgetItem
            item = QtWidgets.QListWidgetItem(self.listWidget)
            # Set size hint
            item.setSizeHint(myItemQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, myItemQWidget)


class ItemQWidget(QtWidgets.QWidget):
    def __init__(self,n,ui,parent = None):
        super(ItemQWidget, self).__init__(parent)
        self.n = n
        self.ui = ui
        self.textQHBoxLayout = QtWidgets.QHBoxLayout()
        self.name	     = QtWidgets.QLabel()#文件或文件夹名
        #self.play_btn= QtWidgets.QToolButton()#播放
        self.textQHBoxLayout.addWidget(self.name)
        #self.textQHBoxLayout.addWidget(self.play_btn)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQHBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    def setName (self):
        self.name.setText(names[self.n])
    def mouseDoubleClickEvent(self, e):##重载鼠标点击事件
        global current_path
        global names
        print("clicked    "+self.name.text())
        current_path = current_path+self.name.text()+"/"
        if(os.path.isdir(current_path)):
            names = listdir.getlist(current_path)
            self.ui.music_list()#刷新路经表
        
class Event():
    def Pre(self):
        global current_path
        global names
        cache = current_path.split("/")
        le = len(cache[len(cache)-2])+1
        current_path = current_path[:-le]
        names = listdir.getlist(current_path)
        self.music_list()#刷新路经表
        print(names)

if __name__ == '__main__':   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Exile()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
