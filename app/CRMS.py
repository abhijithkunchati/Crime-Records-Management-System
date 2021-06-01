import webbrowser as wb
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,storage
from firebase_admin import credentials
from firebase_admin import firestore
import pathlib
cred_path=pathlib.Path(__file__).parent.absolute()


credfullpath=cred_path.absolute().__str__()+"\certificate\crime-records-b069d-firebase-adminsdk-rgpkd-95f65d75d3.json"


cred = credentials.Certificate(credfullpath)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'crime-records-b069d.appspot.com'})
bucket = storage.bucket()
db2 = firestore.client()
col_ref = db2.collection(u'CRMS')


db = firestore.client()
doc_ref = db.collection(u'login-credentials').document(u'username-password').get()



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 812)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 10, 261, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(480, 480, 261, 31))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 441, 261, 31))
        self.lineEdit_2.setClearButtonEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 310, 651, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 440, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 540, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 540, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 480, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRMS"))
        self.label_2.setText(_translate("MainWindow", "CRIME RECORDS MANAGEMENT SYSTEM"))
        self.label_2.setStyleSheet("color:white")
        self.label_3.setStyleSheet("color:white")
        self.label_4.setStyleSheet("color:white")
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.label_4.setText(_translate("MainWindow", "Password"))
# start edit.......button functions on win1

        self.pushButton.clicked.connect(self.clicked)
        self.pushButton_2.clicked.connect(self.clicked_2)

    def clicked_2(self):
        sys.exit(app.exec_())


    def clicked(self):
        password = self.lineEdit.text()
        username = self.lineEdit_2.text()


        try :
            rpass=doc_ref.get(username)
            if rpass == password:

                MainWindow.close()
                MainWindow2.show()
                self.lineEdit_2.setText("")
                self.lineEdit.setText("")
            else:
                self.lineEdit.setText("")
                self.unauth()

        except :
            self.lineEdit.setText("")
            self.unauth()











    def unauth(self):
        msg = QMessageBox()
        msg.setWindowTitle("invalid")
        msg.setText("Invalid Credentials")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec()



