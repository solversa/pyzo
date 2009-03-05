""" MAIN MODULE OF IEP
This module contains the main frame. The menu's are defined here,
and therefore also some functionality (if we do not call
methods in other windows). For example the functions for the running 
of code is implemented here (well, only the part to select the right 
code).

$Author: almar@SAS $
$Date: 2009-01-30 14:48:05 +0100 (Fri, 30 Jan 2009) $
$Rev: 946 $

"""

print "Importing iep.main ..."

import os, sys
import iep
from PyQt4 import QtCore, QtGui
qt = QtGui



class MainWindow(qt.QMainWindow):
    
    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)
        
        # set layout as it was the previous time
        pos = iep.config.layout
        self.move(pos.left, pos.top)
        self.resize(pos.width, pos.heigth)
        if pos.maximized:
            self.setWindowState(QtCore.Qt.WindowMaximized)
        
        # set label and icon
        self.setWindowTitle("IEP")
        icon = qt.QIcon('iep.ico')
        self.setWindowIcon(icon)
        
        # create splitter
        #self.splitter0 = qt.QSplitter(self)
        
        but = qt.QPushButton("asd")
        self.setCentralWidget(but)
        menu = self.menuBar()
        fmenu = menu.addMenu("File")
        ds, cb = "Close and restrat IEP, mainly for testing", self.m_restart
        fmenu.addAction( self.createAction("Restart IEP", ds, "", cb ))
        ds, cb = "Exit from IEP", self.m_exit
        fmenu.addAction( self.createAction("Exit IEP", ds, "Alt+F4", cb ) )
        menu.addMenu("Session")
        
        # test dock widgets
        dock = qt.QDockWidget("Find in files", self)
        dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)
        dock.setFeatures(qt.QDockWidget.DockWidgetMovable)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock)
    
        
        # show now
        self.show()
        
        
    def m_exit(self):
        """ Close IEP """
        self.close()
        
    def m_restart(self):
        """ Restart IEP """
        self.close()
        
        # put a space in front of all args
        args = []
        for i in sys.argv:
            args.append(" "+i)
        # replace the process!                
        os.execv(sys.executable, args)
    
    
    def createAction(self, name, descr, shortcut, cb):
        """ Create an action object, with the specified stuff. """
        act = qt.QAction(name,self)
        act.setShortcut(shortcut)
        act.setStatusTip(descr)
        if cb is not None:
            self.connect(act, QtCore.SIGNAL('triggered()'), cb)
        return act


    def closeEvent(self, event):
        """ Override close event handler. """
        
        # store splitter layout
        pos = iep.config.layout
        if self.windowState() == QtCore.Qt.WindowMaximized:
            pos.maximized = 1
            self.setWindowState(QtCore.Qt.WindowNoState)
        else:
            pos.maximized = 0            
        pos.left, pos.top = self.x(), self.y()
        pos.width, pos.heigth = self.width(), self.height()
        
        # store config
        iep.saveConfig()
        
        # proceed with closing...
        event.accept()
        
    
app = QtGui.QApplication([])
w = MainWindow()
app.exec_()

# if __name__ == "__main__":    
#     iep.startIep()
    
