#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#-                                  Imports                               -#
#--------------------------------------------------------------------------# 
#--------------------------------------------------------------------------#

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import numpy as np
import pandas as pd
import sys
import time
import threading
from datetime import datetime
import wget

#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#-                           Creating Objects                             -#
#--------------------------------------------------------------------------# 
#--------------------------------------------------------------------------#


class Ui_cucm_csv_generator(object):
    def setupUi(self, cucm_csv_generator):
        cucm_csv_generator.setObjectName("cucm_csv_generator")
        cucm_csv_generator.resize(1517, 900)
        cucm_csv_generator.setFixedSize(1517,900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Pictures/cisco-icon-23.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cucm_csv_generator.setWindowIcon(icon)
        self.application = QtWidgets.QWidget(cucm_csv_generator)
        self.application.setObjectName("application")
        self.all_tabs = QtWidgets.QTabWidget(self.application)
        self.all_tabs.setEnabled(True)
        self.all_tabs.setGeometry(QtCore.QRect(0, 0, 1521, 891))
        self.all_tabs.setToolTip("")
        self.all_tabs.setStyleSheet("")
        self.all_tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.all_tabs.setObjectName("all_tabs")
        
        #--------------------------------------------------------------------------
        #-                           tab 1                                       -
        #--------------------------------------------------------------------------

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        font = QtGui.QFont()
        font.setPointSize(12)
        
        #----------------------------Entry Boxes-----------------------------------#
        #--------------------------------------------------------------------------#

        self.tab_1_entry_box_01 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_01.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.tab_1_entry_box_01.setFont(font)
        self.tab_1_entry_box_01.setToolTipDuration(-1)
        self.tab_1_entry_box_01.setTabChangesFocus(True)
        self.tab_1_entry_box_01.setPlaceholderText("")
        self.tab_1_entry_box_01.setObjectName("tab_1_entry_box_01")

        self.tab_1_entry_box_02 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_02.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.tab_1_entry_box_02.setFont(font)
        self.tab_1_entry_box_02.setTabChangesFocus(True)
        self.tab_1_entry_box_02.setPlaceholderText("")
        self.tab_1_entry_box_02.setObjectName("tab_1_entry_box_02")

        self.tab_1_entry_box_03 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_03.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.tab_1_entry_box_03.setObjectName("tab_1_entry_box_03")
        for _ in range(7):
            self.tab_1_entry_box_03.addItem("")
        self.tab_1_entry_box_03.setItemText(0, "")

        self.tab_1_entry_box_04 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_04.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.tab_1_entry_box_04.setCurrentText("")
        self.tab_1_entry_box_04.setMaxVisibleItems(20)
        self.tab_1_entry_box_04.setObjectName("tab_1_entry_box_04")
        for _ in range(20):
            self.tab_1_entry_box_04.addItem("")
        self.tab_1_entry_box_04.setItemText(0, "")
        self.tab_1_entry_box_04.activated.connect(self.tab_1_function_auto_set_drop_downs)

        self.tab_1_entry_box_05 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_05.setGeometry(QtCore.QRect(10, 170, 251, 31))
        self.tab_1_entry_box_05.setMaxVisibleItems(20)
        self.tab_1_entry_box_05.setObjectName("tab_1_entry_box_05")
        for _ in range(17):    
            self.tab_1_entry_box_05.addItem("")
        self.tab_1_entry_box_05.setItemText(0, "")

        self.tab_1_entry_box_06 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_06.setGeometry(QtCore.QRect(10, 210, 251, 31))
        self.tab_1_entry_box_06.setObjectName("tab_1_entry_box_06")
        for _ in range(8):  
            self.tab_1_entry_box_06.addItem("")
        self.tab_1_entry_box_06.setItemText(0, "")

        self.tab_1_entry_box_07 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_07.setGeometry(QtCore.QRect(10, 250, 251, 31))
        self.tab_1_entry_box_07.setObjectName("tab_1_entry_box_07")
        for _ in range(6):  
            self.tab_1_entry_box_07.addItem("")
        self.tab_1_entry_box_07.setItemText(0, "")

        self.tab_1_entry_box_08 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_08.setGeometry(QtCore.QRect(10, 290, 251, 31))
        self.tab_1_entry_box_08.setObjectName("tab_1_entry_box_08")
        for _ in range(3):  
            self.tab_1_entry_box_08.addItem("")
        self.tab_1_entry_box_08.setItemText(0, "")

        self.tab_1_entry_box_09 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_09.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.tab_1_entry_box_09.setObjectName("tab_1_entry_box_09")
        for _ in range(3):  
            self.tab_1_entry_box_09.addItem("")
        self.tab_1_entry_box_09.setItemText(0, "")

        self.tab_1_entry_box_10 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_10.setGeometry(QtCore.QRect(10, 370, 251, 31))
        self.tab_1_entry_box_10.setObjectName("tab_1_entry_box_10")
        for _ in range(3):
            self.tab_1_entry_box_10.addItem("")
        self.tab_1_entry_box_10.setItemText(0, "")

        self.tab_1_entry_box_11 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_11.setGeometry(QtCore.QRect(10, 410, 251, 31))
        self.tab_1_entry_box_11.setFont(font)
        self.tab_1_entry_box_11.setTabChangesFocus(True)
        self.tab_1_entry_box_11.setPlaceholderText("")
        self.tab_1_entry_box_11.setObjectName("tab_1_entry_box_11")

        self.tab_1_entry_box_12 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_12.setGeometry(QtCore.QRect(10, 450, 251, 31))
        self.tab_1_entry_box_12.setObjectName("tab_1_entry_box_12")
        for _ in range(3):  
            self.tab_1_entry_box_12.addItem("")
        self.tab_1_entry_box_12.setItemText(0, "")
        
        self.tab_1_entry_box_13 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_13.setGeometry(QtCore.QRect(10, 490, 251, 31))
        self.tab_1_entry_box_13.setFont(font)
        self.tab_1_entry_box_13.setTabChangesFocus(True)
        self.tab_1_entry_box_13.setPlaceholderText("")
        self.tab_1_entry_box_13.setObjectName("tab_1_entry_box_13")
        
        self.tab_1_entry_box_14 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_14.setGeometry(QtCore.QRect(10, 530, 251, 31))
        self.tab_1_entry_box_14.setMaxVisibleItems(20)
        self.tab_1_entry_box_14.setObjectName("tab_1_entry_box_14")
        for _ in range(17): 
            self.tab_1_entry_box_14.addItem("")
        self.tab_1_entry_box_14.setItemText(0, "")
        
        self.tab_1_entry_box_15 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_15.setGeometry(QtCore.QRect(10, 570, 251, 31))
        self.tab_1_entry_box_15.setMaxVisibleItems(20)
        self.tab_1_entry_box_15.setObjectName("tab_1_entry_box_15")
        for _ in range(17): 
            self.tab_1_entry_box_15.addItem("")
        self.tab_1_entry_box_15.setItemText(0, "")

        self.tab_1_entry_box_16 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_16.setGeometry(QtCore.QRect(10, 610, 251, 31))
        self.tab_1_entry_box_16.setFont(font)
        self.tab_1_entry_box_16.setTabChangesFocus(True)
        self.tab_1_entry_box_16.setPlainText("")
        self.tab_1_entry_box_16.setPlaceholderText("")
        self.tab_1_entry_box_16.setObjectName("tab_1_entry_box_16")
        
        self.tab_1_entry_box_17 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_17.setGeometry(QtCore.QRect(10, 650, 251, 31))
        self.tab_1_entry_box_17.setObjectName("tab_1_entry_box_17")
        for _ in range(3):  
            self.tab_1_entry_box_17.addItem("")
        self.tab_1_entry_box_17.setItemText(0, "")
        
        self.tab_1_entry_box_18 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_18.setGeometry(QtCore.QRect(10, 690, 251, 31))
        self.tab_1_entry_box_18.setObjectName("tab_1_entry_box_18")
        for _ in range(3):
            self.tab_1_entry_box_18.addItem("")
        self.tab_1_entry_box_18.setItemText(0, "")
        
        self.tab_1_entry_box_19 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_19.setGeometry(QtCore.QRect(10, 730, 251, 31))
        self.tab_1_entry_box_19.setObjectName("tab_1_entry_box_19")
        for _ in range(3):  
            self.tab_1_entry_box_19.addItem("")
        self.tab_1_entry_box_19.setItemText(0, "")

        self.tab_1_entry_box_20 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_20.setGeometry(QtCore.QRect(10, 770, 251, 31))
        self.tab_1_entry_box_20.setObjectName("tab_1_entry_box_20")
        for _ in range(3):    
            self.tab_1_entry_box_20.addItem("")
        self.tab_1_entry_box_20.setItemText(0, "")

        self.tab_1_entry_box_21 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_21.setGeometry(QtCore.QRect(460, 10, 251, 31))
        self.tab_1_entry_box_21.setObjectName("tab_1_entry_box_21")
        for _ in range(4):    
            self.tab_1_entry_box_21.addItem("")
        self.tab_1_entry_box_21.setItemText(0, "")

        self.tab_1_entry_box_22 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_22.setGeometry(QtCore.QRect(460, 50, 251, 31))
        self.tab_1_entry_box_22.setFont(font)
        self.tab_1_entry_box_22.setTabChangesFocus(True)
        self.tab_1_entry_box_22.setPlainText("")
        self.tab_1_entry_box_22.setPlaceholderText("")
        self.tab_1_entry_box_22.setObjectName("tab_1_entry_box_22")
        
        self.tab_1_entry_box_23 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_23.setGeometry(QtCore.QRect(460, 90, 251, 31))
        self.tab_1_entry_box_23.setFont(font)
        self.tab_1_entry_box_23.setTabChangesFocus(True)
        self.tab_1_entry_box_23.setPlainText("")
        self.tab_1_entry_box_23.setPlaceholderText("")
        self.tab_1_entry_box_23.setObjectName("tab_1_entry_box_23")
        
        self.tab_1_entry_box_24 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_24.setGeometry(QtCore.QRect(460, 130, 251, 31))
        self.tab_1_entry_box_24.setObjectName("tab_1_entry_box_24")
        for _ in range(7):    
            self.tab_1_entry_box_24.addItem("")
        self.tab_1_entry_box_24.setItemText(0, "")

        self.tab_1_entry_box_25 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_25.setGeometry(QtCore.QRect(460, 170, 251, 31))
        self.tab_1_entry_box_25.setObjectName("tab_1_entry_box_25")
        for _ in range(3):    
            self.tab_1_entry_box_25.addItem("")
        self.tab_1_entry_box_25.setItemText(0, "")

        self.tab_1_entry_box_26 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_26.setGeometry(QtCore.QRect(460, 210, 251, 31))
        self.tab_1_entry_box_26.setFont(font)
        self.tab_1_entry_box_26.setTabChangesFocus(True)
        self.tab_1_entry_box_26.setPlainText("")
        self.tab_1_entry_box_26.setPlaceholderText("")
        self.tab_1_entry_box_26.setObjectName("tab_1_entry_box_26")
        
        self.tab_1_entry_box_27 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_27.setGeometry(QtCore.QRect(460, 250, 251, 31))
        self.tab_1_entry_box_27.setFont(font)
        self.tab_1_entry_box_27.setTabChangesFocus(True)
        self.tab_1_entry_box_27.setPlainText("")
        self.tab_1_entry_box_27.setPlaceholderText("")
        self.tab_1_entry_box_27.setObjectName("tab_1_entry_box_27")

        self.tab_1_entry_box_28 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_28.setGeometry(QtCore.QRect(460, 290, 251, 31))
        self.tab_1_entry_box_28.setObjectName("tab_1_entry_box_28")
        for _ in range(3):    
            self.tab_1_entry_box_28.addItem("")
        self.tab_1_entry_box_28.setItemText(0, "")

        self.tab_1_entry_box_29 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_29.setGeometry(QtCore.QRect(460, 330, 251, 31))
        self.tab_1_entry_box_29.setObjectName("tab_1_entry_box_29")
        for _ in range(4):    
            self.tab_1_entry_box_29.addItem("")
        self.tab_1_entry_box_29.setItemText(0, "")
        
        self.tab_1_entry_box_30 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_30.setGeometry(QtCore.QRect(460, 370, 251, 31))
        self.tab_1_entry_box_30.setObjectName("tab_1_entry_box_30")
        for _ in range(3):    
            self.tab_1_entry_box_30.addItem("")
        self.tab_1_entry_box_30.setItemText(0, "")
        
        self.tab_1_entry_box_31 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_31.setGeometry(QtCore.QRect(460, 410, 251, 31))
        self.tab_1_entry_box_31.setFont(font)
        self.tab_1_entry_box_31.setTabChangesFocus(True)
        self.tab_1_entry_box_31.setPlainText("")
        self.tab_1_entry_box_31.setPlaceholderText("")
        self.tab_1_entry_box_31.setObjectName("tab_1_entry_box_31")
        
        self.tab_1_entry_box_32 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_32.setGeometry(QtCore.QRect(460, 450, 251, 31))
        self.tab_1_entry_box_32.setObjectName("tab_1_entry_box_32")
        for _ in range(3):
            self.tab_1_entry_box_32.addItem("")
        self.tab_1_entry_box_32.setItemText(0, "")

        self.tab_1_entry_box_33 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_33.setEnabled(True)
        self.tab_1_entry_box_33.setGeometry(QtCore.QRect(460, 490, 251, 31))
        self.tab_1_entry_box_33.setFont(font)
        self.tab_1_entry_box_33.setTabChangesFocus(True)
        self.tab_1_entry_box_33.setPlainText("")
        self.tab_1_entry_box_33.setPlaceholderText("")
        self.tab_1_entry_box_33.setObjectName("tab_1_entry_box_33")
        
        self.tab_1_entry_box_34 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_34.setEnabled(True)
        self.tab_1_entry_box_34.setGeometry(QtCore.QRect(460, 530, 251, 31))
        self.tab_1_entry_box_34.setObjectName("tab_1_entry_box_34")
        for _ in range(3):    
            self.tab_1_entry_box_34.addItem("")
        self.tab_1_entry_box_34.setItemText(0, "")
        
        self.tab_1_entry_box_35 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_35.setEnabled(True)
        self.tab_1_entry_box_35.setGeometry(QtCore.QRect(460, 570, 251, 31))
        self.tab_1_entry_box_35.setObjectName("tab_1_entry_box_35")
        for _ in range(3):    
            self.tab_1_entry_box_35.addItem("")
        self.tab_1_entry_box_35.setItemText(0, "")

        self.tab_1_entry_box_36 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_36.setEnabled(True)
        self.tab_1_entry_box_36.setGeometry(QtCore.QRect(460, 610, 251, 31))
        self.tab_1_entry_box_36.setObjectName("tab_1_entry_box_36")
        for _ in range(3):    
            self.tab_1_entry_box_36.addItem("")
        self.tab_1_entry_box_36.setItemText(0, "")

        self.tab_1_entry_box_37 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_37.setEnabled(True)
        self.tab_1_entry_box_37.setGeometry(QtCore.QRect(460, 650, 251, 31))
        self.tab_1_entry_box_37.setObjectName("tab_1_entry_box_37")
        for _ in range(3):    
            self.tab_1_entry_box_37.addItem("")
        self.tab_1_entry_box_37.setItemText(0, "")

        self.tab_1_entry_box_38 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_38.setEnabled(True)
        self.tab_1_entry_box_38.setGeometry(QtCore.QRect(460, 690, 251, 31))
        self.tab_1_entry_box_38.setObjectName("tab_1_entry_box_38")
        for _ in range(4):    
            self.tab_1_entry_box_38.addItem("")
        self.tab_1_entry_box_38.setItemText(0, "")

        self.tab_1_entry_box_39 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_39.setEnabled(True)
        self.tab_1_entry_box_39.setGeometry(QtCore.QRect(460, 730, 251, 31))
        self.tab_1_entry_box_39.setFont(font)
        self.tab_1_entry_box_39.setTabChangesFocus(True)
        self.tab_1_entry_box_39.setPlainText("")
        self.tab_1_entry_box_39.setPlaceholderText("")
        self.tab_1_entry_box_39.setObjectName("tab_1_entry_box_39")
        
        self.tab_1_entry_box_40 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_40.setEnabled(True)
        self.tab_1_entry_box_40.setGeometry(QtCore.QRect(460, 770, 251, 31))
        self.tab_1_entry_box_40.setFont(font)
        self.tab_1_entry_box_40.setTabChangesFocus(True)
        self.tab_1_entry_box_40.setPlainText("")
        self.tab_1_entry_box_40.setPlaceholderText("")
        self.tab_1_entry_box_40.setObjectName("tab_1_entry_box_40")
        
        self.tab_1_entry_box_41 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_41.setEnabled(True)
        self.tab_1_entry_box_41.setGeometry(QtCore.QRect(970, 10, 251, 31))
        self.tab_1_entry_box_41.setFont(font)
        self.tab_1_entry_box_41.setTabChangesFocus(True)
        self.tab_1_entry_box_41.setPlainText("")
        self.tab_1_entry_box_41.setPlaceholderText("")
        self.tab_1_entry_box_41.setObjectName("tab_1_entry_box_41")
        
        self.tab_1_entry_box_42 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_42.setEnabled(True)
        self.tab_1_entry_box_42.setGeometry(QtCore.QRect(970, 50, 251, 31))
        self.tab_1_entry_box_42.setFont(font)
        self.tab_1_entry_box_42.setTabChangesFocus(True)
        self.tab_1_entry_box_42.setPlainText("")
        self.tab_1_entry_box_42.setPlaceholderText("")
        self.tab_1_entry_box_42.setObjectName("tab_1_entry_box_42")
        
        self.tab_1_entry_box_43 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_43.setEnabled(True)
        self.tab_1_entry_box_43.setGeometry(QtCore.QRect(970, 90, 251, 31))
        self.tab_1_entry_box_43.setObjectName("tab_1_entry_box_43")
        for _ in range(4):
            self.tab_1_entry_box_43.addItem("")
        self.tab_1_entry_box_43.setItemText(0, "")
        
        self.tab_1_entry_box_44 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_44.setEnabled(True)
        self.tab_1_entry_box_44.setGeometry(QtCore.QRect(970, 130, 251, 31))
        self.tab_1_entry_box_44.setObjectName("tab_1_entry_box_44")
        for _ in range(4):
            self.tab_1_entry_box_44.addItem("")
        self.tab_1_entry_box_44.setItemText(0, "")

        self.tab_1_entry_box_45 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_45.setEnabled(True)
        self.tab_1_entry_box_45.setGeometry(QtCore.QRect(970, 170, 251, 31))
        self.tab_1_entry_box_45.setObjectName("tab_1_entry_box_45")
        for _ in range(3):
            self.tab_1_entry_box_45.addItem("")
        self.tab_1_entry_box_45.setItemText(0, "")
        
        self.tab_1_entry_box_46 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_46.setEnabled(True)
        self.tab_1_entry_box_46.setGeometry(QtCore.QRect(970, 210, 251, 31))
        self.tab_1_entry_box_46.setFont(font)
        self.tab_1_entry_box_46.setTabChangesFocus(True)
        self.tab_1_entry_box_46.setPlainText("")
        self.tab_1_entry_box_46.setPlaceholderText("")
        self.tab_1_entry_box_46.setObjectName("tab_1_entry_box_46")

        self.tab_1_entry_box_47 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_47.setEnabled(True)
        self.tab_1_entry_box_47.setGeometry(QtCore.QRect(970, 250, 251, 31))
        self.tab_1_entry_box_47.setObjectName("tab_1_entry_box_47")
        for _ in range(3):    
            self.tab_1_entry_box_47.addItem("")
        self.tab_1_entry_box_47.setItemText(0, "")

        self.tab_1_entry_box_48 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_48.setEnabled(True)
        self.tab_1_entry_box_48.setGeometry(QtCore.QRect(970, 290, 251, 31))
        self.tab_1_entry_box_48.setObjectName("tab_1_entry_box_48")
        for _ in range(3):    
            self.tab_1_entry_box_48.addItem("")
        self.tab_1_entry_box_48.setItemText(0, "")

        self.tab_1_entry_box_49 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_49.setEnabled(True)
        self.tab_1_entry_box_49.setGeometry(QtCore.QRect(970, 330, 251, 31))
        self.tab_1_entry_box_49.setObjectName("tab_1_entry_box_49")
        for _ in range(3):    
            self.tab_1_entry_box_49.addItem("")
        self.tab_1_entry_box_49.setItemText(0, "")

        self.tab_1_entry_box_50 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_50.setEnabled(True)
        self.tab_1_entry_box_50.setGeometry(QtCore.QRect(970, 370, 251, 31))
        self.tab_1_entry_box_50.setObjectName("tab_1_entry_box_50")
        for _ in range(3):    
            self.tab_1_entry_box_50.addItem("")
        self.tab_1_entry_box_50.setItemText(0, "")

        self.tab_1_entry_box_51 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_51.setEnabled(True)
        self.tab_1_entry_box_51.setGeometry(QtCore.QRect(970, 410, 251, 31))
        self.tab_1_entry_box_51.setObjectName("tab_1_entry_box_51")
        for _ in range(4):    
            self.tab_1_entry_box_51.addItem("")
        self.tab_1_entry_box_51.setItemText(0, "")

        self.tab_1_entry_box_52 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_52.setEnabled(True)
        self.tab_1_entry_box_52.setGeometry(QtCore.QRect(970, 450, 251, 31))
        self.tab_1_entry_box_52.setFont(font)
        self.tab_1_entry_box_52.setTabChangesFocus(True)
        self.tab_1_entry_box_52.setPlainText("")
        self.tab_1_entry_box_52.setPlaceholderText("")
        self.tab_1_entry_box_52.setObjectName("tab_1_entry_box_52")

        self.tab_1_entry_box_53 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_53.setEnabled(True)
        self.tab_1_entry_box_53.setGeometry(QtCore.QRect(970, 490, 251, 31))
        self.tab_1_entry_box_53.setFont(font)
        self.tab_1_entry_box_53.setTabChangesFocus(True)
        self.tab_1_entry_box_53.setPlainText("")
        self.tab_1_entry_box_53.setPlaceholderText("")
        self.tab_1_entry_box_53.setObjectName("tab_1_entry_box_53")

        self.tab_1_entry_box_54 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_54.setEnabled(True)
        self.tab_1_entry_box_54.setGeometry(QtCore.QRect(970, 530, 251, 31))
        self.tab_1_entry_box_54.setFont(font)
        self.tab_1_entry_box_54.setTabChangesFocus(True)
        self.tab_1_entry_box_54.setPlainText("")
        self.tab_1_entry_box_54.setPlaceholderText("")
        self.tab_1_entry_box_54.setObjectName("tab_1_entry_box_54")

        self.tab_1_entry_box_55 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.tab_1_entry_box_55.setEnabled(True)
        self.tab_1_entry_box_55.setGeometry(QtCore.QRect(970, 570, 251, 31))
        self.tab_1_entry_box_55.setFont(font)
        self.tab_1_entry_box_55.setTabChangesFocus(True)
        self.tab_1_entry_box_55.setPlainText("")
        self.tab_1_entry_box_55.setPlaceholderText("")
        self.tab_1_entry_box_55.setObjectName("tab_1_entry_box_55")

        self.tab_1_entry_box_56 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_56.setEnabled(True)
        self.tab_1_entry_box_56.setGeometry(QtCore.QRect(970, 610, 251, 31))
        self.tab_1_entry_box_56.setObjectName("tab_1_entry_box_56")
        for _ in range(4):    
            self.tab_1_entry_box_56.addItem("")
        self.tab_1_entry_box_56.setItemText(0, "")
        
        self.tab_1_entry_box_57 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_57.setEnabled(True)
        self.tab_1_entry_box_57.setGeometry(QtCore.QRect(970, 650, 251, 31))
        self.tab_1_entry_box_57.setObjectName("tab_1_entry_box_57")
        for _ in range(4):    
            self.tab_1_entry_box_57.addItem("")
        self.tab_1_entry_box_57.setItemText(0, "")

        self.tab_1_entry_box_58 = QtWidgets.QComboBox(self.tab_1)
        self.tab_1_entry_box_58.setEnabled(True)
        self.tab_1_entry_box_58.setGeometry(QtCore.QRect(970, 690, 251, 31))
        self.tab_1_entry_box_58.setObjectName("tab_1_entry_box_58")
        for _ in range(3):    
            self.tab_1_entry_box_58.addItem("")
        self.tab_1_entry_box_58.setItemText(0, "")


        #---------------------------------Labels-----------------------------------#
        #--------------------------------------------------------------------------#
        
        self.tab_1_label_01 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_01.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.tab_1_label_01.setFont(font)
        self.tab_1_label_01.setObjectName("tab_1_label_01")

        self.tab_1_label_02 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_02.setGeometry(QtCore.QRect(270, 50, 121, 31))
        self.tab_1_label_02.setFont(font)
        self.tab_1_label_02.setObjectName("tab_1_label_02")

        self.tab_1_label_03 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_03.setGeometry(QtCore.QRect(270, 90, 171, 31))
        self.tab_1_label_03.setFont(font)
        self.tab_1_label_03.setObjectName("tab_1_label_03")

        self.tab_1_label_04 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_04.setGeometry(QtCore.QRect(270, 130, 121, 31))
        self.tab_1_label_04.setFont(font)
        self.tab_1_label_04.setObjectName("tab_1_label_04")

        self.tab_1_label_05 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_05.setGeometry(QtCore.QRect(270, 170, 121, 31))
        self.tab_1_label_05.setFont(font)
        self.tab_1_label_05.setObjectName("tab_1_label_05")

        self.tab_1_label_06 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_06.setGeometry(QtCore.QRect(270, 210, 171, 31))
        self.tab_1_label_06.setFont(font)
        self.tab_1_label_06.setObjectName("tab_1_label_06")

        self.tab_1_label_07 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_07.setGeometry(QtCore.QRect(270, 250, 171, 31))
        self.tab_1_label_07.setFont(font)
        self.tab_1_label_07.setObjectName("tab_1_label_07")

        self.tab_1_label_08 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_08.setGeometry(QtCore.QRect(270, 290, 171, 31))
        self.tab_1_label_08.setFont(font)
        self.tab_1_label_08.setObjectName("tab_1_label_08")

        self.tab_1_label_09 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_09.setGeometry(QtCore.QRect(270, 330, 171, 31))
        self.tab_1_label_09.setFont(font)
        self.tab_1_label_09.setObjectName("tab_1_label_09")

        self.tab_1_label_10 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_10.setGeometry(QtCore.QRect(270, 370, 171, 31))
        self.tab_1_label_10.setFont(font)
        self.tab_1_label_10.setObjectName("tab_1_label_10")

        self.tab_1_label_11 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_11.setGeometry(QtCore.QRect(270, 410, 171, 31))
        self.tab_1_label_11.setFont(font)
        self.tab_1_label_11.setObjectName("tab_1_label_11")

        self.tab_1_label_12 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_12.setGeometry(QtCore.QRect(270, 450, 171, 31))
        self.tab_1_label_12.setFont(font)
        self.tab_1_label_12.setObjectName("tab_1_label_12")

        self.tab_1_label_13 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_13.setGeometry(QtCore.QRect(270, 490, 171, 31))
        self.tab_1_label_13.setFont(font)
        self.tab_1_label_13.setObjectName("tab_1_label_13")

        self.tab_1_label_14 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_14.setGeometry(QtCore.QRect(270, 530, 171, 31))
        self.tab_1_label_14.setFont(font)
        self.tab_1_label_14.setObjectName("tab_1_label_14")

        self.tab_1_label_15 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_15.setGeometry(QtCore.QRect(270, 570, 171, 31))
        self.tab_1_label_15.setFont(font)
        self.tab_1_label_15.setObjectName("tab_1_label_15")

        self.tab_1_label_16 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_16.setGeometry(QtCore.QRect(270, 610, 171, 31))
        self.tab_1_label_16.setFont(font)
        self.tab_1_label_16.setObjectName("tab_1_label_16")

        self.tab_1_label_17 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_17.setGeometry(QtCore.QRect(270, 650, 171, 31))
        self.tab_1_label_17.setFont(font)
        self.tab_1_label_17.setObjectName("tab_1_label_17")

        self.tab_1_label_18 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_18.setGeometry(QtCore.QRect(270, 690, 171, 31))
        self.tab_1_label_18.setFont(font)
        self.tab_1_label_18.setObjectName("tab_1_label_18")

        self.tab_1_label_19 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_19.setGeometry(QtCore.QRect(270, 730, 171, 31))
        self.tab_1_label_19.setFont(font)
        self.tab_1_label_19.setObjectName("tab_1_label_19")

        self.tab_1_label_20 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_20.setGeometry(QtCore.QRect(270, 770, 171, 31))
        self.tab_1_label_20.setFont(font)
        self.tab_1_label_20.setObjectName("tab_1_label_20")

        self.tab_1_label_21 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_21.setGeometry(QtCore.QRect(720, 10, 171, 31))
        self.tab_1_label_21.setFont(font)
        self.tab_1_label_21.setObjectName("tab_1_label_21")

        self.tab_1_label_22 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_22.setGeometry(QtCore.QRect(720, 50, 131, 31))
        self.tab_1_label_22.setFont(font)
        self.tab_1_label_22.setObjectName("tab_1_label_22")

        self.tab_1_label_23 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_23.setGeometry(QtCore.QRect(720, 90, 231, 31))
        self.tab_1_label_23.setFont(font)
        self.tab_1_label_23.setObjectName("tab_1_label_23")

        self.tab_1_label_24 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_24.setGeometry(QtCore.QRect(720, 130, 211, 31))
        self.tab_1_label_24.setFont(font)
        self.tab_1_label_24.setObjectName("tab_1_label_24")

        self.tab_1_label_25 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_25.setGeometry(QtCore.QRect(720, 170, 131, 31))
        self.tab_1_label_25.setFont(font)
        self.tab_1_label_25.setObjectName("tab_1_label_25")
        
        self.tab_1_label_26 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_26.setGeometry(QtCore.QRect(720, 210, 141, 31))
        self.tab_1_label_26.setFont(font)
        self.tab_1_label_26.setObjectName("tab_1_label_26")

        self.tab_1_label_27 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_27.setGeometry(QtCore.QRect(720, 250, 131, 31))
        self.tab_1_label_27.setFont(font)
        self.tab_1_label_27.setObjectName("tab_1_label_27")

        self.tab_1_label_28 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_28.setGeometry(QtCore.QRect(720, 290, 231, 31))
        self.tab_1_label_28.setFont(font)
        self.tab_1_label_28.setObjectName("tab_1_label_28")

        self.tab_1_label_29 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_29.setGeometry(QtCore.QRect(720, 330, 141, 31))
        self.tab_1_label_29.setFont(font)
        self.tab_1_label_29.setObjectName("tab_1_label_29")

        self.tab_1_label_30 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_30.setGeometry(QtCore.QRect(720, 370, 151, 31))
        self.tab_1_label_30.setFont(font)
        self.tab_1_label_30.setObjectName("tab_1_label_30")

        self.tab_1_label_31 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_31.setGeometry(QtCore.QRect(720, 410, 211, 31))
        self.tab_1_label_31.setFont(font)
        self.tab_1_label_31.setObjectName("tab_1_label_31")

        self.tab_1_label_32 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_32.setGeometry(QtCore.QRect(720, 450, 291, 31))
        self.tab_1_label_32.setFont(font)
        self.tab_1_label_32.setObjectName("tab_1_label_32")

        self.tab_1_label_33 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_33.setEnabled(True)
        self.tab_1_label_33.setGeometry(QtCore.QRect(720, 490, 141, 31))
        self.tab_1_label_33.setFont(font)
        self.tab_1_label_33.setObjectName("tab_1_label_33")

        self.tab_1_label_34 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_34.setEnabled(True)
        self.tab_1_label_34.setGeometry(QtCore.QRect(720, 530, 141, 31))
        self.tab_1_label_34.setFont(font)
        self.tab_1_label_34.setObjectName("tab_1_label_34")

        self.tab_1_label_35 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_35.setEnabled(True)
        self.tab_1_label_35.setGeometry(QtCore.QRect(720, 570, 171, 31))
        self.tab_1_label_35.setFont(font)
        self.tab_1_label_35.setObjectName("tab_1_label_35")

        self.tab_1_label_36 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_36.setEnabled(True)
        self.tab_1_label_36.setGeometry(QtCore.QRect(720, 610, 231, 31))
        self.tab_1_label_36.setFont(font)
        self.tab_1_label_36.setObjectName("tab_1_label_36")

        self.tab_1_label_37 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_37.setEnabled(True)
        self.tab_1_label_37.setGeometry(QtCore.QRect(720, 650, 231, 31))
        self.tab_1_label_37.setFont(font)
        self.tab_1_label_37.setObjectName("tab_1_label_37")

        self.tab_1_label_38 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_38.setEnabled(True)
        self.tab_1_label_38.setGeometry(QtCore.QRect(720, 690, 231, 31))
        self.tab_1_label_38.setFont(font)
        self.tab_1_label_38.setObjectName("tab_1_label_38")

        self.tab_1_label_39 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_39.setEnabled(True)
        self.tab_1_label_39.setGeometry(QtCore.QRect(720, 730, 231, 31))
        self.tab_1_label_39.setFont(font)
        self.tab_1_label_39.setObjectName("tab_1_label_39")

        self.tab_1_label_40 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_40.setEnabled(True)
        self.tab_1_label_40.setGeometry(QtCore.QRect(720, 770, 231, 31))
        self.tab_1_label_40.setFont(font)
        self.tab_1_label_40.setObjectName("tab_1_label_40")

        self.tab_1_label_41 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_41.setEnabled(True)
        self.tab_1_label_41.setGeometry(QtCore.QRect(1230, 10, 291, 31))
        self.tab_1_label_41.setFont(font)
        self.tab_1_label_41.setObjectName("tab_1_label_41")
        
        self.tab_1_label_42 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_42.setEnabled(True)
        self.tab_1_label_42.setGeometry(QtCore.QRect(1230, 50, 291, 31))
        self.tab_1_label_42.setFont(font)
        self.tab_1_label_42.setObjectName("tab_1_label_42")

        self.tab_1_label_43 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_43.setEnabled(True)
        self.tab_1_label_43.setGeometry(QtCore.QRect(1230, 90, 291, 31))
        self.tab_1_label_43.setFont(font)
        self.tab_1_label_43.setObjectName("tab_1_label_43")

        self.tab_1_label_44 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_44.setEnabled(True)
        self.tab_1_label_44.setGeometry(QtCore.QRect(1230, 130, 291, 31))
        self.tab_1_label_44.setFont(font)
        self.tab_1_label_44.setObjectName("tab_1_label_44")

        self.tab_1_label_45 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_45.setEnabled(True)
        self.tab_1_label_45.setGeometry(QtCore.QRect(1230, 170, 291, 31))
        self.tab_1_label_45.setFont(font)
        self.tab_1_label_45.setObjectName("tab_1_label_45")

        self.tab_1_label_46 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_46.setEnabled(True)
        self.tab_1_label_46.setGeometry(QtCore.QRect(1230, 210, 141, 31))
        self.tab_1_label_46.setFont(font)
        self.tab_1_label_46.setObjectName("tab_1_label_46")

        self.tab_1_label_47 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_47.setEnabled(True)
        self.tab_1_label_47.setGeometry(QtCore.QRect(1230, 250, 141, 31))
        self.tab_1_label_47.setFont(font)
        self.tab_1_label_47.setObjectName("tab_1_label_47")

        self.tab_1_label_48 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_48.setEnabled(True)
        self.tab_1_label_48.setGeometry(QtCore.QRect(1230, 290, 171, 31))
        self.tab_1_label_48.setFont(font)
        self.tab_1_label_48.setObjectName("tab_1_label_48")

        self.tab_1_label_49 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_49.setEnabled(True)
        self.tab_1_label_49.setGeometry(QtCore.QRect(1230, 330, 141, 31))
        self.tab_1_label_49.setFont(font)
        self.tab_1_label_49.setObjectName("tab_1_label_49")
        
        self.tab_1_label_50 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_50.setEnabled(True)
        self.tab_1_label_50.setGeometry(QtCore.QRect(1230, 370, 251, 31))
        self.tab_1_label_50.setFont(font)
        self.tab_1_label_50.setObjectName("tab_1_label_50")

        self.tab_1_label_51 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_51.setEnabled(True)
        self.tab_1_label_51.setGeometry(QtCore.QRect(1230, 410, 241, 31))
        self.tab_1_label_51.setFont(font)
        self.tab_1_label_51.setObjectName("tab_1_label_51")
        
        self.tab_1_label_52 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_52.setEnabled(True)
        self.tab_1_label_52.setGeometry(QtCore.QRect(1230, 450, 291, 31))
        self.tab_1_label_52.setFont(font)
        self.tab_1_label_52.setObjectName("tab_1_label_52")

        self.tab_1_label_53 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_53.setEnabled(True)
        self.tab_1_label_53.setGeometry(QtCore.QRect(1230, 490, 291, 31))
        self.tab_1_label_53.setFont(font)
        self.tab_1_label_53.setObjectName("tab_1_label_53")

        self.tab_1_label_54 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_54.setEnabled(True)
        self.tab_1_label_54.setGeometry(QtCore.QRect(1230, 530, 291, 31))
        self.tab_1_label_54.setFont(font)
        self.tab_1_label_54.setObjectName("tab_1_label_54")

        self.tab_1_label_55 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_55.setEnabled(True)
        self.tab_1_label_55.setGeometry(QtCore.QRect(1230, 570, 291, 31))
        self.tab_1_label_55.setFont(font)
        self.tab_1_label_55.setObjectName("tab_1_label_55")

        self.tab_1_label_56 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_56.setEnabled(True)
        self.tab_1_label_56.setGeometry(QtCore.QRect(1230, 610, 291, 31))
        self.tab_1_label_56.setFont(font)
        self.tab_1_label_56.setObjectName("tab_1_label_56")
        
        self.tab_1_label_57 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_57.setEnabled(True)
        self.tab_1_label_57.setGeometry(QtCore.QRect(1230, 650, 291, 31))
        self.tab_1_label_57.setFont(font)
        self.tab_1_label_57.setObjectName("tab_1_label_57")
        
        self.tab_1_label_58 = QtWidgets.QLabel(self.tab_1)
        self.tab_1_label_58.setEnabled(True)
        self.tab_1_label_58.setGeometry(QtCore.QRect(1230, 690, 291, 31))
        self.tab_1_label_58.setFont(font)
        self.tab_1_label_58.setObjectName("tab_1_label_58")
        
        #----------------------------------Other-----------------------------------#
        #--------------------------------------------------------------------------#
        
        self.tab_1_button_01 = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_button_01.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_1_button_01.setObjectName("tab_1_button_01")
        self.tab_1_button_01.clicked.connect(lambda:self.tab_1_function_clear_fields())

        self.tab_1_button_02 = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_button_02.setGeometry(QtCore.QRect(250, 820, 111, 41))
        self.tab_1_button_02.setObjectName("tab_1_button_02")
        self.tab_1_button_02.clicked.connect(lambda:self.tab_1_function_add_to_queue())

        self.tab_1_line_01 = QtWidgets.QFrame(self.tab_1)
        self.tab_1_line_01.setGeometry(QtCore.QRect(440, 10, 21, 801))
        self.tab_1_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_1_line_01.setLineWidth(2)
        self.tab_1_line_01.setMidLineWidth(0)
        self.tab_1_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_1_line_01.setObjectName("tab_1_line_01")

        self.tab_1_line_02 = QtWidgets.QFrame(self.tab_1)
        self.tab_1_line_02.setGeometry(QtCore.QRect(950, 10, 21, 801))
        self.tab_1_line_02.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_1_line_02.setLineWidth(2)
        self.tab_1_line_02.setMidLineWidth(0)
        self.tab_1_line_02.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_1_line_02.setObjectName("tab_1_line_02")

        self.tab_1_check_box_01 = QtWidgets.QCheckBox(self.tab_1)
        self.tab_1_check_box_01.setGeometry(QtCore.QRect(10, 820, 101, 17))
        self.tab_1_check_box_01.setObjectName("tab_1_check_box_01")
        self.tab_1_check_box_01.stateChanged.connect(lambda:self.tab_1_function_hide_line_2())
        
        self.tab_1_check_box_02 = QtWidgets.QCheckBox(self.tab_1)
        self.tab_1_check_box_02.setGeometry(QtCore.QRect(10, 840, 101, 17))
        self.tab_1_check_box_02.setObjectName("tab_1_check_box_02")
        self.tab_1_check_box_02.stateChanged.connect(lambda:self.tab_1_function_hide_line_3())
        for number in range(33,59):
            ref_entry = getattr(self, f"tab_1_entry_box_{number}")
            ref_label = getattr(self, f"tab_1_label_{number}")
            ref_entry.setHidden(True)
            ref_label.setHidden(True)

        #--------------------------------------------------------------------------
        #-                           tab 2                                        -
        #--------------------------------------------------------------------------    
        
        self.all_tabs.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2_label_02 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_02.setGeometry(QtCore.QRect(270, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_02.setFont(font)
        self.tab_2_label_02.setObjectName("tab_2_label_02")
        self.tab_2_entry_box_01 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_01.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_01.setFont(font)
        self.tab_2_entry_box_01.setToolTipDuration(-1)
        self.tab_2_entry_box_01.setTabChangesFocus(True)
        self.tab_2_entry_box_01.setPlaceholderText("")
        self.tab_2_entry_box_01.setObjectName("tab_2_entry_box_01")
        self.tab_2_entry_box_02 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_02.setGeometry(QtCore.QRect(10, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_02.setFont(font)
        self.tab_2_entry_box_02.setTabChangesFocus(True)
        self.tab_2_entry_box_02.setPlaceholderText("")
        self.tab_2_entry_box_02.setObjectName("tab_2_entry_box_02")
        self.tab_2_label_01 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_01.setGeometry(QtCore.QRect(270, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_01.setFont(font)
        self.tab_2_label_01.setObjectName("tab_2_label_01")
        self.tab_2_label_04 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_04.setGeometry(QtCore.QRect(270, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_04.setFont(font)
        self.tab_2_label_04.setObjectName("tab_2_label_04")
        self.tab_2_entry_box_04 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_04.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.tab_2_entry_box_04.setObjectName("tab_2_entry_box_04")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.setItemText(0, "")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_04.addItem("")
        self.tab_2_entry_box_03 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_03.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.tab_2_entry_box_03.setObjectName("tab_2_entry_box_03")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.setItemText(0, "")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_entry_box_03.addItem("")
        self.tab_2_label_03 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_03.setGeometry(QtCore.QRect(270, 90, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_03.setFont(font)
        self.tab_2_label_03.setObjectName("tab_2_label_03")
        self.tab_2_entry_box_05 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_05.setGeometry(QtCore.QRect(10, 170, 251, 31))
        self.tab_2_entry_box_05.setObjectName("tab_2_entry_box_05")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.setItemText(0, "")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_entry_box_05.addItem("")
        self.tab_2_label_05 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_05.setGeometry(QtCore.QRect(270, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_05.setFont(font)
        self.tab_2_label_05.setObjectName("tab_2_label_05")
        self.tab_2_label_06 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_06.setGeometry(QtCore.QRect(270, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_06.setFont(font)
        self.tab_2_label_06.setObjectName("tab_2_label_06")
        self.tab_2_entry_box_06 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_06.setGeometry(QtCore.QRect(10, 210, 251, 31))
        self.tab_2_entry_box_06.setObjectName("tab_2_entry_box_06")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_entry_box_06.setItemText(0, "")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_entry_box_06.addItem("")
        self.tab_2_label_07 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_07.setGeometry(QtCore.QRect(270, 250, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_07.setFont(font)
        self.tab_2_label_07.setObjectName("tab_2_label_07")
        self.tab_2_entry_box_07 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_07.setGeometry(QtCore.QRect(10, 250, 251, 31))
        self.tab_2_entry_box_07.setObjectName("tab_2_entry_box_07")
        self.tab_2_entry_box_07.addItem("")
        self.tab_2_entry_box_07.setItemText(0, "")
        self.tab_2_entry_box_07.addItem("")
        self.tab_2_entry_box_07.addItem("")
        self.tab_2_entry_box_07.addItem("")
        self.tab_2_entry_box_07.addItem("")
        self.tab_2_line_01 = QtWidgets.QFrame(self.tab_2)
        self.tab_2_line_01.setGeometry(QtCore.QRect(500, 10, 21, 801))
        self.tab_2_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_2_line_01.setLineWidth(2)
        self.tab_2_line_01.setMidLineWidth(0)
        self.tab_2_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_2_line_01.setObjectName("tab_2_line_01")
        self.tab_2_label_08 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_08.setGeometry(QtCore.QRect(270, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_08.setFont(font)
        self.tab_2_label_08.setObjectName("tab_2_label_08")
        self.tab_2_entry_box_08 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_08.setGeometry(QtCore.QRect(10, 290, 251, 31))
        self.tab_2_entry_box_08.setObjectName("tab_2_entry_box_08")
        self.tab_2_entry_box_08.addItem("")
        self.tab_2_entry_box_08.setItemText(0, "")
        self.tab_2_entry_box_08.addItem("")
        self.tab_2_entry_box_08.addItem("")
        self.tab_2_label_09 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_09.setGeometry(QtCore.QRect(270, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_09.setFont(font)
        self.tab_2_label_09.setObjectName("tab_2_label_09")
        self.tab_2_entry_box_09 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_09.setGeometry(QtCore.QRect(10, 330, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_09.setFont(font)
        self.tab_2_entry_box_09.setTabChangesFocus(True)
        self.tab_2_entry_box_09.setPlaceholderText("")
        self.tab_2_entry_box_09.setObjectName("tab_2_entry_box_09")
        self.tab_2_label_10 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_10.setGeometry(QtCore.QRect(270, 370, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_10.setFont(font)
        self.tab_2_label_10.setObjectName("tab_2_label_10")
        self.tab_2_entry_box_10 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_10.setGeometry(QtCore.QRect(10, 370, 251, 31))
        self.tab_2_entry_box_10.setObjectName("tab_2_entry_box_10")
        for _ in range(12): 
            self.tab_2_entry_box_10.addItem("")
        self.tab_2_entry_box_10.setItemText(0, "")
        self.tab_2_entry_box_11 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_11.setGeometry(QtCore.QRect(10, 410, 251, 31))
        self.tab_2_entry_box_11.setObjectName("tab_2_entry_box_11")
        for _ in range(11): 
            self.tab_2_entry_box_11.addItem("")
        
        self.tab_2_entry_box_11.setItemText(0, "")
        self.tab_2_label_11 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_11.setGeometry(QtCore.QRect(270, 410, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_11.setFont(font)
        self.tab_2_label_11.setObjectName("tab_2_label_11")
        self.tab_2_label_12 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_12.setGeometry(QtCore.QRect(270, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_12.setFont(font)
        self.tab_2_label_12.setObjectName("tab_2_label_12")
        self.tab_2_entry_box_12 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_12.setGeometry(QtCore.QRect(10, 450, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_12.setFont(font)
        self.tab_2_entry_box_12.setTabChangesFocus(True)
        self.tab_2_entry_box_12.setPlaceholderText("")
        self.tab_2_entry_box_12.setObjectName("tab_2_entry_box_12")
        self.tab_2_label_13 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_13.setGeometry(QtCore.QRect(270, 490, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_13.setFont(font)
        self.tab_2_label_13.setObjectName("tab_2_label_13")
        self.tab_2_entry_box_13 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_13.setGeometry(QtCore.QRect(10, 490, 251, 31))
        self.tab_2_entry_box_13.setObjectName("tab_2_entry_box_13")
        self.tab_2_entry_box_13.addItem("")
        self.tab_2_entry_box_13.setItemText(0, "")
        self.tab_2_entry_box_13.addItem("")
        self.tab_2_entry_box_13.addItem("")
        self.tab_2_label_14 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_14.setGeometry(QtCore.QRect(270, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_14.setFont(font)
        self.tab_2_label_14.setObjectName("tab_2_label_14")
        self.tab_2_entry_box_14 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_14.setGeometry(QtCore.QRect(10, 530, 251, 31))
        self.tab_2_entry_box_14.setObjectName("tab_2_entry_box_14")
        self.tab_2_entry_box_14.addItem("")
        self.tab_2_entry_box_14.setItemText(0, "")
        self.tab_2_entry_box_14.addItem("")
        self.tab_2_entry_box_14.addItem("")
        self.tab_2_entry_box_15 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_15.setGeometry(QtCore.QRect(10, 570, 251, 31))
        self.tab_2_entry_box_15.setObjectName("tab_2_entry_box_15")
        self.tab_2_entry_box_15.addItem("")
        self.tab_2_entry_box_15.setItemText(0, "")
        self.tab_2_entry_box_15.addItem("")
        self.tab_2_entry_box_15.addItem("")
        self.tab_2_label_15 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_15.setGeometry(QtCore.QRect(270, 570, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_15.setFont(font)
        self.tab_2_label_15.setObjectName("tab_2_label_15")
        self.tab_2_label_16 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_16.setGeometry(QtCore.QRect(270, 610, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_16.setFont(font)
        self.tab_2_label_16.setObjectName("tab_2_label_16")
        self.tab_2_entry_box_16 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_16.setGeometry(QtCore.QRect(10, 610, 251, 31))
        self.tab_2_entry_box_16.setObjectName("tab_2_entry_box_16")
        self.tab_2_entry_box_16.addItem("")
        self.tab_2_entry_box_16.setItemText(0, "")
        self.tab_2_entry_box_16.addItem("")
        self.tab_2_entry_box_16.addItem("")
        self.tab_2_label_17 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_17.setGeometry(QtCore.QRect(270, 650, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_17.setFont(font)
        self.tab_2_label_17.setObjectName("tab_2_label_17")
        self.tab_2_entry_box_17 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_17.setGeometry(QtCore.QRect(10, 650, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_17.setFont(font)
        self.tab_2_entry_box_17.setTabChangesFocus(True)
        self.tab_2_entry_box_17.setPlaceholderText("")
        self.tab_2_entry_box_17.setObjectName("tab_2_entry_box_17")
        self.tab_2_label_18 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_18.setGeometry(QtCore.QRect(270, 690, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_18.setFont(font)
        self.tab_2_label_18.setObjectName("tab_2_label_18")
        self.tab_2_entry_box_18 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_18.setGeometry(QtCore.QRect(10, 690, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_18.setFont(font)
        self.tab_2_entry_box_18.setTabChangesFocus(True)
        self.tab_2_entry_box_18.setPlaceholderText("")
        self.tab_2_entry_box_18.setObjectName("tab_2_entry_box_18")
        self.tab_2_label_19 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_19.setGeometry(QtCore.QRect(270, 730, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_19.setFont(font)
        self.tab_2_label_19.setObjectName("tab_2_label_19")
        self.tab_2_entry_box_19 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_19.setGeometry(QtCore.QRect(10, 730, 251, 31))
        self.tab_2_entry_box_19.setObjectName("tab_2_entry_box_19")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.setItemText(0, "")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_entry_box_19.addItem("")
        self.tab_2_label_20 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_20.setGeometry(QtCore.QRect(270, 770, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_20.setFont(font)
        self.tab_2_label_20.setObjectName("tab_2_label_20")
        self.tab_2_entry_box_20 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_20.setGeometry(QtCore.QRect(10, 770, 251, 31))
        self.tab_2_entry_box_20.setObjectName("tab_2_entry_box_20")
        self.tab_2_entry_box_20.addItem("")
        self.tab_2_entry_box_20.setItemText(0, "")
        self.tab_2_entry_box_20.addItem("")
        self.tab_2_entry_box_20.addItem("")
        self.tab_2_check_box_02 = QtWidgets.QCheckBox(self.tab_2)
        self.tab_2_check_box_02.setGeometry(QtCore.QRect(10, 840, 101, 17))
        self.tab_2_check_box_02.setObjectName("tab_2_check_box_02")
        self.tab_2_button_02 = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_button_02.setGeometry(QtCore.QRect(250, 820, 111, 41))
        self.tab_2_button_02.setObjectName("tab_2_button_02")
        self.tab_2_check_box_01 = QtWidgets.QCheckBox(self.tab_2)
        self.tab_2_check_box_01.setGeometry(QtCore.QRect(10, 820, 101, 17))
        self.tab_2_check_box_01.setObjectName("tab_2_check_box_01")
        self.tab_2_button_01 = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_button_01.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_2_button_01.setObjectName("tab_2_button_01")
        self.tab_2_label_21 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_21.setGeometry(QtCore.QRect(780, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_21.setFont(font)
        self.tab_2_label_21.setObjectName("tab_2_label_21")
        self.tab_2_entry_box_21 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_21.setGeometry(QtCore.QRect(520, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_21.setFont(font)
        self.tab_2_entry_box_21.setTabChangesFocus(True)
        self.tab_2_entry_box_21.setPlaceholderText("")
        self.tab_2_entry_box_21.setObjectName("tab_2_entry_box_21")
        self.tab_2_label_30 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_30.setGeometry(QtCore.QRect(780, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_30.setFont(font)
        self.tab_2_label_30.setObjectName("tab_2_label_30")
        self.tab_2_entry_box_30 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_30.setGeometry(QtCore.QRect(520, 370, 251, 31))
        self.tab_2_entry_box_30.setObjectName("tab_2_entry_box_30")
        self.tab_2_entry_box_30.addItem("")
        self.tab_2_entry_box_30.setItemText(0, "")
        self.tab_2_entry_box_30.addItem("")
        self.tab_2_entry_box_30.addItem("")
        self.tab_2_label_24 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_24.setGeometry(QtCore.QRect(780, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_24.setFont(font)
        self.tab_2_label_24.setObjectName("tab_2_label_24")
        self.tab_2_entry_box_27 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_27.setGeometry(QtCore.QRect(520, 250, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_27.setFont(font)
        self.tab_2_entry_box_27.setTabChangesFocus(True)
        self.tab_2_entry_box_27.setPlaceholderText("")
        self.tab_2_entry_box_27.setObjectName("tab_2_entry_box_27")
        self.tab_2_entry_box_26 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_26.setGeometry(QtCore.QRect(520, 210, 251, 31))
        self.tab_2_entry_box_26.setObjectName("tab_2_entry_box_26")
        self.tab_2_entry_box_26.addItem("")
        self.tab_2_entry_box_26.setItemText(0, "")
        self.tab_2_entry_box_26.addItem("")
        self.tab_2_entry_box_26.addItem("")
        self.tab_2_entry_box_24 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_24.setGeometry(QtCore.QRect(520, 130, 251, 31))
        self.tab_2_entry_box_24.setObjectName("tab_2_entry_box_24")
        self.tab_2_entry_box_24.addItem("")
        self.tab_2_entry_box_24.setItemText(0, "")
        self.tab_2_entry_box_24.addItem("")
        self.tab_2_entry_box_24.addItem("")
        self.tab_2_label_22 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_22.setGeometry(QtCore.QRect(780, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_22.setFont(font)
        self.tab_2_label_22.setObjectName("tab_2_label_22")
        self.tab_2_label_27 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_27.setGeometry(QtCore.QRect(780, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_27.setFont(font)
        self.tab_2_label_27.setObjectName("tab_2_label_27")
        self.tab_2_entry_box_25 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_25.setGeometry(QtCore.QRect(520, 170, 251, 31))
        self.tab_2_entry_box_25.setObjectName("tab_2_entry_box_25")
        self.tab_2_entry_box_25.addItem("")
        self.tab_2_entry_box_25.setItemText(0, "")
        self.tab_2_entry_box_25.addItem("")
        self.tab_2_entry_box_25.addItem("")
        self.tab_2_label_23 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_23.setGeometry(QtCore.QRect(780, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_23.setFont(font)
        self.tab_2_label_23.setObjectName("tab_2_label_23")
        self.tab_2_label_26 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_26.setGeometry(QtCore.QRect(780, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_26.setFont(font)
        self.tab_2_label_26.setObjectName("tab_2_label_26")
        self.tab_2_entry_box_22 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_22.setGeometry(QtCore.QRect(520, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_22.setFont(font)
        self.tab_2_entry_box_22.setTabChangesFocus(True)
        self.tab_2_entry_box_22.setPlaceholderText("")
        self.tab_2_entry_box_22.setObjectName("tab_2_entry_box_22")
        self.tab_2_label_28 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_28.setGeometry(QtCore.QRect(780, 290, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_28.setFont(font)
        self.tab_2_label_28.setObjectName("tab_2_label_28")
        self.tab_2_label_25 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_25.setGeometry(QtCore.QRect(780, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_25.setFont(font)
        self.tab_2_label_25.setObjectName("tab_2_label_25")
        self.tab_2_entry_box_28 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_28.setGeometry(QtCore.QRect(520, 290, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_28.setFont(font)
        self.tab_2_entry_box_28.setTabChangesFocus(True)
        self.tab_2_entry_box_28.setPlaceholderText("")
        self.tab_2_entry_box_28.setObjectName("tab_2_entry_box_28")
        self.tab_2_label_29 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_29.setGeometry(QtCore.QRect(780, 330, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_29.setFont(font)
        self.tab_2_label_29.setObjectName("tab_2_label_29")
        self.tab_2_entry_box_29 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_29.setGeometry(QtCore.QRect(520, 330, 251, 31))
        self.tab_2_entry_box_29.setObjectName("tab_2_entry_box_29")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.setItemText(0, "")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_29.addItem("")
        self.tab_2_entry_box_23 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_23.setGeometry(QtCore.QRect(520, 90, 251, 31))
        self.tab_2_entry_box_23.setObjectName("tab_2_entry_box_23")
        self.tab_2_entry_box_23.addItem("")
        self.tab_2_entry_box_23.setItemText(0, "")
        self.tab_2_entry_box_23.addItem("")
        self.tab_2_entry_box_23.addItem("")
        self.tab_2_label_31 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_31.setGeometry(QtCore.QRect(780, 410, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_31.setFont(font)
        self.tab_2_label_31.setObjectName("tab_2_label_31")
        self.tab_2_entry_box_31 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_31.setGeometry(QtCore.QRect(520, 410, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_31.setFont(font)
        self.tab_2_entry_box_31.setTabChangesFocus(True)
        self.tab_2_entry_box_31.setPlaceholderText("")
        self.tab_2_entry_box_31.setObjectName("tab_2_entry_box_31")
        self.tab_2_entry_box_34 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_34.setGeometry(QtCore.QRect(520, 530, 251, 31))
        self.tab_2_entry_box_34.setObjectName("tab_2_entry_box_34")
        self.tab_2_entry_box_34.addItem("")
        self.tab_2_entry_box_34.setItemText(0, "")
        self.tab_2_entry_box_34.addItem("")
        self.tab_2_entry_box_34.addItem("")
        self.tab_2_label_38 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_38.setGeometry(QtCore.QRect(780, 690, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_38.setFont(font)
        self.tab_2_label_38.setObjectName("tab_2_label_38")
        self.tab_2_entry_box_33 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_33.setGeometry(QtCore.QRect(520, 490, 251, 31))
        self.tab_2_entry_box_33.setObjectName("tab_2_entry_box_33")
        self.tab_2_entry_box_33.addItem("")
        self.tab_2_entry_box_33.setItemText(0, "")
        self.tab_2_entry_box_33.addItem("")
        self.tab_2_entry_box_33.addItem("")
        self.tab_2_label_40 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_40.setGeometry(QtCore.QRect(780, 770, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_40.setFont(font)
        self.tab_2_label_40.setObjectName("tab_2_label_40")
        self.tab_2_label_33 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_33.setGeometry(QtCore.QRect(780, 490, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_33.setFont(font)
        self.tab_2_label_33.setObjectName("tab_2_label_33")
        self.tab_2_label_34 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_34.setGeometry(QtCore.QRect(780, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_34.setFont(font)
        self.tab_2_label_34.setObjectName("tab_2_label_34")
        self.tab_2_entry_box_39 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_39.setGeometry(QtCore.QRect(520, 730, 251, 31))
        self.tab_2_entry_box_39.setObjectName("tab_2_entry_box_39")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.setItemText(0, "")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_39.addItem("")
        self.tab_2_entry_box_32 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_32.setGeometry(QtCore.QRect(520, 450, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_32.setFont(font)
        self.tab_2_entry_box_32.setTabChangesFocus(True)
        self.tab_2_entry_box_32.setPlaceholderText("")
        self.tab_2_entry_box_32.setObjectName("tab_2_entry_box_32")
        self.tab_2_entry_box_37 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_37.setGeometry(QtCore.QRect(520, 650, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_37.setFont(font)
        self.tab_2_entry_box_37.setTabChangesFocus(True)
        self.tab_2_entry_box_37.setPlaceholderText("")
        self.tab_2_entry_box_37.setObjectName("tab_2_entry_box_37")
        self.tab_2_label_39 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_39.setGeometry(QtCore.QRect(780, 730, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_39.setFont(font)
        self.tab_2_label_39.setObjectName("tab_2_label_39")
        self.tab_2_entry_box_38 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_38.setGeometry(QtCore.QRect(520, 690, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_38.setFont(font)
        self.tab_2_entry_box_38.setTabChangesFocus(True)
        self.tab_2_entry_box_38.setPlaceholderText("")
        self.tab_2_entry_box_38.setObjectName("tab_2_entry_box_38")
        self.tab_2_label_35 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_35.setGeometry(QtCore.QRect(780, 570, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_35.setFont(font)
        self.tab_2_label_35.setObjectName("tab_2_label_35")
        self.tab_2_label_32 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_32.setGeometry(QtCore.QRect(780, 450, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_32.setFont(font)
        self.tab_2_label_32.setObjectName("tab_2_label_32")
        self.tab_2_entry_box_41 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tab_2_entry_box_41.setGeometry(QtCore.QRect(1030, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_entry_box_41.setFont(font)
        self.tab_2_entry_box_41.setTabChangesFocus(True)
        self.tab_2_entry_box_41.setPlaceholderText("")
        self.tab_2_entry_box_41.setObjectName("tab_2_entry_box_41")
        self.tab_2_label_37 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_37.setGeometry(QtCore.QRect(780, 650, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_37.setFont(font)
        self.tab_2_label_37.setObjectName("tab_2_label_37")
        self.tab_2_entry_box_35 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_35.setGeometry(QtCore.QRect(520, 570, 251, 31))
        self.tab_2_entry_box_35.setObjectName("tab_2_entry_box_35")
        self.tab_2_entry_box_35.addItem("")
        self.tab_2_entry_box_35.setItemText(0, "")
        self.tab_2_entry_box_35.addItem("")
        self.tab_2_entry_box_35.addItem("")
        self.tab_2_label_41 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_41.setGeometry(QtCore.QRect(1290, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_41.setFont(font)
        self.tab_2_label_41.setObjectName("tab_2_label_41")
        self.tab_2_label_36 = QtWidgets.QLabel(self.tab_2)
        self.tab_2_label_36.setGeometry(QtCore.QRect(780, 610, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_2_label_36.setFont(font)
        self.tab_2_label_36.setObjectName("tab_2_label_36")
        self.tab_2_entry_box_40 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_40.setGeometry(QtCore.QRect(520, 770, 251, 31))
        self.tab_2_entry_box_40.setObjectName("tab_2_entry_box_40")
        self.tab_2_entry_box_40.addItem("")
        self.tab_2_entry_box_40.setItemText(0, "")
        self.tab_2_entry_box_40.addItem("")
        self.tab_2_entry_box_40.addItem("")
        self.tab_2_entry_box_36 = QtWidgets.QComboBox(self.tab_2)
        self.tab_2_entry_box_36.setGeometry(QtCore.QRect(520, 610, 251, 31))
        self.tab_2_entry_box_36.setObjectName("tab_2_entry_box_36")
        self.tab_2_entry_box_36.addItem("")
        self.tab_2_entry_box_36.setItemText(0, "")
        self.tab_2_entry_box_36.addItem("")
        self.tab_2_entry_box_36.addItem("")
        self.tab_2_line_02 = QtWidgets.QFrame(self.tab_2)
        self.tab_2_line_02.setGeometry(QtCore.QRect(1010, 10, 21, 801))
        self.tab_2_line_02.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_2_line_02.setLineWidth(2)
        self.tab_2_line_02.setMidLineWidth(0)
        self.tab_2_line_02.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_2_line_02.setObjectName("tab_2_line_02")
        self.all_tabs.addTab(self.tab_2, "")
        
        #--------------------------------------------------------------------------
        #-                             tab 3                                      -
        #--------------------------------------------------------------------------    
        
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.all_tabs.addTab(self.tab_3, "")
        
        #--------------------------------------------------------------------------
        #-                              tab 4                                     -
        #--------------------------------------------------------------------------    
        
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        font = QtGui.QFont()
        font.setPointSize(12)

        #----------------------------Entry Boxes-----------------------------------
        #--------------------------------------------------------------------------

        self.tab_4_entry_box_01 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_01.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.tab_4_entry_box_01.setFont(font)
        self.tab_4_entry_box_01.setPlaceholderText("")
        self.tab_4_entry_box_01.setObjectName("tab_4_entry_box_01")
        self.tab_4_entry_box_01.setTabChangesFocus(True)

        self.tab_4_entry_box_02 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_02.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.tab_4_entry_box_02.setFont(font)
        self.tab_4_entry_box_02.setPlaceholderText("")
        self.tab_4_entry_box_02.setObjectName("tab_4_entry_box_02")
        self.tab_4_entry_box_02.setTabChangesFocus(True)
 
        self.tab_4_entry_box_03 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_03.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.tab_4_entry_box_03.setObjectName("tab_4_entry_box_03")
        for _ in range(7):
            self.tab_4_entry_box_03.addItem("")
        self.tab_4_entry_box_03.setItemText(0, "")
        self.tab_4_entry_box_03.activated.connect(self.tab_4_function_auto_set_drop_downs)
 
        self.tab_4_entry_box_04 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_04.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.tab_4_entry_box_04.setObjectName("tab_4_entry_box_04")
        for _ in range(6):    
            self.tab_4_entry_box_04.addItem("")
        self.tab_4_entry_box_04.setItemText(0, "")
 
        self.tab_4_entry_box_05 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_05.setGeometry(QtCore.QRect(10, 170, 251, 31))
        self.tab_4_entry_box_05.setObjectName("tab_4_entry_box_05")
        for _ in range(3):    
            self.tab_4_entry_box_05.addItem("")
        self.tab_4_entry_box_05.setItemText(0, "")
 
        self.tab_4_entry_box_06 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_06.setGeometry(QtCore.QRect(10, 210, 251, 31))
        self.tab_4_entry_box_06.setObjectName("tab_4_entry_box_06")
        for _ in range(4):
            self.tab_4_entry_box_06.addItem("")
        self.tab_4_entry_box_06.setItemText(0, "")
 
        self.tab_4_entry_box_07 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_07.setGeometry(QtCore.QRect(10, 250, 251, 31))
        self.tab_4_entry_box_07.setObjectName("tab_4_entry_box_07")
        for _ in range(3):    
            self.tab_4_entry_box_07.addItem("")
        self.tab_4_entry_box_07.setItemText(0, "")
 
        self.tab_4_entry_box_08 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_08.setGeometry(QtCore.QRect(10, 290, 251, 31))
        self.tab_4_entry_box_08.setFont(font)
        self.tab_4_entry_box_08.setPlaceholderText("")
        self.tab_4_entry_box_08.setObjectName("tab_4_entry_box_08")
        self.tab_4_entry_box_08.setTabChangesFocus(True)
 
        self.tab_4_entry_box_09 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_09.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.tab_4_entry_box_09.setObjectName("tab_4_entry_box_09")
        for _ in range(6):
            self.tab_4_entry_box_09.addItem("")
        self.tab_4_entry_box_09.setItemText(0, "")
 
        self.tab_4_entry_box_10 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_10.setGeometry(QtCore.QRect(10, 370, 251, 31))
        self.tab_4_entry_box_10.setObjectName("tab_4_entry_box_10")
        for _ in range(6):
            self.tab_4_entry_box_10.addItem("")
        self.tab_4_entry_box_10.setItemText(0, "")
 
        self.tab_4_entry_box_11 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_11.setGeometry(QtCore.QRect(10, 410, 251, 31))
        self.tab_4_entry_box_11.setObjectName("tab_4_entry_box_11")
        for _ in range(3):
            self.tab_4_entry_box_11.addItem("")
        self.tab_4_entry_box_11.setItemText(0, "")
 
        self.tab_4_entry_box_12 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_12.setGeometry(QtCore.QRect(10, 450, 251, 31))
        self.tab_4_entry_box_12.setFont(font)
        self.tab_4_entry_box_12.setPlaceholderText("")
        self.tab_4_entry_box_12.setObjectName("tab_4_entry_box_12")
        self.tab_4_entry_box_12.setTabChangesFocus(True)
 
        self.tab_4_entry_box_13 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_13.setGeometry(QtCore.QRect(10, 490, 251, 31))
        self.tab_4_entry_box_13.setObjectName("tab_4_entry_box_13")
        for _ in range(4):
            self.tab_4_entry_box_13.addItem("")
        self.tab_4_entry_box_13.setItemText(0, "")
 
        self.tab_4_entry_box_14 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_14.setGeometry(QtCore.QRect(10, 530, 251, 31))
        self.tab_4_entry_box_14.setObjectName("tab_4_entry_box_14")
        for _ in range(3):    
            self.tab_4_entry_box_14.addItem("")
        self.tab_4_entry_box_14.setItemText(0, "")
 
        self.tab_4_entry_box_15 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_15.setGeometry(QtCore.QRect(10, 570, 251, 31))
        self.tab_4_entry_box_15.setFont(font)
        self.tab_4_entry_box_15.setPlaceholderText("")
        self.tab_4_entry_box_15.setObjectName("tab_4_entry_box_15")
        self.tab_4_entry_box_15.setTabChangesFocus(True)
 
        self.tab_4_entry_box_16 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_16.setGeometry(QtCore.QRect(10, 610, 251, 31))
        self.tab_4_entry_box_16.setObjectName("tab_4_entry_box_16")
        for _ in range(3):    
            self.tab_4_entry_box_16.addItem("")
        self.tab_4_entry_box_16.setItemText(0, "")
 
        self.tab_4_entry_box_17 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_17.setGeometry(QtCore.QRect(10, 650, 251, 31))
        self.tab_4_entry_box_17.setObjectName("tab_4_entry_box_17")
        for _ in range(2):    
            self.tab_4_entry_box_17.addItem("")
        self.tab_4_entry_box_17.setItemText(0, "")
 
        self.tab_4_entry_box_18 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_18.setGeometry(QtCore.QRect(10, 690, 251, 31))
        self.tab_4_entry_box_18.setFont(font)
        self.tab_4_entry_box_18.setPlaceholderText("")
        self.tab_4_entry_box_18.setObjectName("tab_4_entry_box_18")
        self.tab_4_entry_box_18.setTabChangesFocus(True)
 
        self.tab_4_entry_box_19 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_19.setGeometry(QtCore.QRect(10, 730, 251, 31))
        self.tab_4_entry_box_19.setFont(font)
        self.tab_4_entry_box_19.setPlaceholderText("")
        self.tab_4_entry_box_19.setObjectName("tab_4_entry_box_19")
        self.tab_4_entry_box_19.setTabChangesFocus(True)
 
        self.tab_4_entry_box_20 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_20.setGeometry(QtCore.QRect(10, 770, 251, 31))
        self.tab_4_entry_box_20.setObjectName("tab_4_entry_box_20")
        for _ in range(4):    
            self.tab_4_entry_box_20.addItem("")
        self.tab_4_entry_box_20.setItemText(0, "")
 
        self.tab_4_entry_box_21 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_21.setGeometry(QtCore.QRect(470, 10, 251, 31))
        self.tab_4_entry_box_21.setObjectName("tab_4_entry_box_21")
        for _ in range(3):    
            self.tab_4_entry_box_21.addItem("")
        self.tab_4_entry_box_21.setItemText(0, "")
 
        self.tab_4_entry_box_22 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_22.setGeometry(QtCore.QRect(470, 50, 251, 31))
        self.tab_4_entry_box_22.setFont(font)
        self.tab_4_entry_box_22.setPlaceholderText("")
        self.tab_4_entry_box_22.setObjectName("tab_4_entry_box_22")
        self.tab_4_entry_box_22.setTabChangesFocus(True)
 
        self.tab_4_entry_box_23 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_23.setGeometry(QtCore.QRect(470, 90, 251, 31))
        self.tab_4_entry_box_23.setFont(font)
        self.tab_4_entry_box_23.setPlaceholderText("")
        self.tab_4_entry_box_23.setObjectName("tab_4_entry_box_23")
        self.tab_4_entry_box_23.setTabChangesFocus(True)
 
        self.tab_4_entry_box_24 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_24.setGeometry(QtCore.QRect(470, 130, 251, 31))
        self.tab_4_entry_box_24.setFont(font)
        self.tab_4_entry_box_24.setPlaceholderText("")
        self.tab_4_entry_box_24.setObjectName("tab_4_entry_box_24")
        self.tab_4_entry_box_24.setTabChangesFocus(True)
 
        self.tab_4_entry_box_25 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_25.setGeometry(QtCore.QRect(470, 170, 251, 31))
        self.tab_4_entry_box_25.setFont(font)
        self.tab_4_entry_box_25.setPlaceholderText("")
        self.tab_4_entry_box_25.setObjectName("tab_4_entry_box_26")
        self.tab_4_entry_box_25.setTabChangesFocus(True)
 
        self.tab_4_entry_box_26 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_26.setGeometry(QtCore.QRect(470, 210, 251, 31))
        self.tab_4_entry_box_26.setObjectName("tab_4_entry_box_27")
        for _ in range(4):   
            self.tab_4_entry_box_26.addItem("")
        self.tab_4_entry_box_26.setItemText(0, "")
 
        self.tab_4_entry_box_27 = QtWidgets.QComboBox(self.tab_4)
        self.tab_4_entry_box_27.setGeometry(QtCore.QRect(470, 250, 251, 31))
        self.tab_4_entry_box_27.setObjectName("tab_4_entry_box_28")
        for _ in range(3):    
            self.tab_4_entry_box_27.addItem("")
        self.tab_4_entry_box_27.setItemText(0, "")
 
        self.tab_4_entry_box_28 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_28.setGeometry(QtCore.QRect(470, 290, 251, 31))
        self.tab_4_entry_box_28.setFont(font)
        self.tab_4_entry_box_28.setPlaceholderText("")
        self.tab_4_entry_box_28.setObjectName("tab_4_entry_box_29")
        self.tab_4_entry_box_28.setTabChangesFocus(True)
 
        self.tab_4_entry_box_29 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_29.setGeometry(QtCore.QRect(470, 330, 251, 31))
        self.tab_4_entry_box_29.setFont(font)
        self.tab_4_entry_box_29.setPlaceholderText("")
        self.tab_4_entry_box_29.setObjectName("tab_4_entry_box_30")
        self.tab_4_entry_box_29.setTabChangesFocus(True)
 
        self.tab_4_entry_box_30 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.tab_4_entry_box_30.setGeometry(QtCore.QRect(470, 370, 251, 31))
        self.tab_4_entry_box_30.setFont(font)
        self.tab_4_entry_box_30.setPlaceholderText("")
        self.tab_4_entry_box_30.setObjectName("tab_4_entry_box_31")
        self.tab_4_entry_box_30.setTabChangesFocus(True) 
        
        #-------------------------------Labels-------------------------------------
        #--------------------------------------------------------------------------
        
        self.tab_4_label_01 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_01.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.tab_4_label_01.setFont(font)
        self.tab_4_label_01.setObjectName("tab_4_label_01")
        
        self.tab_4_label_02 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_02.setGeometry(QtCore.QRect(270, 50, 121, 31))
        self.tab_4_label_02.setFont(font)
        self.tab_4_label_02.setObjectName("tab_4_label_02")

        self.tab_4_label_03 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_03.setGeometry(QtCore.QRect(270, 90, 121, 31))
        self.tab_4_label_03.setFont(font)
        self.tab_4_label_03.setObjectName("tab_4_label_03")

        self.tab_4_label_04 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_04.setGeometry(QtCore.QRect(270, 130, 121, 31))
        self.tab_4_label_04.setFont(font)
        self.tab_4_label_04.setObjectName("tab_4_label_04")
        
        self.tab_4_label_05 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_05.setGeometry(QtCore.QRect(270, 170, 121, 31))
        self.tab_4_label_05.setFont(font)
        self.tab_4_label_05.setObjectName("tab_4_label_05")

        self.tab_4_label_06 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_06.setGeometry(QtCore.QRect(270, 210, 181, 31))
        self.tab_4_label_06.setFont(font)
        self.tab_4_label_06.setObjectName("tab_4_label_06")

        self.tab_4_label_07 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_07.setGeometry(QtCore.QRect(270, 250, 181, 31))
        self.tab_4_label_07.setFont(font)
        self.tab_4_label_07.setObjectName("tab_4_label_07")

        self.tab_4_label_08 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_08.setGeometry(QtCore.QRect(270, 290, 121, 31))
        self.tab_4_label_08.setFont(font)
        self.tab_4_label_08.setObjectName("tab_4_label_08")
        
        self.tab_4_label_09 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_09.setGeometry(QtCore.QRect(270, 330, 181, 31))
        self.tab_4_label_09.setFont(font)
        self.tab_4_label_09.setObjectName("tab_4_label_09")

        self.tab_4_label_10 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_10.setGeometry(QtCore.QRect(270, 370, 181, 31))
        self.tab_4_label_10.setFont(font)
        self.tab_4_label_10.setObjectName("tab_4_label_10")
        
        self.tab_4_label_11 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_11.setGeometry(QtCore.QRect(270, 410, 181, 31))
        self.tab_4_label_11.setFont(font)
        self.tab_4_label_11.setObjectName("tab_4_label_11")

        self.tab_4_label_12 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_12.setGeometry(QtCore.QRect(270, 450, 181, 31))
        self.tab_4_label_12.setFont(font)
        self.tab_4_label_12.setObjectName("tab_4_label_12")

        self.tab_4_label_13 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_13.setGeometry(QtCore.QRect(270, 490, 181, 31))
        self.tab_4_label_13.setFont(font)
        self.tab_4_label_13.setObjectName("tab_4_label_13")

        self.tab_4_label_14 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_14.setGeometry(QtCore.QRect(270, 530, 181, 31))
        self.tab_4_label_14.setFont(font)
        self.tab_4_label_14.setObjectName("tab_4_label_14")

        self.tab_4_label_15 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_15.setGeometry(QtCore.QRect(270, 570, 181, 31))
        self.tab_4_label_15.setFont(font)
        self.tab_4_label_15.setObjectName("tab_4_label_15")

        self.tab_4_label_16 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_16.setGeometry(QtCore.QRect(270, 610, 181, 31))
        self.tab_4_label_16.setFont(font)
        self.tab_4_label_16.setObjectName("tab_4_label_16")

        self.tab_4_label_17 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_17.setGeometry(QtCore.QRect(270, 650, 181, 31))
        self.tab_4_label_17.setFont(font)
        self.tab_4_label_17.setObjectName("tab_4_label_17")
 
        self.tab_4_label_18 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_18.setGeometry(QtCore.QRect(270, 690, 181, 31))
        self.tab_4_label_18.setFont(font)
        self.tab_4_label_18.setObjectName("tab_4_label_18")

        self.tab_4_label_19 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_19.setGeometry(QtCore.QRect(270, 730, 181, 31))
        self.tab_4_label_19.setFont(font)
        self.tab_4_label_19.setObjectName("tab_4_label_19")

        self.tab_4_label_20 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_20.setGeometry(QtCore.QRect(270, 770, 181, 31))
        self.tab_4_label_20.setFont(font)
        self.tab_4_label_20.setObjectName("tab_4_label_20")

        self.tab_4_label_21 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_21.setGeometry(QtCore.QRect(730, 10, 131, 31))
        self.tab_4_label_21.setFont(font)
        self.tab_4_label_21.setObjectName("tab_4_label_21")

        self.tab_4_label_22 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_22.setGeometry(QtCore.QRect(730, 50, 181, 31))
        self.tab_4_label_22.setFont(font)
        self.tab_4_label_22.setObjectName("tab_4_label_22")

        self.tab_4_label_23 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_23.setGeometry(QtCore.QRect(730, 90, 241, 31))
        self.tab_4_label_23.setFont(font)
        self.tab_4_label_23.setObjectName("tab_4_label_23")
        
        self.tab_4_label_24 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_24.setGeometry(QtCore.QRect(730, 130, 241, 31))
        self.tab_4_label_24.setFont(font)
        self.tab_4_label_24.setObjectName("tab_4_label_24")
        
        self.tab_4_label_25 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_25.setGeometry(QtCore.QRect(730, 170, 181, 31))
        self.tab_4_label_25.setFont(font)
        self.tab_4_label_25.setObjectName("tab_4_label_26")
        
        self.tab_4_label_26 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_26.setGeometry(QtCore.QRect(730, 210, 181, 31))
        self.tab_4_label_26.setFont(font)
        self.tab_4_label_26.setObjectName("tab_4_label_27")
        
        self.tab_4_label_27 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_27.setGeometry(QtCore.QRect(730, 250, 131, 31))
        self.tab_4_label_27.setFont(font)
        self.tab_4_label_27.setObjectName("tab_4_label_28")
        
        self.tab_4_label_28 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_28.setGeometry(QtCore.QRect(730, 290, 181, 31))
        self.tab_4_label_28.setFont(font)
        self.tab_4_label_28.setObjectName("tab_4_label_29")

        self.tab_4_label_29 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_29.setGeometry(QtCore.QRect(730, 330, 241, 31))
        self.tab_4_label_29.setFont(font)
        self.tab_4_label_29.setObjectName("tab_4_label_30")

        self.tab_4_label_30 = QtWidgets.QLabel(self.tab_4)
        self.tab_4_label_30.setGeometry(QtCore.QRect(730, 370, 241, 31))
        self.tab_4_label_30.setFont(font)
        self.tab_4_label_30.setObjectName("tab_4_label_31")

        #-------------------------------Other--------------------------------------
        #--------------------------------------------------------------------------
        
        self.tab_4_line_01 = QtWidgets.QFrame(self.tab_4)
        self.tab_4_line_01.setGeometry(QtCore.QRect(450, 10, 21, 801))
        self.tab_4_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_4_line_01.setLineWidth(2)
        self.tab_4_line_01.setMidLineWidth(0)
        self.tab_4_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_4_line_01.setObjectName("tab_4_line_01")

        self.tab_4_line_02 = QtWidgets.QFrame(self.tab_4)
        self.tab_4_line_02.setGeometry(QtCore.QRect(970, 10, 21, 801))
        self.tab_4_line_02.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_4_line_02.setLineWidth(2)
        self.tab_4_line_02.setMidLineWidth(0)
        self.tab_4_line_02.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_4_line_02.setObjectName("tab_4_line_02")

        self.tab_4_check_box_01 = QtWidgets.QCheckBox(self.tab_4)
        self.tab_4_check_box_01.setGeometry(QtCore.QRect(10, 820, 101, 17))
        self.tab_4_check_box_01.setObjectName("tab_4_check_box_01")
        self.tab_4_check_box_01.stateChanged.connect(lambda:self.tab_4_function_hide_line_2())
        for number in range(19,25):
            ref_entry = getattr(self, f"tab_4_entry_box_{number}")
            ref_label = getattr(self, f"tab_4_label_{number}")
            ref_entry.setHidden(True)
            ref_label.setHidden(True)

        self.tab_4_check_box_02 = QtWidgets.QCheckBox(self.tab_4)
        self.tab_4_check_box_02.setGeometry(QtCore.QRect(10, 840, 101, 17))
        self.tab_4_check_box_02.setObjectName("tab_4_check_box_02")
        self.tab_4_check_box_02.stateChanged.connect(lambda:self.tab_4_function_hide_line_3())
        for number in range(25,31):
            ref_entry = getattr(self, f"tab_4_entry_box_{number}")
            ref_label = getattr(self, f"tab_4_label_{number}")
            ref_entry.setHidden(True)
            ref_label.setHidden(True)

        self.tab_4_button_01 = QtWidgets.QPushButton(self.tab_4)
        self.tab_4_button_01.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_4_button_01.setObjectName("tab_4_button_01")
        self.tab_4_button_01.clicked.connect(lambda:self.tab_4_function_clear_fields())

        self.tab_4_button_02 = QtWidgets.QPushButton(self.tab_4)
        self.tab_4_button_02.setGeometry(QtCore.QRect(250, 820, 111, 41))
        self.tab_4_button_02.setObjectName("tab_4_button_02")
        self.tab_4_button_02.clicked.connect(lambda:self.tab_4_function_add_to_queue())

        self.all_tabs.addTab(self.tab_4, "")
        
        #--------------------------------------------------------------------------
        #-                           tab 5                                        -
        #--------------------------------------------------------------------------    
        
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tab_5_label_02 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_02.setGeometry(QtCore.QRect(270, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_02.setFont(font)
        self.tab_5_label_02.setObjectName("tab_5_label_02")
        self.tab_5_entry_box_03 = QtWidgets.QComboBox(self.tab_5)
        self.tab_5_entry_box_03.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.tab_5_entry_box_03.setObjectName("tab_5_entry_box_03")
        self.tab_5_entry_box_03.addItem("")
        self.tab_5_entry_box_03.setItemText(0, "")
        self.tab_5_entry_box_03.addItem("")
        self.tab_5_entry_box_03.addItem("")
        self.tab_5_entry_box_01 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_01.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_01.setFont(font)
        self.tab_5_entry_box_01.setToolTipDuration(-1)
        self.tab_5_entry_box_01.setTabChangesFocus(True)
        self.tab_5_entry_box_01.setPlaceholderText("")
        self.tab_5_entry_box_01.setObjectName("tab_5_entry_box_01")
        self.tab_5_entry_box_02 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_02.setGeometry(QtCore.QRect(10, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_02.setFont(font)
        self.tab_5_entry_box_02.setTabChangesFocus(True)
        self.tab_5_entry_box_02.setPlaceholderText("")
        self.tab_5_entry_box_02.setObjectName("tab_5_entry_box_02")
        self.tab_5_label_01 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_01.setGeometry(QtCore.QRect(270, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_01.setFont(font)
        self.tab_5_label_01.setObjectName("tab_5_label_01")
        self.tab_5_label_03 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_03.setGeometry(QtCore.QRect(270, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_03.setFont(font)
        self.tab_5_label_03.setObjectName("tab_5_label_03")
        self.tab_5_entry_box_04 = QtWidgets.QComboBox(self.tab_5)
        self.tab_5_entry_box_04.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.tab_5_entry_box_04.setObjectName("tab_5_entry_box_04")
        self.tab_5_entry_box_04.addItem("")
        self.tab_5_entry_box_04.setItemText(0, "")
        self.tab_5_entry_box_04.addItem("")
        self.tab_5_entry_box_04.addItem("")
        self.tab_5_label_04 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_04.setGeometry(QtCore.QRect(270, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_04.setFont(font)
        self.tab_5_label_04.setObjectName("tab_5_label_04")
        self.tab_5_entry_box_06 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_06.setGeometry(QtCore.QRect(10, 210, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_06.setFont(font)
        self.tab_5_entry_box_06.setTabChangesFocus(True)
        self.tab_5_entry_box_06.setPlaceholderText("")
        self.tab_5_entry_box_06.setObjectName("tab_5_entry_box_06")
        self.tab_5_label_06 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_06.setGeometry(QtCore.QRect(270, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_06.setFont(font)
        self.tab_5_label_06.setObjectName("tab_5_label_06")
        self.tab_5_label_05 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_05.setGeometry(QtCore.QRect(270, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_05.setFont(font)
        self.tab_5_label_05.setObjectName("tab_5_label_05")
        self.tab_5_entry_box_05 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_05.setGeometry(QtCore.QRect(10, 170, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_05.setFont(font)
        self.tab_5_entry_box_05.setToolTipDuration(-1)
        self.tab_5_entry_box_05.setTabChangesFocus(True)
        self.tab_5_entry_box_05.setPlaceholderText("")
        self.tab_5_entry_box_05.setObjectName("tab_5_entry_box_05")
        self.tab_5_label_07 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_07.setGeometry(QtCore.QRect(270, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_07.setFont(font)
        self.tab_5_label_07.setObjectName("tab_5_label_07")
        self.tab_5_entry_box_07 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_07.setGeometry(QtCore.QRect(10, 250, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_07.setFont(font)
        self.tab_5_entry_box_07.setTabChangesFocus(True)
        self.tab_5_entry_box_07.setPlaceholderText("")
        self.tab_5_entry_box_07.setObjectName("tab_5_entry_box_07")
        self.tab_5_label_08 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_08.setGeometry(QtCore.QRect(270, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_08.setFont(font)
        self.tab_5_label_08.setObjectName("tab_5_label_08")
        self.tab_5_entry_box_08 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_08.setGeometry(QtCore.QRect(10, 290, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_08.setFont(font)
        self.tab_5_entry_box_08.setTabChangesFocus(True)
        self.tab_5_entry_box_08.setPlaceholderText("")
        self.tab_5_entry_box_08.setObjectName("tab_5_entry_box_08")
        self.tab_5_entry_box_09 = QtWidgets.QComboBox(self.tab_5)
        self.tab_5_entry_box_09.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.tab_5_entry_box_09.setObjectName("tab_5_entry_box_09")
        self.tab_5_entry_box_09.addItem("")
        self.tab_5_entry_box_09.setItemText(0, "")
        self.tab_5_entry_box_09.addItem("")
        self.tab_5_entry_box_09.addItem("")
        self.tab_5_label_09 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_09.setGeometry(QtCore.QRect(270, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_09.setFont(font)
        self.tab_5_label_09.setObjectName("tab_5_label_09")
        self.tab_5_label_10 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_10.setGeometry(QtCore.QRect(270, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_10.setFont(font)
        self.tab_5_label_10.setObjectName("tab_5_label_10")
        self.tab_5_entry_box_10 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_10.setGeometry(QtCore.QRect(10, 370, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_10.setFont(font)
        self.tab_5_entry_box_10.setTabChangesFocus(True)
        self.tab_5_entry_box_10.setPlaceholderText("")
        self.tab_5_entry_box_10.setObjectName("tab_5_entry_box_10")
        self.tab_5_entry_box_11 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_11.setGeometry(QtCore.QRect(10, 410, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_11.setFont(font)
        self.tab_5_entry_box_11.setTabChangesFocus(True)
        self.tab_5_entry_box_11.setPlaceholderText("")
        self.tab_5_entry_box_11.setObjectName("tab_5_entry_box_11")
        self.tab_5_label_11 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_11.setGeometry(QtCore.QRect(270, 410, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_11.setFont(font)
        self.tab_5_label_11.setObjectName("tab_5_label_11")
        self.tab_5_label_12 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_label_12.setGeometry(QtCore.QRect(270, 450, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_label_12.setFont(font)
        self.tab_5_label_12.setObjectName("tab_5_label_12")
        self.tab_5_entry_box_12 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab_5_entry_box_12.setGeometry(QtCore.QRect(10, 450, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_5_entry_box_12.setFont(font)
        self.tab_5_entry_box_12.setTabChangesFocus(True)
        self.tab_5_entry_box_12.setPlaceholderText("")
        self.tab_5_entry_box_12.setObjectName("tab_5_entry_box_12")
        self.tab_5_button_02 = QtWidgets.QPushButton(self.tab_5)
        self.tab_5_button_02.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_5_button_02.setObjectName("tab_5_button_02")
        self.tab_5_button_01 = QtWidgets.QPushButton(self.tab_5)
        self.tab_5_button_01.setGeometry(QtCore.QRect(10, 820, 111, 41))
        self.tab_5_button_01.setObjectName("tab_5_button_01")
        self.tab_5_line_01 = QtWidgets.QFrame(self.tab_5)
        self.tab_5_line_01.setGeometry(QtCore.QRect(490, 10, 21, 801))
        self.tab_5_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_5_line_01.setLineWidth(2)
        self.tab_5_line_01.setMidLineWidth(0)
        self.tab_5_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_5_line_01.setObjectName("tab_5_line_01")
        self.all_tabs.addTab(self.tab_5, "")
        
        
        #--------------------------------------------------------------------------#
        #--------------------------------------------------------------------------#
        #-                              tab 6                                     -#
        #--------------------------------------------------------------------------#    
        #--------------------------------------------------------------------------#
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        font = QtGui.QFont()
        font.setPointSize(12)
        
        #----------------------------Entry Boxes-----------------------------------#
        #--------------------------------------------------------------------------#
        
        self.tab_6_entry_box_01 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_01.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.tab_6_entry_box_01.setFont(font)
        self.tab_6_entry_box_01.setToolTipDuration(-1)
        self.tab_6_entry_box_01.setTabChangesFocus(True)
        self.tab_6_entry_box_01.setPlaceholderText("")
        self.tab_6_entry_box_01.setObjectName("tab_6_entry_box_01")
        
        self.tab_6_entry_box_02 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_02.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.tab_6_entry_box_02.setFont(font)
        self.tab_6_entry_box_02.setTabChangesFocus(True)
        self.tab_6_entry_box_02.setPlaceholderText("")
        self.tab_6_entry_box_02.setObjectName("tab_6_entry_box_02")
        
        self.tab_6_entry_box_03 = QtWidgets.QComboBox(self.tab_6)
        self.tab_6_entry_box_03.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.tab_6_entry_box_03.setObjectName("tab_6_entry_box_03")
        for _ in range(4):
            self.tab_6_entry_box_03.addItem("")
        self.tab_6_entry_box_03.setItemText(0, "")
        self.tab_6_entry_box_03.activated.connect(self.tab_6_function_auto_set_drop_downs)
        
        self.tab_6_entry_box_04 = QtWidgets.QComboBox(self.tab_6)
        self.tab_6_entry_box_04.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.tab_6_entry_box_04.setObjectName("tab_6_entry_box_04")
        for _ in range(3):    
            self.tab_6_entry_box_04.addItem("")
        self.tab_6_entry_box_04.setItemText(0, "")
        
        self.tab_6_entry_box_05 = QtWidgets.QComboBox(self.tab_6)
        self.tab_6_entry_box_05.setGeometry(QtCore.QRect(10, 170, 251, 31))
        self.tab_6_entry_box_05.setObjectName("tab_6_entry_box_05")
        for _ in range(3):
            self.tab_6_entry_box_05.addItem("")
        self.tab_6_entry_box_05.setItemText(0, "")
        
        self.tab_6_entry_box_06 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_06.setGeometry(QtCore.QRect(10, 210, 251, 31))
        self.tab_6_entry_box_06.setFont(font)
        self.tab_6_entry_box_06.setToolTipDuration(-1)
        self.tab_6_entry_box_06.setTabChangesFocus(True)
        self.tab_6_entry_box_06.setPlaceholderText("")
        self.tab_6_entry_box_06.setObjectName("tab_6_entry_box_06")
        
        self.tab_6_entry_box_07 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_07.setGeometry(QtCore.QRect(10, 250, 251, 31))
        self.tab_6_entry_box_07.setFont(font)
        self.tab_6_entry_box_07.setTabChangesFocus(True)
        self.tab_6_entry_box_07.setPlaceholderText("")
        self.tab_6_entry_box_07.setObjectName("tab_6_entry_box_07")
        self.tab_6_entry_box_07.textChanged.connect(lambda:self.tab_6_function_auto_fill_entry_box_08())
        
        self.tab_6_entry_box_08 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_08.setGeometry(QtCore.QRect(10, 290, 251, 31))
        self.tab_6_entry_box_08.setFont(font)
        self.tab_6_entry_box_08.setTabChangesFocus(True)
        self.tab_6_entry_box_08.setPlaceholderText("")
        self.tab_6_entry_box_08.setObjectName("tab_6_entry_box_08")
        
        self.tab_6_entry_box_09 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_09.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.tab_6_entry_box_09.setFont(font)
        self.tab_6_entry_box_09.setTabChangesFocus(True)
        self.tab_6_entry_box_09.setPlaceholderText("")
        self.tab_6_entry_box_09.setObjectName("tab_6_entry_box_09")
        
        self.tab_6_entry_box_10 = QtWidgets.QComboBox(self.tab_6)
        self.tab_6_entry_box_10.setGeometry(QtCore.QRect(10, 370, 251, 31))
        self.tab_6_entry_box_10.setObjectName("tab_6_entry_box_10")
        for _ in range(3):
            self.tab_6_entry_box_10.addItem("")
        self.tab_6_entry_box_10.setItemText(0, "")
        
        self.tab_6_entry_box_11 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_11.setGeometry(QtCore.QRect(10, 410, 251, 31))
        self.tab_6_entry_box_11.setFont(font)
        self.tab_6_entry_box_11.setTabChangesFocus(True)
        self.tab_6_entry_box_11.setPlaceholderText("")
        self.tab_6_entry_box_11.setObjectName("tab_6_entry_box_11")
        
        self.tab_6_entry_box_12 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_12.setGeometry(QtCore.QRect(10, 450, 251, 31))
        self.tab_6_entry_box_12.setFont(font)
        self.tab_6_entry_box_12.setTabChangesFocus(True)
        self.tab_6_entry_box_12.setPlaceholderText("")
        self.tab_6_entry_box_12.setObjectName("tab_6_entry_box_12")
        
        self.tab_6_entry_box_13 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.tab_6_entry_box_13.setGeometry(QtCore.QRect(10, 490, 251, 31))
        self.tab_6_entry_box_13.setFont(font)
        self.tab_6_entry_box_13.setTabChangesFocus(True)
        self.tab_6_entry_box_13.setPlaceholderText("")
        self.tab_6_entry_box_13.setObjectName("tab_6_entry_box_13")
        
        #------------------------------Labels---------------------------------------#
        #---------------------------------------------------------------------------#
        self.tab_6_label_01 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_01.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.tab_6_label_01.setFont(font)
        self.tab_6_label_01.setObjectName("tab_6_label_01")
        
        self.tab_6_label_02 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_02.setGeometry(QtCore.QRect(270, 50, 121, 31))
        self.tab_6_label_02.setFont(font)
        self.tab_6_label_02.setObjectName("tab_6_label_02")
        
        self.tab_6_label_03 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_03.setGeometry(QtCore.QRect(270, 90, 171, 31))
        self.tab_6_label_03.setFont(font)
        self.tab_6_label_03.setObjectName("tab_6_label_03")
        
        self.tab_6_label_04 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_04.setGeometry(QtCore.QRect(270, 130, 181, 31))
        self.tab_6_label_04.setFont(font)
        self.tab_6_label_04.setObjectName("tab_6_label_04")
        
        self.tab_6_label_05 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_05.setGeometry(QtCore.QRect(270, 170, 171, 31))
        self.tab_6_label_05.setFont(font)
        self.tab_6_label_05.setObjectName("tab_6_label_05")
        
        self.tab_6_label_06 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_06.setGeometry(QtCore.QRect(270, 210, 121, 31))
        self.tab_6_label_06.setFont(font)
        self.tab_6_label_06.setObjectName("tab_6_label_06")
        
        self.tab_6_label_07 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_07.setGeometry(QtCore.QRect(270, 250, 121, 31))
        self.tab_6_label_07.setFont(font)
        self.tab_6_label_07.setObjectName("tab_6_label_07")
        
        self.tab_6_label_08 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_08.setGeometry(QtCore.QRect(270, 290, 121, 31))
        self.tab_6_label_08.setFont(font)
        self.tab_6_label_08.setObjectName("tab_6_label_08")
        
        self.tab_6_label_09 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_09.setGeometry(QtCore.QRect(270, 330, 151, 31))
        self.tab_6_label_09.setFont(font)
        self.tab_6_label_09.setObjectName("tab_6_label_09")
        
        self.tab_6_label_10 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_10.setGeometry(QtCore.QRect(270, 370, 171, 31))
        self.tab_6_label_10.setFont(font)
        self.tab_6_label_10.setObjectName("tab_6_label_10")
        
        self.tab_6_label_11 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_11.setGeometry(QtCore.QRect(270, 410, 241, 31))
        self.tab_6_label_11.setFont(font)
        self.tab_6_label_11.setObjectName("tab_6_label_11")
        
        self.tab_6_label_12 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_12.setGeometry(QtCore.QRect(270, 450, 241, 31))
        self.tab_6_label_12.setFont(font)
        self.tab_6_label_12.setObjectName("tab_6_label_12")
        
        self.tab_6_label_13 = QtWidgets.QLabel(self.tab_6)
        self.tab_6_label_13.setGeometry(QtCore.QRect(270, 490, 241, 31))
        self.tab_6_label_13.setFont(font)
        self.tab_6_label_13.setObjectName("tab_6_label_13")
        
        #------------------------------Other---------------------------------------#
        #--------------------------------------------------------------------------#
        
        self.tab_6_button_01 = QtWidgets.QPushButton(self.tab_6)
        self.tab_6_button_01.setGeometry(QtCore.QRect(10, 820, 111, 41))
        self.tab_6_button_01.setObjectName("tab_6_button_01")
        self.tab_6_button_01.clicked.connect(lambda:self.tab_6_function_clear_fields())
        
        self.tab_6_button_02 = QtWidgets.QPushButton(self.tab_6)
        self.tab_6_button_02.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_6_button_02.setObjectName("tab_6_button_02")
        self.tab_6_button_02.clicked.connect(lambda:self.tab_6_function_add_to_queue())
        
        self.tab_6_line_01 = QtWidgets.QFrame(self.tab_6)
        self.tab_6_line_01.setGeometry(QtCore.QRect(490, 10, 21, 801))
        self.tab_6_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_6_line_01.setLineWidth(2)
        self.tab_6_line_01.setMidLineWidth(0)
        self.tab_6_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_6_line_01.setObjectName("tab_6_line_01")
        
        self.all_tabs.addTab(self.tab_6, "")
        
        
        #---------------------------------------------------------------------------#
        #---------------------------------------------------------------------------#
        #-                               tab 7                                     -#
        #---------------------------------------------------------------------------#    
        #---------------------------------------------------------------------------#
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tab_7_entry_box_09 = QtWidgets.QComboBox(self.tab_7)
        self.tab_7_entry_box_09.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.tab_7_entry_box_09.setObjectName("tab_7_entry_box_09")
        self.tab_7_entry_box_09.addItem("")
        self.tab_7_entry_box_09.setItemText(0, "")
        self.tab_7_entry_box_09.addItem("")
        self.tab_7_entry_box_09.addItem("")
        self.tab_7_entry_box_02 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_02.setGeometry(QtCore.QRect(10, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_02.setFont(font)
        self.tab_7_entry_box_02.setTabChangesFocus(True)
        self.tab_7_entry_box_02.setPlaceholderText("")
        self.tab_7_entry_box_02.setObjectName("tab_7_entry_box_02")
        self.tab_7_label_08 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_08.setGeometry(QtCore.QRect(270, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_08.setFont(font)
        self.tab_7_label_08.setObjectName("tab_7_label_08")
        self.tab_7_entry_box_04 = QtWidgets.QComboBox(self.tab_7)
        self.tab_7_entry_box_04.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.tab_7_entry_box_04.setObjectName("tab_7_entry_box_04")
        self.tab_7_entry_box_04.addItem("")
        self.tab_7_entry_box_04.setItemText(0, "")
        self.tab_7_entry_box_04.addItem("")
        self.tab_7_entry_box_04.addItem("")
        self.tab_7_entry_box_03 = QtWidgets.QComboBox(self.tab_7)
        self.tab_7_entry_box_03.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.tab_7_entry_box_03.setObjectName("tab_7_entry_box_03")
        self.tab_7_entry_box_03.addItem("")
        self.tab_7_entry_box_03.setItemText(0, "")
        self.tab_7_entry_box_03.addItem("")
        self.tab_7_entry_box_03.addItem("")
        self.tab_7_entry_box_05 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_05.setGeometry(QtCore.QRect(10, 170, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_05.setFont(font)
        self.tab_7_entry_box_05.setToolTipDuration(-1)
        self.tab_7_entry_box_05.setTabChangesFocus(True)
        self.tab_7_entry_box_05.setPlaceholderText("")
        self.tab_7_entry_box_05.setObjectName("tab_7_entry_box_05")
        self.tab_7_label_05 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_05.setGeometry(QtCore.QRect(270, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_05.setFont(font)
        self.tab_7_label_05.setObjectName("tab_7_label_05")
        self.tab_7_entry_box_01 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_01.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_01.setFont(font)
        self.tab_7_entry_box_01.setToolTipDuration(-1)
        self.tab_7_entry_box_01.setTabChangesFocus(True)
        self.tab_7_entry_box_01.setPlaceholderText("")
        self.tab_7_entry_box_01.setObjectName("tab_7_entry_box_01")
        self.tab_7_label_06 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_06.setGeometry(QtCore.QRect(270, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_06.setFont(font)
        self.tab_7_label_06.setObjectName("tab_7_label_06")
        self.tab_7_label_11 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_11.setGeometry(QtCore.QRect(270, 410, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_11.setFont(font)
        self.tab_7_label_11.setObjectName("tab_7_label_11")
        self.tab_7_entry_box_08 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_08.setGeometry(QtCore.QRect(10, 290, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_08.setFont(font)
        self.tab_7_entry_box_08.setTabChangesFocus(True)
        self.tab_7_entry_box_08.setPlaceholderText("")
        self.tab_7_entry_box_08.setObjectName("tab_7_entry_box_08")
        self.tab_7_label_10 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_10.setGeometry(QtCore.QRect(270, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_10.setFont(font)
        self.tab_7_label_10.setObjectName("tab_7_label_10")
        self.tab_7_button_01 = QtWidgets.QPushButton(self.tab_7)
        self.tab_7_button_01.setGeometry(QtCore.QRect(10, 820, 111, 41))
        self.tab_7_button_01.setObjectName("tab_7_button_01")
        self.tab_7_entry_box_06 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_06.setGeometry(QtCore.QRect(10, 210, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_06.setFont(font)
        self.tab_7_entry_box_06.setTabChangesFocus(True)
        self.tab_7_entry_box_06.setPlaceholderText("")
        self.tab_7_entry_box_06.setObjectName("tab_7_entry_box_06")
        self.tab_7_label_03 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_03.setGeometry(QtCore.QRect(270, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_03.setFont(font)
        self.tab_7_label_03.setObjectName("tab_7_label_03")
        self.tab_7_entry_box_10 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_10.setGeometry(QtCore.QRect(10, 370, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_10.setFont(font)
        self.tab_7_entry_box_10.setTabChangesFocus(True)
        self.tab_7_entry_box_10.setPlaceholderText("")
        self.tab_7_entry_box_10.setObjectName("tab_7_entry_box_10")
        self.tab_7_label_01 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_01.setGeometry(QtCore.QRect(270, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_01.setFont(font)
        self.tab_7_label_01.setObjectName("tab_7_label_01")
        self.tab_7_label_09 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_09.setGeometry(QtCore.QRect(270, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_09.setFont(font)
        self.tab_7_label_09.setObjectName("tab_7_label_09")
        self.tab_7_entry_box_11 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_11.setGeometry(QtCore.QRect(10, 410, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_11.setFont(font)
        self.tab_7_entry_box_11.setTabChangesFocus(True)
        self.tab_7_entry_box_11.setPlaceholderText("")
        self.tab_7_entry_box_11.setObjectName("tab_7_entry_box_11")
        self.tab_7_entry_box_07 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_07.setGeometry(QtCore.QRect(10, 250, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_07.setFont(font)
        self.tab_7_entry_box_07.setTabChangesFocus(True)
        self.tab_7_entry_box_07.setPlaceholderText("")
        self.tab_7_entry_box_07.setObjectName("tab_7_entry_box_07")
        self.tab_7_label_07 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_07.setGeometry(QtCore.QRect(270, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_07.setFont(font)
        self.tab_7_label_07.setObjectName("tab_7_label_07")
        self.tab_7_label_04 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_04.setGeometry(QtCore.QRect(270, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_04.setFont(font)
        self.tab_7_label_04.setObjectName("tab_7_label_04")
        self.tab_7_button_02 = QtWidgets.QPushButton(self.tab_7)
        self.tab_7_button_02.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_7_button_02.setObjectName("tab_7_button_02")
        self.tab_7_entry_box_12 = QtWidgets.QPlainTextEdit(self.tab_7)
        self.tab_7_entry_box_12.setGeometry(QtCore.QRect(10, 450, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_entry_box_12.setFont(font)
        self.tab_7_entry_box_12.setTabChangesFocus(True)
        self.tab_7_entry_box_12.setPlaceholderText("")
        self.tab_7_entry_box_12.setObjectName("tab_7_entry_box_12")
        self.tab_7_label_12 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_12.setGeometry(QtCore.QRect(270, 450, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_12.setFont(font)
        self.tab_7_label_12.setObjectName("tab_7_label_12")
        self.tab_7_label_02 = QtWidgets.QLabel(self.tab_7)
        self.tab_7_label_02.setGeometry(QtCore.QRect(270, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_7_label_02.setFont(font)
        self.tab_7_label_02.setObjectName("tab_7_label_02")
        self.tab_7_line_01 = QtWidgets.QFrame(self.tab_7)
        self.tab_7_line_01.setGeometry(QtCore.QRect(490, 10, 21, 801))
        self.tab_7_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab_7_line_01.setLineWidth(2)
        self.tab_7_line_01.setMidLineWidth(0)
        self.tab_7_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.tab_7_line_01.setObjectName("tab_7_line_01")
        self.all_tabs.addTab(self.tab_7, "")

        #--------------------------------------------------------------------------#
        #-                           tab 8                                        -#
        #--------------------------------------------------------------------------#   

        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tab_8_list_box_01 = QtWidgets.QListWidget(self.tab_8)
        self.tab_8_list_box_01.setGeometry(QtCore.QRect(0, 0, 1521, 811))
        self.tab_8_list_box_01.setObjectName("tab_8_list_box_01")
        for _ in range(99):
            item = QtWidgets.QListWidgetItem()
            self.tab_8_list_box_01.addItem(item)
        self.tab_8_button_01 = QtWidgets.QPushButton(self.tab_8)
        self.tab_8_button_01.setGeometry(QtCore.QRect(10, 820, 111, 41))
        self.tab_8_button_01.setObjectName("tab_8_button_01")
        self.tab_8_button_02 = QtWidgets.QPushButton(self.tab_8)
        self.tab_8_button_02.setGeometry(QtCore.QRect(130, 820, 111, 41))
        self.tab_8_button_02.setObjectName("tab_8_button_02")
        self.tab_8_button_03 = QtWidgets.QPushButton(self.tab_8)
        self.tab_8_button_03.setGeometry(QtCore.QRect(1390, 820, 111, 41))
        self.tab_8_button_03.setObjectName("tab_8_button_03")
        self.tab_8_label_01 = QtWidgets.QLabel(self.tab_8)
        self.tab_8_label_01.setGeometry(QtCore.QRect(1330, 820, 111, 41))
        self.tab_8_label_01.setFont(font)
        self.tab_8_label_01.setObjectName("tab_8_label_01")
        self.all_tabs.addTab(self.tab_8, "")

        #--------------------------------------------------------------------------#
        #-                           Whole App                                    -#
        #--------------------------------------------------------------------------#   

        cucm_csv_generator.setCentralWidget(self.application)
        self.statusBar = QtWidgets.QStatusBar(cucm_csv_generator)
        self.statusBar.setObjectName("statusBar")
        cucm_csv_generator.setStatusBar(self.statusBar)

        self.retranslateUi(cucm_csv_generator)
        self.all_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cucm_csv_generator)

    
    #--------------------------------------------------------------------------#
    #--------------------------------------------------------------------------#
    #-                           Setting Text                                 -#
    #--------------------------------------------------------------------------# 
    #--------------------------------------------------------------------------#
    
    def retranslateUi(self, cucm_csv_generator):
        _translate = QtCore.QCoreApplication.translate
        cucm_csv_generator.setWindowTitle(_translate("cucm_csv_generator", "CUCM CSV Generator"))

        #--------------------------------------------------------------------------#
        #-                           Tab 1                                        -#
        #--------------------------------------------------------------------------#   
        
        self.tab_1_label_01.setText(_translate("cucm_csv_generator", "Device Name"))
        self.tab_1_label_02.setText(_translate("cucm_csv_generator", "Description"))
        self.tab_1_label_03.setText(_translate("cucm_csv_generator", "Phone Button Template"))
        self.tab_1_label_04.setText(_translate("cucm_csv_generator", "Device Pool"))
        self.tab_1_label_05.setText(_translate("cucm_csv_generator", "CSS"))
        self.tab_1_label_06.setText(_translate("cucm_csv_generator", "Location"))
        self.tab_1_label_07.setText(_translate("cucm_csv_generator", "Media Resource Group"))
        self.tab_1_label_08.setText(_translate("cucm_csv_generator", "Built in Bridge"))
        self.tab_1_label_09.setText(_translate("cucm_csv_generator", "Privacy"))
        self.tab_1_label_10.setText(_translate("cucm_csv_generator", "Softkey Template"))
        self.tab_1_label_11.setText(_translate("cucm_csv_generator", "User ID 1"))
        self.tab_1_label_12.setText(_translate("cucm_csv_generator", "Common Phone Profile"))
        self.tab_1_label_13.setText(_translate("cucm_csv_generator", "Owner User ID"))
        self.tab_1_label_14.setText(_translate("cucm_csv_generator", "Device Subscribe CSS"))
        self.tab_1_label_15.setText(_translate("cucm_csv_generator", "CSS Reroute"))
        self.tab_1_label_16.setText(_translate("cucm_csv_generator", "Directory Number 1"))
        self.tab_1_label_17.setText(_translate("cucm_csv_generator", "Voice Mail Profile 1"))
        self.tab_1_label_18.setText(_translate("cucm_csv_generator", "Line CSS 1"))
        self.tab_1_label_19.setText(_translate("cucm_csv_generator", "Foward All CSS 1"))
        self.tab_1_label_20.setText(_translate("cucm_csv_generator", "Foward Voice Maill"))
        self.tab_1_label_21.setText(_translate("cucm_csv_generator", "Foward Voice Mail CSS"))
        self.tab_1_label_22.setText(_translate("cucm_csv_generator", "Line Text Label 1"))
        self.tab_1_label_23.setText(_translate("cucm_csv_generator", "External Phone Number Mask 1"))
        self.tab_1_label_24.setText(_translate("cucm_csv_generator", "Maximum Number of Calls 1"))
        self.tab_1_label_25.setText(_translate("cucm_csv_generator", "Dialed Number 1"))
        self.tab_1_label_26.setText(_translate("cucm_csv_generator", "Line Description 1"))
        self.tab_1_label_27.setText(_translate("cucm_csv_generator", "Alerting Name 1"))
        self.tab_1_label_28.setText(_translate("cucm_csv_generator", "Secondary CSS for Foward All 1"))
        self.tab_1_label_29.setText(_translate("cucm_csv_generator", "Recording Option 1"))
        self.tab_1_label_30.setText(_translate("cucm_csv_generator", "Recording Profile 1"))
        self.tab_1_label_31.setText(_translate("cucm_csv_generator", "URI 1 on Directory Number 1"))
        self.tab_1_label_32.setText(_translate("cucm_csv_generator", "Recording Media Source 1"))
        self.tab_1_label_33.setText(_translate("cucm_csv_generator", "Directory Number 2"))
        self.tab_1_label_34.setText(_translate("cucm_csv_generator", "Voice Mail Profile 2"))
        self.tab_1_label_35.setText(_translate("cucm_csv_generator", "Foward All Voice Mail 2"))
        self.tab_1_label_36.setText(_translate("cucm_csv_generator", "Foward All CSS 2"))
        self.tab_1_label_37.setText(_translate("cucm_csv_generator", "Foward Voice Maill 2"))
        self.tab_1_label_38.setText(_translate("cucm_csv_generator", "Foward Voice Mail CSS 2"))
        self.tab_1_label_39.setText(_translate("cucm_csv_generator", "Line Text Label 2"))
        self.tab_1_label_40.setText(_translate("cucm_csv_generator", "External Phone Number Mask 2"))
        self.tab_1_label_41.setText(_translate("cucm_csv_generator", "Line Description 2"))
        self.tab_1_label_42.setText(_translate("cucm_csv_generator", "Alerting Name 2"))
        self.tab_1_label_43.setText(_translate("cucm_csv_generator", "Recording Option 2"))
        self.tab_1_label_44.setText(_translate("cucm_csv_generator", "Recording Profile 2"))
        self.tab_1_label_45.setText(_translate("cucm_csv_generator", "Recording Media Source 2"))
        self.tab_1_label_46.setText(_translate("cucm_csv_generator", "Directory Number 3"))
        self.tab_1_label_47.setText(_translate("cucm_csv_generator", "Voice Mail Profile 3"))
        self.tab_1_label_48.setText(_translate("cucm_csv_generator", "Foward All Voice Mail 3"))
        self.tab_1_label_49.setText(_translate("cucm_csv_generator", "Foward All CSS 3"))
        self.tab_1_label_50.setText(_translate("cucm_csv_generator", "Foward Voice Maill 3"))
        self.tab_1_label_51.setText(_translate("cucm_csv_generator", "Foward Voice Mail CSS 3"))
        self.tab_1_label_52.setText(_translate("cucm_csv_generator", "Line Text Label 3"))
        self.tab_1_label_53.setText(_translate("cucm_csv_generator", "External Phone Number Mask 3"))
        self.tab_1_label_54.setText(_translate("cucm_csv_generator", "Line Description 3"))
        self.tab_1_label_55.setText(_translate("cucm_csv_generator", "Alerting Name 3"))
        self.tab_1_label_56.setText(_translate("cucm_csv_generator", "Recording Option 3"))
        self.tab_1_label_57.setText(_translate("cucm_csv_generator", "Recording Profile 3"))
        self.tab_1_label_58.setText(_translate("cucm_csv_generator", "Recording Media Source 3"))

        self.tab_1_entry_box_03.setItemText(1, _translate("cucm_csv_generator", "Standard 7841 SIP"))
        self.tab_1_entry_box_03.setItemText(2, _translate("cucm_csv_generator", "Standard 7841 SIP w/DND"))
        self.tab_1_entry_box_03.setItemText(3, _translate("cucm_csv_generator", "Standard 7841 SIP w/HLog"))
        self.tab_1_entry_box_03.setItemText(4, _translate("cucm_csv_generator", "Standard 7841 SIP - 2 LN + 2 SD"))
        self.tab_1_entry_box_03.setItemText(5, _translate("cucm_csv_generator", "UNIV-Cardio-Standard 7841 SIP - 2 LN + 2 SD"))
        self.tab_1_entry_box_03.setItemText(6, _translate("cucm_csv_generator", "7841 SIP - 3 Lines + 1 Intercom"))
        self.tab_1_entry_box_03.setItemText(7, _translate("cucm_csv_generator", "7841 SIP + HG Logout (3rd LN)"))
        
        self.tab_1_entry_box_04.setItemText(1, _translate("cucm_csv_generator", "Alcoa-Infusion-DP"))
        self.tab_1_entry_box_04.setItemText(2, _translate("cucm_csv_generator", "Cardiology Fellows-HLVI-DP"))
        self.tab_1_entry_box_04.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-DP"))
        self.tab_1_entry_box_04.setItemText(4, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-DP"))
        self.tab_1_entry_box_04.setItemText(5, _translate("cucm_csv_generator", "Cedar-Bluff-UHN-UHS-DP"))
        self.tab_1_entry_box_04.setItemText(6, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-DP"))
        self.tab_1_entry_box_04.setItemText(7, _translate("cucm_csv_generator", "Cedar-Bluff-TTU-DP"))
        self.tab_1_entry_box_04.setItemText(8, _translate("cucm_csv_generator", "Cherokee-Farms-DP"))
        self.tab_1_entry_box_04.setItemText(9, _translate("cucm_csv_generator", "Halls-DP"))
        self.tab_1_entry_box_04.setItemText(10, _translate("cucm_csv_generator", "Lenoir-City-DP"))
        self.tab_1_entry_box_04.setItemText(11, _translate("cucm_csv_generator", "Patient-Registration-HLVI-DP"))
        self.tab_1_entry_box_04.setItemText(12, _translate("cucm_csv_generator", "PoB-DP1"))
        self.tab_1_entry_box_04.setItemText(13, _translate("cucm_csv_generator", "Pulm-Critical-Care-DP"))
        self.tab_1_entry_box_04.setItemText(14, _translate("cucm_csv_generator", "Pulm-Function-DP"))
        self.tab_1_entry_box_04.setItemText(15, _translate("cucm_csv_generator", "Sevierville-DP"))
        self.tab_1_entry_box_04.setItemText(16, _translate("cucm_csv_generator", "Town-Center-DP"))
        self.tab_1_entry_box_04.setItemText(17, _translate("cucm_csv_generator", "Univ-Cardio-DP"))
        self.tab_1_entry_box_04.setItemText(18, _translate("cucm_csv_generator", "University-Heart-Surgeons-DP"))
        self.tab_1_entry_box_04.setItemText(19, _translate("cucm_csv_generator", "Wound-Care-HLVI-DP"))
        
        self.tab_1_entry_box_05.setItemText(1, _translate("cucm_csv_generator", "Alcoa-Infusion-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(2, _translate("cucm_csv_generator", "Cardiology Fellows-HLVI-CSS"))
        self.tab_1_entry_box_05.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(4, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(5, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(6, _translate("cucm_csv_generator", "Halls-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(7, _translate("cucm_csv_generator", "Lenoir-City-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(8, _translate("cucm_csv_generator", "Patient-Registration-HLVI-CSS"))
        self.tab_1_entry_box_05.setItemText(9, _translate("cucm_csv_generator", "PoB-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(10, _translate("cucm_csv_generator", "Pulm-Function-CSS"))
        self.tab_1_entry_box_05.setItemText(11, _translate("cucm_csv_generator", "Pulm-Critical-Care-CSS"))
        self.tab_1_entry_box_05.setItemText(12, _translate("cucm_csv_generator", "Sevierville-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(13, _translate("cucm_csv_generator", "Town-Center-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(14, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        self.tab_1_entry_box_05.setItemText(15, _translate("cucm_csv_generator", "University-Heart-Surgeons-CSS"))
        self.tab_1_entry_box_05.setItemText(16, _translate("cucm_csv_generator", "Wound-Care-HLVI-CSS"))
        
        self.tab_1_entry_box_06.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-LOC"))
        self.tab_1_entry_box_06.setItemText(2, _translate("cucm_csv_generator", "POB-LOC"))
        self.tab_1_entry_box_06.setItemText(3, _translate("cucm_csv_generator", "Town-Center-LOC"))
        self.tab_1_entry_box_06.setItemText(4, _translate("cucm_csv_generator", "Halls-LOC"))
        self.tab_1_entry_box_06.setItemText(5, _translate("cucm_csv_generator", "Alcoa-Infusion-LOC"))
        self.tab_1_entry_box_06.setItemText(6, _translate("cucm_csv_generator", "Lenoir-City-LOC"))
        self.tab_1_entry_box_06.setItemText(7, _translate("cucm_csv_generator", "Sevierville-LOC"))

        self.tab_1_entry_box_07.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-MRGL"))
        self.tab_1_entry_box_07.setItemText(2, _translate("cucm_csv_generator", "Lenoir-MRGL"))
        self.tab_1_entry_box_07.setItemText(3, _translate("cucm_csv_generator", "Sevierville-MRGL"))
        self.tab_1_entry_box_07.setItemText(4, _translate("cucm_csv_generator", "POB-MRGL1"))
        self.tab_1_entry_box_07.setItemText(5, _translate("cucm_csv_generator", "POB-MRGL2"))

        self.tab_1_entry_box_08.setItemText(1, _translate("cucm_csv_generator", "Default"))
        self.tab_1_entry_box_08.setItemText(2, _translate("cucm_csv_generator", "On"))
        
        self.tab_1_entry_box_09.setItemText(1, _translate("cucm_csv_generator", "Default"))
        self.tab_1_entry_box_09.setItemText(2, _translate("cucm_csv_generator", "Off"))

        self.tab_1_entry_box_10.setItemText(1, _translate("cucm_csv_generator", "Standard User"))
        self.tab_1_entry_box_10.setItemText(2, _translate("cucm_csv_generator", "Standard User with Hunt Login and Logoff"))

        self.tab_1_entry_box_12.setItemText(1, _translate("cucm_csv_generator", "Standard Common Phone Profile"))
        self.tab_1_entry_box_12.setItemText(2, _translate("cucm_csv_generator", "Sevierville CPP"))

        self.tab_1_entry_box_14.setItemText(1, _translate("cucm_csv_generator", "Alcoa-Infusion-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(2, _translate("cucm_csv_generator", "Cardiology Fellows-HLVI-CSS"))
        self.tab_1_entry_box_14.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(4, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(5, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(6, _translate("cucm_csv_generator", "Halls-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(7, _translate("cucm_csv_generator", "Lenoir-City-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(8, _translate("cucm_csv_generator", "Patient-Registration-HLVI-CSS"))
        self.tab_1_entry_box_14.setItemText(9, _translate("cucm_csv_generator", "PoB-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(10, _translate("cucm_csv_generator", "Pulm-Critical-Care-CSS"))
        self.tab_1_entry_box_14.setItemText(11, _translate("cucm_csv_generator", "Pulm-Function-CSS"))
        self.tab_1_entry_box_14.setItemText(12, _translate("cucm_csv_generator", "Sevierville-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(13, _translate("cucm_csv_generator", "Town-Center-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(14, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        self.tab_1_entry_box_14.setItemText(15, _translate("cucm_csv_generator", "University-Heart-Surgeons-CSS"))
        self.tab_1_entry_box_14.setItemText(16, _translate("cucm_csv_generator", "Wound-Care-HLVI-CSS"))

        self.tab_1_entry_box_15.setItemText(1, _translate("cucm_csv_generator", "Cardiology Fellows-HLVI-CSS"))
        self.tab_1_entry_box_15.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(4, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(5, _translate("cucm_csv_generator", "Halls-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(6, _translate("cucm_csv_generator", "Lenoir-City-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(7, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_1_entry_box_15.setItemText(8, _translate("cucm_csv_generator", "Patient-Registration-HLVI-CSS"))
        self.tab_1_entry_box_15.setItemText(9, _translate("cucm_csv_generator", "PoB-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(10, _translate("cucm_csv_generator", "Pulm-Critical-Care-CSS"))
        self.tab_1_entry_box_15.setItemText(11, _translate("cucm_csv_generator", "Pulm-Function-CSS"))
        self.tab_1_entry_box_15.setItemText(12, _translate("cucm_csv_generator", "Sevierville-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(13, _translate("cucm_csv_generator", "Town-Center-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(14, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        self.tab_1_entry_box_15.setItemText(15, _translate("cucm_csv_generator", "University-Heart-Surgeons-CSS"))
        self.tab_1_entry_box_15.setItemText(16, _translate("cucm_csv_generator", "Wound-Care-HLVI-CSS"))

        self.tab_1_entry_box_17.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_1_entry_box_17.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))
        
        self.tab_1_entry_box_18.setItemText(1, _translate("cucm_csv_generator", "LongDistanceCSS"))
        self.tab_1_entry_box_18.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_19.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_19.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_20.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_1_entry_box_20.setItemText(2, _translate("cucm_csv_generator", "f"))
        
        self.tab_1_entry_box_21.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_21.setItemText(2, _translate("cucm_csv_generator", "International-CSS"))
        self.tab_1_entry_box_21.setItemText(3, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_24.setItemText(1, _translate("cucm_csv_generator", "1"))
        self.tab_1_entry_box_24.setItemText(2, _translate("cucm_csv_generator", "2"))
        self.tab_1_entry_box_24.setItemText(3, _translate("cucm_csv_generator", "3"))
        self.tab_1_entry_box_24.setItemText(4, _translate("cucm_csv_generator", "4"))
        self.tab_1_entry_box_24.setItemText(5, _translate("cucm_csv_generator", "5"))
        self.tab_1_entry_box_24.setItemText(6, _translate("cucm_csv_generator", "6"))

        self.tab_1_entry_box_25.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_1_entry_box_25.setItemText(2, _translate("cucm_csv_generator", "f"))

        self.tab_1_entry_box_28.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_28.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_29.setItemText(1, _translate("cucm_csv_generator", "Call Recording Disabled"))
        self.tab_1_entry_box_29.setItemText(2, _translate("cucm_csv_generator", "Selective Call Recording Enabled"))
        self.tab_1_entry_box_29.setItemText(3, _translate("cucm_csv_generator", "Automatic Call Recording Enabled"))

        self.tab_1_entry_box_30.setItemText(1, _translate("cucm_csv_generator", "Call-Copy-Recorder-Profile"))
        self.tab_1_entry_box_30.setItemText(2, _translate("cucm_csv_generator", "Zoom-CallRec-Recording-Profile"))

        self.tab_1_entry_box_32.setItemText(1, _translate("cucm_csv_generator", "Phone Preferred"))
        self.tab_1_entry_box_32.setItemText(2, _translate("cucm_csv_generator", "Gateway Preferred"))

        self.tab_1_entry_box_34.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_1_entry_box_34.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))
        
        self.tab_1_entry_box_35.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_1_entry_box_35.setItemText(2, _translate("cucm_csv_generator", "f"))

        self.tab_1_entry_box_36.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_36.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        
        self.tab_1_entry_box_37.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_1_entry_box_37.setItemText(2, _translate("cucm_csv_generator", "f"))

        self.tab_1_entry_box_38.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_38.setItemText(2, _translate("cucm_csv_generator", "International-CSS"))
        self.tab_1_entry_box_38.setItemText(3, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_43.setItemText(1, _translate("cucm_csv_generator", "Call Recording Disabled"))
        self.tab_1_entry_box_43.setItemText(2, _translate("cucm_csv_generator", "Selective Call Recording Enabled"))
        self.tab_1_entry_box_43.setItemText(3, _translate("cucm_csv_generator", "Automatic Call Recording Enabled"))

        self.tab_1_entry_box_44.setItemText(1, _translate("cucm_csv_generator", "Call-Copy-Recorder-Profile"))
        self.tab_1_entry_box_44.setItemText(2, _translate("cucm_csv_generator", "Zoom-CallRec-Recording-Profile"))
        self.tab_1_entry_box_44.setItemText(3, _translate("cucm_csv_generator", "New Item"))
        
        self.tab_1_entry_box_45.setItemText(1, _translate("cucm_csv_generator", "Phone Preferred"))
        self.tab_1_entry_box_45.setItemText(2, _translate("cucm_csv_generator", "Gateway Preferred"))

        self.tab_1_entry_box_47.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_1_entry_box_47.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))

        self.tab_1_entry_box_48.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_1_entry_box_48.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))

        self.tab_1_entry_box_49.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_49.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_50.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_1_entry_box_50.setItemText(2, _translate("cucm_csv_generator", "f"))

        self.tab_1_entry_box_51.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_1_entry_box_51.setItemText(2, _translate("cucm_csv_generator", "International-CSS"))
        self.tab_1_entry_box_51.setItemText(3, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))

        self.tab_1_entry_box_56.setItemText(1, _translate("cucm_csv_generator", "Call Recording Disabled"))
        self.tab_1_entry_box_56.setItemText(2, _translate("cucm_csv_generator", "Selective Call Recording Enabled"))
        self.tab_1_entry_box_56.setItemText(3, _translate("cucm_csv_generator", "Automatic Call Recording Enabled"))
        
        self.tab_1_entry_box_57.setItemText(1, _translate("cucm_csv_generator", "Call-Copy-Recorder-Profile"))
        self.tab_1_entry_box_57.setItemText(2, _translate("cucm_csv_generator", "Zoom-CallRec-Recording-Profile"))
        self.tab_1_entry_box_57.setItemText(3, _translate("cucm_csv_generator", "New Item"))

        self.tab_1_entry_box_58.setItemText(1, _translate("cucm_csv_generator", "Phone Preferred"))
        self.tab_1_entry_box_58.setItemText(2, _translate("cucm_csv_generator", "Gateway Preferred"))
        
        self.tab_1_check_box_01.setText(_translate("cucm_csv_generator", "2nd Line Device"))
        self.tab_1_check_box_02.setText(_translate("cucm_csv_generator", "3rd Line Device"))
        self.tab_1_button_01.setText(_translate("cucm_csv_generator", "Clear Fields"))
        self.tab_1_button_02.setText(_translate("cucm_csv_generator", "Add to Queue"))
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_1), _translate("cucm_csv_generator", "Phone (7841)"))

        #--------------------------------------------------------------------------#
        #-                           Tab 2                                        -#
        #--------------------------------------------------------------------------#   
        
        self.tab_2_label_02.setText(_translate("cucm_csv_generator", "Description"))
        self.tab_2_entry_box_01.setToolTip(_translate("cucm_csv_generator", "SEP************"))
        self.tab_2_label_01.setText(_translate("cucm_csv_generator", "Device Name"))
        self.tab_2_label_04.setText(_translate("cucm_csv_generator", "Phone Button Template"))
        self.tab_2_entry_box_04.setItemText(1, _translate("cucm_csv_generator", "Cherokee-8851-Intercom-SIP-Individual Template"))
        self.tab_2_entry_box_04.setItemText(2, _translate("cucm_csv_generator", "Pulm_Crit_Care_MULIT_LINE_8851 SIP"))
        self.tab_2_entry_box_04.setItemText(3, _translate("cucm_csv_generator", "Pulm-Function-Lab-8851-Intercom-SIP-Phone-Template"))
        self.tab_2_entry_box_04.setItemText(4, _translate("cucm_csv_generator", "Standard 8851 SIP"))
        self.tab_2_entry_box_04.setItemText(5, _translate("cucm_csv_generator", "Standard 8851 SIP w/Sidecar and HLog"))
        self.tab_2_entry_box_04.setItemText(6, _translate("cucm_csv_generator", "WCG 8851 SIP w/sidecar"))
        self.tab_2_entry_box_04.setItemText(7, _translate("cucm_csv_generator", "WCG 8851 SIP w/sidecar and logout"))
        self.tab_2_entry_box_04.setItemText(8, _translate("cucm_csv_generator", "8851 SIP 4L +1 Intercom + Expansion 36 BLF SD"))
        self.tab_2_entry_box_04.setItemText(9, _translate("cucm_csv_generator", "8851 SIP 4L w Log-Out/Expansion 36 SD and BLF/SD"))
        self.tab_2_entry_box_04.setItemText(10, _translate("cucm_csv_generator", "8851 SIP 6L + Expansion 35 BLF SD"))
        self.tab_2_entry_box_04.setItemText(11, _translate("cucm_csv_generator", "8851 SIP 10L w Expansion 36 + Int"))
        self.tab_2_entry_box_03.setItemText(1, _translate("cucm_csv_generator", "Alcoa-Infusion-DP"))
        self.tab_2_entry_box_03.setItemText(2, _translate("cucm_csv_generator", "Cardio-Diagnostics-DP"))
        self.tab_2_entry_box_03.setItemText(3, _translate("cucm_csv_generator", "Cherokee-Farms-DP"))
        self.tab_2_entry_box_03.setItemText(4, _translate("cucm_csv_generator", "Lenoir-City-DP"))
        self.tab_2_entry_box_03.setItemText(5, _translate("cucm_csv_generator", "PoB-DP1"))
        self.tab_2_entry_box_03.setItemText(6, _translate("cucm_csv_generator", "Pulm-Critical-Care-DP"))
        self.tab_2_entry_box_03.setItemText(7, _translate("cucm_csv_generator", "Pulm-Function-DP"))
        self.tab_2_entry_box_03.setItemText(8, _translate("cucm_csv_generator", "Sevierville-DP"))
        self.tab_2_entry_box_03.setItemText(9, _translate("cucm_csv_generator", "Seymour-FP-DP"))
        self.tab_2_entry_box_03.setItemText(10, _translate("cucm_csv_generator", "Town-Center-DP"))
        self.tab_2_entry_box_03.setItemText(11, _translate("cucm_csv_generator", "Turkey-Creek-DP"))
        self.tab_2_entry_box_03.setItemText(12, _translate("cucm_csv_generator", "Univ-Cardio-DP"))
        self.tab_2_entry_box_03.setItemText(13, _translate("cucm_csv_generator", "University-Heart-Surgeons-DP"))
        self.tab_2_entry_box_03.setItemText(14, _translate("cucm_csv_generator", "Wound-Care-HLVI-DP"))
        self.tab_2_label_03.setText(_translate("cucm_csv_generator", "Device Pool"))
        self.tab_2_entry_box_05.setItemText(1, _translate("cucm_csv_generator", "Alcoa-Infusion-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(2, _translate("cucm_csv_generator", "Cardio-Diagnostics-CSS"))
        self.tab_2_entry_box_05.setItemText(3, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(4, _translate("cucm_csv_generator", "Lenoir-City-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(5, _translate("cucm_csv_generator", "PoB-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(6, _translate("cucm_csv_generator", "Pulm-Critical-Care-CSS"))
        self.tab_2_entry_box_05.setItemText(7, _translate("cucm_csv_generator", "Pulm-Function-CSS"))
        self.tab_2_entry_box_05.setItemText(8, _translate("cucm_csv_generator", "Sevierville-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(9, _translate("cucm_csv_generator", "Seymour-FP-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(10, _translate("cucm_csv_generator", "Town-Center-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(11, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        self.tab_2_entry_box_05.setItemText(12, _translate("cucm_csv_generator", "University-Heart-Surgeons-CSS"))
        self.tab_2_entry_box_05.setItemText(13, _translate("cucm_csv_generator", "Wound-Care-HLVI-CSS"))
        self.tab_2_label_05.setText(_translate("cucm_csv_generator", "CSS"))
        self.tab_2_label_06.setText(_translate("cucm_csv_generator", "Location"))
        self.tab_2_entry_box_06.setItemText(1, _translate("cucm_csv_generator", "Alcoa-Infusion-LOC"))
        self.tab_2_entry_box_06.setItemText(2, _translate("cucm_csv_generator", "Lenoir-City-LOC"))
        self.tab_2_entry_box_06.setItemText(3, _translate("cucm_csv_generator", "POB-LOC"))
        self.tab_2_entry_box_06.setItemText(4, _translate("cucm_csv_generator", "Sevierville-LOC"))
        self.tab_2_entry_box_06.setItemText(5, _translate("cucm_csv_generator", "Seymour-FP-LOC"))
        self.tab_2_entry_box_06.setItemText(6, _translate("cucm_csv_generator", "Town-Center-LOC"))
        self.tab_2_label_07.setText(_translate("cucm_csv_generator", "Media Resource Group List"))
        self.tab_2_entry_box_07.setItemText(1, _translate("cucm_csv_generator", "Lenoir-MRGL"))
        self.tab_2_entry_box_07.setItemText(2, _translate("cucm_csv_generator", "POB-MRGL1"))
        self.tab_2_entry_box_07.setItemText(3, _translate("cucm_csv_generator", "POB-MRGL2"))
        self.tab_2_entry_box_07.setItemText(4, _translate("cucm_csv_generator", "Sevierville-MGRL"))
        self.tab_2_label_08.setText(_translate("cucm_csv_generator", "Module 1"))
        self.tab_2_entry_box_08.setItemText(1, _translate("cucm_csv_generator", "BEKEM 36-Button Line Expansion Module"))
        self.tab_2_entry_box_08.setItemText(2, _translate("cucm_csv_generator", "CP-8800-Audio 28-Button Key Expansion Module"))
        self.tab_2_label_09.setText(_translate("cucm_csv_generator", "User ID 1"))
        self.tab_2_label_10.setText(_translate("cucm_csv_generator", "Device Subscribe CSS"))
        self.tab_2_entry_box_10.setItemText(1, _translate("cucm_csv_generator", "PoB-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(2, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(3, _translate("cucm_csv_generator", "Lenoir-City-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(4, _translate("cucm_csv_generator", "Town-Center-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(5, _translate("cucm_csv_generator", "Alcoa-Infusion-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(6, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(7, _translate("cucm_csv_generator", "Sevierville-Device-CSS"))
        self.tab_2_entry_box_10.setItemText(8, _translate("cucm_csv_generator", "Pulm-Critical-Care-CSS"))
        self.tab_2_entry_box_10.setItemText(9, _translate("cucm_csv_generator", "Wound-Care-HLVI-CSS"))
        self.tab_2_entry_box_10.setItemText(10, _translate("cucm_csv_generator", "University-Heart-Surgeons-CSS"))
        self.tab_2_entry_box_10.setItemText(11, _translate("cucm_csv_generator", "Cardio-Diagnostics-CSS"))
        self.tab_2_entry_box_10.setItemText(12, _translate("cucm_csv_generator", "Pulm-Function-CSS"))
        self.tab_2_entry_box_11.setItemText(1, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_2_entry_box_11.setItemText(2, _translate("cucm_csv_generator", "PoB-Device-CSS"))
        self.tab_2_entry_box_11.setItemText(3, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_2_entry_box_11.setItemText(4, _translate("cucm_csv_generator", "Lenoir-City-Device-CSS"))
        self.tab_2_entry_box_11.setItemText(5, _translate("cucm_csv_generator", "Town-Center-Device-CSS"))
        self.tab_2_entry_box_11.setItemText(6, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        self.tab_2_entry_box_11.setItemText(7, _translate("cucm_csv_generator", "Pulm-Critical-Care-CSS"))
        self.tab_2_entry_box_11.setItemText(8, _translate("cucm_csv_generator", "Wound-Care-HLVI-CSS"))
        self.tab_2_entry_box_11.setItemText(9, _translate("cucm_csv_generator", "University-Heart-Surgeons-CSS"))
        self.tab_2_entry_box_11.setItemText(10, _translate("cucm_csv_generator", "Cardio-Diagnostics-CSS"))
        self.tab_2_entry_box_11.setItemText(11, _translate("cucm_csv_generator", "Pulm-Function-CSS"))
        self.tab_2_label_11.setText(_translate("cucm_csv_generator", "CSS Reroute"))
        self.tab_2_label_12.setText(_translate("cucm_csv_generator", "Directory Number 1"))
        self.tab_2_label_13.setText(_translate("cucm_csv_generator", "Voice Mail Profile 1"))
        self.tab_2_entry_box_13.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_2_entry_box_13.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))
        self.tab_2_label_14.setText(_translate("cucm_csv_generator", "Foward All CSS 1"))
        self.tab_2_entry_box_14.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_14.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_entry_box_15.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_2_entry_box_15.setItemText(2, _translate("cucm_csv_generator", "f"))
        self.tab_2_label_15.setText(_translate("cucm_csv_generator", "Foward Voice Mail 1"))
        self.tab_2_label_16.setText(_translate("cucm_csv_generator", "Foward Busy External CSS 1"))
        self.tab_2_entry_box_16.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_16.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_label_17.setText(_translate("cucm_csv_generator", "Line Text Label 1"))
        self.tab_2_label_18.setText(_translate("cucm_csv_generator", "External Phone Number Mask 1"))
        self.tab_2_label_19.setText(_translate("cucm_csv_generator", "Maximum Number of Calls 1"))
        self.tab_2_entry_box_19.setItemText(1, _translate("cucm_csv_generator", "1"))
        self.tab_2_entry_box_19.setItemText(2, _translate("cucm_csv_generator", "2"))
        self.tab_2_entry_box_19.setItemText(3, _translate("cucm_csv_generator", "3"))
        self.tab_2_entry_box_19.setItemText(4, _translate("cucm_csv_generator", "4"))
        self.tab_2_entry_box_19.setItemText(5, _translate("cucm_csv_generator", "5"))
        self.tab_2_entry_box_19.setItemText(6, _translate("cucm_csv_generator", "6"))
        self.tab_2_entry_box_19.setItemText(7, _translate("cucm_csv_generator", "7"))
        self.tab_2_entry_box_19.setItemText(8, _translate("cucm_csv_generator", "8"))
        self.tab_2_entry_box_19.setItemText(9, _translate("cucm_csv_generator", "9"))
        self.tab_2_entry_box_19.setItemText(10, _translate("cucm_csv_generator", "10"))
        self.tab_2_label_20.setText(_translate("cucm_csv_generator", "Secondary CSS for Forward All 1"))
        self.tab_2_entry_box_20.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_20.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_check_box_02.setText(_translate("cucm_csv_generator", "3rd Line Device"))
        self.tab_2_button_02.setText(_translate("cucm_csv_generator", "Add to Queue"))
        self.tab_2_check_box_01.setText(_translate("cucm_csv_generator", "2nd Line Device"))
        self.tab_2_button_01.setText(_translate("cucm_csv_generator", "Clear Fields"))
        self.tab_2_label_21.setText(_translate("cucm_csv_generator", "URI 1 on Directory Number 1"))
        self.tab_2_label_30.setText(_translate("cucm_csv_generator", "Secondary CSS for Forward All 2"))
        self.tab_2_entry_box_30.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_30.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_label_24.setText(_translate("cucm_csv_generator", "Foward All CSS 2"))
        self.tab_2_entry_box_26.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_26.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_entry_box_24.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_24.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_label_22.setText(_translate("cucm_csv_generator", "Directory Number 2"))
        self.tab_2_label_27.setText(_translate("cucm_csv_generator", "Line Text Label 2"))
        self.tab_2_entry_box_25.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_2_entry_box_25.setItemText(2, _translate("cucm_csv_generator", "f"))
        self.tab_2_label_23.setText(_translate("cucm_csv_generator", "Voice Mail Profile 2"))
        self.tab_2_label_26.setText(_translate("cucm_csv_generator", "Foward Busy External CSS 2"))
        self.tab_2_label_28.setText(_translate("cucm_csv_generator", "External Phone Number Mask 2"))
        self.tab_2_label_25.setText(_translate("cucm_csv_generator", "Foward Voice Mail 2"))
        self.tab_2_label_29.setText(_translate("cucm_csv_generator", "Maximum Number of Calls 2"))
        self.tab_2_entry_box_29.setItemText(1, _translate("cucm_csv_generator", "1"))
        self.tab_2_entry_box_29.setItemText(2, _translate("cucm_csv_generator", "2"))
        self.tab_2_entry_box_29.setItemText(3, _translate("cucm_csv_generator", "3"))
        self.tab_2_entry_box_29.setItemText(4, _translate("cucm_csv_generator", "4"))
        self.tab_2_entry_box_29.setItemText(5, _translate("cucm_csv_generator", "5"))
        self.tab_2_entry_box_29.setItemText(6, _translate("cucm_csv_generator", "6"))
        self.tab_2_entry_box_29.setItemText(7, _translate("cucm_csv_generator", "7"))
        self.tab_2_entry_box_29.setItemText(8, _translate("cucm_csv_generator", "8"))
        self.tab_2_entry_box_29.setItemText(9, _translate("cucm_csv_generator", "9"))
        self.tab_2_entry_box_29.setItemText(10, _translate("cucm_csv_generator", "10"))
        self.tab_2_entry_box_23.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_2_entry_box_23.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))
        self.tab_2_label_31.setText(_translate("cucm_csv_generator", "URI 1 on Directory Number 2"))
        self.tab_2_entry_box_34.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_34.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_label_38.setText(_translate("cucm_csv_generator", "External Phone Number Mask 3"))
        self.tab_2_entry_box_33.setItemText(1, _translate("cucm_csv_generator", "Unity-Connection-VMP"))
        self.tab_2_entry_box_33.setItemText(2, _translate("cucm_csv_generator", "NoVoiceMail"))
        self.tab_2_label_40.setText(_translate("cucm_csv_generator", "Secondary CSS for Forward All 3"))
        self.tab_2_label_33.setText(_translate("cucm_csv_generator", "Voice Mail Profile 3"))
        self.tab_2_label_34.setText(_translate("cucm_csv_generator", "Foward All CSS 3"))
        self.tab_2_entry_box_39.setItemText(1, _translate("cucm_csv_generator", "1"))
        self.tab_2_entry_box_39.setItemText(2, _translate("cucm_csv_generator", "2"))
        self.tab_2_entry_box_39.setItemText(3, _translate("cucm_csv_generator", "3"))
        self.tab_2_entry_box_39.setItemText(4, _translate("cucm_csv_generator", "4"))
        self.tab_2_entry_box_39.setItemText(5, _translate("cucm_csv_generator", "5"))
        self.tab_2_entry_box_39.setItemText(6, _translate("cucm_csv_generator", "6"))
        self.tab_2_entry_box_39.setItemText(7, _translate("cucm_csv_generator", "7"))
        self.tab_2_entry_box_39.setItemText(8, _translate("cucm_csv_generator", "8"))
        self.tab_2_entry_box_39.setItemText(9, _translate("cucm_csv_generator", "9"))
        self.tab_2_entry_box_39.setItemText(10, _translate("cucm_csv_generator", "10"))
        self.tab_2_label_39.setText(_translate("cucm_csv_generator", "Maximum Number of Calls 3"))
        self.tab_2_label_35.setText(_translate("cucm_csv_generator", "Foward Voice Mail 3"))
        self.tab_2_label_32.setText(_translate("cucm_csv_generator", "Directory Number 3"))
        self.tab_2_label_37.setText(_translate("cucm_csv_generator", "Line Text Label 3"))
        self.tab_2_entry_box_35.setItemText(1, _translate("cucm_csv_generator", "t"))
        self.tab_2_entry_box_35.setItemText(2, _translate("cucm_csv_generator", "f"))
        self.tab_2_label_41.setText(_translate("cucm_csv_generator", "URI 1 on Directory Number 3"))
        self.tab_2_label_36.setText(_translate("cucm_csv_generator", "Foward Busy External CSS 3"))
        self.tab_2_entry_box_40.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_40.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_2_entry_box_36.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_2_entry_box_36.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_2), _translate("cucm_csv_generator", "Phone (8851)"))

        #--------------------------------------------------------------------------#
        #-                           Tab 3                                        -#
        #--------------------------------------------------------------------------#    
         
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_3), _translate("cucm_csv_generator", "Phone (New Model)"))

        #--------------------------------------------------------------------------#
        #-                           Tab 4                                        -#
        #--------------------------------------------------------------------------#   
         
        self.tab_4_label_01.setText(_translate("cucm_csv_generator", "Device Name"))
        self.tab_4_label_02.setText(_translate("cucm_csv_generator", "Description"))
        self.tab_4_label_03.setText(_translate("cucm_csv_generator", "Device Pool"))
        self.tab_4_label_04.setText(_translate("cucm_csv_generator", "CSS"))
        self.tab_4_label_05.setText(_translate("cucm_csv_generator", "Location"))
        self.tab_4_label_06.setText(_translate("cucm_csv_generator", "Media Resource Group"))
        self.tab_4_label_07.setText(_translate("cucm_csv_generator", "Built in Bridge"))
        self.tab_4_label_08.setText(_translate("cucm_csv_generator", "User Name 1"))
        self.tab_4_label_09.setText(_translate("cucm_csv_generator", "Device Subscribe CSS"))
        self.tab_4_label_10.setText(_translate("cucm_csv_generator", "CSS Reroute"))
        self.tab_4_label_11.setText(_translate("cucm_csv_generator", "Device Mobility Mode"))
        self.tab_4_label_12.setText(_translate("cucm_csv_generator", "Directory Number 1"))
        self.tab_4_label_13.setText(_translate("cucm_csv_generator", "Line CSS 1"))
        self.tab_4_label_14.setText(_translate("cucm_csv_generator", "Foward All CSS 1"))
        self.tab_4_label_15.setText(_translate("cucm_csv_generator", "External Mask"))
        self.tab_4_label_16.setText(_translate("cucm_csv_generator", "Recording Option 1"))
        self.tab_4_label_17.setText(_translate("cucm_csv_generator", "Recording Profile 1"))
        self.tab_4_label_18.setText(_translate("cucm_csv_generator", "URI on Directory Number 1"))
        self.tab_4_label_19.setText(_translate("cucm_csv_generator", "Directory Number 2"))
        self.tab_4_label_20.setText(_translate("cucm_csv_generator", "Line CSS 2"))
        self.tab_4_label_21.setText(_translate("cucm_csv_generator", "Foward All CSS 2"))
        self.tab_4_label_22.setText(_translate("cucm_csv_generator", "Line Text Label 2"))
        self.tab_4_label_23.setText(_translate("cucm_csv_generator", "External Phone Number Mask 2"))
        self.tab_4_label_24.setText(_translate("cucm_csv_generator", "Line Description 2"))  
        self.tab_4_label_25.setText(_translate("cucm_csv_generator", "Directory Number 3"))
        self.tab_4_label_26.setText(_translate("cucm_csv_generator", "Line CSS 3"))
        self.tab_4_label_27.setText(_translate("cucm_csv_generator", "Foward All CSS 3"))
        self.tab_4_label_28.setText(_translate("cucm_csv_generator", "Line Text Label 3"))
        self.tab_4_label_29.setText(_translate("cucm_csv_generator", "External Phone Number Mask 3"))
        self.tab_4_label_30.setText(_translate("cucm_csv_generator", "Line Description 3"))        

        self.tab_4_entry_box_03.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-DP"))
        self.tab_4_entry_box_03.setItemText(2, _translate("cucm_csv_generator", "Cherokee-Farms-DP"))
        self.tab_4_entry_box_03.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-DP"))
        self.tab_4_entry_box_03.setItemText(4, _translate("cucm_csv_generator", "Cedar-Bluff-UHN-UPA-DP"))
        self.tab_4_entry_box_03.setItemText(5, _translate("cucm_csv_generator", "Specialty-Pharmacy-DP"))
        self.tab_4_entry_box_03.setItemText(6, _translate("cucm_csv_generator", "Univ-Cardio-DP"))
        
        self.tab_4_entry_box_04.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_4_entry_box_04.setItemText(2, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_4_entry_box_04.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-Device-CSS"))
        self.tab_4_entry_box_04.setItemText(4, _translate("cucm_csv_generator", "Specialty-Pharmacy-Device-CSS"))
        self.tab_4_entry_box_04.setItemText(5, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))
        
        self.tab_4_entry_box_05.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-LOC"))
        self.tab_4_entry_box_05.setItemText(2, _translate("cucm_csv_generator", "POB-LOC"))
        
        self.tab_4_entry_box_06.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-MRGL"))
        self.tab_4_entry_box_06.setItemText(2, _translate("cucm_csv_generator", "POB-MRGL1"))
        self.tab_4_entry_box_06.setItemText(3, _translate("cucm_csv_generator", "POB-MRGL2"))
        
        self.tab_4_entry_box_07.setItemText(1, _translate("cucm_csv_generator", "Default"))
        self.tab_4_entry_box_07.setItemText(2, _translate("cucm_csv_generator", "On"))        
        
        self.tab_4_entry_box_09.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_4_entry_box_09.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-Device-CSS"))
        self.tab_4_entry_box_09.setItemText(3, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_4_entry_box_09.setItemText(4, _translate("cucm_csv_generator", "Specialty-Pharmacy-Device-CSS"))
        self.tab_4_entry_box_09.setItemText(5, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))        
        
        self.tab_4_entry_box_10.setItemText(1, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_4_entry_box_10.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-Device-CSS"))
        self.tab_4_entry_box_10.setItemText(3, _translate("cucm_csv_generator", "Cherokee-Farm-Device-CSS"))
        self.tab_4_entry_box_10.setItemText(4, _translate("cucm_csv_generator", "Specialty-Pharmacy-Device-CSS"))
        self.tab_4_entry_box_10.setItemText(5, _translate("cucm_csv_generator", "Univ-Cardio-Device-CSS"))     
        
        self.tab_4_entry_box_11.setItemText(1, _translate("cucm_csv_generator", "Default"))
        self.tab_4_entry_box_11.setItemText(2, _translate("cucm_csv_generator", "On"))
        
        self.tab_4_entry_box_13.setItemText(1, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_4_entry_box_13.setItemText(2, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_4_entry_box_13.setItemText(3, _translate("cucm_csv_generator", "International-CSS"))
        
        self.tab_4_entry_box_14.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_4_entry_box_14.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        
        self.tab_4_entry_box_16.setItemText(1, _translate("cucm_csv_generator", "Call Recording Disabled"))
        self.tab_4_entry_box_16.setItemText(2, _translate("cucm_csv_generator", "Automatic Call Recording Enabled"))
        
        self.tab_4_entry_box_17.setItemText(1, _translate("cucm_csv_generator", "Call-Copy-Recorder-Profile"))
        
        self.tab_4_entry_box_20.setItemText(1, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_4_entry_box_20.setItemText(2, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_4_entry_box_20.setItemText(3, _translate("cucm_csv_generator", "International-CSS"))
        
        self.tab_4_entry_box_21.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_4_entry_box_21.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        
        self.tab_4_entry_box_26.setItemText(1, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_4_entry_box_26.setItemText(2, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_4_entry_box_26.setItemText(3, _translate("cucm_csv_generator", "International-CSS"))
        
        self.tab_4_entry_box_27.setItemText(1, _translate("cucm_csv_generator", "Local-LineFWD-CSS"))
        self.tab_4_entry_box_27.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        
        self.tab_4_check_box_01.setText(_translate("cucm_csv_generator", "2nd Line Device"))
        self.tab_4_check_box_02.setText(_translate("cucm_csv_generator", "3rd Line Device"))
        self.tab_4_button_02.setText(_translate("cucm_csv_generator", "Add to Queue"))
        self.tab_4_button_01.setText(_translate("cucm_csv_generator", "Clear Fields"))
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_4), _translate("cucm_csv_generator", "PC/Mac"))

        #--------------------------------------------------------------------------#
        #-                           Tab 5                                        -#
        #--------------------------------------------------------------------------#   
         
        self.tab_5_label_02.setText(_translate("cucm_csv_generator", "Description"))
        self.tab_5_entry_box_03.setItemText(1, _translate("cucm_csv_generator", "Cherokee-Farms-DP"))
        self.tab_5_entry_box_03.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-DP"))
        self.tab_5_entry_box_01.setToolTip(_translate("cucm_csv_generator", "SEP************"))
        self.tab_5_label_01.setText(_translate("cucm_csv_generator", "Device Name"))
        self.tab_5_label_03.setText(_translate("cucm_csv_generator", "Device Pool"))
        self.tab_5_entry_box_04.setItemText(1, _translate("cucm_csv_generator", "Cherokee-Farms-Device-CSS"))
        self.tab_5_entry_box_04.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_5_label_04.setText(_translate("cucm_csv_generator", "CSS"))
        self.tab_5_label_06.setText(_translate("cucm_csv_generator", "User ID 2"))
        self.tab_5_label_05.setText(_translate("cucm_csv_generator", "User ID 1"))
        self.tab_5_entry_box_05.setToolTip(_translate("cucm_csv_generator", "SEP************"))
        self.tab_5_label_07.setText(_translate("cucm_csv_generator", "Owner User ID"))
        self.tab_5_label_08.setText(_translate("cucm_csv_generator", "Directory Number 1"))
        self.tab_5_entry_box_09.setItemText(1, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_5_entry_box_09.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_5_label_09.setText(_translate("cucm_csv_generator", "Line CSS 1"))
        self.tab_5_label_10.setText(_translate("cucm_csv_generator", "External Phone Number Mask 1"))
        self.tab_5_label_11.setText(_translate("cucm_csv_generator", "Line Description 1"))
        self.tab_5_label_12.setText(_translate("cucm_csv_generator", "Display 1"))
        self.tab_5_button_02.setText(_translate("cucm_csv_generator", "Add to Queue"))
        self.tab_5_button_01.setText(_translate("cucm_csv_generator", "Clear Fields"))
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_5), _translate("cucm_csv_generator", "Jabber (Android)"))

        #--------------------------------------------------------------------------#
        #-                           Tab 6                                        -#
        #--------------------------------------------------------------------------#  
         
        self.tab_6_entry_box_03.setItemText(1, _translate("cucm_csv_generator", "Cherokee-Farms-DP"))
        self.tab_6_entry_box_03.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-DP"))
        self.tab_6_entry_box_03.setItemText(3, _translate("cucm_csv_generator", "Cedar-Bluff-UHS-DP"))
        
        self.tab_6_entry_box_04.setItemText(1, _translate("cucm_csv_generator", "Standard Dual Mode for iPhone"))
        self.tab_6_entry_box_04.setItemText(2, _translate("cucm_csv_generator", "TCTRFUGATE-SIP-Individual Template"))
        
        self.tab_6_entry_box_05.setItemText(1, _translate("cucm_csv_generator", "Cherokee-Farms-Device-CSS"))
        self.tab_6_entry_box_05.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        
        self.tab_6_entry_box_10.setItemText(1, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_6_entry_box_10.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        
        self.tab_6_label_01.setText(_translate("cucm_csv_generator", "Device Name"))
        self.tab_6_label_02.setText(_translate("cucm_csv_generator", "Description"))
        self.tab_6_label_03.setText(_translate("cucm_csv_generator", "Device Pool"))
        self.tab_6_label_04.setText(_translate("cucm_csv_generator", "Phone Button Template"))
        self.tab_6_label_05.setText(_translate("cucm_csv_generator", "CSS"))
        self.tab_6_label_06.setText(_translate("cucm_csv_generator", "User ID 1"))
        self.tab_6_label_07.setText(_translate("cucm_csv_generator", "User ID 2"))
        self.tab_6_label_08.setText(_translate("cucm_csv_generator", "Owner User ID"))
        self.tab_6_label_09.setText(_translate("cucm_csv_generator", "Directory Number 1"))
        self.tab_6_label_10.setText(_translate("cucm_csv_generator", "Line CSS 1"))
        self.tab_6_label_11.setText(_translate("cucm_csv_generator", "External Phone Number Mask 1"))
        self.tab_6_label_12.setText(_translate("cucm_csv_generator", "Line Description 1"))
        self.tab_6_label_13.setText(_translate("cucm_csv_generator", "Display 1"))
        
        self.tab_6_button_01.setText(_translate("cucm_csv_generator", "Clear Fields"))
        self.tab_6_button_02.setText(_translate("cucm_csv_generator", "Add to Queue"))
        
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_6), _translate("cucm_csv_generator", "Jabber (iPhone)"))

        #--------------------------------------------------------------------------#
        #-                           Tab 7                                        -#
        #--------------------------------------------------------------------------# 
         
        self.tab_7_entry_box_09.setItemText(1, _translate("cucm_csv_generator", "LongDistance-CSS"))
        self.tab_7_entry_box_09.setItemText(2, _translate("cucm_csv_generator", "LongDistance-LineFWD-CSS"))
        self.tab_7_label_08.setText(_translate("cucm_csv_generator", "Directory Number 1"))
        self.tab_7_entry_box_04.setItemText(1, _translate("cucm_csv_generator", "Cherokee-Farms-Device-CSS"))
        self.tab_7_entry_box_04.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-Device-CSS"))
        self.tab_7_entry_box_03.setItemText(1, _translate("cucm_csv_generator", "Cherokee-Farms-DP"))
        self.tab_7_entry_box_03.setItemText(2, _translate("cucm_csv_generator", "Cedar-Bluff-UPA-DP"))
        self.tab_7_entry_box_05.setToolTip(_translate("cucm_csv_generator", "SEP************"))
        self.tab_7_label_05.setText(_translate("cucm_csv_generator", "User ID 1"))
        self.tab_7_entry_box_01.setToolTip(_translate("cucm_csv_generator", "SEP************"))
        self.tab_7_label_06.setText(_translate("cucm_csv_generator", "User ID 2"))
        self.tab_7_label_11.setText(_translate("cucm_csv_generator", "Line Description 1"))
        self.tab_7_label_10.setText(_translate("cucm_csv_generator", "External Phone Number Mask 1"))
        self.tab_7_button_01.setText(_translate("cucm_csv_generator", "Clear Fields"))
        self.tab_7_label_03.setText(_translate("cucm_csv_generator", "Device Pool"))
        self.tab_7_label_01.setText(_translate("cucm_csv_generator", "Device Name"))
        self.tab_7_label_09.setText(_translate("cucm_csv_generator", "Line CSS 1"))
        self.tab_7_label_07.setText(_translate("cucm_csv_generator", "Owner User ID"))
        self.tab_7_label_04.setText(_translate("cucm_csv_generator", "CSS"))
        self.tab_7_button_02.setText(_translate("cucm_csv_generator", "Add to Queue"))
        self.tab_7_label_12.setText(_translate("cucm_csv_generator", "Display 1"))
        self.tab_7_label_02.setText(_translate("cucm_csv_generator", "Description"))
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_7), _translate("cucm_csv_generator", "Jabber (iPad)"))

        #--------------------------------------------------------------------------#
        #-                           Tab 8                                        -#
        #--------------------------------------------------------------------------#    
         
        __sortingEnabled = self.tab_8_list_box_01.isSortingEnabled()
        self.tab_8_list_box_01.setSortingEnabled(False)
        self.tab_8_list_box_01.setSortingEnabled(__sortingEnabled)
        self.tab_8_button_01.setText(_translate("cucm_csv_generator", "Clear Entries"))
        self.tab_8_button_01.clicked.connect(lambda:self.tab_8_function_clear_fields())
        self.tab_8_button_02.setText(_translate("cucm_csv_generator", "Generate CSV"))
        self.tab_8_button_02.clicked.connect(lambda:self.tab_8_function_choose_template_to_generate())
        self.tab_8_button_03.setText(_translate("cucm_csv_generator", "Download Update"))
        self.tab_8_button_03.clicked.connect(lambda:self.tab_8_function_download_update())
        self.tab_8_label_01.setText(_translate("cucm_csv_generator", " v1.3.1"))
        self.all_tabs.setTabText(self.all_tabs.indexOf(self.tab_8), _translate("cucm_csv_generator", "Current Queue"))

    #--------------------------------------------------------------------------#
    #--------------------------------------------------------------------------#
    #-                              Functions                                 -#
    #--------------------------------------------------------------------------#   
    #--------------------------------------------------------------------------#
    def check_template(self, prefix):
        string_to_check = (self.tab_8_list_box_01.item(0).text().split("="))[0]
        if string_to_check.startswith(prefix):
            return True
        else:
            return False

    def threaded_wait_time(self):
        time.sleep(.1)
        item = self.tab_8_list_box_01.item(0)
        item.setText("")


    #--------------------------------------------------------------------------#
    #-                                 Tab 1                                  -#
    #--------------------------------------------------------------------------#
    
    def tab_1_function_hide_line_2(self):
        if self.tab_1_check_box_01.checkState() == 2:
            for number in range(33,46):
                ref_entry = getattr(self, f"tab_1_entry_box_{number}")
                ref_label = getattr(self, f"tab_1_label_{number}")
                ref_entry.setHidden(False)
                ref_label.setHidden(False)
        if self.tab_1_check_box_01.checkState() == 0:
            for number in range(33,46):
                ref_entry = getattr(self, f"tab_1_entry_box_{number}")
                ref_label = getattr(self, f"tab_1_label_{number}")
                ref_entry.setHidden(True)
                ref_label.setHidden(True)

    def tab_1_function_hide_line_3(self):
        if self.tab_1_check_box_02.checkState() == 2:
            for number in range(46,59):
                ref_entry = getattr(self, f"tab_1_entry_box_{number}")
                ref_label = getattr(self, f"tab_1_label_{number}")
                ref_entry.setHidden(False)
                ref_label.setHidden(False)
        if self.tab_1_check_box_02.checkState() == 0:
            for number in range(46,59):
                ref_entry = getattr(self, f"tab_1_entry_box_{number}")
                ref_label = getattr(self, f"tab_1_label_{number}")
                ref_entry.setHidden(True)
                ref_label.setHidden(True)

    def tab_1_function_clear_fields(self):
        all_fields = [self.tab_1_entry_box_01, self.tab_1_entry_box_02, self.tab_1_entry_box_03,
        self.tab_1_entry_box_04, self.tab_1_entry_box_05, self.tab_1_entry_box_06,
        self.tab_1_entry_box_07, self.tab_1_entry_box_08, self.tab_1_entry_box_09,
        self.tab_1_entry_box_10, self.tab_1_entry_box_11, self.tab_1_entry_box_12,
        self.tab_1_entry_box_13, self.tab_1_entry_box_14, self.tab_1_entry_box_15,
        self.tab_1_entry_box_16, self.tab_1_entry_box_17, self.tab_1_entry_box_18,
        self.tab_1_entry_box_19, self.tab_1_entry_box_20, self.tab_1_entry_box_21,
        self.tab_1_entry_box_22, self.tab_1_entry_box_23, self.tab_1_entry_box_24,
        self.tab_1_entry_box_25, self.tab_1_entry_box_26, self.tab_1_entry_box_27,
        self.tab_1_entry_box_28, self.tab_1_entry_box_29, self.tab_1_entry_box_30,
        self.tab_1_entry_box_31, self.tab_1_entry_box_32, self.tab_1_entry_box_33,
        self.tab_1_entry_box_34, self.tab_1_entry_box_35, self.tab_1_entry_box_36,
        self.tab_1_entry_box_37, self.tab_1_entry_box_38, self.tab_1_entry_box_39,
        self.tab_1_entry_box_40, self.tab_1_entry_box_41, self.tab_1_entry_box_42,
        self.tab_1_entry_box_43, self.tab_1_entry_box_44, self.tab_1_entry_box_45,
        self.tab_1_entry_box_46, self.tab_1_entry_box_47, self.tab_1_entry_box_48,
        self.tab_1_entry_box_49, self.tab_1_entry_box_50, self.tab_1_entry_box_51,
        self.tab_1_entry_box_52, self.tab_1_entry_box_53, self.tab_1_entry_box_54,
        self.tab_1_entry_box_55, self.tab_1_entry_box_56, self.tab_1_entry_box_57,
        self.tab_1_entry_box_58]
        for each in all_fields:
            try:
                each.setPlainText("")
            except: 
                each.setCurrentIndex(0)

    def tab_1_function_add_to_queue(self):
        string_to_add = f"{self.tab_1_entry_box_01.toPlainText()}={self.tab_1_entry_box_02.toPlainText()}={self.tab_1_entry_box_03.currentText()}={self.tab_1_entry_box_04.currentText()}={self.tab_1_entry_box_05.currentText()}={self.tab_1_entry_box_06.currentText()}={self.tab_1_entry_box_07.currentText()}={self.tab_1_entry_box_08.currentText()}={self.tab_1_entry_box_09.currentText()}={self.tab_1_entry_box_10.currentText()}={self.tab_1_entry_box_11.toPlainText()}={self.tab_1_entry_box_12.currentText()}={self.tab_1_entry_box_13.toPlainText()}={self.tab_1_entry_box_14.currentText()}={self.tab_1_entry_box_15.currentText()}={self.tab_1_entry_box_16.toPlainText()}={self.tab_1_entry_box_17.currentText()}={self.tab_1_entry_box_18.currentText()}={self.tab_1_entry_box_19.currentText()}={self.tab_1_entry_box_20.currentText()}={self.tab_1_entry_box_21.currentText()}={self.tab_1_entry_box_22.toPlainText()}={self.tab_1_entry_box_23.toPlainText()}={self.tab_1_entry_box_24.currentText()}={self.tab_1_entry_box_25.currentText()}={self.tab_1_entry_box_26.toPlainText()}={self.tab_1_entry_box_27.toPlainText()}={self.tab_1_entry_box_28.currentText()}={self.tab_1_entry_box_29.currentText()}={self.tab_1_entry_box_30.currentText()}={self.tab_1_entry_box_31.toPlainText()}={self.tab_1_entry_box_32.currentText()}={self.tab_1_entry_box_33.toPlainText()}={self.tab_1_entry_box_34.currentText()}={self.tab_1_entry_box_35.currentText()}={self.tab_1_entry_box_36.currentText()}={self.tab_1_entry_box_37.currentText()}={self.tab_1_entry_box_38.currentText()}={self.tab_1_entry_box_39.toPlainText()}={self.tab_1_entry_box_40.toPlainText()}={self.tab_1_entry_box_41.toPlainText()}={self.tab_1_entry_box_42.toPlainText()}={self.tab_1_entry_box_43.currentText()}={self.tab_1_entry_box_44.currentText()}={self.tab_1_entry_box_45.currentText()}={self.tab_1_entry_box_46.toPlainText()}={self.tab_1_entry_box_47.currentText()}={self.tab_1_entry_box_48.currentText()}={self.tab_1_entry_box_49.currentText()}={self.tab_1_entry_box_50.currentText()}={self.tab_1_entry_box_51.currentText()}={self.tab_1_entry_box_52.toPlainText()}={self.tab_1_entry_box_53.toPlainText()}={self.tab_1_entry_box_54.toPlainText()}={self.tab_1_entry_box_55.toPlainText()}={self.tab_1_entry_box_56.currentText()}={self.tab_1_entry_box_57.currentText()}={self.tab_1_entry_box_58.currentText()}"
        try:
            status = self.check_template("SEP")
            if status == True:
                pass
            else:
                for i in range(100):    
                    item = self.tab_8_list_box_01.item(i)
                    item.setText("")
        except:
            pass
        for i in range(100):
            item = self.tab_8_list_box_01.item(i)
            if item.text() == "":
                item.setText(string_to_add)
                break
            else:
                continue

    def tab_1_function_auto_set_drop_downs_function(self, index_list):
        self.tab_1_entry_box_03.setCurrentIndex(index_list[0])
        self.tab_1_entry_box_05.setCurrentIndex(index_list[1])
        self.tab_1_entry_box_06.setCurrentIndex(index_list[2])
        self.tab_1_entry_box_07.setCurrentIndex(index_list[3])
        self.tab_1_entry_box_08.setCurrentIndex(index_list[4])
        self.tab_1_entry_box_09.setCurrentIndex(index_list[5])
        self.tab_1_entry_box_10.setCurrentIndex(index_list[6])
        self.tab_1_entry_box_12.setCurrentIndex(index_list[7])
        self.tab_1_entry_box_14.setCurrentIndex(index_list[8])
        self.tab_1_entry_box_15.setCurrentIndex(index_list[9])
        self.tab_1_entry_box_17.setCurrentIndex(index_list[10])
        self.tab_1_entry_box_18.setCurrentIndex(index_list[11])
        self.tab_1_entry_box_19.setCurrentIndex(index_list[12])
        self.tab_1_entry_box_20.setCurrentIndex(index_list[13])
        self.tab_1_entry_box_21.setCurrentIndex(index_list[14])
        self.tab_1_entry_box_24.setCurrentIndex(index_list[15])
        self.tab_1_entry_box_25.setCurrentIndex(index_list[16])
        self.tab_1_entry_box_28.setCurrentIndex(index_list[17])
        self.tab_1_entry_box_29.setCurrentIndex(index_list[18])
        self.tab_1_entry_box_30.setCurrentIndex(index_list[19])
        self.tab_1_entry_box_32.setCurrentIndex(index_list[20])
    
    def tab_1_function_auto_set_drop_downs(self):
        current_index = self.tab_1_entry_box_04.currentIndex()
        if current_index == 1: #Alcoa-Infusions-DP
            self.tab_1_function_auto_set_drop_downs_function([6,1,5,5,1,1,1,1,1,7,2,1,0,2,0,4,1,0,1,0,2])
        elif current_index == 2: #Cardiology Fellows-HLVI-DP
            self.tab_1_function_auto_set_drop_downs_function([1,2,2,4,1,1,1,1,2,2,1,1,2,2,1,4,2,2,1,0,2])
        elif current_index == 3: #Cedar-Bluff-DP
            self.tab_1_function_auto_set_drop_downs_function([1,3,1,1,2,2,1,1,3,3,1,1,1,2,1,4,1,1,2,1,1])
        elif current_index == 4: #Cedar-Bluff-UHS-DP
            self.tab_1_function_auto_set_drop_downs_function([1,3,1,1,1,1,1,1,3,3,1,1,1,1,1,4,1,1,2,1,1])
        elif current_index == 5: #Cedar-Bluff-UNH-UHS-DP
            self.tab_1_function_auto_set_drop_downs_function([1,3,1,1,1,1,1,1,3,3,1,1,1,1,1,4,1,1,1,0,2])
        elif current_index == 6: #Cedar-Bluff-UPA-DP
            self.tab_1_function_auto_set_drop_downs_function([1,4,1,1,1,1,1,1,4,2,1,2,1,1,1,4,2,1,1,0,2])
        elif current_index == 7: #Cedar-Bluff-TTU-DP
            self.tab_1_function_auto_set_drop_downs_function([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        elif current_index == 8: #Cherokee-Farms-DP
            self.tab_1_function_auto_set_drop_downs_function([1,5,2,4,1,1,1,1,5,4,1,1,2,1,1,4,2,1,1,0,2])
        elif current_index == 9: #Halls-DP
            self.tab_1_function_auto_set_drop_downs_function([6,6,4,4,1,1,1,1,6,5,1,1,1,1,1,4,2,1,1,0,2])
        elif current_index == 10: #Lenoir-City-DP
            self.tab_1_function_auto_set_drop_downs_function([6,7,6,2,1,1,1,1,7,6,1,1,1,2,1,4,1,1,1,0,2])
        elif current_index == 11: #Patient-Registration-HLVI-DP
            self.tab_1_function_auto_set_drop_downs_function([1,8,2,4,1,1,1,1,8,8,1,1,2,2,1,4,1,2,1,0,2])
        elif current_index == 12: #PoB-DP1
            self.tab_1_function_auto_set_drop_downs_function([1,9,2,4,1,1,1,1,9,9,1,1,1,2,1,4,2,1,1,0,2])
        elif current_index == 13: #Pulm-Critcal-Care-DP
            self.tab_1_function_auto_set_drop_downs_function([1,10,2,4,1,1,1,1,10,10,1,1,2,2,1,4,2,2,1,0,2])
        elif current_index == 14: #Pulm-Function-DP
            self.tab_1_function_auto_set_drop_downs_function([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        elif current_index == 15: #Sevierville-DP
            self.tab_1_function_auto_set_drop_downs_function([1,12,7,3,1,1,1,2,12,12,1,1,1,2,1,4,2,1,1,0,2])
        elif current_index == 16: #Town-Center-DP
            self.tab_1_function_auto_set_drop_downs_function([4,13,3,5,1,1,1,1,13,13,1,1,1,1,1,4,2,1,1,0,2])
        elif current_index == 17: #Univ-Cardio-DP
            self.tab_1_function_auto_set_drop_downs_function([5,14,2,4,1,1,1,1,14,14,1,1,2,1,1,4,2,2,1,0,2])
        elif current_index == 18: #University-Heart-Surgeons-DP
            self.tab_1_function_auto_set_drop_downs_function([1,15,2,4,1,1,1,1,15,15,1,1,2,2,1,4,2,2,1,0,2])
        elif current_index == 19: #Wound-Care-HLVI-DP
            self.tab_1_function_auto_set_drop_downs_function([1,16,2,4,1,1,1,1,16,16,1,1,2,2,1,4,2,2,1,0,2])

    #--------------------------------------------------------------------------#
    #-                                 Tab 4                                  -#
    #--------------------------------------------------------------------------#
    
    def tab_4_function_hide_line_2(self):
        if self.tab_4_check_box_01.checkState() == 2:
            for number in range(19,25):
                ref_entry = getattr(self, f"tab_4_entry_box_{number}")
                ref_label = getattr(self, f"tab_4_label_{number}")
                ref_entry.setHidden(False)
                ref_label.setHidden(False)
        if self.tab_4_check_box_01.checkState() == 0:
            for number in range(19,25):
                ref_entry = getattr(self, f"tab_4_entry_box_{number}")
                ref_label = getattr(self, f"tab_4_label_{number}")
                ref_entry.setHidden(True)
                ref_label.setHidden(t)

    def tab_4_function_hide_line_3(self):
        if self.tab_4_check_box_02.checkState() == 2:
            for number in range(25,31):
                ref_entry = getattr(self, f"tab_4_entry_box_{number}")
                ref_label = getattr(self, f"tab_4_label_{number}")
                ref_entry.setHidden(False)
                ref_label.setHidden(False)
        if self.tab_4_check_box_02.checkState() == 0:
            for number in range(25,31):
                ref_entry = getattr(self, f"tab_4_entry_box_{number}")
                ref_label = getattr(self, f"tab_4_label_{number}")
                ref_entry.setHidden(True)
                ref_label.setHidden(True)

    def tab_4_function_clear_fields(self):
        all_fields = [self.tab_4_entry_box_01, self.tab_4_entry_box_02, self.tab_4_entry_box_03,
        self.tab_4_entry_box_04, self.tab_4_entry_box_05, self.tab_4_entry_box_06,
        self.tab_4_entry_box_07, self.tab_4_entry_box_08, self.tab_4_entry_box_09,
        self.tab_4_entry_box_10, self.tab_4_entry_box_11, self.tab_4_entry_box_12,
        self.tab_4_entry_box_13, self.tab_4_entry_box_14, self.tab_4_entry_box_15,
        self.tab_4_entry_box_16, self.tab_4_entry_box_17, self.tab_4_entry_box_18,
        self.tab_4_entry_box_19, self.tab_4_entry_box_20, self.tab_4_entry_box_21,
        self.tab_4_entry_box_22, self.tab_4_entry_box_23, self.tab_4_entry_box_24,
        self.tab_4_entry_box_25, self.tab_4_entry_box_26, self.tab_4_entry_box_27,
        self.tab_4_entry_box_28, self.tab_4_entry_box_29, self.tab_4_entry_box_30]
        for each in all_fields:
            try:
                each.setPlainText("")
            except: 
                each.setCurrentIndex(0)

    def tab_4_function_add_to_queue(self):
        string_to_add = f"{self.tab_4_entry_box_01.toPlainText()}={self.tab_4_entry_box_02.toPlainText()}={self.tab_4_entry_box_03.currentText()}={self.tab_4_entry_box_04.currentText()}={self.tab_4_entry_box_05.currentText()}={self.tab_4_entry_box_06.currentText()}={self.tab_4_entry_box_07.currentText()}={self.tab_4_entry_box_08.toPlainText()}={self.tab_4_entry_box_09.currentText()}={self.tab_4_entry_box_10.currentText()}={self.tab_4_entry_box_11.currentText()}={self.tab_4_entry_box_12.toPlainText()}={self.tab_4_entry_box_13.currentText()}={self.tab_4_entry_box_14.currentText()}={self.tab_4_entry_box_15.toPlainText()}={self.tab_4_entry_box_16.currentText()}={self.tab_4_entry_box_17.currentText()}={self.tab_4_entry_box_18.toPlainText()}={self.tab_4_entry_box_19.toPlainText()}={self.tab_4_entry_box_20.currentText()}={self.tab_4_entry_box_21.currentText()}={self.tab_4_entry_box_22.toPlainText()}={self.tab_4_entry_box_23.toPlainText()}={self.tab_4_entry_box_24.toPlainText()}={self.tab_4_entry_box_25.toPlainText()}={self.tab_4_entry_box_26.currentText()}={self.tab_4_entry_box_27.currentText()}={self.tab_4_entry_box_28.toPlainText()}={self.tab_4_entry_box_29.toPlainText()}={self.tab_4_entry_box_30.toPlainText()}"
        try:
            status = self.check_template("CSF")
            if status == True:
                pass
            else:
                for i in range(100):
                    item = self.tab_8_list_box_01.item(i)
                    item.setText("")
        except:
            pass
        for i in range(100):
            item = self.tab_8_list_box_01.item(i)
            if item.text() == "":
                item.setText(string_to_add)
                break
            else:
                continue

    def tab_4_function_auto_set_drop_downs_function(self, index_list):
        self.tab_4_entry_box_04.setCurrentIndex(index_list[0])
        self.tab_4_entry_box_05.setCurrentIndex(index_list[1])
        self.tab_4_entry_box_06.setCurrentIndex(index_list[2])
        self.tab_4_entry_box_09.setCurrentIndex(index_list[3])
        self.tab_4_entry_box_10.setCurrentIndex(index_list[4])
        self.tab_4_entry_box_11.setCurrentIndex(index_list[5])
        self.tab_4_entry_box_13.setCurrentIndex(index_list[6])
        self.tab_4_entry_box_14.setCurrentIndex(index_list[7])
    def tab_4_function_auto_set_drop_downs(self):
        current_index = self.tab_4_entry_box_03.currentIndex()
        if current_index == 1:
            self.tab_4_function_auto_set_drop_downs_function([1,1,1,1,1,1,1,1])
        elif current_index == 2:
            self.tab_4_function_auto_set_drop_downs_function([2,2,2,3,1,1,1,1])
        elif current_index == 3:
            self.tab_4_function_auto_set_drop_downs_function([3,1,1,2,2,1,2,1])
        elif current_index == 4:
            self.tab_4_function_auto_set_drop_downs_function([3,1,1,2,2,1,1,1])
        elif current_index == 5:
            self.tab_4_function_auto_set_drop_downs_function([4,2,3,4,4,1,2,1])
        elif current_index == 6:
            self.tab_4_function_auto_set_drop_downs_function([5,2,3,5,5,1,2,2])


    #--------------------------------------------------------------------------#
    #-                                 Tab 6                                  -#
    #--------------------------------------------------------------------------#
    def tab_6_function_add_to_queue(self):
        string_to_add = f"{self.tab_6_entry_box_01.toPlainText()}={self.tab_6_entry_box_02.toPlainText()}={self.tab_6_entry_box_03.currentText()}={self.tab_6_entry_box_04.currentText()}={self.tab_6_entry_box_05.currentText()}={self.tab_6_entry_box_06.toPlainText()}={self.tab_6_entry_box_07.toPlainText()}={self.tab_6_entry_box_08.toPlainText()}={self.tab_6_entry_box_09.toPlainText()}={self.tab_6_entry_box_10.currentText()}={self.tab_6_entry_box_11.toPlainText()}={self.tab_6_entry_box_12.toPlainText()}={self.tab_6_entry_box_13.toPlainText()}"
        try:
            status = self.check_template("TCT")
            if status == True:
                pass
            else:
                for i in range(100):
                    item = self.tab_8_list_box_01.item(i)
                    item.setText("")
        except:
            pass
        for i in range(100):
            item = self.tab_8_list_box_01.item(i)
            if item.text() == "":
                item.setText(string_to_add)
                break
            else:
                continue

    def tab_6_function_auto_fill_entry_box_08(self):
        text_to_fill = self.tab_6_entry_box_07.toPlainText()
        self.tab_6_entry_box_08.setPlainText(text_to_fill)

    def tab_6_function_auto_set_drop_downs(self):
        current_index = self.tab_6_entry_box_03.currentIndex()
        if current_index == 1:
            self.tab_6_entry_box_05.setCurrentIndex(current_index)
        elif current_index in (2,3):
            self.tab_6_entry_box_05.setCurrentIndex(2)
        self.tab_6_entry_box_04.setCurrentIndex(1)
        self.tab_6_entry_box_10.setCurrentIndex(1)

    def tab_6_function_clear_fields(self):
        all_fields = [self.tab_6_entry_box_01, self.tab_6_entry_box_02, self.tab_6_entry_box_03,
        self.tab_6_entry_box_04, self.tab_6_entry_box_05, self.tab_6_entry_box_06,
        self.tab_6_entry_box_07, self.tab_6_entry_box_08, self.tab_6_entry_box_09,
        self.tab_6_entry_box_10, self.tab_6_entry_box_11, self.tab_6_entry_box_12,
        self.tab_6_entry_box_13]
        for each in all_fields:
            try:
                each.setPlainText("")
            except: 
                each.setCurrentIndex(0)
    #--------------------------------------------------------------------------
    #-                                 Tab 8                                  -
    #--------------------------------------------------------------------------
    def tab_8_function_clear_fields(self):
        for i in range(99):
            item = self.tab_8_list_box_01.item(i)
            item.setText("")
    
    def tab_8_function_choose_template_to_generate(self):
        check_string = (self.tab_8_list_box_01.item(0).text().split("="))[0]
        if check_string.startswith("TCT"):
            self.tab_8_function_generate_csv_tab_06()
        elif check_string.startswith("CSF"):
            self.tab_8_function_generate_csv_tab_04()
        elif check_string.startswith("SEP"):
            self.tab_8_function_generate_csv_tab_01()
    
    def tab_8_function_generate_csv_tab_01(self):
        ready = []
        date_time_suffix = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        with open('./csv_templates/phone_7841_template.csv', encoding="utf-8") as csv_file:
            rows = [row for row in csv.reader(csv_file)]
            row_len = len(rows[0])
            for i in range(100): 
                current_line = self.tab_8_list_box_01.item(i)
                if current_line.text() == "": 
                    break
                else:
                    rows.append([""] * row_len)
            for i in range(100):
                current_line = self.tab_8_list_box_01.item(i)
                if current_line.text() == "":
                    break
                else: #All cell filling goes in this else logic tree
                    string_list = current_line.text().split("=")
                    extra_options = []
                    line_2 = []
                    zip_list_1 = [string_list[32],'Endpoints-PT',string_list[33],'LongDistance-CSS','Auto Answer Off',string_list[34],
                    string_list[35],string_list[36],string_list[37],string_list[36],string_list[37],string_list[36],string_list[37],
                    string_list[36],string_list[37],string_list[36],string_list[37],string_list[36],string_list[37],
                    string_list[38],string_list[39],'4','2','Use System Policy','Use System Default','Use System Default',
                    'f','f','f','f',string_list[40],string_list[41],string_list[41],'Standard Presence group','Local-LineFWD-CSS',string_list[36],
                    'Local-LineFWD-CSS',string_list[38],string_list[38],'f',string_list[36],string_list[37],string_list[36],string_list[37],'t',
                    'Default',string_list[42],string_list[43],'Use System Default','t','Use System Default','Use System Default',
                    'f','f','Default','t','f','f',string_list[44],'-1','Default']
                    line_3 = []
                    zip_list_2 = [string_list[45],'Endpoints-PT',string_list[46],'LongDistance-CSS','Auto Answer Off',
                    string_list[47],'98658397604',string_list[48],string_list[49],string_list[48],string_list[49],string_list[48],string_list[49],
                    string_list[48],string_list[49],string_list[48],string_list[49],string_list[48],string_list[49],
                    string_list[48],string_list[51],string_list[52],'4','2','Use System Policy','Use System Default',
                    'Use System Default','f','f','f','f',string_list[53],string_list[54],string_list[54],'Standard Presence Group',
                    string_list[50],'f',string_list[50],string_list[54],string_list[54],'f','f',string_list[50],'f',string_list[50],
                    't','Default',string_list[55],string_list[56],'Use System Default','t','Use System Default','Use System Default',
                    'f','f','Default','t','f','f',string_list[57],'-1','Default']
                    for each in range(200):
                        extra_options.append('')
                        line_2.append('')
                        line_3.append('')
                    if string_list[30] != '':
                        extra_options[0] = 't'
                    if self.tab_1_check_box_01.isChecked(): #line_2
                        for index, value in zip(range(61),(zip_list_1)):
                            line_2[index] = value
                    if self.tab_1_check_box_02.isChecked(): #line_2
                        for index, value in zip(range(61),(zip_list_2)):
                            line_3[index] = value
                    try:
                        value_list = [string_list[0], string_list[1],string_list[4],string_list[3],string_list[5],'f','United States',
                        string_list[6],'English United States','None','0',string_list[7],string_list[8],'t','f',
                        string_list[9],'Default','Default','Csico 7841',string_list[10],string_list[11],string_list[12],
                        't','Standard Presence group','Cisco 7841 - Standard SIP Non-Secure Profile',string_list[13],
                        'f','f','f','No Pending Operation','SIP','<disableSpeaker>f</disableSpeaker><disableSpeakerAndHeadset>f</disableSpeakerAndHeadset><pcPort>0</pcPort><garp>1</garp><voiceVlanAccess>0</voiceVlanAccess><webAccess>0</webAccess><spanToPCPort>1</spanToPCPort><loggingDisplay>1</loggingDisplay><recordingTone>0</recordingTone><recordingToneLocalVolume>100</recordingToneLocalVolume><recordingToneRemoteVolume>50</recordingToneRemoteVolume><recordingToneDuration></recordingToneDuration><moreKeyReversionTimer>5</moreKeyReversionTimer><lldpAssetId></lldpAssetId><powerPriority>0</powerPriority><LineKeyBarge>0</LineKeyBarge><minimumRingVolume>0</minimumRingVolume><ehookEnable>0</ehookEnable><headsetWidebandUIControl>0</headsetWidebandUIControl><headsetWidebandEnable>0</headsetWidebandEnable><recentsSoftkey>1</recentsSoftkey>',
                        string_list[14],'No Preference','0','Standard SIP Profile','711ulaw','f','t','f','Default',
                        'POB-Media-Resources-CDC','Use Common Phone Profile Setting','f','Off','Off','Default','Default',
                        'Default','Default','No Rollover','Default','f','Default','Default','f','f','Not Trusted',
                        'f','t','t','f','f','f','-1','f',string_list[15],'Endpoints-PT',string_list[16], string_list[17],
                        'Auto Answer Off', 'f',string_list[18],string_list[19],string_list[20],string_list[19],string_list[20],
                        string_list[19],string_list[20],string_list[19],string_list[20],string_list[19],string_list[20],
                        string_list[19],string_list[20],string_list[21],string_list[22],string_list[23],'2','Use System Policy',
                        'Use System Default','Use System Default','f','f','f',string_list[24],string_list[25],string_list[26],string_list[26],
                        'Standard Presence group',string_list[27],'f','Local-LineFWD-CSS',string_list[26],string_list[26],'f',string_list[19],string_list[20],
                        string_list[19],string_list[20],'t','Default',string_list[28],string_list[29],'Use System Default',
                        't','Use System Default', ' Use System Default','f','f','Default','t',string_list[30], extra_options[0],
                        'f','f',string_list[31],'-1','Default',line_2[0],line_2[1],line_2[2],line_2[3],line_2[4],line_2[5],
                        line_2[6],line_2[7],line_2[8],line_2[9],line_2[10],line_2[11],line_2[12],line_2[13],line_2[14],line_2[15],line_2[16],
                        line_2[17],line_2[18],line_2[19],line_2[20],line_2[21],line_2[22],line_2[23],line_2[24],line_2[25],line_2[26],line_2[27],
                        line_2[28],line_2[29],line_2[30],line_2[31],line_2[32],line_2[33],line_2[34],line_2[35],line_2[36],line_2[37],line_2[38],
                        line_2[39],line_2[40],line_2[41],line_2[42],line_2[43],line_2[44],line_2[45],line_2[46],line_2[47],line_2[48],line_2[49],
                        line_2[50],line_2[51],line_2[52],line_2[53],line_2[54],line_2[55],line_2[56],line_2[57],line_2[58],line_2[59],line_2[60],
                        line_3[0],line_3[1],line_3[2],line_3[3],line_3[4],line_3[5],line_3[6],line_3[7],line_3[8],line_3[9],line_3[10],line_3[11],line_3[12],line_3[13],line_3[14],line_3[15],line_3[16],
                        line_3[17],line_3[18],line_3[19],line_3[20],line_3[21],line_3[22],line_3[23],line_3[24],line_3[25],line_3[26],line_3[27],
                        line_3[28],line_3[29],line_3[30],line_3[31],line_3[32],line_3[33],line_3[34],line_3[35],line_3[36],line_3[37],line_3[38],
                        line_3[39],line_3[40],line_3[41],line_3[42],line_3[43],line_3[44],line_3[45],line_3[46],line_3[47],line_3[48],line_3[49],
                        line_3[50],line_3[51],line_3[52],line_3[53],line_3[54],line_3[55],line_3[56],line_3[57],line_3[58],line_3[59],line_3[60]]
                        if rows[i+1][0] == "":
                            start_index = 0
                            for value in value_list:
                                rows[i+1][start_index] = value
                                start_index +=1
                    except IndexError:
                        continue
            rows_csv = pd.DataFrame(rows)
            rows_csv.to_csv(f"./output/phone_7841_export_{date_time_suffix}.csv", header=False, index=False)
        _translate = QtCore.QCoreApplication.translate
        for i in range(99):
            item = self.tab_8_list_box_01.item(i)
            item.setText("")
        item = self.tab_8_list_box_01.item(0)
        item.setText("SUCCESS")
        start_wait_timer = threading.Thread(target=self.threaded_wait_time)
        start_wait_timer.start()
    def tab_8_function_generate_csv_tab_02(self):
        pass
    def tab_8_function_generate_csv_tab_03(self):
        pass
    def tab_8_function_generate_csv_tab_04(self):
        ready = []
        date_time_suffix = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        with open('./csv_templates/jabber_pcmac_template.csv', encoding="utf-8") as csv_file:
            rows = [row for row in csv.reader(csv_file)]
            row_len = len(rows[0])
            for i in range(100):
                current_line = self.tab_8_list_box_01.item(i)
                if current_line.text() == "":
                    break
                else:
                    rows.append([""] * row_len)
            for i in range(100):
                current_line = self.tab_8_list_box_01.item(i)
                if current_line.text() == "":
                    break
                else:
                    string_list = current_line.text().split("=")
                    variable_list = []
                    entry_list = ["Endpoints-PT","NoVoiceMail","Auto Answer Off","f","f",
                    "LongDistance-LineFWD-CSS","f","Local-LineFWD-CSS","f","Local-LineFWD-CSS",
                    "f","Local-LineFWD-CSS","f","Local-LineFWD-CSS","f","Local-LineFWD-CSS","f","Local-LineFWD-CSS",
                    "2","1","Use System Policy","Ring","Use System Default","f","f","f","f","Standard Presence Group","Local-LineFWD-CSS","f","Local-LineFWD-CSS","f","f","f","Local-LineFWD-CSS","f","Local-LineFWD-CSS","Default","Call Recording Disabled","Cherokee-Farm-Device-CSS","Use System Default","t","f","f","Default","t","f","f","Gateway Preferred","-1","Default"]
                    for each in range(53):
                        variable_list.append("")
                    if string_list[16] != "":
                        variable_list[0] = "t"
                        variable_list[1] = "t"
                    if self.tab_4_check_box_01.isChecked():
                        for index,value in enumerate(zip(entry_list, entry_list)):
                            variable_list[index+2] = value[0]
                    try:
                        value_list = [string_list[0],string_list[1],string_list[2],"Standard Client Services Framework",
                        string_list[3], string_list[4],"f","United States",string_list[5],"English United States",
                        "None", string_list[6],"Default","t","f","Off","Disabled","Cisco Unified Client Services Framework",
                        string_list[7],string_list[7],"Standard Common Phone Profile",string_list[7],"t","Standard Presence group",
                        "Cisco Unified Client Services Framework - Standard SIP Non-Secure Profile",string_list[8],
                        "f","f","f","No Pending Operation","SIP","<ice></ice><instantMessaging></instantMessaging><desktopClient></desktopClient>",
                        string_list[9],"No Preference","0","Standard SIP Profile","711ulaw","f",string_list[7],
                        "t","f",string_list[10],"POB-Media-Resources-CDC","Ringer Off","f","Off","Off","Default",
                        "Default","Default","Default","No Rollover","Default","f","Default","Default","f","f","Not Trusted",
                        "f","t","t","f","f","f","-1","f","f",string_list[11],"endpoints-PT","Unity-Connection-VMP",
                        string_list[12],"Auto Answer Off","f",string_list[13],"t","Local-LineFWD-CSS","t","Local-LineFWD-CSS",
                        "t","Local-LineFWD-CSS","t","Local-LineFWD-CSS","t","Local-LineFWD-CSS","t","Local-LineFWD-CSS",
                        string_list[2],string_list[14],"6","2","Use System Policy","Ring","Use System Default","f","f","f",
                        string_list[2],string_list[2],string_list[2],"Standard Presence Group","Local-LineFWD-CSS","t",
                        "Local-LineFWD-CSS",string_list[2],string_list[2],"f","t","Local-LineFWD-CSS","t","Local-LineFWD-CSS",
                        "t","Default",string_list[15], string_list[16],"Use System Default","t","f","f","Default","t",string_list[17],
                        variable_list[0],"f","f","Gateway Preferred","-1",variable_list[1],"Default",string_list[18],
                        variable_list[2],variable_list[3],string_list[19],variable_list[4],variable_list[5],string_list[20],
                        variable_list[6], variable_list[7],variable_list[8], variable_list[9],variable_list[10],variable_list[11],
                        variable_list[12],variable_list[13],variable_list[14],variable_list[15],variable_list[16],variable_list[17],
                        variable_list[18],variable_list[19],string_list[21],string_list[22],variable_list[20],variable_list[21],
                        variable_list[22],variable_list[23],variable_list[24],variable_list[25],variable_list[26],variable_list[27],
                        variable_list[28], string_list[23],string_list[23],string_list[23], variable_list[29],variable_list[30],variable_list[31],
                        variable_list[32], string_list[23], string_list[24], variable_list[33],variable_list[34],variable_list[35],variable_list[36],
                        variable_list[37],variable_list[38],variable_list[39],variable_list[40],variable_list[41],variable_list[42],
                        variable_list[43],variable_list[44],variable_list[45],variable_list[46],variable_list[47],
                        variable_list[48],variable_list[49],variable_list[50],variable_list[51],variable_list[52]]

                        if rows[i+1][0] == "":
                            start_index = 0
                            for value in value_list:
                                rows[i+1][start_index] = value
                                start_index +=1
                    except IndexError:
                        continue
            rows_csv = pd.DataFrame(rows)
            rows_csv.to_csv(f"./output/jabber_pcmac_export_{date_time_suffix}.csv", header=False, index=False)
        _translate = QtCore.QCoreApplication.translate
        for i in range(99):
            item = self.tab_8_list_box_01.item(i)
            item.setText("")
        item = self.tab_8_list_box_01.item(0)
        item.setText("SUCCESS")
        start_wait_timer = threading.Thread(target=self.threaded_wait_time)
        start_wait_timer.start()
    def tab_8_function_generate_csv_tab_05(self):
        pass
    def tab_8_function_generate_csv_tab_06(self):
        ready = []
        date_time_suffix = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        with open('./csv_templates/jabber_iphone_template.csv', encoding="utf-8") as csv_file:
            rows = [row for row in csv.reader(csv_file)]
            row_len = len(rows[0])
            for i in range(100):
                current_line = self.tab_8_list_box_01.item(i)
                if current_line.text() == "":
                    break
                else:
                    rows.append([""] * row_len)
            for i in range(100):
                current_line = self.tab_8_list_box_01.item(i)
                if current_line.text() == "":
                    break
                else:
                    string_list = current_line.text().split("=")
                    try:
                        value_list = [string_list[0],string_list[1],string_list[2],
                        string_list[3], string_list[4], "POB-LOC", "f", "United States",
                        "POB-MRGL1", "English United States", "None", "Default", "Default",
                        "t","f","off","Disabled","Cisco Dual Mode for iPhone", string_list[5],
                        string_list[6],"Standard Common Phone Profile",string_list[7],
                        "t","Standard Presence group","Cisco Dual Mode for iPhone - Standard SIP Non-Secure Profile",
                        "Cherokee-Farm-Device-CSS","f","f","f","No Pending Operation",
                        "SIP","<paramEditability>0</paramEditability><iPhoneCountryCode></iPhoneCountryCode><cuetLevel>1</cuetLevel><cucmUseSipDigest>0</cucmUseSipDigest><cucmSipDigestUserName></cucmSipDigestUserName><cucmCtiUserName></cucmCtiUserName><dialViaOffice>0</dialViaOffice><cucmUseVoiceDialing>1</cucmUseVoiceDialing><cucmVoiceDialingPhoneNumber></cucmVoiceDialingPhoneNumber><cucmAddVoiceDialingNumberToFavorites>1</cucmAddVoiceDialingNumberToFavorites><emEnabled>0</emEnabled><cucmDirectoryLookupRulesURL></cucmDirectoryLookupRulesURL><cucmApplicationDialRulesURL></cucmApplicationDialRulesURL><cucmGSMHandoffPreference>1</cucmGSMHandoffPreference><vmUserName></vmUserName><vmUnityServer></vmUnityServer><vmMessageStoreUserName></vmMessageStoreUserName><vmMessageStore></vmMessageStore><ldapUseLDAPUserAuthentication>0</ldapUseLDAPUserAuthentication><ldapServer></ldapServer><ldapUseSSL>0</ldapUseSSL><ldapSearchBase></ldapSearchBase><ldapFieldMapping></ldapFieldMapping><ldapPhoto></ldapPhoto><dialerEmergencyNumbers>999,911,112</dialerEmergencyNumbers><vpnLaunchURL></vpnLaunchURL><PreWifiNetworks></PreWifiNetworks><Ringtone>0</Ringtone><videoCapability>1</videoCapability><ciscoSupportField></ciscoSupportField><reserved></reserved><ice></ice>",
                        "","Cherokee-Farm-Device-CSS","No Preference","0","Standard SIP Profile",
                        "711ulaw","f",string_list[5],"t","f","Default","POB-Media-Resources-CDC",
                        "Call Reject","Disable","f","Off","Off","Default","Default","Default",
                        "Default","No Rollover","Default","f","Default","Default","f","f","Not Trusted",
                        "f","t","t","f","f","f","-1","f","f",string_list[8],"endpoints-PT","Unity-Connection-VMP",
                        string_list[9],"Auto Answer Off","f","","LongDistance-LineFWD-CSS","t","Local-LineFWD-CSS",
                        "t","Local-LineFWD-CSS","t","Local-LineFWD-CSS","t","Local-LineFWD-CSS","t",
                        "Local-LineFWD-CSS","t","Local-LineFWD-CSS","",string_list[10],"2","2","Use System Policy",
                        "Ring","Use System Default","f","f","f","f",string_list[11],string_list[11],string_list[11],
                        "Standard Presence group","Local-LineFWD-CSS","t","Local-LineFWD-CSS",
                        string_list[12],string_list[12],"f","t","Local-LineFWD-CSS","t","Local-LineFWD-CSS","t",
                        "Default","Call Recording Disabled","Use System Default","t","f","t",
                        "Default","t","","","f","f","Gateway Preferred","-1", "Default"]
                        if rows[i+1][0] == "":
                            start_index = 0
                            for value in value_list:
                                rows[i+1][start_index] = value
                                start_index +=1
                    except IndexError:
                        continue
            rows_csv = pd.DataFrame(rows)
            rows_csv.to_csv(f"./output/jabber_iphone_export_{date_time_suffix}.csv", header=False, index=False)
        _translate = QtCore.QCoreApplication.translate
        for i in range(99):
            item = self.tab_8_list_box_01.item(i)
            item.setText("")
        item = self.tab_8_list_box_01.item(0)
        item.setText("SUCCESS")
        start_wait_timer = threading.Thread(target=self.threaded_wait_time)
        start_wait_timer.start()
    def tab_8_function_generate_csv_tab_07(self):
        pass
    def tab_8_function_download_update(self):
        url = "https://github.com/JustinTArnold/CUCM_CSV_Generator/archive/main.zip"
        date_time_suffix = datetime.now().strftime("%d_%m_%Y")
        wget.download(url, f'./Update_Files/Update_files_{date_time_suffix}.zip')

#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#-                              Render Program                            -#
#--------------------------------------------------------------------------#   
#--------------------------------------------------------------------------#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cucm_csv_generator = QtWidgets.QMainWindow()
    ui = Ui_cucm_csv_generator()
    ui.setupUi(cucm_csv_generator)
    cucm_csv_generator.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    cucm_csv_generator.show()
    sys.exit(app.exec_())
