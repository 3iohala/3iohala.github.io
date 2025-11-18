
# MIDI_naktis

An interactive terminal-based web game set in a mysterious space station. Navigate through locked doors, uncover hidden files, and piece together what happened at Station-TK through command-line exploration.

## 🎮 Game Overview

You're accessing the terminal system of Station-TK, a space station with locked doors and protected files. Use terminal commands to explore the station, open airlocks, and read classified documents to uncover the story.

## 🚀 Features

- **Retro Terminal Interface**: Built with xterm.js for an authentic command-line experience
- **Interactive Storytelling**: Discover the narrative through file fragments and transcripts
- **Password-Protected Content**: Some files and doors require passwords found during exploration
- **Audio & Visual Effects**: Cinematic alerts, glitch effects, and audio feedback when opening doors
- **Typewriter Effect**: Important messages display with a classic typing animation

## 📋 Requirements

- Python 3.9+
- Flask
- Modern web browser with JavaScript enabled

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url> cd terminalas
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv source .venv/bin/activate 
```
On Windows:
```bash
.venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install flask
```


## ▶️ Running the Game

1. Start the Flask server:
```bash
python app.py
```
2. Open your browser and navigate to:
[http://localhost:5000](http://localhost:5000)

3. Wait for the boot sequence to complete, then type `.komandos` to see available commands

## 🎯 Available Commands

- `.komandos` - Display all available commands
- `.skaityti [filename]` - Read a file (some require passwords)
- `.atidaryti_duris [door_code]` - Open station doors (some require passwords)

## 🎪 Gameplay Tips

- Start by typing `.komandos` to see what's available
- Read public files first - they may contain clues
- Door codes follow the format D## (e.g., D67)
- Passwords are case-sensitive
- Pay attention to transcripts and conversations



## 🎨 Technical Details

- **Backend**: Flask (Python) handles command processing and game state
- **Frontend**: xterm.js provides the terminal emulation
- **Effects**: Custom JavaScript for audio, visual glitches, and typewriter effects
- **Audio**: Web Audio API for retro typing sounds and static noise

## 🔧 Development

The game state is managed in `logic.py`:
- `failai` dictionary stores files with their passwords and content
- `durys_sarasas` dictionary tracks door states and access codes
- Command parsing happens in `process_command()`



