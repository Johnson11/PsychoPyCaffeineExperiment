#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Thu 25 Jun 2015 02:52:35 PM CEST
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
expName = 'coffee_distCheck'  # from the Builder filename that created this script
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
    originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/coffee_distCheck.psyexp',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Englisch:\nFirst of all we will define your optimal distance.\nTherefore you are asked to fixate the cross in the middle of the screen and report to press \'Space\' as soon as you see a switch.\nThe squares are first diverging in the vertical direction, so as soon you see horizontal movement press \'Space\'.\nThey are directly moving together, and again as soon you see a switch, so a movement into vertical direction, press \'Space\'.\nDo not press \'Space\' after that but wait instead for the end of the routine.\nPress "Space" to continue\n\nDeutsch: \nZu aller erst werden wir Ihre optimale Distanz der Quadrate bestimmen.\nDazu fixieren Sie bitte den Fixpunkt in der Mitte aber achten Sie trotzdem auf die vier Quadrate.\nSie werden beim ersten Blick eine bestimmte Bewegungsrichtung wahrnehmen, entweder horizontal oder vertikal.\nDie Quadrate werden in der vertikalen Richtung auseinandergehen und sobald Sie einen Wechsel in ihrer wahrgenommenen Bewegung wahrnehmen, dr\xfccken sie schnellstm\xf6glich die \'Leertaste\'. \nDas Ganze wird dann ebenfalls f\xfcr das Zusammenlaufen der Quarate in der vertikalen Richtung gemacht.\n',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "resetRoutine"
resetRoutineClock = core.Clock()


# Initialize components for Routine "DistanceCheck"
DistanceCheckClock = core.Clock()
with open("./ScreenRatio") as f:
    content = f.readlines()

ScreenH = float(content[0])
ScreenV = float(content[1])

YPOS = 0.1
XPOS = 9.08/(ScreenH/2)


demValues = []


W = 0.05
H = 0.075

changeRate=0.025



