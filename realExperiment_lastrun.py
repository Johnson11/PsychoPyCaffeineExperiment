#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Thu 25 Jun 2015 02:54:36 PM CEST
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'realExperiment'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/realExperiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "testTrial"
testTrialClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u"English:\nWelcome to our experiment.\nIn this experiment you are asked to press the 'Space' button as soon as you detect a switch.\nEach trial lasts 1.5 minutes for all in all 6 trials.\nThe following trial is a Test-Trial where you can get prepared for the experiment. The Test-Trial will be presented for 10 seconds.\nThe distance in the Test Trial differs from the one calculated before.\nPress 'Space' to continue\n\nDeutsch:\nWillkommen zu unserem Experiment!\nDruecken Sie bitte so schnell wie moeglich die 'Leertaste' sobald sie eine Veraenderung in der Bewegungsrichtung sehen. \nJeder Test dauert 1.5 Minuten jeweils 6 Mal.\nDer folgende Versuch ist nur ein Test und dauert 10 Sekunden. Machen Sie sich mit dem Stimuli vertraut. \nDie Distanz ist jedoch nicht ihre individuelle sondern willkuerlich gewaehlt. \nViel Spass!\nDr\xfccken Sie die Leertaste um weiterzufahren.",    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "testTrial_Setup"
testTrial_SetupClock = core.Clock()
cubeLU = visual.ImageStim(win=win, name='cubeLU',
    image='cube.png', mask=None,
    ori=0, pos=[-0.3, 0.5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
cubeRD = visual.ImageStim(win=win, name='cubeRD',
    image='cube.png', mask=None,
    ori=0, pos=[0.3,-0.5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
cubeLD = visual.ImageStim(win=win, name='cubeLD',
    image='cube.png', mask=None,
    ori=0, pos=[-0.3, -0.5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cubeRU = visual.ImageStim(win=win, name='cubeRU',
    image='cube.png', mask=None,
    ori=0, pos=[0.3, 0.5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
WW = 0.05
HH = 0.075

image = visual.ImageStim(win=win, name='image',
    image='fixcross.png', mask=None,
    ori=0, pos=[0, 0], size=[0.1, 0.1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
text = visual.TextStim(win=win, ori=0, name='text',
    text='Now the real experiment starts.\nThe changing dots will be presented in 6 trials that each last 1.5 minutes.\nAfter each trial a short break is placed. Feel free to stand up or drink in that time, and as soon as you feel ready \nPress "Space" to continue',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "resetClock"
resetClockClock = core.Clock()
CurrentTime = 0.0


# Initialize components for Routine "DistanceCheck"
DistanceCheckClock = core.Clock()
with open("./ScreenRatio") as f:
    content = f.readlines()

ScreenH = float(content[0])
ScreenV = float(content[1])


DISTANCE = 1.0

YPOS = DISTANCE
XPOS = 5/(ScreenH/2)


W = 0.05
H = 0.075

my_time = 0
String = []
String.append(expInfo['participant'])

newString = "./DISTANCES/%s"%expInfo['participant']
with open(newString) as f:
    NR = float(f.readline())

print DISTANCE,NR,"##############"
YPOS = NR
XPOS = (YPOS*ScreenV)/ScreenH
if YPOS == 1.0:
    print "ERROR!"
    win.close()
    core.quit()

JustinClock = core.Clock()
blockLU = visual.ImageStim(win=win, name='blockLU',
    image='cube.png', mask=None,
    ori=0, pos=[-XPOS, YPOS], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
blockRD = visual.ImageStim(win=win, name='blockRD',
    image='cube.png', mask=None,
    ori=0, pos=[XPOS, -YPOS], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
blockLD = visual.ImageStim(win=win, name='blockLD',
    image='cube.png', mask=None,
    ori=0, pos=[-XPOS, -YPOS], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blockRU = visual.ImageStim(win=win, name='blockRU',
    image='cube.png', mask=None,
    ori=0, pos=[XPOS, YPOS], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
fixcross = visual.ImageStim(win=win, name='fixcross',
    image='fixcross.png', mask=None,
    ori=0, pos=[0, 0], size=[0.1, 0.1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "BreakScreen"
BreakScreenClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
ROUND = 1
textPause = "End of Round %s. %s to go! \nTake a break and press 'Space' as soon as you are ready" % (ROUND,6-ROUND)


# Initialize components for Routine "whatFirst"
whatFirstClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Done!\nThank You for your participation!\n\nThis Screen will automatically close in 5 Seconds\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "testTrial"-------
t = 0
testTrialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
testTrialComponents = []
testTrialComponents.append(text_4)
testTrialComponents.append(key_resp_5)
for thisComponent in testTrialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "testTrial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = testTrialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "testTrial"-------
for thisComponent in testTrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "testTrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=12, method='random', 
    extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/realExperiment.psyexp',
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "testTrial_Setup"-------
    t = 0
    testTrial_SetupClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    cubeLU.setSize([WW, HH])
    cubeRD.setSize([WW, HH])
    cubeLD.setSize([WW, HH])
    cubeRU.setSize([WW, HH])
    WW = 0.05
    HH = 0.075
    
    # keep track of which components have finished
    testTrial_SetupComponents = []
    testTrial_SetupComponents.append(cubeLU)
    testTrial_SetupComponents.append(cubeRD)
    testTrial_SetupComponents.append(cubeLD)
    testTrial_SetupComponents.append(cubeRU)
    testTrial_SetupComponents.append(image)
    for thisComponent in testTrial_SetupComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "testTrial_Setup"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testTrial_SetupClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cubeLU* updates
        if t >= 0.0 and cubeLU.status == NOT_STARTED:
            # keep track of start time/frame for later
            cubeLU.tStart = t  # underestimates by a little under one frame
            cubeLU.frameNStart = frameN  # exact frame index
            cubeLU.setAutoDraw(True)
        if cubeLU.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
            cubeLU.setAutoDraw(False)
        
        # *cubeRD* updates
        if t >= 0.0 and cubeRD.status == NOT_STARTED:
            # keep track of start time/frame for later
            cubeRD.tStart = t  # underestimates by a little under one frame
            cubeRD.frameNStart = frameN  # exact frame index
            cubeRD.setAutoDraw(True)
        if cubeRD.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
            cubeRD.setAutoDraw(False)
        
        # *cubeLD* updates
        if t >= 0.4 and cubeLD.status == NOT_STARTED:
            # keep track of start time/frame for later
            cubeLD.tStart = t  # underestimates by a little under one frame
            cubeLD.frameNStart = frameN  # exact frame index
            cubeLD.setAutoDraw(True)
        if cubeLD.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
            cubeLD.setAutoDraw(False)
        
        # *cubeRU* updates
        if t >= 0.4 and cubeRU.status == NOT_STARTED:
            # keep track of start time/frame for later
            cubeRU.tStart = t  # underestimates by a little under one frame
            cubeRU.frameNStart = frameN  # exact frame index
            cubeRU.setAutoDraw(True)
        if cubeRU.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
            cubeRU.setAutoDraw(False)
        
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial_SetupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "testTrial_Setup"-------
    for thisComponent in testTrial_SetupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 12 repeats of 'trials'


#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
trialComponents = []
trialComponents.append(ISI)
trialComponents.append(text)
trialComponents.append(key_resp_2)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t  # underestimates by a little under one frame
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED: #one frame should pass before updating params and completing
        ISI.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
JustinClock.reset()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsReal = data.TrialHandler(nReps=6, method='random', 
    extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/realExperiment.psyexp',
    trialList=[None],
    seed=None, name='trialsReal')
thisExp.addLoop(trialsReal)  # add the loop to the experiment
thisTrialsReal = trialsReal.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrialsReal.rgb)
if thisTrialsReal != None:
    for paramName in thisTrialsReal.keys():
        exec(paramName + '= thisTrialsReal.' + paramName)

for thisTrialsReal in trialsReal:
    currentLoop = trialsReal
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsReal.rgb)
    if thisTrialsReal != None:
        for paramName in thisTrialsReal.keys():
            exec(paramName + '= thisTrialsReal.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    timeGetterTrial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/realExperiment.psyexp',
        trialList=[None],
        seed=None, name='timeGetterTrial')
    thisExp.addLoop(timeGetterTrial)  # add the loop to the experiment
    thisTimeGetterTrial = timeGetterTrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTimeGetterTrial.rgb)
    if thisTimeGetterTrial != None:
        for paramName in thisTimeGetterTrial.keys():
            exec(paramName + '= thisTimeGetterTrial.' + paramName)
    
    for thisTimeGetterTrial in timeGetterTrial:
        currentLoop = timeGetterTrial
        # abbreviate parameter names if possible (e.g. rgb = thisTimeGetterTrial.rgb)
        if thisTimeGetterTrial != None:
            for paramName in thisTimeGetterTrial.keys():
                exec(paramName + '= thisTimeGetterTrial.' + paramName)
        
        #------Prepare to start Routine "resetClock"-------
        t = 0
        resetClockClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        CookieClock = core.Clock()
        
        # keep track of which components have finished
        resetClockComponents = []
        for thisComponent in resetClockComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "resetClock"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = resetClockClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in resetClockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "resetClock"-------
        for thisComponent in resetClockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "resetClock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        repetitionsOfDistanceCheck = data.TrialHandler(nReps=113, method='random', 
            extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/realExperiment.psyexp',
            trialList=[None],
            seed=None, name='repetitionsOfDistanceCheck')
        thisExp.addLoop(repetitionsOfDistanceCheck)  # add the loop to the experiment
        thisRepetitionsOfDistanceCheck = repetitionsOfDistanceCheck.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisRepetitionsOfDistanceCheck.rgb)
        if thisRepetitionsOfDistanceCheck != None:
            for paramName in thisRepetitionsOfDistanceCheck.keys():
                exec(paramName + '= thisRepetitionsOfDistanceCheck.' + paramName)
        
        for thisRepetitionsOfDistanceCheck in repetitionsOfDistanceCheck:
            currentLoop = repetitionsOfDistanceCheck
            # abbreviate parameter names if possible (e.g. rgb = thisRepetitionsOfDistanceCheck.rgb)
            if thisRepetitionsOfDistanceCheck != None:
                for paramName in thisRepetitionsOfDistanceCheck.keys():
                    exec(paramName + '= thisRepetitionsOfDistanceCheck.' + paramName)
            
            #------Prepare to start Routine "DistanceCheck"-------
            t = 0
            DistanceCheckClock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.800000)
            # update component parameters for each repeat
            
            key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            key_resp_3.status = NOT_STARTED
            # keep track of which components have finished
            DistanceCheckComponents = []
            DistanceCheckComponents.append(blockLU)
            DistanceCheckComponents.append(blockRD)
            DistanceCheckComponents.append(blockLD)
            DistanceCheckComponents.append(blockRU)
            DistanceCheckComponents.append(fixcross)
            DistanceCheckComponents.append(key_resp_3)
            for thisComponent in DistanceCheckComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "DistanceCheck"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = DistanceCheckClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if key_resp_3.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                        time_tmp = CookieClock.getTime()-CurrentTime
                        String.append(str(time_tmp))
                
                
                
                # *blockLU* updates
                if t >= 0.0 and blockLU.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blockLU.tStart = t  # underestimates by a little under one frame
                    blockLU.frameNStart = frameN  # exact frame index
                    blockLU.setAutoDraw(True)
                if blockLU.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                    blockLU.setAutoDraw(False)
                
                # *blockRD* updates
                if t >= 0.0 and blockRD.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blockRD.tStart = t  # underestimates by a little under one frame
                    blockRD.frameNStart = frameN  # exact frame index
                    blockRD.setAutoDraw(True)
                if blockRD.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                    blockRD.setAutoDraw(False)
                
                # *blockLD* updates
                if t >= 0.4 and blockLD.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blockLD.tStart = t  # underestimates by a little under one frame
                    blockLD.frameNStart = frameN  # exact frame index
                    blockLD.setAutoDraw(True)
                if blockLD.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                    blockLD.setAutoDraw(False)
                
                # *blockRU* updates
                if t >= 0.4 and blockRU.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blockRU.tStart = t  # underestimates by a little under one frame
                    blockRU.frameNStart = frameN  # exact frame index
                    blockRU.setAutoDraw(True)
                if blockRU.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                    blockRU.setAutoDraw(False)
                
                # *fixcross* updates
                if t >= 0.0 and fixcross.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixcross.tStart = t  # underestimates by a little under one frame
                    fixcross.frameNStart = frameN  # exact frame index
                    fixcross.setAutoDraw(True)
                if fixcross.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixcross.setAutoDraw(False)
                
                # *key_resp_3* updates
                if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_3.tStart = t  # underestimates by a little under one frame
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    key_resp_3.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if key_resp_3.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
                    key_resp_3.status = STOPPED
                if key_resp_3.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_3.rt = key_resp_3.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in DistanceCheckComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "DistanceCheck"-------
            for thisComponent in DistanceCheckComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            my_time = my_time + 0.8
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
               key_resp_3.keys=None
            # store data for repetitionsOfDistanceCheck (TrialHandler)
            repetitionsOfDistanceCheck.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                repetitionsOfDistanceCheck.addData('key_resp_3.rt', key_resp_3.rt)
            thisExp.nextEntry()
            
        # completed 113 repeats of 'repetitionsOfDistanceCheck'
        
        
        #------Prepare to start Routine "BreakScreen"-------
        t = 0
        BreakScreenClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        text_3.setText(textPause

)
        key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_4.status = NOT_STARTED
        ROUND = ROUND + 1
        textPause = "End of Round %s. %s to go! \nTake a break and press 'Space' as soon as you are ready" % (ROUND,6-ROUND)
        
        
        
        # keep track of which components have finished
        BreakScreenComponents = []
        BreakScreenComponents.append(text_3)
        BreakScreenComponents.append(key_resp_4)
        for thisComponent in BreakScreenComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "BreakScreen"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = BreakScreenClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t  # underestimates by a little under one frame
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            
            # *key_resp_4* updates
            if t >= 0.0 and key_resp_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_4.tStart = t  # underestimates by a little under one frame
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "BreakScreen"-------
        for thisComponent in BreakScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        JustinClock.reset()
        # the Routine "BreakScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'timeGetterTrial'
    
    thisExp.nextEntry()
    
# completed 6 repeats of 'trialsReal'


#------Prepare to start Routine "whatFirst"-------
t = 0
whatFirstClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
whatFirstComponents = []
whatFirstComponents.append(text_2)
for thisComponent in whatFirstComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "whatFirst"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = whatFirstClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and t >= (0.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in whatFirstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "whatFirst"-------
for thisComponent in whatFirstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





win.close()
core.quit()
