# Timer

## About

The timer is a count-down application. It count-downs from 10 sec to 0.
To reset the timer press f1/f2/f3/f4
To end the timer press f12

## Create Executable

```
pyinstaller --onefile timer.py
```

### Locate Your Executable:
After running the above command, PyInstaller will create a dist directory in the same folder as your script. Inside the dist directory, you'll find the standalone executable with the same name as your Python script (without the .py extension).

### Run Your Executable:
You can now run your standalone executable like you would with any other program. Just double-click on it (in Windows) or run it from the command line.