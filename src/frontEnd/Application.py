
#===============================================================================
#
#          FILE: Application.py
# 
#         USAGE: --- 
# 
#   DESCRIPTION: This main file use to start the Application
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Fahim Khan, fahim.elex@gmail.com
#  ORGANIZATION: eSim team at FOSSEE, IIT Bombay.
#       CREATED: Wednesday 21 January 2015 
#      REVISION:  ---
#===============================================================================


from PyQt4 import QtGui, QtCore
from configuration.Appconfig import Appconfig
from projManagement.openProject import OpenProjectInfo
from projManagement.newProject import NewProjectInfo
import os
import ViewManagement
import Workspace
import sys 
import time
import subprocess


class Application(QtGui.QMainWindow):
    """
    Its our main window of application
    """
    def __init__(self,*args):
        """
        Initialize main Application window
        """
        #Calling __init__ of super class
        QtGui.QMainWindow.__init__(self,*args)
        
        
        #Creating Application configuration object
        self.obj_appconfig = Appconfig() 
        self.setGeometry(self.obj_appconfig._app_xpos,
                         self.obj_appconfig._app_ypos,
                         self.obj_appconfig._app_width,
                         self.obj_appconfig._app_heigth)
        self.setWindowTitle(self.obj_appconfig._APPLICATION) 
        #Init Workspace
        self.obj_workspace = Workspace.Workspace()
      
        #Init necessary components in sequence
        self.initActions()
        self.initView()
        
        
    def initActions(self):
        
        self.newproj = QtGui.QAction(QtGui.QIcon('../images/newProject.png'),'<b>New Project</b>',self)
        self.newproj.setShortcut('Ctrl+N')
        self.newproj.triggered.connect(self.new_project)
        
        
        self.openproj = QtGui.QAction(QtGui.QIcon('../images/openProject.png'),'<b>Open Project</b>',self)
        self.openproj.setShortcut('Ctrl+O')
        self.openproj.triggered.connect(self.open_project)
        
        self.exitproj = QtGui.QAction(QtGui.QIcon('../images/closeProject.png'),'<b>Exit</b>',self)
        self.exitproj.setShortcut('Ctrl+X')
        self.exitproj.triggered.connect(self.exit_project)
        
        self.helpfile = QtGui.QAction(QtGui.QIcon('../images/helpProject.png'),'<b>Help</b>',self)
        self.helpfile.setShortcut('Ctrl+H')
        self.helpfile.triggered.connect(self.help_project)
        
        self.mainToolbar = self.addToolBar('Top Navigation')
        self.mainToolbar.addAction(self.newproj)
        self.mainToolbar.addAction(self.openproj)
        self.mainToolbar.addAction(self.exitproj)
        self.mainToolbar.addAction(self.helpfile)
        
            
        
              
      
    def initView(self):
        """
        Create GUI from the class Views and initialize it
        """
        self.view = ViewManagement.ViewManagement()
        self.setCentralWidget(self.view)
          
    def new_project(self):
        """
        This function call New Project Info class.
        """
        print "New Project called"
        self.project = NewProjectInfo()
        self.project.body()
        
    
    def open_project(self):
        """
        This project call Open Project Info class
        """
        print "Open Project called"
        self.project = OpenProjectInfo()
        self.project.body()
        
    def exit_project(self):
        print "Exit Project called"
        for proc in self.obj_appconfig.procThread_list:
                try:
                        proc.terminate()
                except:
                        pass
        ##Just checking if open and New window is open. If yes just close it when application is closed
        try:
            self.project.close()
        except:
            pass
        
        self.close()
        
    def help_project(self):
        print "Help is called"
        print "Current Project : ",self.obj_appconfig.current_project
              
        
        
    def testing(self):
        print "Success hit kicad button"
        
   
      

def main(args):
    """
    It is main function of the module.It starts the application
    """
    print "Starting eSim......"
    app = QtGui.QApplication(args)
   
    """
    splash_pix = QtGui.QPixmap('../images/FreeEDAlogo.jpg')
    splash = QtGui.QSplashScreen(splash_pix,QtCore.Qt.WindowStaysOnTopHint)
    progressBar = QtGui.QProgressBar(splash)
    splash.setMask(splash_pix.mask())
    splash.show()
    
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()    
    
    time.sleep(2)
    
    appView = Application()
    appView.show()
    splash.finish(appView)
    sys.exit(app.exec_())
    """
    appView = Application()
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    appView.show()
    sys.exit(app.exec_())
    
    


# Call main function
if __name__ == '__main__':
    # Create and display the splash screen
    main(sys.argv)
    


