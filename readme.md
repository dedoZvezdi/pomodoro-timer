# Pomodoro Timer

A simple Pomodoro timer application for managing study and rest sessions.
The core idea is minimal pomodoro timer taking the minimal space of the screen.
There's also animations with sonic sprites.

## Features

- Two configurable session types: Study and Rest
- Session navigation with arrow keys 
- Timer control with spacebar (pause and resume)
- Customizable session durations via pop up window by pressing ESC
- Sonic animations. Running in study session. Waiting in rest session
- Dissapiring circle indicating how much time until timer stops

## Controls

- **Left/Right Arrow Keys**: Switch between Study and Rest sessions
- **Spacebar**: Start/Stop timer
- **Escape**: Open the configuration window
- **Enter**: Load updated times from configuration file

## Configuration

1. Press ESCAPE to open configuration window
2. Edit session durations as needed  
3. Press Enter in the application to apply changes
**Note: When the popup window has been opened, the state of the timer in main window will be lost.**

if ```config.json``` is deleted, program generate this file with default configuration.

## Required packages

- Make sure python 3.x is installed on your machine
- Install pygame module with
```bash
pip install pygame
```

## How to run
### For linux distros
```bash
python3 main.py
```

### For Windows
```bash
python main.py
```