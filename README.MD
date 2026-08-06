# Log and Print

[![PyPI version](https://img.shields.io/pypi/v/logandprint)](https://pypi.org/project/logandprint/) [![License](https://img.shields.io/github/license/guisaldanha/logandprint)](LICENSE) [![Downloads](https://img.shields.io/pypi/dm/logandprint?cacheSeconds=86400)](https://pypi.org/project/logandprint/)

A simple logging package that helps you to log what is happening in your application.

## Installation

You can install [Log and Print](https://pypi.org/project/logandprint/) using pip:

```bash
pip install logandprint
```

## Usage

To start logging it is as simple as importing the logandprint object and issuing the logging commands:

### write, info, error, success, warning, debug

To logging a message to the log:

```python
import logandprint as log

log.write("This is a common log message")
log.info("This is log information, it appears blue in the terminal")
log.error("This is an error message, it appears red in the terminal")
log.success("This is a success message, it appears green in the terminal")
log.warning("This is a warning message, it appears yellow in the terminal")
log.debug("This is a debug message, it appears white in the terminal")
```

The `write`, `info`, `error`, `success`, `warning` methods accept two parameters, the message and the console flag (boolean) to display or not the message in the terminal.

In the `debub` method, messages will only be displayed in the terminal if debug mode is active `log.debugMode(True)`

### setLogFile

By default, the log is saved in the `log.log` file in the current directory. But you can change the log file by using the `setLogFile` function.

```python
log.setLogFile("./logs/myLogFile.log")
```

### setMaxFileSize

By default, the log file is rotated once it reaches 2,000,000 bytes (2MB), or when the day changes. You can change the maximum size (in bytes) with `setMaxFileSize`.

```python
log.setMaxFileSize(10000000)  # 10MB
```

### setBackupCount

When the log file is rotated, by default 1 backup is kept (`myLogFile.log.bak1`). You can change how many backups are kept with `setBackupCount`. Older backups are shifted (`.bak1` -> `.bak2`, and so on) and the oldest one beyond the configured count is discarded.

```python
log.setBackupCount(3)  # keeps myLogFile.log.bak1, .bak2 and .bak3
```

Set it to `0` to disable backups entirely: the log file is simply cleared on rotation instead of being kept, which is the fastest option if you don't care about old logs.

```python
log.setBackupCount(0)
```

### debugMode

The log packet will not be printed to the console. You can change this by setting `debugMode` to True.

```python
log.debugMode(True)
```

To stop printing to the console, change the `debugMode` setting to False. Don't worry, the log file will still be writing.

```python
log.debugMode(False)
```

### enable

To disable the `log` you can call the `enable` function and set it to False.

```python
log.enable(False)
```

And to enable it again you can call the `enable` function and set it to True.

```python
log.enable(True)
```

### export_to_csv

You can export the log to a csv file by calling the `export_to_csv` function.

```python
log.export_to_csv("./logs/myLogFile.csv")
```

## Author

- Guilherme Saldanha

## Copyright

This software is free to use and distribute. You can use it for any purpose, but please give credit to the original author.

For more info see LICENSE file.
