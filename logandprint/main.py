"""
Log and Print
pip install logandprint

This module is used to log messages in a file and, if debug mode is enabled, in the console.

Author: Guilherme Saldanha
"""

import time
import datetime
import os
import sys
from datetime import date
from inspect import getframeinfo, stack
import re
import csv

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
        sys.exit('Error creating directory for: ' + logFile + ' - ' + str(e))


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
        sys.exit('Error creating file: ' + logFile + ' - ' + str(e))


def write(msg, console=True, type=''):
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

            # separator = '\\' if '\\' in origin.filename else '/'
            # if type != '' and not origin.filename.endswith('logandprint' + separator + 'main.py'):
            if type != '':
                origin = getframeinfo(stack()[2][0])

            spaceFileName = len(os.path.dirname(origin.filename)) + 25
            numSpacesAfterFileName = spaceFileName - (len(os.path.basename(origin.filename)) + len(os.path.dirname(origin.filename)) + len(str(origin.lineno)))

            msgType = type if type != '' else 'LOG'
            spaceMsgType = 7
            numSpacesAfterMsgType = spaceMsgType - len(msgType)


            logMsg = time.strftime("%Y-%m-%d %H:%M:%S") + ' - [' + origin.filename + ':' + str(origin.lineno) + '] ' + ' ' * numSpacesAfterFileName + ' - ' + msgType + ' ' * numSpacesAfterMsgType + ' - ' + str(msg)

            if printInConsole or console:
                match type:
                    case 'INFO':
                        print('\033[96m' + logMsg + '\033[0m')
                    case 'ERROR':
                        print('\033[91m' + logMsg + '\033[0m')
                    case 'SUCCESS':
                        print('\033[92m' + logMsg + '\033[0m')
                    case 'WARNING':
                        print('\033[93m' + logMsg + '\033[0m')
                    case _:
                        print(logMsg)

            logMsg = logMsg + '\n'
            with open(logFile, 'a+', encoding="UTF-8") as f:
                f.write(logMsg)
    except OSError as e:
        sys.exit('Error writing to file: ' + logFile + ' - ' + str(e))


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


def info(msg, console=True):
    """
    Write a info message in the log file.

    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    write(msg, console, 'INFO')


def error(msg, console=True):
    """
    Write a error message in the log file.

    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    write(msg, console, 'ERROR')


def success(msg, console=True):
    """
    Write a success message in the log file.

    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    write(msg, console, 'SUCCESS')


def warning(msg, console=True):
    """
    Write a warning message in the log file.

    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    write(msg, console, 'WARNING')


def export_to_csv(file='./log.csv'):
    """
    Export the log file to a csv file.
    """
    global logFile
    global enable

    try:
        if enable:
            data = []
            pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - \[(.*?):(\d+)\]\s+-\s+(\w+)\s+-\s+(.+)'
            with open(logFile, 'r', encoding="UTF-8") as log_file:
                for line in log_file:
                    match = re.match(pattern, line)
                    if match:
                        timestamp, arquivo, linha, nivel, mensagem = match.groups()
                        data.append([timestamp.strip(), arquivo.strip(), linha.strip(), nivel.strip(), mensagem.strip()])

            with open(file, 'w+', newline='') as csv_file:
                header = ['Date and Time', 'File', 'Line', 'Level', 'Message']
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow(header)
                writer.writerows(data)

    except OSError as e:
        sys.exit('Error exporting to csv file: ' + logFile + ' - ' + str(e))
