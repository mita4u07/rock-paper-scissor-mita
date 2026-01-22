import pytest
from unittest.mock import patch, call
from main import (
    get_computer_choice,
    get_user_choice,
    determine_winner,
    display_result,
    main
)


class TestGetComputerChoice:
    """Tests for get_computer_choice function."""
    
    def test_computer_choice_returns_valid_option(self):
        """Test that computer choice is one of the valid options."""
        valid_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        choice = get_computer_choice()
        assert choice in valid_choices
    
    def test_computer_choice_randomness(self):
        """Test that computer choice varies (probabilistic test)."""
        choices = [get_computer_choice() for _ in range(20)]
        # With 20 random choices from 5 options, we expect at least 2 different values
        assert len(set(choices)) >= 2


class TestGetUserChoice:
    """Tests for get_user_choice function."""
    
    @pytest.mark.parametrize("user_input,expected", [
        ('1', 'rock'),
        ('2', 'paper'),
        ('3', 'scissors'),
        ('4', 'lizard'),
        ('5', 'spock'),
        ('6', 'quit'),
    ])
    def test_valid_numeric_inputs(self, user_input, expected):
        """Test that valid numeric inputs return correct choices."""
        with patch('builtins.input', return_value=user_input):
            with patch('builtins.print'):  # Suppress print output
                result = get_user_choice()
                assert result == expected
    
    def test_invalid_then_valid_input(self):
        """Test that invalid input prompts again until valid input received."""
        with patch('builtins.input', side_effect=['invalid', '7', '0', '1']):
            with patch('builtins.print') as mock_print:
                result = get_user_choice()
                assert result == 'rock'
                # Check that error message was printed 3 times
                error_calls = [c for c in mock_print.call_args_list 
                             if 'Invalid choice' in str(c)]
                assert len(error_calls) == 3
    
    def test_whitespace_handling(self):
        """Test that input with whitespace is handled correctly."""
        with patch('builtins.input', return_value='  1  '):
            with patch('builtins.print'):
                result = get_user_choice()
                assert result == 'rock'


class TestDetermineWinner:
    """Tests for determine_winner function."""
    
    # Test ties
    @pytest.mark.parametrize("choice", ['rock', 'paper', 'scissors', 'lizard', 'spock'])
    def test_tie_scenarios(self, choice):
        """Test that same choices result in a tie."""
        assert determine_winner(choice, choice) == "tie"
    
    # Test Rock wins
    @pytest.mark.parametrize("computer_choice", ['scissors', 'lizard'])
    def test_rock_wins(self, computer_choice):
        """Test that rock beats scissors and lizard."""
        assert determine_winner('rock', computer_choice) == "user"
    
    @pytest.mark.parametrize("computer_choice", ['paper', 'spock'])
    def test_rock_loses(self, computer_choice):
        """Test that rock loses to paper and spock."""
        assert determine_winner('rock', computer_choice) == "computer"
    
    # Test Paper wins
    @pytest.mark.parametrize("computer_choice", ['rock', 'spock'])
    def test_paper_wins(self, computer_choice):
        """Test that paper beats rock and spock."""
        assert determine_winner('paper', computer_choice) == "user"
    
    @pytest.mark.parametrize("computer_choice", ['scissors', 'lizard'])
    def test_paper_loses(self, computer_choice):
        """Test that paper loses to scissors and lizard."""
        assert determine_winner('paper', computer_choice) == "computer"
    
    # Test Scissors wins
    @pytest.mark.parametrize("computer_choice", ['paper', 'lizard'])
    def test_scissors_wins(self, computer_choice):
        """Test that scissors beats paper and lizard."""
        assert determine_winner('scissors', computer_choice) == "user"
    
    @pytest.mark.parametrize("computer_choice", ['rock', 'spock'])
    def test_scissors_loses(self, computer_choice):
        """Test that scissors loses to rock and spock."""
        assert determine_winner('scissors', computer_choice) == "computer"
    
    # Test Lizard wins
    @pytest.mark.parametrize("computer_choice", ['paper', 'spock'])
    def test_lizard_wins(self, computer_choice):
        """Test that lizard beats paper and spock."""
        assert determine_winner('lizard', computer_choice) == "user"
    
    @pytest.mark.parametrize("computer_choice", ['rock', 'scissors'])
    def test_lizard_loses(self, computer_choice):
        """Test that lizard loses to rock and scissors."""
        assert determine_winner('lizard', computer_choice) == "computer"
    
    # Test Spock wins
    @pytest.mark.parametrize("computer_choice", ['rock', 'scissors'])
    def test_spock_wins(self, computer_choice):
        """Test that spock beats rock and scissors."""
        assert determine_winner('spock', computer_choice) == "user"
    
    @pytest.mark.parametrize("computer_choice", ['paper', 'lizard'])
    def test_spock_loses(self, computer_choice):
        """Test that spock loses to paper and lizard."""
        assert determine_winner('spock', computer_choice) == "computer"