blockLU = visual.ImageStim(win=win, name='blockLU',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
blockRD = visual.ImageStim(win=win, name='blockRD',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
blockLD = visual.ImageStim(win=win, name='blockLD',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
cubeRU = visual.ImageStim(win=win, name='cubeRU',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
fixcross = visual.ImageStim(win=win, name='fixcross',
    image='fixcross.png', mask=None,
    ori=0, pos=[0, 0], size=[0.1, 0.1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "resetRoutine2"
resetRoutine2Clock = core.Clock()


# Initialize components for Routine "DistCheckV_"
DistCheckV_Clock = core.Clock()
blockLU2 = visual.ImageStim(win=win, name='blockLU2',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
blockRD2 = visual.ImageStim(win=win, name='blockRD2',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
blockLD2 = visual.ImageStim(win=win, name='blockLD2',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cubeRU2 = visual.ImageStim(win=win, name='cubeRU2',
    image='cube.png', mask=None,
    ori=0, pos=[0,0], size=[W, H],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_4 = visual.ImageStim(win=win, name='image_4',
    image='fixcross.png', mask=None,
    ori=0, pos=[0, 0], size=[0.1, 0.1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)


# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
finalText = "Thank You! \n Now we are set for the real experiment! \n Danke, jetzt koennen wir zum echten Experiment ueber gehen."

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
    if t >= 0.0 and text.status == NOT_STARTED:
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
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/coffee_distCheck.psyexp',
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
    
    #------Prepare to start Routine "resetRoutine"-------
    t = 0
    resetRoutineClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    YPOS = 0.1
    
    # keep track of which components have finished
    resetRoutineComponents = []
    for thisComponent in resetRoutineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "resetRoutine"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = resetRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resetRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "resetRoutine"-------
    for thisComponent in resetRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "resetRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    repetitionsOfDistanceCheck = data.TrialHandler(nReps=40, method='random', 
        extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/coffee_distCheck.psyexp',
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
        YPOS= YPOS + changeRate
        blockLU.setPos([-XPOS, YPOS])
        blockRD.setPos([XPOS, -YPOS])
        blockLD.setPos([-XPOS, -YPOS])
        cubeRU.setPos([XPOS, YPOS])
        key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_3.status = NOT_STARTED
        # keep track of which components have finished
        DistanceCheckComponents = []
        DistanceCheckComponents.append(blockLU)
        DistanceCheckComponents.append(blockRD)
        DistanceCheckComponents.append(blockLD)
        DistanceCheckComponents.append(cubeRU)
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
                    print YPOS
                    name = "./DISTANCES/%s"%(expInfo['participant'])
                    demValues.append(YPOS)
                    repetitionsOfDistanceCheck.finished=True
                   
            
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
            
            # *cubeRU* updates
            if t >= 0.4 and cubeRU.status == NOT_STARTED:
                # keep track of start time/frame for later
                cubeRU.tStart = t  # underestimates by a little under one frame
                cubeRU.frameNStart = frameN  # exact frame index
                cubeRU.setAutoDraw(True)
            if cubeRU.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                cubeRU.setAutoDraw(False)
            
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
        
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
           key_resp_3.keys=None
        # store data for repetitionsOfDistanceCheck (TrialHandler)
        repetitionsOfDistanceCheck.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            repetitionsOfDistanceCheck.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.nextEntry()
        
    # completed 40 repeats of 'repetitionsOfDistanceCheck'
    
    
    #------Prepare to start Routine "resetRoutine2"-------
    t = 0
    resetRoutine2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    YPOS = 0.95
    
    # keep track of which components have finished
    resetRoutine2Components = []
    for thisComponent in resetRoutine2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "resetRoutine2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = resetRoutine2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resetRoutine2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "resetRoutine2"-------
    for thisComponent in resetRoutine2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "resetRoutine2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    wiederholeBisTot = data.TrialHandler(nReps=40, method='random', 
        extraInfo=expInfo, originPath=u'/home/justin/PsychoPy/newCoffee/PsychoPyCaffeineExperiment/coffee_distCheck.psyexp',
        trialList=[None],
        seed=None, name='wiederholeBisTot')
    thisExp.addLoop(wiederholeBisTot)  # add the loop to the experiment
    thisWiederholeBisTot = wiederholeBisTot.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisWiederholeBisTot.rgb)
    if thisWiederholeBisTot != None:
        for paramName in thisWiederholeBisTot.keys():
            exec(paramName + '= thisWiederholeBisTot.' + paramName)
    
    for thisWiederholeBisTot in wiederholeBisTot:
        currentLoop = wiederholeBisTot
        # abbreviate parameter names if possible (e.g. rgb = thisWiederholeBisTot.rgb)
        if thisWiederholeBisTot != None:
            for paramName in thisWiederholeBisTot.keys():
                exec(paramName + '= thisWiederholeBisTot.' + paramName)
        
        #------Prepare to start Routine "DistCheckV_"-------
        t = 0
        DistCheckV_Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        blockLU2.setPos([-XPOS, YPOS])
        blockRD2.setPos([XPOS, -YPOS])
        blockLD2.setPos([-XPOS, -YPOS])
        
        YPOS= YPOS - changeRate
        key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_5.status = NOT_STARTED
        # keep track of which components have finished
        DistCheckV_Components = []
        DistCheckV_Components.append(blockLU2)
        DistCheckV_Components.append(blockRD2)
        DistCheckV_Components.append(blockLD2)
        DistCheckV_Components.append(cubeRU2)
        DistCheckV_Components.append(image_4)
        DistCheckV_Components.append(key_resp_5)
        for thisComponent in DistCheckV_Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "DistCheckV_"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = DistCheckV_Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blockLU2* updates
            if t >= 0.0 and blockLU2.status == NOT_STARTED:
                # keep track of start time/frame for later
                blockLU2.tStart = t  # underestimates by a little under one frame
                blockLU2.frameNStart = frameN  # exact frame index
                blockLU2.setAutoDraw(True)
            if blockLU2.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                blockLU2.setAutoDraw(False)
            
            # *blockRD2* updates
            if t >= 0.0 and blockRD2.status == NOT_STARTED:
                # keep track of start time/frame for later
                blockRD2.tStart = t  # underestimates by a little under one frame
                blockRD2.frameNStart = frameN  # exact frame index
                blockRD2.setAutoDraw(True)
            if blockRD2.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                blockRD2.setAutoDraw(False)
            
            # *blockLD2* updates
            if t >= 0.4 and blockLD2.status == NOT_STARTED:
                # keep track of start time/frame for later
                blockLD2.tStart = t  # underestimates by a little under one frame
                blockLD2.frameNStart = frameN  # exact frame index
                blockLD2.setAutoDraw(True)
            if blockLD2.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                blockLD2.setAutoDraw(False)
            
            # *cubeRU2* updates
            if t >= 0.4 and cubeRU2.status == NOT_STARTED:
                # keep track of start time/frame for later
                cubeRU2.tStart = t  # underestimates by a little under one frame
                cubeRU2.frameNStart = frameN  # exact frame index
                cubeRU2.setAutoDraw(True)
            if cubeRU2.status == STARTED and t >= (0.4 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                cubeRU2.setAutoDraw(False)
            if cubeRU2.status == STARTED:  # only update if being drawn
                cubeRU2.setPos([XPOS, YPOS], log=False)
            
            # *image_4* updates
            if t >= 0.0 and image_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_4.tStart = t  # underestimates by a little under one frame
                image_4.frameNStart = frameN  # exact frame index
                image_4.setAutoDraw(True)
            if image_4.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
                image_4.setAutoDraw(False)
            if key_resp_5.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                    print YPOS
                    demValues.append(YPOS)
                    wiederholeBisTot.finished=True
                  
            
            
            # *key_resp_5* updates
            if t >= 0.0 and key_resp_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_5.tStart = t  # underestimates by a little under one frame
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                key_resp_5.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_5.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_5.status = STOPPED
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
            for thisComponent in DistCheckV_Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "DistCheckV_"-------
        for thisComponent in DistCheckV_Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
           key_resp_5.keys=None
        # store data for wiederholeBisTot (TrialHandler)
        wiederholeBisTot.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            wiederholeBisTot.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.nextEntry()
        
    # completed 40 repeats of 'wiederholeBisTot'
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


#------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
text_4.setText(finalText)

# keep track of which components have finished
ThanksComponents = []
ThanksComponents.append(text_4)
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    if text_4.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_4.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





import numpy as np
means = np.mean(demValues)
print means
save = "./DISTANCES/%s" % expInfo['participant']
with open(save, "w") as myfile:
    myfile.write(str(means))
win.close()
core.quit()
