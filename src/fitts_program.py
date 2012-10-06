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
import math
from pymouse import PyMouse
### note that is is pymouse 1.0, available here
### http://pepijndevos.nl/2010/04/pymouse-mouse-control-and-events-on-python/index.html
## this is how you use it
##http://code.google.com/p/pymouse/wiki/Documentation
## pymouse is what you use to get the mouse coordinates

class target(swing.JButton):
    def __init__(self,targetWidth,xPos, yPos):
        ### radius is something that will be fed to this at instantiation from the condition generator
        ### all of our targets will be squares.
        ### xpos and ypos is the CENTER of the target
        self.targetWidth = targetWidth
        self.color = awt.Color.BLUE
        self.hide()
        self.position =([xPos, yPos])
        ### this actually needs to change, I think- it depends what we are doing for target width.  length along movement axis?
        ### INTERESTING
        self.sideLength = self.targetWidth/math.sqrt(2)


    def draw(self):
        ## should not be necessary, but in case it is not refreshing, call this
        self.show()
        self.validate()
        self.repaint()

class trialCondition():
    def __init__(self):
        ### this is whether the border is there to simulate 'fullscreen'
        self.windowBorderPresent = "False"
        self.targetWidth = 0
        self.targetX = 0
        self.targetY = 0


class trialListBuilder():
    def __init__(self,settings):
        ### some sort of latin square logic here
        ### it looks at the information in the settings file, and is able to output the
        ### appropriate trial at a given time
        ### so first we make a condition list of all conditions
        self.conditionList = []
        #test condition
        self.conditionList.append(condition(self.targetWidth, self.currenttargetDistance))
        ### then we need to build a TRIAL list with multiple trials per condition
        ### and then we do the ordering in a certain way
        ####### populate list

    def generateNewTrialList(self):
        self.trialList = []
        ## so we acc trialCondtions objects to this



    def getTrial(self):
        ### so the trial object will call this to get this information
        trial = self.trialList[-1]
        return trial

    def remove_Recent(self):
        self.trialList.pop()
        ###so it is important NOT to call this until there has been a SUCCESSFUL trial- that is, there was NOT a miss
        ### technically you might need to reorder the whole square if there was a miss, but who cares, really :)


class trial():
    def __init__(self, fixationTime, timeoutTime, trialCondition):
        ### code for carrying out an actual trial
        ### the sequence is: render fixation cross, wait fixation time, display target, wait for mouse click on target, write information,
        ### condition is an object
        self.movementTime = 0
        self.targetCoordinates = []
        ## calculate the target coordinates here
        self.targetX = 0
        self.targetY = 0
        self.mouseClickX = 0
        self.mouseClickY = 0
        ### so, if a click is outside the target (a 'miss') we need to THROW IT OUT, put it back into the condition builder, then redo the latin square thing


    def execTrial(self):
        time.sleep(fixationTime/1000)
        ### records the trial starting time
        self.startTime = dateTime.time()

        ### this should center the mouse
        screenSize = mouse.screen_size()
        mouse.move( int(mouse.screen_size[0]/2), int(mouse.screen_size[2]/2))

        ## clean everything out of the experiment pane
        ## experiment needs to be a global
        experiment.mainPanel.removeAll()

        currentTarget = target(trialCondition.targetWidth, trialCondition.targetX, trialCondition.targetY)


        ### question to answer: are we ok with misses?

class experiment(swing.JFrame):
    def __init__(self, settings):
        ## so an experiment is both a data structure containing the sequence of events, and the actual window
        self.setUndecorated(true)
        self.mainPanel = swing.JPanel()
        self.add(self.mainPanel)
        self.size = (1024,768)
        ### need to make this fullscreen somehow
        self.show()
        self.showInstructionPage()
        ### these times are in ms
        self.fixationTime = settings.fixationTime
        self.timeoutTime =  settings.self.timeoutTime
        self.trialListBuilder = trialListBuilder()

    def showInstructionPage(self):
        self.mainPanel.add(swing.JLabel('You are going to be clicking on targets.  When you are done, recenter the mouse.'))
        continueButton = swing.JButton()
        continueButton.add(swing.JLabel('I understand- start the experiment.'))
        ### this is like adding a listener- it just associated the button with a method
        continueButton.actionPerformed(self.callback_startExperiment)
        self.mainPanel.add(continueButton)

    def callback_startExperiment(self):
        self.trialListBuilder.getTrial(self.fixationTime, self.timeoutTime, self.trialListBuilder.getTrial())





class settings():
    def __init__(self):
        ## just guessing what these would be
        self.targetRadiusList = []
        self.targetDistanceList = []
        self.trialsPerCondition = 50
        ### this is the time to display the fixatin cross in between trials, in ms
        self.fixationTime = 10
        ### this is the number of training trials that the subject will get initially.  these will not be recorded.
        self.trainingTrialNumber = 10
        ### this is to allow the subject to take periodic breaks, say every 25 trials
        self.breakNumber = 0
        self.breakTime = 0
        #### if the person is taking too long, time out and redo the trial
        self.timeoutTime = 5000





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
