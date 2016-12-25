import sys
from PyQt4 import QtGui, QtCore
import os



class DragButton(QtGui.QPushButton):
    def __init__(self, title, parent, linked_line_edit):
        super(DragButton, self).__init__(title, parent)
        self.path = None
        self.setAcceptDrops(True)
        self.linked_line_edit = linked_line_edit


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile().toLocal8Bit().data()
            if os.path.isfile(path):
                self.path = path
                self.linked_line_edit.setText(path)
            else:
                print('Not a Valid Path =(')






class TAIA_APP(QtGui.QWidget):

    def __init__(self):
        super(TAIA_APP, self).__init__()
        self.initUI()

    def selectFile(self):
        self.assesment_load_line_edit.setText(QtGui.QFileDialog.getOpenFileName())



    def initUI(self):




        # Logo
        self.logo = QtGui.QLabel()
        self.logo.setFixedSize(1000,200)
        self.logo_pixmap = QtGui.QPixmap('C:\\Users\\nate\\PycharmProjects\\TAIA\\Images\\logo.png')
        self.logo_pixmap = self.logo_pixmap.scaled(self.logo.size(), QtCore.Qt.KeepAspectRatio)
        self.logo.setPixmap(self.logo_pixmap)

        self.website = QtGui.QLabel()
        self.website.setText('''<a href='https://nate-russell.github.io/TAIA/'>TAIA Website</a>''')
        self.website.setOpenExternalLinks(True)



        # Layout Boxes
        self.outer_vbox = QtGui.QVBoxLayout()
        self.top_hbox = QtGui.QHBoxLayout() # logo and links
        self.bottom_hbox = QtGui.QHBoxLayout() # three panels
        self.left_vbox = QtGui.QVBoxLayout() # Make/Modify Assessment
        self.center_vbox = QtGui.QVBoxLayout() # Load Assessment
        self.right_vbox = QtGui.QVBoxLayout() # Review Assessment
        # Nest Layout Boxes
        self.bottom_hbox.addLayout(self.left_vbox)
        self.bottom_hbox.addLayout(self.center_vbox)
        self.bottom_hbox.addLayout(self.right_vbox)
        self.outer_vbox.addLayout(self.top_hbox)
        self.outer_vbox.addLayout(self.bottom_hbox)
        self.outer_vbox.addStretch(1)
        # 3 panel labels
        self.left_label = QtGui.QLabel('Make Assessment')
        self.center_label = QtGui.QLabel('Load Assessment')
        self.right_label = QtGui.QLabel('Review Assessment')
        self.left_vbox.addWidget(self.left_label)
        self.center_vbox.addWidget(self.center_label)
        self.right_vbox.addWidget(self.right_label)

        # Top Hbox
        self.top_hbox.addWidget(self.logo)
        self.top_hbox.addStretch(1)
        self.top_hbox.addWidget(self.website)



        # Left Panel

        self.make_assessment = QtGui.QPushButton()
        self.make_assessment.setText('Make Assessment')

        self.modify_assessment = QtGui.QPushButton()
        self.modify_assessment.setText('Modify Assessment')

        self.modify_list = QtGui.QListWidget()
        #self.modify_list.addScrollBarWidget()
        self.modify_list.addItems(['a','b','c'])

        self.left_vbox.addWidget(self.make_assessment)
        self.left_vbox.addWidget(QtGui.QLabel('Modify Assessment'))
        self.left_vbox.addWidget(self.modify_list)
        self.left_vbox.addWidget(self.modify_assessment)
        self.left_vbox.addStretch(1)




        # Center Panel

        self.assesment_load_line_edit_label = QtGui.QLabel('Path to Assessment')
        self.assesment_load_line_edit = QtGui.QLineEdit()
        self.assessment_path = QtGui.QHBoxLayout()
        self.assessment_path.addWidget(self.assesment_load_line_edit_label)
        self.assessment_path.addWidget(self.assesment_load_line_edit)

        self.browse_file = DragButton("Get Path Button", self, self.assesment_load_line_edit)
        self.browse_file.setText('Click to Browse Files on Local Machine\nor\nDrag File on to this Button')
        self.browse_file.clicked.connect(self.selectFile)
        self.browse_file.setFixedHeight(300)

        self.center_vbox.addLayout(self.assessment_path)
        self.center_vbox.addWidget(self.browse_file)



        # Right Panel

        self.review_assessment = QtGui.QPushButton()
        self.review_assessment.setText('Review Assessment')

        self.review_assessment_list = QtGui.QListWidget()
        self.review_assessment_list.addItems(['a', 'b', 'c'])
        self.review_assessment_list.setAlternatingRowColors(True)


        self.right_vbox.addWidget(self.review_assessment_list)
        self.right_vbox.addWidget(self.review_assessment)
        self.right_vbox.addStretch(1)





        self.setLayout(self.outer_vbox)
        self.setGeometry(100, 100, 2800, 1400)
        self.setWindowTitle('TAIA')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("cleanlooks"))

    ex = TAIA_APP()
    app.setStyleSheet('QLabel{color: #fff;} QPushButton{background-color: rgb(216,33,100); color: #fff} QListWidget{}')

    QtGui.QColor('')

    p = ex.palette()
    #print(type(QtCore.Qt.red))
    #print(QtCore.Qt.red)
    p.setColor(ex.backgroundRole(), QtGui.QColor(38,38,38))
    ex.setPalette(p)

    #ex.setStyleSheet('')
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()