# Pomodoro Timer

A simple Pomodoro timer application for managing study and rest sessions.
The core idea is minimal pomodoro timer taking the minimal space of the screen.
There's also animations with sonic sprites.

## Features

- Two configurable session types: Study and Rest
- Session navigation with arrow keys 
- Timer control with spacebar (pause and resume)
- Customizable session durations via external file
- Sonic animations. Running in study session. Waiting in rest session
- Dissapiring circle indicating how much time until timer stops

## Controls

- **Left/Right Arrow Keys**: Switch between Study and Rest sessions
- **Spacebar**: Start/Stop timer
- **Escape**: Open time configuration file (```config.txt```)
- **Enter**: Load updated times from configuration file

## Configuration

1. Press Escape to open config_file
2. Edit session durations as needed  
3. Press Enter in the application to apply changes

if ```config.txt``` is deleted, program generate this file with default configuration.

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