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

import csv
import re

_enabled = True
printInConsole = False
logFile = './log.log'
maxFileSize = 2000000
backupCount = 1

_fileHandle = None
_openLogFile = None
_currentFileSize = 0
_currentFileDate = None


def checkDir():
    """
    Check if the log directory exists. If not, it will be created.
    """
    global logFile
    try:
        dirName = os.path.dirname(logFile)
        if dirName and not os.path.isdir(dirName):
            os.makedirs(dirName)
    except OSError as e:
        sys.exit('Error creating directory for: ' + logFile + ' - ' + str(e))


def _closeFile():
    """
    Close the currently open log file handle, if any.
    """
    global _fileHandle
    if _fileHandle is not None:
        try:
            _fileHandle.close()
        except OSError:
            pass
        _fileHandle = None


def _rotate():
    """
    Rotate the current log file into backup files (logFile.bak1, logFile.bak2, ...).
    The number of backups kept is controlled by backupCount. If backupCount is 0,
    the log file is simply removed, with no backup kept.
    """
    global _fileHandle
    _closeFile()
    try:
        if backupCount > 0:
            oldest = logFile + '.bak' + str(backupCount)
            if os.path.isfile(oldest):
                os.remove(oldest)
            for i in range(backupCount - 1, 0, -1):
                src = logFile + '.bak' + str(i)
                dst = logFile + '.bak' + str(i + 1)
                if os.path.isfile(src):
                    os.replace(src, dst)
            if os.path.isfile(logFile):
                os.replace(logFile, logFile + '.bak1')
        elif os.path.isfile(logFile):
            os.remove(logFile)
    except OSError as e:
        sys.exit('Error rotating file: ' + logFile + ' - ' + str(e))


def _openFile():
    """
    Ensure a log file handle is open and ready to be written to, keeping it open
    across calls instead of reopening it on every write. Also (re)loads the
    in-memory file size/date used to decide when rotation is due, so that decision
    doesn't require a filesystem stat() on every write.
    """
    global _fileHandle, _openLogFile, _currentFileSize, _currentFileDate
    if _fileHandle is not None and _openLogFile == logFile:
        return _fileHandle
    checkDir()
    try:
        if os.path.isfile(logFile):
            _currentFileSize = os.path.getsize(logFile)
            _currentFileDate = datetime.datetime.fromtimestamp(os.path.getmtime(logFile)).date()
        else:
            _currentFileSize = 0
            _currentFileDate = date.today()
        _fileHandle = open(logFile, 'ab')
        _openLogFile = logFile
        return _fileHandle
    except OSError as e:
        sys.exit('Error creating file: ' + logFile + ' - ' + str(e))


def write(msg, console=True, type=''):
    """
    Write a message in the log file.

    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    global _currentFileSize, _currentFileDate
    try:
        if _enabled:
            frame = sys._getframe(2 if type != '' else 1)
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno

            spaceFileName = len(os.path.dirname(filename)) + 25
            numSpacesAfterFileName = spaceFileName - (len(os.path.basename(filename)) + len(os.path.dirname(filename)) + len(str(lineno)))

            msgType = type if type != '' else 'LOG'
            spaceMsgType = 7
            numSpacesAfterMsgType = spaceMsgType - len(msgType)

            logMsg = time.strftime("%Y-%m-%d %H:%M:%S") + ' - [' + filename + ':' + str(lineno) + '] ' + ' ' * numSpacesAfterFileName + ' - ' + msgType + ' ' * numSpacesAfterMsgType + ' - ' + str(msg)

            if printInConsole or console:
                match type:
                    case 'INFO':
                        print('\033[96m' + logMsg + '\033[0m') # cyan
                    case 'ERROR':
                        print('\033[91m' + logMsg + '\033[0m') # red
                    case 'SUCCESS':
                        print('\033[92m' + logMsg + '\033[0m') # green
                    case 'WARNING':
                        print('\033[93m' + logMsg + '\033[0m') # yellow
                    case 'DEBUG':
                        print('\033[97m' + logMsg + '\033[0m') # white
                    case _:
                        print(logMsg)

            encoded = (logMsg + '\n').encode('UTF-8')

            fileHandle = _openFile()

            if date.today() != _currentFileDate or _currentFileSize + len(encoded) > maxFileSize:
                _rotate()
                fileHandle = _openFile()

            fileHandle.write(encoded)
            fileHandle.flush()
            _currentFileSize += len(encoded)
            _currentFileDate = date.today()
    except OSError as e:
        sys.exit('Error writing to file: ' + logFile + ' - ' + str(e))


def setLogFile(file):
    """
    With this function you can set the log file, the file and directories will be created if it doesn't exist. The default log file is './log.log'.
    """
    global logFile
    if file != logFile:
        _closeFile()
    logFile = file


def setMaxFileSize(size):
    """
    Set the maximum size, in bytes, the log file can reach before it is rotated.
    The default is 2,000,000 bytes (2MB).
    """
    global maxFileSize
    maxFileSize = size


def setBackupCount(count):
    """
    Set how many rotated backup files (logFile.bak1, logFile.bak2, ...) are kept when
    the log file is rotated (because it reached the maximum size or a new day started).
    The default is 1. Set to 0 to disable backups: the log file will be deleted instead
    of rotated, same as the old behaviour.
    """
    global backupCount
    backupCount = count


def enable(active):
    """
    This function will enable or disable the log.
    """
    global _enabled
    _enabled = active
    if not active:
        _closeFile()


def debugMode(active):
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


def debug(msg):
    """
    Write a debug message in the log file.

    param msg: The message to be logged.
    param console: If you want to print the message in the console.
    """
    write(msg, False, 'DEBUG')


def export_to_csv(file='./log.csv'):
    """
    Export the log file to a csv file.
    """
    global logFile
    global _enabled

    try:
        if _enabled:
            if _fileHandle is not None:
                _fileHandle.flush()

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
