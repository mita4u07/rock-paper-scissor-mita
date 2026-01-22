# Web UI for Rock-Paper-Scissors-Lizard-Spock

A modern, responsive web interface for the Rock-Paper-Scissors-Lizard-Spock game.

## Features

- 🎨 **Beautiful UI** - Modern gradient design with smooth animations
- 📊 **Score Tracking** - Persistent statistics stored in browser localStorage
- 📱 **Responsive** - Works perfectly on desktop, tablet, and mobile devices
- ⌨️ **Keyboard Support** - Play using number keys (1-5) or letter shortcuts (R, P, S, L, K)
- 🎮 **Real-time Play** - Connects to the FastAPI backend for game logic
- 📖 **Built-in Rules** - Collapsible rules section for easy reference

## Quick Start

### 1. Start the API Server

First, make sure the backend API is running:

```bash
python api.py
```

The API will start on `http://localhost:8000`

### 2. Open the Web UI

Simply open `index.html` in your web browser:

```bash
# Using default browser
xdg-open index.html  # Linux
open index.html      # macOS
start index.html     # Windows
```

Or, for better CORS handling, use a local web server:

```bash
# Using Python's built-in server
python -m http.server 8080

# Then open http://localhost:8080 in your browser
```

## How to Play

### Mouse/Touch
Click or tap on any of the five choices:
- 🪨 Rock
- 📄 Paper
- ✂️ Scissors
- 🦎 Lizard
- 🖖 Spock

### Keyboard Shortcuts
- **Number keys**: `1` (Rock), `2` (Paper), `3` (Scissors), `4` (Lizard), `5` (Spock)
- **Letter keys**: `R` (Rock), `P` (Paper), `S` (Scissors), `L` (Lizard), `K` (Spock)

## Features

### Score Tracking
Your wins, losses, and ties are automatically saved to your browser's localStorage and persist across sessions.

### Reset Statistics
Click the **🔄 Reset** button in the scoreboard to clear all statistics.

### Game Rules
Click on **📖 Game Rules** to expand the rules section and see what beats what.

## Architecture

The web UI consists of three files:

1. **index.html** - Main HTML structure
2. **style.css** - All styling and animations
3. **app.js** - Game logic and API integration

The UI communicates with the FastAPI backend via REST API calls to play the game and retrieve results.

## Troubleshooting

### "Failed to connect to the game API" Error

If you see this error:
1. Make sure the API server is running: `python api.py`
2. Verify the API is accessible at `http://localhost:8000`
3. Check the browser console (F12) for detailed error messages

### CORS Issues

If you encounter CORS errors:
- The API has been configured with CORS middleware to allow cross-origin requests
- For production, update the `allow_origins` in `api.py` to specify your domain

## Browser Compatibility

The UI works on all modern browsers:
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## Files Structure

```
.
├── index.html      # Main HTML file
├── style.css       # Styling and animations
├── app.js          # JavaScript game logic
├── api.py          # FastAPI backend (updated with CORS)
└── UI_README.md    # This file
```

## Technical Details

### API Integration
The UI uses the following API endpoints:
- `POST /play` - Play a game round
- `GET /rules` - Get game rules (optional)
- `GET /` - Check API availability

### Local Storage
Statistics are saved using localStorage with the key `rpsls-stats`:
```javascript
{
  "wins": 0,
  "losses": 0,
  "ties": 0
}
```

### Responsive Breakpoints
- Desktop: > 768px
- Tablet: 481px - 768px
- Mobile: < 480px

## Customization

### Change Colors
Edit the gradient backgrounds in `style.css`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change API URL
If your API is running on a different port or host, update `app.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

## Future Enhancements

Potential features to add:
- 🏆 Leaderboards
- 🎵 Sound effects
- 🌙 Dark mode toggle
- 📈 Win/loss charts
- 👥 Multiplayer mode
- 🎯 Achievement system

## License

This project is part of the Rock-Paper-Scissors-Lizard-Spock workshop repository.
