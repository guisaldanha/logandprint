# Log and Print

A simple logging package that helps you to log what is happening in your application.

## Installation

You can install `LogAndPrint` using pip:

```bash
pip install logandprint
```

## Usage

To start logging it is as simple as importing the logandprint object and issuing the logging commands:

### write

To write a message to the log:

```python
import logandprint as log

log.write("This is a message that will be logged")
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

To disable the `logg` you can call the `enable` function and set it to False.

```python
log.enable(False)
```

And to enable it again you can call the `enable` function and set it to True.

```python
log.enable(True)
```

## Author

- Guilherme Saldanha

## Copyright

This software is free to use and distribute. You can use it for any purpose, but please give credit to the original author.

For more info see LICENSE file.