class TestDisplayResult:
    """Tests for display_result function."""
    
    def test_display_tie(self):
        """Test display output for a tie."""
        with patch('builtins.print') as mock_print:
            display_result('rock', 'rock', 'tie')
            
            # Verify the printed messages
            calls = [str(call) for call in mock_print.call_args_list]
            assert any('You chose: rock' in call for call in calls)
            assert any('Computer chose: rock' in call for call in calls)
            assert any("It's a tie!" in call for call in calls)
    
    def test_display_user_win(self):
        """Test display output for user win."""
        with patch('builtins.print') as mock_print:
            display_result('rock', 'scissors', 'user')
            
            calls = [str(call) for call in mock_print.call_args_list]
            assert any('You chose: rock' in call for call in calls)
            assert any('Computer chose: scissors' in call for call in calls)
            assert any('You win!' in call for call in calls)
    
    def test_display_computer_win(self):
        """Test display output for computer win."""
        with patch('builtins.print') as mock_print:
            display_result('rock', 'paper', 'computer')
            
            calls = [str(call) for call in mock_print.call_args_list]
            assert any('You chose: rock' in call for call in calls)
            assert any('Computer chose: paper' in call for call in calls)
            assert any('Computer wins!' in call for call in calls)


class TestMain:
    """Tests for main function."""
    
    def test_main_quit_immediately(self):
        """Test quitting the game immediately."""
        with patch('builtins.input', return_value='6'):
            with patch('builtins.print') as mock_print:
                main()
                
                calls = [str(call) for call in mock_print.call_args_list]
                assert any('Welcome to Rock, Paper, Scissors, Lizard, Spock!' in call for call in calls)
                assert any('Final Score' in call for call in calls)
                assert any('Thanks for playing!' in call for call in calls)
    
    def test_main_single_round_user_wins(self):
        """Test a single round where user wins."""
        with patch('builtins.input', side_effect=['1', '6']):  # rock, then quit
            with patch('main.get_computer_choice', return_value='scissors'):
                with patch('builtins.print') as mock_print:
                    main()
                    
                    calls = [str(call) for call in mock_print.call_args_list]
                    assert any('You win!' in call for call in calls)
                    assert any('Score - You: 1, Computer: 0' in call for call in calls)
    
    def test_main_single_round_computer_wins(self):
        """Test a single round where computer wins."""
        with patch('builtins.input', side_effect=['1', '6']):  # rock, then quit
            with patch('main.get_computer_choice', return_value='paper'):
                with patch('builtins.print') as mock_print:
                    main()
                    
                    calls = [str(call) for call in mock_print.call_args_list]
                    assert any('Computer wins!' in call for call in calls)
                    assert any('Score - You: 0, Computer: 1' in call for call in calls)
    
    def test_main_single_round_tie(self):
        """Test a single round that results in a tie."""
        with patch('builtins.input', side_effect=['1', '6']):  # rock, then quit
            with patch('main.get_computer_choice', return_value='rock'):
                with patch('builtins.print') as mock_print:
                    main()
                    
                    calls = [str(call) for call in mock_print.call_args_list]
                    assert any("It's a tie!" in call for call in calls)
                    assert any('Score - You: 0, Computer: 0' in call for call in calls)
    
    def test_main_multiple_rounds(self):
        """Test multiple rounds with varied results."""
        # User choices: rock (wins), paper (loses), scissors (tie), quit
        with patch('builtins.input', side_effect=['1', '2', '3', '6']):
            with patch('main.get_computer_choice', side_effect=['lizard', 'scissors', 'scissors']):
                with patch('builtins.print') as mock_print:
                    main()
                    
                    calls = [str(call) for call in mock_print.call_args_list]
                    # Check that final score appears
                    assert any('Final Score - You: 1, Computer: 1' in call for call in calls)
    
    def test_main_displays_rules(self):
        """Test that game rules are displayed at startup."""
        with patch('builtins.input', return_value='6'):
            with patch('builtins.print') as mock_print:
                main()
                
                calls = [str(call) for call in mock_print.call_args_list]
                assert any('Rock crushes Scissors and Lizard' in call for call in calls)
                assert any('Paper covers Rock and disproves Spock' in call for call in calls)
                assert any('Scissors cuts Paper and decapitates Lizard' in call for call in calls)
                assert any('Lizard eats Paper and poisons Spock' in call for call in calls)
                assert any('Spock vaporizes Rock and smashes Scissors' in call for call in calls)


class TestIntegration:
    """Integration tests for complete game scenarios."""
    
    def test_complete_game_flow(self):
        """Test a complete game with multiple rounds."""
        # Simulate a game: user plays spock, lizard, then quits
        with patch('builtins.input', side_effect=['5', '4', '6']):
            with patch('main.get_computer_choice', side_effect=['scissors', 'spock']):
                with patch('builtins.print') as mock_print:
                    main()
                    
                    calls = [str(call) for call in mock_print.call_args_list]
                    # User should win round 1 (spock beats scissors)
                    # User should win round 2 (lizard beats spock)
                    assert any('Final Score - You: 2, Computer: 0' in call for call in calls)


class TestMainGuard:
    """Test the __main__ guard."""
    
    def test_main_module_has_guard(self):
        """Test that the __main__ guard exists in the module."""
        import main
        import inspect
        
        # Read the source code and verify __main__ guard exists
        source = inspect.getsource(main)
        assert 'if __name__ == "__main__":' in source
        assert source.strip().endswith('main()')
