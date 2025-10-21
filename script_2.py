
js_content = """// Game State
let deck = [];
let playerHand = [];
let computerHand = [];
let discardPile = [];
let currentPlayer = 'player'; // 'player' or 'computer'
let currentColor = '';
let gameOver = false;
let pendingWildCard = null; // Track wild card being played for cancellation

// Card colors and values
const colors = ['red', 'yellow', 'green', 'blue'];
const values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw2'];
const wilds = ['Wild', 'Wild Draw4'];

// Initialize the game
function initGame() {
    gameOver = false;
    deck = [];
    playerHand = [];
    computerHand = [];
    discardPile = [];
    currentPlayer = 'player';
    pendingWildCard = null;
    
    // Create deck
    createDeck();
    shuffleDeck();
    
    // Deal initial cards
    for (let i = 0; i < 7; i++) {
        playerHand.push(deck.pop());
        computerHand.push(deck.pop());
    }
    
    // Set first discard card (not a wild card)
    let firstCard;
    do {
        firstCard = deck.pop();
    } while (firstCard.color === 'wild');
    
    discardPile.push(firstCard);
    currentColor = firstCard.color;
    
    updateDisplay();
    updateMessage('Your turn! Play a card or draw from the deck.');
}

// Create deck of UNO cards
function createDeck() {
    // Add number and action cards (2 of each except 0)
    colors.forEach(color => {
        deck.push({ color: color, value: '0' });
        for (let i = 0; i < 2; i++) {
            values.slice(1).forEach(value => {
                deck.push({ color: color, value: value });
            });
        }
    });
    
    // Add wild cards (4 of each type)
    for (let i = 0; i < 4; i++) {
        wilds.forEach(wild => {
            deck.push({ color: 'wild', value: wild });
        });
    }
}

// Shuffle deck
function shuffleDeck() {
    for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
    }
}

// Draw card from deck
function drawCard() {
    if (currentPlayer !== 'player' || gameOver) return;
    
    if (deck.length === 0) {
        reshuffleDeck();
    }
    
    const drawnCard = deck.pop();
    playerHand.push(drawnCard);
    
    // Check if the drawn card can be played
    if (canPlayCard(drawnCard)) {
        updateMessage('You drew a card that can be played! Play it or pass your turn.');
        updateDisplay();
    } else {
        updateMessage('You drew a card. Computer\\'s turn...');
        currentPlayer = 'computer';
        updateDisplay();
        
        setTimeout(() => {
            computerTurn();
        }, 1000);
    }
}

// Reshuffle discard pile into deck
function reshuffleDeck() {
    const topCard = discardPile.pop();
    deck = [...discardPile];
    discardPile = [topCard];
    shuffleDeck();
}

// Play a card
function playCard(cardIndex, isPlayer = true) {
    const hand = isPlayer ? playerHand : computerHand;
    const card = hand[cardIndex];
    
    if (!canPlayCard(card)) {
        if (isPlayer) {
            updateMessage('You cannot play that card!');
        }
        return false;
    }
    
    // Remove card from hand
    hand.splice(cardIndex, 1);
    
    // Add to discard pile
    discardPile.push(card);
    
    // Handle wild cards
    if (card.color === 'wild') {
        if (isPlayer) {
            pendingWildCard = card; // Store for potential cancellation
            showColorPicker();
            return true;
        } else {
            // Computer chooses most common color in hand
            currentColor = chooseColorForComputer();
            updateMessage(`Computer played ${card.value} and chose ${currentColor}!`);
        }
    } else {
        currentColor = card.color;
    }
    
    // Handle special cards
    const shouldSkipTurn = handleSpecialCard(card, isPlayer);
    
    // Check for win
    if (hand.length === 0) {
        gameOver = true;
        updateMessage(isPlayer ? '🎉 YOU WIN! 🎉' : '😢 Computer wins!');
        updateDisplay();
        return true;
    }
    
    // For Skip and Reverse, player can play another card
    if (!gameOver && (card.value === 'Skip' || card.value === 'Reverse') && isPlayer) {
        updateMessage('Turn skipped! You can play another card or draw.');
        updateDisplay();
        return true;
    }
    
    // Switch turns for other cards
    if (!gameOver && !shouldSkipTurn) {
        currentPlayer = isPlayer ? 'computer' : 'player';
        updateDisplay();
        
        if (currentPlayer === 'computer') {
            setTimeout(() => {
                computerTurn();
            }, 1000);
        } else {
            updateMessage('Your turn!');
        }
    }
    
    return true;
}

// Check if a card can be played
function canPlayCard(card) {
    const topCard = discardPile[discardPile.length - 1];
    
    if (card.color === 'wild') return true;
    if (card.color === currentColor) return true;
    if (card.value === topCard.value) return true;
    
    return false;
}

// Handle special cards
function handleSpecialCard(card, isPlayer) {
    const opponent = isPlayer ? computerHand : playerHand;
    let skipTurn = false;
    
    switch (card.value) {
        case 'Skip':
            updateMessage(isPlayer ? 'Computer\\'s turn is skipped! Play another card.' : 'Your turn is skipped!');
            skipTurn = isPlayer; // Player keeps their turn
            break;
            
        case 'Reverse':
            updateMessage(isPlayer ? 'Computer\\'s turn is skipped! Play another card.' : 'Your turn is skipped!');
            skipTurn = isPlayer; // Player keeps their turn
            break;
            
        case 'Draw2':
            for (let i = 0; i < 2; i++) {
                if (deck.length === 0) reshuffleDeck();
                opponent.push(deck.pop());
            }
            updateMessage(isPlayer ? 'Computer draws 2 cards!' : 'You draw 2 cards!');
            break;
            
        case 'Wild Draw4':
            for (let i = 0; i < 4; i++) {
                if (deck.length === 0) reshuffleDeck();
                opponent.push(deck.pop());
            }
            updateMessage(isPlayer ? 'Computer draws 4 cards!' : 'You draw 4 cards!');
            break;
    }
    
    return skipTurn;
}

// Computer's turn AI
function computerTurn() {
    if (gameOver) return;
    
    // Find playable cards
    const playableCards = computerHand.map((card, index) => ({ card, index }))
        .filter(({ card }) => canPlayCard(card));
    
    if (playableCards.length > 0) {
        // Prioritize action cards and wild cards
        playableCards.sort((a, b) => {
            const priorities = {
                'Wild Draw4': 5,
                'Wild': 4,
                'Draw2': 3,
                'Skip': 2,
                'Reverse': 2
            };
            const aPriority = priorities[a.card.value] || 1;
            const bPriority = priorities[b.card.value] || 1;
            return bPriority - aPriority;
        });
        
        const { index } = playableCards[0];
        updateMessage('Computer is playing...');
        
        setTimeout(() => {
            playCard(index, false);
        }, 500);
    } else {
        // Computer must draw a card
        updateMessage('Computer draws a card...');
        
        if (deck.length === 0) reshuffleDeck();
        const drawnCard = deck.pop();
        computerHand.push(drawnCard);
        
        // Check if computer can play the drawn card
        if (canPlayCard(drawnCard)) {
            updateMessage('Computer drew a playable card and plays it...');
            const cardIndex = computerHand.length - 1;
            setTimeout(() => {
                playCard(cardIndex, false);
            }, 1000);
        } else {
            setTimeout(() => {
                currentPlayer = 'player';
                updateDisplay();
                updateMessage('Your turn!');
            }, 1000);
        }
    }
}

// Choose color for computer (most common color in hand)
function chooseColorForComputer() {
    const colorCounts = { red: 0, yellow: 0, green: 0, blue: 0 };
    
    computerHand.forEach(card => {
        if (card.color !== 'wild') {
            colorCounts[card.color]++;
        }
    });
    
    let maxColor = 'red';
    let maxCount = 0;
    
    for (const [color, count] of Object.entries(colorCounts)) {
        if (count > maxCount) {
            maxCount = count;
            maxColor = color;
        }
    }
    
    return maxColor;
}

// Show color picker modal
function showColorPicker() {
    document.getElementById('color-picker').style.display = 'block';
}

// Hide color picker modal
function hideColorPicker() {
    document.getElementById('color-picker').style.display = 'none';
}

// Cancel wild card selection
function cancelWildCard() {
    if (pendingWildCard) {
        // Return the wild card to player's hand
        discardPile.pop(); // Remove from discard pile
        playerHand.push(pendingWildCard); // Add back to hand
        pendingWildCard = null;
        
        hideColorPicker();
        updateDisplay();
        updateMessage('Wild card canceled. Choose another card.');
    }
}

// Choose color from modal
function chooseColor(color) {
    currentColor = color;
    pendingWildCard = null; // Clear pending card
    hideColorPicker();
    
    // Check for win after playing wild card
    if (playerHand.length === 0) {
        gameOver = true;
        updateMessage('🎉 YOU WIN! 🎉');
        updateDisplay();
        return;
    }
    
    updateMessage(`You chose ${color}. Computer's turn...`);
    currentPlayer = 'computer';
    updateDisplay();
    
    setTimeout(() => {
        computerTurn();
    }, 1000);
}

// Update display
function updateDisplay() {
    // Update player cards
    const playerCardsDiv = document.getElementById('player-cards');
    playerCardsDiv.innerHTML = '';
    
    playerHand.forEach((card, index) => {
        const cardDiv = createCardElement(card, index, true);
        playerCardsDiv.appendChild(cardDiv);
    });
    
    // Update computer cards (show as card backs)
    const computerCardsDiv = document.getElementById('computer-cards');
    computerCardsDiv.innerHTML = '';
    
    computerHand.forEach(() => {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'card card-back';
        cardDiv.textContent = 'UNO';
        computerCardsDiv.appendChild(cardDiv);
    });
    
    // Update card counts
    document.getElementById('computer-count').textContent = computerHand.length;
    
    // Update discard pile
    const discardPileDiv = document.getElementById('discard-pile');
    discardPileDiv.innerHTML = '';
    
    if (discardPile.length > 0) {
        const topCard = discardPile[discardPile.length - 1];
        const cardDiv = createCardElement(topCard, -1, false);
        discardPileDiv.appendChild(cardDiv);
    }
    
    // Update current player
    document.getElementById('current-player').textContent = 
        `Current Turn: ${currentPlayer === 'player' ? 'Player' : 'Computer'}`;
}

// Create card element
function createCardElement(card, index, isClickable) {
    const cardDiv = document.createElement('div');
    const displayColor = card.color === 'wild' ? 'wild' : card.color;
    cardDiv.className = `card ${displayColor}`;
    
    if (isClickable && currentPlayer === 'player' && !gameOver) {
        if (canPlayCard(card)) {
            cardDiv.addEventListener('click', () => playCard(index, true));
            cardDiv.style.cursor = 'pointer';
        } else {
            cardDiv.classList.add('disabled');
        }
    }
    
    cardDiv.innerHTML = `<span class="card-value">${card.value}</span>`;
    
    return cardDiv;
}

// Update message
function updateMessage(message) {
    document.getElementById('game-message').textContent = message;
}

// Set up event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // New Game button
    const newGameBtn = document.getElementById('new-game-btn');
    if (newGameBtn) {
        newGameBtn.addEventListener('click', initGame);
    }
    
    // Draw pile
    const drawPile = document.getElementById('draw-pile');
    if (drawPile) {
        drawPile.addEventListener('click', drawCard);
    }
    
    // Color picker buttons
    const colorButtons = document.querySelectorAll('.color-btn');
    colorButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const color = this.getAttribute('data-color');
            chooseColor(color);
        });
    });
    
    // Close button for color picker
    const closeBtn = document.getElementById('close-color-picker');
    if (closeBtn) {
        closeBtn.addEventListener('click', cancelWildCard);
    }
    
    // Start the game
    initGame();
});"""

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✓ Updated script.js")
print("\n" + "="*60)
print("ALL FIXES APPLIED:")
print("="*60)
print("1. ✓ Fixed card text size - Long text now stays inside cards")
print("2. ✓ Added X button to color picker - Cancel wild cards anytime")
print("3. ✓ Skip/Reverse now let you play another card immediately")
print("4. ✓ Drawing a playable card lets you play it before turn ends")
print("5. ✓ Computer also plays drawn cards if they match")
print("\n" + "="*60)
print("Refresh your browser to see all changes!")
print("="*60)
