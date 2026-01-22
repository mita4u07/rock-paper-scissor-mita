# GitHub Copilot Workshop

## Build a Rock, Paper, Scissors game from scratch with GitHub Copilot

<img width="400" alt="Rock Paper Scissors image" src="./assets/Rock Paper Scissors image.png">

In this fun workshop, you will learn how to use GitHub Copilot to build a simple game in Python, with little to no coding experience required.

Estimated time to complete: `10 to 60 minutes`

Participants will be guided to install the GitHub Copilot VS Code extension, follow a CodeTour to learn how to interact with GitHub Copilot, and then use GitHub Copilot to build a Rock, Paper, Scissors game from scratch. 

Depending on the time available, participants will be able to complete the game or just get started, from a simple version all the way to introducing additional logic to make the game more interesting complete, with unit tests and REST API endpoints.

## ✅ Completed Challenges

This repository now includes all three challenge implementations:

1. **✅ Rock-Paper-Scissors-Lizard-Spock** - Enhanced game with 5 choices and numbered menu interface
2. **✅ Unit Tests** - Comprehensive test suite with 98% coverage (46 tests for CLI, 30 tests for API)
3. **✅ REST API** - Full FastAPI implementation with interactive documentation
4. **✅ Web UI** - Modern, responsive web interface for playing the game



## Instructions 

Inside the `.instructions` folder you will find a number of markdown files that contain the instructions for this workshop.

Filename | Description
--- | ---
[1. setup.md](</.instructions/1. setup.md>) | Instructions for installing the GitHub Copilot VS Code extension and joining the GitHub Copilot trial.
[2. core exercises.md](</.instructions/2. core exercises.md>) | Instructions for getting started with GitHub Copilot.
[3. challenge exercises.md](</.instructions/3. challenge exercises.md>) | Challenge exercises for participants to complete.
[4. additional resources.md](</.instructions/4. additional resources.md>) | Additional resources for participants to explore after the workshop.


## Running a workshop?

If you're planning to run a GitHub Copilot workshop, please review the [workshop guide](</.instructions/workshop organisers.md>) for tips and tricks to help you run a successful workshop. 


## Quick Start

### Play the Web UI
```bash
# 1. Start the API server
python api.py

# 2. Open index.html in your browser
# Or use a local web server:
python -m http.server 8080
# Then visit http://localhost:8080
```

See [UI_README.md](UI_README.md) for detailed UI documentation.

### Play the CLI Game
```bash
python main.py
```

### Run Unit Tests
```bash
# Run all tests with coverage
./run_tests.sh

# Or run tests manually
pytest test_main.py test_api.py -v --cov
```

### Start the REST API
```bash
# Start the API server
./start_api.sh

# Or run directly
python api.py
```

Visit http://localhost:8000/docs for interactive API documentation.

### Test the API
```bash
# Run the demo script
python demo_api.py

# Or use curl
curl -X POST http://localhost:8000/play -H "Content-Type: application/json" -d '{"choice": "spock"}'
```

## Project Structure

In this project you will find: 

* `main.py` - Complete Rock-Paper-Scissors-Lizard-Spock CLI game
* `api.py` - FastAPI REST API implementation with CORS support
* `index.html` - Web UI main page
* `style.css` - Web UI styling and animations
* `app.js` - Web UI JavaScript logic and API integration
* `test_main.py` - Comprehensive unit tests for CLI game (46 tests, 98% coverage)
* `test_api.py` - API endpoint tests (30 tests, 98% coverage)
* `demo_api.py` - API demonstration script
* `requirements.txt` - Python dependencies
* `API_README.md` - Detailed API documentation
* `UI_README.md` - Web UI documentation and guide
* `run_tests.sh` - Test runner script
* `start_api.sh` - API server launcher
* a devcontainer that installs CodeTour and GitHub Copilot when the Codespace is created (If you want to use Codespaces)
* an `.instructions` folder all the instructions for this workshop.
* an `assets` folder containing images used in this workshop documentation.
* a `.tours` folder that includes the CodeTour file if you wish to use it.




## FAQ 

- **How do I get a GitHub Copilot license?**
  - You can request a trial license from your GitHub Sales representative or via Copilot for Individuals or Business licenses.
- **How do I get a GitHub Codespaces license?**
    - Codespaces is included with GitHub Enterprise Cloud, GitHub Enterprise Server, and GitHub Free. You can check under your [billing settings page](https://github.com/settings/billing).
- **I am having trouble activating GitHub Copilot after I load the plugin, what should I do?**
    - This could be because you launched your Codespace before you activated GitHub Copilot or accepted the invitation to the trial org. Please try to reload your Codespace and try again.

## Acknowledgements

A special thanks to the following awesome Hubbers who have contributed in many different ways to our workshops. 
[blackgirlbytes](https://github.com/blackgirlbytes), [pierluigi](https://github.com/pierluigi), [yuichielectric](https://github.com/yuichielectric), [dchomh](https://github.com/dchomh), [nolecram](https://github.com/nolecram), [rsymo](https://github.com/rsymo), [damovisa](https://github.com/damovisa) and anyone else I've inadvertently missed.

Enjoy your workshop!
[anthonyborton](https://github.com/anthonyborton)

_v1.0 Released May, 2023_
