# Log and Print

[![PyPI version](https://img.shields.io/pypi/v/logandprint)](https://pypi.org/project/logandprint/) [![License](https://img.shields.io/github/license/guisaldanha/logandprint)](LICENSE) [![Downloads](https://img.shields.io/pypi/dm/logandprint)](https://img.shields.io/pypi/dm/logandprint)

A simple logging package that helps you to log what is happening in your application.

## Installation

You can install [Log and Print](https://pypi.org/project/logandprint/) using pip:

```bash
pip install logandprint
```

## Usage

To start logging it is as simple as importing the logandprint object and issuing the logging commands:

### write

To write a message to the log:

```python
import logandprint as log

log.write("This is a common log message")
log.info("This is log information, it appears blue in the terminal")
log.error("This is an error message, it appears red in the terminal")
log.success("This is a success message, it appears green in the terminal")
log.warning("This is a warning message, it appears yellow in the terminal")
log.debug("This is a debug message, it appears white in the terminal")
log.log("This is a common log message, it is an alias for log.write")
log.print("This is a common log message and will be printed to the terminal")
```

### setLogFile

By default, the log is saved in the `log.log` file in the current directory. But you can change the log file by using the `setLogFile` function.

```python
log.setLogFile("./logs/myLogFile.log")
```

### debubMode

The log packet will not be printed to the console. You can change this by setting `debugMode` to True.

```python
log.debubMode(True)
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
