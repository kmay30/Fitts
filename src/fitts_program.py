# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="krm"
__date__ ="$Sep 20, 2012 1:58:33 PM$"



import javax.swing as swing
import java.awt as awt
import java.net as net
import sys
import threading
import datetime
import time
from pymouse import PyMouse
### note that is is pymouse 1.0, available here
### http://pepijndevos.nl/2010/04/pymouse-mouse-control-and-events-on-python/index.html
## this is how you use it
##http://code.google.com/p/pymouse/wiki/Documentation

class target(swing.JButton):
    def __init__(self,radius,shape,xPos, yPos):
        ### radius is something that will be fed to this at instantiation from the condition generator
        self.radius = radius
        self.color = awt.Color.BLUE
        self.hide()
        self.position =([xPos, yPos])
        ## shape would be interesting to do here.
        ## http://harryjoy.com/2011/08/21/different-button-shapes-in-swing/
        #need to find out how to make the button circular
        ## need to set the button radius to self.radius
    def draw(self):
        ## should not be necessary, but in case it is not refreshing, call this
        self.show()
        self.validate()
        self.repaint()


class condition():
    def __init__(self, targetRadius, targetDistance, targetShape):
        ### just a class for a condition.  shoudl probably be a struct or something
        self.targetRadius = targetRadius
        self.targetDistance = targetDistance
        self.targetShape = targetShape


class conditionBuilder():
    def __init__(self,settings):
        ### some sort of latin square logic here
        ### it looks at the information in the settings file, and is able to output the
        ### appropriate condition at a given time
        ### it needs to remove conditions that were already used, etc. etc.

    def getCondition(self):
        ### so the trial object will call this to get this information
        condition = condition(self.currenttargetRadius, self.currenttargetDistance, self.currentTargetShape)
        return condition


class trial():
    def __init__(self, experiment, fixationTime, timeoutTime, condition):
        ### code for carrying out an actual trial
        ### the sequence is: render fixation cross, wait fixation time, display target, wait for mouse click on target, write information,
        ### condition is an object
        self.movementTime = 0
        self.targetCoordinates = []
        self.experiment = experiment
        ## calculate the target coordinates here
        self.targetX = 0
        self.targetY = 0
        self.mouseClickX = 0
        self.mouseClickY = 0
        ### raw size of the error.  just pythogorean theorem it
        self.errorMagnitude = 0
        #### not sure if we need these- interesting stuff here, but perhaps not what we want to study
        #self.onAxisError = 0
        #self.offAxisError = 0

    def execTrial(self):
        time.sleep(fixationTime/1000)
        ### records the trial starting time
        self.startTime = dateTime.time()

        ### this should center the mouse
        screenSize = mouse.screen_size()
        mouse.move( int(mouse.screen_size[0]/2), int(mouse.screen_size[2]/2))

        ## clean everything out of the experimet panel
        experiment.mainPanel.removeAll()

        currentTarget =


class experiment(swing.JFrame):
    def __init__(self):
        ## so an experiment is both a data structure containing the sequence of events, and the actual window
        self.setUndecorated(true)
        self.mainPanel = swing.JPanel()
        self.add(self.mainPanel)
        self.size = (1024,768)
        ### need to make this fullscreen somehow
        self.show()
        self.showInstructionPage()

        self.conditionBuilder = conditionBuilder()

    def showInstructionPage(self):
        self.mainPanel.add(swing.JLabel('You are going to be clicking on targets.  When you are done, recenter the mouse.'))
        continueButton = swing.JButton()
        continueButton.add(swing.JLabel('I understand- start the experiment.'))
        ### this is like adding a listener- it just associated the button with a method
        continueButton.actionPerformed(self.callback_startExperiment)
        self.mainPanel.add(continueButton)

    def callback_startExperiment(self):
        ##... generate the first trial





class settings():
    def __init__(self):
        ## just guessing what these would be
        self.targetRadiusList = []
        self.targetDistanceList = []
        self.targetShapeList = []
        self.trialsPerCondition = 50
        ### this is the time to display the fixatin cross in between trials, in ms
        self.fixationTime = 10
        ### this is the number of training trials that the subject will get initially.  these will not be recorded.
        self.trainingTrialNumber = 10
        ### this is to allow the subject to take periodic breaks, say every 25 trials
        self.breakNumber = 0
        self.breakTime = 0
        #### if the person is taking too long, time out and redo the trial
        self.timeOutTime = 5000





class setupWindow(swing.JFrame):
    def __init__(self):
        self.mainPanel = swing.JPanel()
        #self.mainPanel.pack()
        self.add(self.mainPanel)
        self.size = (1024,768)
        self.show()


    def create_Buttons(self):
        ### build the settings buttons, sliders, etc.


class introWindow(swing.JFrame):
    def __init__(self):
        self.size = (512,512)

        self.mainPanel = swing.JPanel(preferredSize = (512, 512))

        self.editSettings = swing.JButton()
        settingsLabel = swing.JLabel('Edit Settings')
        self.editSettings.add(settingsLabel)
        self.editSettings.actionPerformed = self.callback_editSettings
        self.mainPanel.add(self.editSettings)

        self.startExperiment = swing.JButton()
        expStartLabel = swing.JLabel('Start Experiment')
        self.startExperiment.add(expStartLabel)
        self.startExperiment.actionPerformed = self.callback_startExperiment
        self.mainPanel.add(self.startExperiment)

        #self.mainPanel.pack()
        self.mainPanel.show()
        self.add(self.mainPanel)
        self.show()


    def callback_editSettings(self, event):
        sWindow = setupWindow()


    def callback_startExperiment(self, event):
        x = 1


if __name__ == "__main__":
    mouse = PyMouse()
    ## this is a global, but whatever
    test = introWindow()
