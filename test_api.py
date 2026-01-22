import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from api import app

client = TestClient(app)


class TestRootEndpoint:
    """Tests for root endpoint."""
    
    def test_root_returns_welcome_message(self):
        """Test that root endpoint returns API information."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "Rock-Paper-Scissors-Lizard-Spock API" in data["message"]
        assert "endpoints" in data


class TestRulesEndpoint:
    """Tests for rules endpoint."""
    
    def test_rules_endpoint(self):
        """Test that rules endpoint returns game rules."""
        response = client.get("/rules")
        assert response.status_code == 200
        data = response.json()
        assert "rules" in data
        assert "rock" in data["rules"]
        assert "paper" in data["rules"]
        assert "scissors" in data["rules"]
        assert "lizard" in data["rules"]
        assert "spock" in data["rules"]


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_check(self):
        """Test that health check returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


class TestPlayWithPayload:
    """Tests for /play endpoint with JSON payload."""
    
    @pytest.mark.parametrize("choice", ["rock", "paper", "scissors", "lizard", "spock"])
    def test_play_with_valid_choice(self, choice):
        """Test playing with valid choices."""
        with patch('api.get_computer_choice', return_value='rock'):
            response = client.post("/play", json={"choice": choice})
            assert response.status_code == 200
            data = response.json()
            assert data["user_choice"] == choice
            assert data["computer_choice"] == "rock"
            assert data["result"] in ["user", "computer", "tie"]
            assert "message" in data
    
    def test_play_with_invalid_choice(self):
        """Test playing with invalid choice."""
        response = client.post("/play", json={"choice": "invalid"})
        assert response.status_code == 422  # Validation error
    
    def test_play_without_choice(self):
        """Test playing without providing a choice."""
        response = client.post("/play", json={})
        assert response.status_code == 422  # Validation error


class TestIndividualEndpoints:
    """Tests for individual choice endpoints."""
    
    def test_rock_endpoint(self):
        """Test POST /rock endpoint."""
        with patch('api.get_computer_choice', return_value='scissors'):
            response = client.post("/rock")
            assert response.status_code == 200
            data = response.json()
            assert data["user_choice"] == "rock"
            assert data["computer_choice"] == "scissors"
            assert data["result"] == "user"
            assert "win" in data["message"].lower()
    
    def test_paper_endpoint(self):
        """Test POST /paper endpoint."""
        with patch('api.get_computer_choice', return_value='rock'):
            response = client.post("/paper")
            assert response.status_code == 200
            data = response.json()
            assert data["user_choice"] == "paper"
            assert data["result"] == "user"
    
    def test_scissors_endpoint(self):
        """Test POST /scissors endpoint."""
        with patch('api.get_computer_choice', return_value='paper'):
            response = client.post("/scissors")
            assert response.status_code == 200
            data = response.json()
            assert data["user_choice"] == "scissors"
            assert data["result"] == "user"
    
    def test_lizard_endpoint(self):
        """Test POST /lizard endpoint."""
        with patch('api.get_computer_choice', return_value='spock'):
            response = client.post("/lizard")
            assert response.status_code == 200
            data = response.json()
            assert data["user_choice"] == "lizard"
            assert data["result"] == "user"
    
    def test_spock_endpoint(self):
        """Test POST /spock endpoint."""
        with patch('api.get_computer_choice', return_value='scissors'):
            response = client.post("/spock")
            assert response.status_code == 200
            data = response.json()
            assert data["user_choice"] == "spock"
            assert data["result"] == "user"


class TestGameLogic:
    """Tests for game logic integration."""
    
    def test_user_wins(self):
        """Test scenario where user wins."""
        with patch('api.get_computer_choice', return_value='scissors'):
            response = client.post("/play", json={"choice": "rock"})
            data = response.json()
            assert data["result"] == "user"
            assert "win" in data["message"].lower()
    
    def test_computer_wins(self):
        """Test scenario where computer wins."""
        with patch('api.get_computer_choice', return_value='paper'):
            response = client.post("/play", json={"choice": "rock"})
            data = response.json()
            assert data["result"] == "computer"
            assert "Computer wins" in data["message"]
    
    def test_tie(self):
        """Test scenario where it's a tie."""
        with patch('api.get_computer_choice', return_value='rock'):
            response = client.post("/play", json={"choice": "rock"})
            data = response.json()
            assert data["result"] == "tie"
            assert "tie" in data["message"].lower()


class TestResponseFormat:
    """Tests for response format consistency."""
    
    def test_response_has_all_fields(self):
        """Test that response has all required fields."""
        with patch('api.get_computer_choice', return_value='rock'):
            response = client.post("/play", json={"choice": "rock"})
            data = response.json()
            assert "user_choice" in data
            assert "computer_choice" in data
            assert "result" in data
            assert "message" in data
    
    def test_response_field_types(self):
        """Test that response fields have correct types."""
        with patch('api.get_computer_choice', return_value='rock'):
            response = client.post("/play", json={"choice": "rock"})
            data = response.json()
            assert isinstance(data["user_choice"], str)
            assert isinstance(data["computer_choice"], str)
            assert isinstance(data["result"], str)
            assert isinstance(data["message"], str)


class TestAllWinningCombinations:
    """Test all possible winning combinations through the API."""
    
    @pytest.mark.parametrize("user_choice,computer_choice", [
        ("rock", "scissors"),
        ("rock", "lizard"),
        ("paper", "rock"),
        ("paper", "spock"),
        ("scissors", "paper"),
        ("scissors", "lizard"),
        ("lizard", "paper"),
        ("lizard", "spock"),
        ("spock", "rock"),
        ("spock", "scissors"),
    ])
    def test_winning_combinations(self, user_choice, computer_choice):
        """Test all winning combinations."""
        with patch('api.get_computer_choice', return_value=computer_choice):
            response = client.post("/play", json={"choice": user_choice})
            data = response.json()
            assert data["result"] == "user"
            assert data["user_choice"] == user_choice
            assert data["computer_choice"] == computer_choice
