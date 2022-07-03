"""This module is used to log messages in a file and, if debug mode is enabled, in the console."""

import time
import datetime
import os
from datetime import date
from inspect import getframeinfo, stack

enable = True
printInConsole = False
logFile = './log.log'


def checkDir():
    """
    Check if the log directory exists. If not, it will be created.
    """
    global logFile
    global enable
    try:
        if enable:
            if not os.path.isdir(os.path.dirname(logFile)):
                os.makedirs(os.path.dirname(logFile))
    except OSError as e:
        die('Error creating directory for: ' + logFile + ' - ' + str(e))


def checkFile():
    """
    Check if the log file exists. If not, it will be created.
    Also, if the file is older than 1 day or larger than 5mb, it will be deleted.
    """
    global logFile
    global enable
    try:
        if enable:
            checkDir()
            if not os.path.isfile(logFile):
                with open(logFile, 'w+', encoding="UTF-8") as f:
                    f.write('')
            date1 = date.today()
            date2 = datetime.datetime.fromtimestamp(
                os.path.getmtime(logFile)).date()
            diff = abs(date1-date2).days
            if diff > 0 or os.path.getsize(logFile) > 5000000:
                os.remove(logFile)
    except OSError as e:
        die('Error creating file: ' + logFile + ' - ' + str(e))


def write(msg, console=True):
    """
    Write a message in the log file.
    
    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    global logFile
    global printInConsole
    global enable
    try:
        if enable:
            checkFile()

            origin = getframeinfo(stack()[1][0])

            spaceFileName = len(os.path.dirname(origin.filename)) + 25
            numSpacesAfterFileName = spaceFileName - (len(os.path.basename(origin.filename)) + len(
            os.path.dirname(origin.filename)) + len(str(origin.lineno)))

            logMsg = time.strftime("%Y-%m-%d %H:%M:%S") + ' - [' + origin.filename + ':' + str(
                origin.lineno) + '] ' + ' ' * numSpacesAfterFileName + ' - ' + str(msg)

            if printInConsole or console:
                print(logMsg)
            logMsg = logMsg + '\n'
            with open(logFile, 'a+', encoding="UTF-8") as f:
                f.write(logMsg)
    except OSError as e:
        die('Error writing to file: ' + logFile + ' - ' + str(e))


def setLogFile(file):
    """
    With this function you can set the log file, the file and directories will be created if it doesn't exist. The default log file is './log.log'. 
    """
    global logFile
    logFile = file


def enable(active):
    """
    This function will enable or disable the log.
    """
    global enable
    enable = active


def debubMode(active):
    """
    With this function you can enable or disable the debug mode. This will print the logs in the console.
    """
    global printInConsole
    printInConsole = active
