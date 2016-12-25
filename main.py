# -*- coding: utf-8 -*-
"""
ZetCode PyQt4 tutorial

This is a simple drag and
drop example.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt4 import QtGui
import os
import cv2
from Review import launch_review
import bokeh
import subprocess



print(cv2.__version__)



class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

        self.setAcceptDrops(True)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile().toLocal8Bit().data()
            if os.path.isfile(path):
                print path
                # do other stuff with path...


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    #launch_review()
    main()
#import matplotlib.pyplot as plt
#import numpy as np
#import time

print('Hello World')
#x = np.random.randn(10)
#y = np.random.randn(10)
#print(x,y)
#time.sleep(3)

#plt.scatter(x,y)
#plt.title("Hello World")
#plt.show()


