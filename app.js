// API Configuration
// Dynamically determine API URL based on current page URL
function getApiBaseUrl() {
    const hostname = window.location.hostname;
    const protocol = window.location.protocol;
    
    // For GitHub Codespaces forwarded URLs pattern (e.g., xxx-8080.app.github.dev)
    if (hostname.includes('app.github.dev') || hostname.includes('github.dev')) {
        // Replace the port number in the hostname
        const apiHostname = hostname.replace(/-8080\./, '-8000.');
        return `${protocol}//${apiHostname}`;
    }
    
    // If the URL contains a port, replace 8080 with 8000
    if (window.location.port === '8080') {
        return `${protocol}//${hostname.replace(':8080', '')}:8000`;
    }
    
    // Default to localhost:8000
    return 'http://localhost:8000';
}

const API_BASE_URL = getApiBaseUrl();
console.log('API Base URL:', API_BASE_URL);

// Emoji mapping
const EMOJI_MAP = {
    rock: '🪨',
    paper: '📄',
    scissors: '✂️',
    lizard: '🦎',
    spock: '🖖'
};

// Game state
let stats = {
    wins: 0,
    losses: 0,
    ties: 0
};

// Load stats from localStorage
function loadStats() {
    const savedStats = localStorage.getItem('rpsls-stats');
    if (savedStats) {
        stats = JSON.parse(savedStats);
        updateScoreboard();
    }
}

// Save stats to localStorage
function saveStats() {
    localStorage.setItem('rpsls-stats', JSON.stringify(stats));
}

// Update scoreboard display
function updateScoreboard() {
    document.getElementById('wins').textContent = stats.wins;
    document.getElementById('losses').textContent = stats.losses;
    document.getElementById('ties').textContent = stats.ties;
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
}

// Show loading state
function showLoading(show) {
    const loading = document.getElementById('loading');
    const choices = document.querySelector('.choices');
    
    if (show) {
        loading.style.display = 'block';
        choices.style.opacity = '0.5';
        choices.style.pointerEvents = 'none';
    } else {
        loading.style.display = 'none';
        choices.style.opacity = '1';
        choices.style.pointerEvents = 'auto';
    }
}

// Play the game
async function playGame(userChoice) {
    showLoading(true);
    document.getElementById('resultSection').style.display = 'none';
    
    try {
        const response = await fetch(`${API_BASE_URL}/play`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ choice: userChoice })
        });
        
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        
        const data = await response.json();
        displayResult(data);
        updateStats(data.result);
        
    } catch (error) {
        console.error('Error playing game:', error);
        showError('Failed to connect to the game API. Make sure the server is running on port 8000.');
    } finally {
        showLoading(false);
    }
}

// Display game result
function displayResult(data) {
    const resultSection = document.getElementById('resultSection');
    const playerEmoji = document.getElementById('playerEmoji');
    const playerChoice = document.getElementById('playerChoice');
    const computerEmoji = document.getElementById('computerEmoji');
    const computerChoice = document.getElementById('computerChoice');
    const resultMessage = document.getElementById('resultMessage');
    const explanation = document.getElementById('explanation');
    
    // Set choices
    playerEmoji.textContent = EMOJI_MAP[data.user_choice];
    playerChoice.textContent = data.user_choice;
    computerEmoji.textContent = EMOJI_MAP[data.computer_choice];
    computerChoice.textContent = data.computer_choice;
    
    // Set result message
    resultMessage.textContent = data.result;
    resultMessage.className = 'result-message';
    
    if (data.result.toLowerCase().includes('win')) {
        resultMessage.classList.add('win');
    } else if (data.result.toLowerCase().includes('lose')) {
        resultMessage.classList.add('lose');
    } else {
        resultMessage.classList.add('tie');
    }
    
    // Set explanation
    explanation.textContent = data.message;
    
    // Show result section with animation
    resultSection.style.display = 'block';
}

// Update statistics
function updateStats(result) {
    if (result.toLowerCase().includes('win')) {
        stats.wins++;
    } else if (result.toLowerCase().includes('lose')) {
        stats.losses++;
    } else {
        stats.ties++;
    }
    
    updateScoreboard();
    saveStats();
}

// Load game rules from API
async function loadRules() {
    try {
        const response = await fetch(`${API_BASE_URL}/rules`);
        if (response.ok) {
            const data = await response.json();
            // Rules are already hardcoded in HTML, but we could update them dynamically here
            console.log('Game rules loaded:', data);
        }
    } catch (error) {
        console.log('Could not load rules from API, using default rules');
    }
}

// Reset statistics
function resetStats() {
    if (confirm('Are you sure you want to reset all statistics?')) {
        stats = { wins: 0, losses: 0, ties: 0 };
        saveStats();
        updateScoreboard();
    }
}

// Add reset button functionality
function addResetButton() {
    const scoreboard = document.querySelector('.scoreboard');
    const resetBtn = document.createElement('button');
    resetBtn.textContent = '🔄 Reset';
    resetBtn.className = 'reset-btn';
    resetBtn.onclick = resetStats;
    resetBtn.style.cssText = `
        padding: 10px 20px;
        background: #ff6b6b;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
    `;
    resetBtn.onmouseover = () => {
        resetBtn.style.background = '#ff5252';
        resetBtn.style.transform = 'translateY(-50%) scale(1.05)';
    };
    resetBtn.onmouseout = () => {
        resetBtn.style.background = '#ff6b6b';
        resetBtn.style.transform = 'translateY(-50%) scale(1)';
    };
    
    scoreboard.style.position = 'relative';
    scoreboard.appendChild(resetBtn);
}

// Check if API is available
async function checkAPI() {
    try {
        const response = await fetch(`${API_BASE_URL}/`);
        if (response.ok) {
            console.log('API is available');
            return true;
        }
    } catch (error) {
        console.warn('API is not available. Make sure to start the server with: python api.py');
        showError('⚠️ API server not detected. Please run: python api.py');
        return false;
    }
}

// Initialize the application
function init() {
    // Load saved statistics
    loadStats();
    
    // Add reset button
    addResetButton();
    
    // Load rules from API
    loadRules();
    
    // Check API availability
    checkAPI();
    
    // Add event listeners to choice buttons
    const choiceButtons = document.querySelectorAll('.choice-btn');
    choiceButtons.forEach(button => {
        button.addEventListener('click', () => {
            const choice = button.getAttribute('data-choice');
            playGame(choice);
        });
    });
    
    // Add keyboard support
    document.addEventListener('keydown', (e) => {
        const keyMap = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors',
            '4': 'lizard',
            '5': 'spock',
            'r': 'rock',
            'p': 'paper',
            's': 'scissors',
            'l': 'lizard',
            'k': 'spock'
        };
        
        const choice = keyMap[e.key.toLowerCase()];
        if (choice) {
            playGame(choice);
        }
    });
}

// Start the application when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
