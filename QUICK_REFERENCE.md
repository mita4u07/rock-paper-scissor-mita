# 🚀 Quick Reference Guide

## One-Command Cheat Sheet

### Play the Game
```bash
python main.py
```

### Run All Tests
```bash
./run_tests.sh
```

### Start the API
```bash
./start_api.sh
```

### Demo the API
```bash
python demo_api.py
```

---

## API Quick Reference

### Base URL
```
http://localhost:8000
```

### Interactive Docs
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Example Requests

#### Play with JSON
```bash
curl -X POST http://localhost:8000/play \
  -H "Content-Type: application/json" \
  -d '{"choice": "spock"}'
```

#### Play with Endpoint
```bash
curl -X POST http://localhost:8000/lizard
```

#### Get Rules
```bash
curl http://localhost:8000/rules
```

---

## Test Commands

### Run All Tests
```bash
pytest -v
```

### Run CLI Tests Only
```bash
pytest test_main.py -v
```

### Run API Tests Only
```bash
pytest test_api.py -v
```

### Run with Coverage
```bash
pytest --cov=main --cov=api --cov-report=term-missing
```

### Run with HTML Coverage Report
```bash
pytest --cov=main --cov=api --cov-report=html
open htmlcov/index.html
```

---

## Game Rules (Quick Reference)

| Choice | Beats |
|--------|-------|
| 🪨 Rock | Scissors, Lizard |
| 📄 Paper | Rock, Spock |
| ✂️ Scissors | Paper, Lizard |
| 🦎 Lizard | Paper, Spock |
| 🖖 Spock | Rock, Scissors |

---

## Project Structure

```
rock-paper-scissor-mita/
├── main.py                 # CLI game
├── api.py                  # REST API
├── test_main.py           # CLI tests
├── test_api.py            # API tests
├── demo_api.py            # API demo
├── requirements.txt       # Dependencies
├── run_tests.sh          # Test runner
├── start_api.sh          # API launcher
├── README.md             # Main documentation
├── API_README.md         # API documentation
└── COMPLETION_SUMMARY.md # Challenge completion summary
```

---

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Make scripts executable
chmod +x run_tests.sh start_api.sh
```

---

## Dependencies

```
fastapi==0.115.6
uvicorn[standard]==0.34.0
pydantic==2.10.5
pytest==7.4.3
pytest-cov==4.1.0
httpx==0.27.2
requests (for demo script)
```

---

## Key Features

✅ 5 choices (Rock, Paper, Scissors, Lizard, Spock)
✅ Numbered menu interface (1-6)
✅ Score tracking
✅ 98% test coverage
✅ REST API with auto-docs
✅ Comprehensive error handling
✅ Input validation
✅ Health checks

---

## Status

🎯 **All 3 Challenges Complete**

1. ✅ Lizard & Spock added
2. ✅ Unit tests (98% coverage)
3. ✅ REST API with FastAPI

---

## Need Help?

- Check [README.md](README.md) for detailed information
- Review [API_README.md](API_README.md) for API details
- See [COMPLETION_SUMMARY.md](COMPLETION_SUMMARY.md) for full challenge completion details
- Visit http://localhost:8000/docs for interactive API documentation
