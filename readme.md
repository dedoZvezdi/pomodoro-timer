# Pomodoro Timer

A simple Pomodoro timer application for managing study and rest sessions.

## Features

- Two configurable session types: Study and Rest
- Session navigation with arrow keys 
- Timer control with spacebar
- Customizable session durations via external file
- Sonic animations. Running in study session. Waiting in rest session

## Controls

- **Left/Right Arrow Keys**: Switch between Study and Rest sessions
- **Spacebar**: Start/Stop timer
- **Escape**: Open time configuration file ("time.txt")
- **Enter**: Load updated times from configuration file

## Configuration

1. Press Escape to open "time.txt"
2. Edit session durations as needed  
3. Press Enter in the application to apply changes

## Intallation

- Make sure python 3.x is installed on your machine
- Install pygame module with
```bash
pip install pygame