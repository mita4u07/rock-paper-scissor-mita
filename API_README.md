# Rock-Paper-Scissors-Lizard-Spock REST API

A REST API implementation of the classic Rock-Paper-Scissors game with Lizard and Spock additions.

## Installation

```bash
pip install -r requirements.txt
```

## Running the API

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## API Endpoints

### GET /
Returns API information and available endpoints.

### GET /rules
Returns the game rules.

**Response:**
```json
{
  "rules": {
    "rock": "Rock crushes Scissors and Lizard",
    "paper": "Paper covers Rock and disproves Spock",
    "scissors": "Scissors cuts Paper and decapitates Lizard",
    "lizard": "Lizard eats Paper and poisons Spock",
    "spock": "Spock vaporizes Rock and smashes Scissors"
  }
}
```

### POST /play
Play the game with a JSON payload.

**Request:**
```json
{
  "choice": "rock"
}
```

**Response:**
```json
{
  "user_choice": "rock",
  "computer_choice": "scissors",
  "result": "user",
  "message": "You win! Rock beats scissors."
}
```

### POST /rock, /paper, /scissors, /lizard, /spock
Play the game with a specific choice via endpoint.

**Response:**
```json
{
  "user_choice": "rock",
  "computer_choice": "paper",
  "result": "computer",
  "message": "Computer wins! Paper beats rock."
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Usage Examples

### Using curl

```bash
# Play with JSON payload
curl -X POST http://localhost:8000/play \
  -H "Content-Type: application/json" \
  -d '{"choice": "rock"}'

# Play using specific endpoint
curl -X POST http://localhost:8000/rock

# Get rules
curl http://localhost:8000/rules

# Get API info
curl http://localhost:8000/
```

### Using Python requests

```python
import requests

# Play with JSON payload
response = requests.post(
    'http://localhost:8000/play',
    json={'choice': 'spock'}
)
print(response.json())

# Play using specific endpoint
response = requests.post('http://localhost:8000/lizard')
print(response.json())
```

### Using JavaScript fetch

```javascript
// Play with JSON payload
fetch('http://localhost:8000/play', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ choice: 'scissors' }),
})
  .then(response => response.json())
  .then(data => console.log(data));

// Play using specific endpoint
fetch('http://localhost:8000/paper', { method: 'POST' })
  .then(response => response.json())
  .then(data => console.log(data));
```

## Running Tests

```bash
# Run API tests
pytest test_api.py -v

# Run with coverage
pytest test_api.py --cov=api --cov-report=term-missing

# Run all tests
pytest -v
```

## Response Fields

All game endpoints return the following fields:

- `user_choice`: The choice you made
- `computer_choice`: The computer's random choice
- `result`: `"user"` (you win), `"computer"` (computer wins), or `"tie"`
- `message`: A descriptive message about the game result

## Valid Choices

- `rock` - Crushes Scissors and Lizard
- `paper` - Covers Rock and disproves Spock
- `scissors` - Cuts Paper and decapitates Lizard
- `lizard` - Eats Paper and poisons Spock
- `spock` - Vaporizes Rock and smashes Scissors

## HTTP Status Codes

- `200 OK` - Successful game play
- `422 Unprocessable Entity` - Invalid choice provided
- `500 Internal Server Error` - Server error

## Features

- ✅ RESTful API design
- ✅ Automatic API documentation (Swagger/OpenAPI)
- ✅ Input validation with Pydantic
- ✅ Comprehensive test coverage
- ✅ Health check endpoint
- ✅ Multiple ways to play (JSON payload or specific endpoints)