##### end edit
##############2nd window
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.setEnabled(True)
        MainWindow2.resize(1067, 780)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow2.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 340, 1041, 331))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QtCore.QRect(20, 370, 1031, 301))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(480, 110, 151, 22))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(382, 110, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(640, 110, 93, 21))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(270, 210, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 240, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setGeometry(QtCore.QRect(500, 210, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(510, 170, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(200, 230, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(450, 210, 41, 20))
        self.label_4.setObjectName("label_4")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setEnabled(False)
        self.dateEdit_2.setGeometry(QtCore.QRect(500, 240, 110, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(460, 240, 16, 16))
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 110, 101, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 130, 120, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(390, 230, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(650, 230, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(820, 720, 191, 16))
        self.label_8.setObjectName("label_8")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setGeometry(QtCore.QRect(740, 210, 101, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(740, 240, 121, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 680, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 680, 131, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(960, 30, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(890, 220, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(960, 70, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.addrec)

        MainWindow2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        #####################################################################################################
        self.pushButton.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.logout)
        self.pushButton_5.clicked.connect(self.filter)
        self.radioButton.clicked.connect(self.sel_search)
        self.radioButton_2.clicked.connect(self.sel_filter)
        self.pushButton_3.clicked.connect(self.get_charge)
        self.pushButton_2.clicked.connect(self.get_fir)
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0,0,QTableWidgetItem("S.NO"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("File-ID"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Nature of Crime"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Victim-ID"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("FIR-ID"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("ChargeSheet-ID"))
        self.tableWidget.setItem(0, 6, QTableWidgetItem("Gender"))
        self.tableWidget.setItem(0, 7, QTableWidgetItem("Date (Y/M/D)"))
        self.tableWidget.setItem(0, 8, QTableWidgetItem("Offence Type"))
        self.tableWidget.pressed.connect(self.enable)
    fir=""
    chr=""
    def search(self):
        self.tableWidget.setEnabled(True)
        self.clear()
        cur_ind = self.comboBox.currentIndex()
        if cur_ind==0:
            id_type = "File_ID"
        if cur_ind == 1:
            id_type = "Victim_ID"
        if cur_ind == 2:
            id_type = "FIR_ID"

        search_string =self.lineEdit.text()

        docs = db2.collection(u'CRMS').where(id_type, u"==", search_string).stream()
        stream_empty = True
        i=0
        for doc in docs:
            i+=1
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            stream_empty = False
            self.fir =doc.get("FIR_ID")
            self.chr =doc.get("Chargesheet_ID")
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(i)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(doc.get("File_ID")))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(doc.get("Nature_of_Crime")))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(doc.get("Victim_ID")))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(doc.get("FIR_ID")))
            self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(doc.get("Chargesheet_ID")))
            self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(doc.get("Gender")))
            self.tableWidget.setItem(rowPosition, 7, QTableWidgetItem(doc.get("Date")))
            self.tableWidget.setItem(rowPosition, 8, QTableWidgetItem(doc.get("Offence_Type")))






        if stream_empty:
            msg=QMessageBox()
            msg.setWindowTitle("NOT FOUND")
            msg.setText("No Records Found")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec()

    def enable(self):
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.label_8.close()


    def filter(self):
        self.tableWidget.setEnabled(True)
        self.clear()
        gender1="none"

        if self.checkBox.isChecked():
            gender1="Male"

        if self.checkBox_2.isChecked():
            gender1="Female"

        if self.checkBox.isChecked() and self.checkBox_2.isChecked():
            gender1="none"
        offence="none"
        if self.checkBox_3.isChecked():
            offence="Cognizable"
        if self.checkBox_4.isChecked():
            offence="Non_Cognizable"
        if self.checkBox_4.isChecked() and self.checkBox_3.isChecked():
            offence="none"
        fdate= self.dateEdit.date()
        fdate = fdate.toString(self.dateEdit.displayFormat())
        todate = self.dateEdit_2.date()
        todate = todate.toString(self.dateEdit_2.displayFormat())
        doc1_ref = col_ref
        if gender1 != "none":
            doc1_ref = doc1_ref.where(u"Gender", u"==", gender1)
        if offence != "none":
            doc1_ref = doc1_ref.where(u"Offence_Type", u"==", offence)

        docs = doc1_ref.where(u"Date", u"<=", todate).where(u"Date", u">=", fdate).stream()
        stream_empty= True
        i = 0
        for doc in docs:
            i+=1
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            stream_empty = False
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(i)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(doc.get("File_ID")))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(doc.get("Nature_of_Crime")))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(doc.get("Victim_ID")))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(doc.get("FIR_ID")))
            self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(doc.get("Chargesheet_ID")))
            self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(doc.get("Gender")))
            self.tableWidget.setItem(rowPosition, 7, QTableWidgetItem(doc.get("Date")))
            self.tableWidget.setItem(rowPosition, 8, QTableWidgetItem(doc.get("Offence_Type")))






        if stream_empty:
            msg = QMessageBox()
            msg.setWindowTitle("NOT FOUND")
            msg.setText("No Records Match Your Filters")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec()


    def clear(self):
        rows=self.tableWidget.rowCount()
        rows = rows-1
        while rows != 0 :
            self.tableWidget.removeRow(rows)
            rows = rows -1






    def sel_search(self):
        self.lineEdit.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.label_8.show()
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.label_2.setEnabled(False)
        self.label_3.setEnabled(False)
        self.label_4.setEnabled(False)
        self.dateEdit_2.setEnabled(False)
        self.label_5.setEnabled(False)
        self.label_6.setEnabled(False)
        self.label_7.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
    def sel_filter(self):
        self.lineEdit.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.label_8.show()
        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.dateEdit.setEnabled(True)
        self.label_2.setEnabled(True)
        self.label_3.setEnabled(True)
        self.label_4.setEnabled(True)
        self.dateEdit_2.setEnabled(True)
        self.label_5.setEnabled(True)
        self.label_6.setEnabled(True)
        self.label_7.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        self.checkBox_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)

    def get_charge(self):
        col=5
        row=self.tableWidget.currentRow()
        ID = self.tableWidget.item(row, col).text()
        chradr = "Chargesheets/" + ID + ".pdf"
        dwnadr = cred_path.absolute().__str__()+"\\" + ID + ".pdf"
        pdf = bucket.blob(chradr)
        pdf.download_to_filename(dwnadr)
        wb.open_new(dwnadr)



    def get_fir(self):
        col=4
        row = self.tableWidget.currentRow()
        ID = self.tableWidget.item(row, col).text()
        firadr = "FIR/" + ID + ".pdf"
        dwnadr = cred_path.absolute().__str__()+"\\" + ID + ".pdf"
        pdf = bucket.blob(firadr)
        pdf.download_to_filename(dwnadr)
        wb.open_new(dwnadr)

    def logout(self):
        MainWindow2.close()
        MainWindow.show()
    def addrec(self):
        MainWindow2.close()
        MainWindow3.show()



        ######################################################################################################

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "CRMS"))

        self.label.setText(_translate("MainWindow2", "Crime Records Management System"))
        self.comboBox.setItemText(0, _translate("MainWindow2", "File  ID"))
        self.comboBox.setItemText(1, _translate("MainWindow2", "Victim ID"))
        self.comboBox.setItemText(2, _translate("MainWindow2", "FIR  ID"))
        self.pushButton.setText(_translate("MainWindow2", "Search"))
        self.checkBox.setText(_translate("MainWindow2", "Male"))
        self.checkBox_2.setText(_translate("MainWindow2", "Female"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow2", "yyyy/M/d"))
        self.label_2.setText(_translate("MainWindow2", "Filters:"))
        self.label_3.setText(_translate("MainWindow2", "Gender:"))
        self.label_4.setText(_translate("MainWindow2", "From"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow2", "yyyy/M/d"))
        self.label_5.setText(_translate("MainWindow2", "To"))
        self.radioButton.setText(_translate("MainWindow2", "Search by ID"))
        self.radioButton_2.setText(_translate("MainWindow2", "Filter Records"))
        self.label_6.setText(_translate("MainWindow2", "Date:"))
        self.label_7.setText(_translate("MainWindow2", "Offence Type:"))
        self.checkBox_3.setText(_translate("MainWindow2", "Cognizable"))
        self.checkBox_4.setText(_translate("MainWindow2", "Non-Cognizable"))
        self.pushButton_2.setText(_translate("MainWindow2", "View FIR"))
        self.pushButton_3.setText(_translate("MainWindow2", "View ChargeSheet"))
        self.pushButton_4.setText(_translate("MainWindow2", "Log Out"))
        self.pushButton_6.setText(_translate("MainWindow2", "Add Record"))
        self.pushButton_5.setText(_translate("MainWindow2", "Filter"))
        self.label_8.setText(_translate("MainWindow2", "*Select a Record to view"))


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(1067, 780)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow3.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 180, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 180, 201, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 260, 201, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 260, 55, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(450, 320, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 320, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 290, 55, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(450, 290, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 350, 91, 20))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(450, 350, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 220, 101, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 220, 201, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(660, 390, 27, 22))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.pressed.connect(self.openfir)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 390, 31, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 390, 201, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(354, 430, 81, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 430, 201, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(660, 430, 27, 22))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.pressed.connect(self.openchr)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 480, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 26))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "CRMS"))
        self.pushButton.setText(_translate("MainWindow3", "Back"))
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.setText(_translate("MainWindow3", "Logout"))
        self.pushButton_2.clicked.connect(self.logout)
        self.label.setText(_translate("MainWindow3", "File ID :"))
        self.label_2.setText(_translate("MainWindow3", "Victim ID:"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow3", "yyyy/M/d"))
        self.label_3.setText(_translate("MainWindow3", "Date:"))
        self.label_4.setText(_translate("MainWindow3", "Gender:"))
        self.comboBox.setItemText(0, _translate("MainWindow3", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow3", "Female"))
        self.label_5.setText(_translate("MainWindow3", "Offence Type:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow3", "Cognizable"))
        self.comboBox_2.setItemText(1, _translate("MainWindow3", "Non-Cognizable"))
        self.label_6.setText(_translate("MainWindow3", "Nature of Crime:"))
        self.toolButton.setText(_translate("MainWindow3", "..."))
        self.label_7.setText(_translate("MainWindow3", "FIR:"))
        self.label_8.setText(_translate("MainWindow3", "Chargesheet:"))
        self.toolButton_2.setText(_translate("MainWindow3", "..."))
        self.pushButton_3.setText(_translate("MainWindow3", "Add Record"))
        self.pushButton_3.clicked.connect(self.clicked1)
    def openchr(self):
        file2 = QFileDialog.getOpenFileName()
        file2 = str(file2).split("'")
        self.url2=file2[1]
        name2 = self.url1.split("/")
        name2 = name2[-1]
        name2 = name2.split(".")
        name2 = name2[0]

        self.names2=name2
        self.lineEdit_5.setText(str(file2[1]))


    def openfir(self):

        file1 = QFileDialog.getOpenFileName()
        file1=str(file1).split("'")
        self.url1=file1[1]
        name1=self.url1.split("/")
        name1=name1[-1]
        name1=name1.split(".")
        name1=name1[0]
        self.names1=name1
        self.lineEdit_4.setText(str(file1[1]))

    def clicked1(self):
        fileid=self.lineEdit.text()
        victimid=self.lineEdit_2.text()
        nature=self.lineEdit_3.text()
        if self.comboBox.currentIndex() ==0:
            gender = "Male"
        else:
            gender= "Female"
        if self.comboBox_2.currentIndex()==0:

            offence="Cognizable"
        else:
            offence="Non_Cognizable"
        date = self.dateEdit.date().toString(self.dateEdit.displayFormat())
        counts=col_ref.stream()
        i=0
        for count in counts :
            i+=1
        i=i+1
        name="record"+str(i)


        firadr = "FIR/" + self.names1+".pdf"
        chradr = "Chargesheets/" + self.names2+".pdf"
        blob1 = bucket.blob(firadr)
        blob2 = bucket.blob(chradr)
        blob1.upload_from_filename(self.url1)
        blob2.upload_from_filename(self.url2)
        col_ref.document(name).set({"File_ID": fileid, "Victim_ID": victimid, "Nature_of_Crime": nature, "Gender": gender, "FIR_ID": self.names1,"Chargesheet_ID": self.names2, "Offence_Type":offence,"Date":date  })
        msg = QMessageBox()
        msg.setWindowTitle("Done")
        msg.setText("Record Added Sucessfully")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec()
    def back(self):
        MainWindow2.show()
        MainWindow3.close()
    def logout(self):
        MainWindow3.close()
        MainWindow.show()


############2nd window end
if __name__ == "__main__":
    import sys

    stylesheet = """
            QMainWindow {
                 background-image: url(\""""+cred_path.absolute().__str__().replace("\\","/")+"""/images/2.jpg"); 
                background-repeat: no-repeat; 
                background-position: top;
                }
            """
    stylesheet1 = """
            QMainWindow {
                 background-image: url(\""""+cred_path.absolute().__str__().replace("\\","/")+"""/images/4.jpg"); 
                background-repeat: no-repeat; 
                background-position: top;
                }
            """
    stylesheet2 = """
                    QMainWindow {
                        background-image: url(\""""+cred_path.absolute().__str__().replace("\\","/")+"""/images/3.jpg");
                        background-repeat: no-repeat; 
                        background-position: top;
                    }
                """

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet(stylesheet1)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #####################################
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow2.setStyleSheet(stylesheet)
    ui2 = Ui_MainWindow2()
    ui2.setupUi(MainWindow2)
    #####################################
    MainWindow3=QtWidgets.QMainWindow()
    MainWindow3.setStyleSheet(stylesheet2)
    ui3 = Ui_MainWindow3()
    ui3.setupUi(MainWindow3)
    sys.exit(app.exec_())
