from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Literal
from main import get_computer_choice, determine_winner
import uvicorn

app = FastAPI(
    title="Rock-Paper-Scissors-Lizard-Spock API",
    description="Play Rock-Paper-Scissors-Lizard-Spock via REST API",
    version="1.0.0"
)

# Configure CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GameRequest(BaseModel):
    """Request model for playing the game."""
    choice: Literal['rock', 'paper', 'scissors', 'lizard', 'spock'] = Field(
        ...,
        description="Your choice: rock, paper, scissors, lizard, or spock"
    )


class GameResponse(BaseModel):
    """Response model for game results."""
    user_choice: str
    computer_choice: str
    result: str
    message: str


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Rock-Paper-Scissors-Lizard-Spock API!",
        "endpoints": {
            "POST /play": "Play the game with JSON payload: {'choice': 'rock'}",
            "POST /rock": "Play with rock",
            "POST /paper": "Play with paper",
            "POST /scissors": "Play with scissors",
            "POST /lizard": "Play with lizard",
            "POST /spock": "Play with spock",
            "GET /rules": "Get game rules"
        },
        "docs": "/docs for interactive API documentation"
    }


@app.get("/rules")
async def get_rules():
    """Get the game rules."""
    return {
        "rules": {
            "rock": "Rock crushes Scissors and Lizard",
            "paper": "Paper covers Rock and disproves Spock",
            "scissors": "Scissors cuts Paper and decapitates Lizard",
            "lizard": "Lizard eats Paper and poisons Spock",
            "spock": "Spock vaporizes Rock and smashes Scissors"
        }
    }


def play_game(user_choice: str) -> GameResponse:
    """
    Play a round of the game.
    
    Args:
        user_choice: The user's choice
        
    Returns:
        GameResponse with game results
    """
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    # Generate message based on result
    if result == "tie":
        message = f"It's a tie! Both chose {user_choice}."
    elif result == "user":
        message = f"You win! {user_choice.capitalize()} beats {computer_choice}."
    else:
        message = f"Computer wins! {computer_choice.capitalize()} beats {user_choice}."
    
    return GameResponse(
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        message=message
    )


@app.post("/play", response_model=GameResponse)
async def play_with_payload(request: GameRequest):
    """
    Play the game by sending a JSON payload.
    
    Example:
        POST /play
        {"choice": "rock"}
    """
    return play_game(request.choice)


@app.post("/rock", response_model=GameResponse)
async def play_rock():
    """Play with rock."""
    return play_game("rock")


@app.post("/paper", response_model=GameResponse)
async def play_paper():
    """Play with paper."""
    return play_game("paper")


@app.post("/scissors", response_model=GameResponse)
async def play_scissors():
    """Play with scissors."""
    return play_game("scissors")


@app.post("/lizard", response_model=GameResponse)
async def play_lizard():
    """Play with lizard."""
    return play_game("lizard")


@app.post("/spock", response_model=GameResponse)
async def play_spock():
    """Play with spock."""
    return play_game("spock")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
