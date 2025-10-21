

css_content = """@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    position: relative;
    overflow-x: hidden;
}

body::before {
    content: '';
    position: absolute;
    width: 300px;
    height: 300px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    top: -100px;
    left: -100px;
    animation: float 20s infinite ease-in-out;
}

body::after {
    content: '';
    position: absolute;
    width: 400px;
    height: 400px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 50%;
    bottom: -150px;
    right: -150px;
    animation: float 25s infinite ease-in-out reverse;
}

@keyframes float {
    0%, 100% {
        transform: translate(0, 0) scale(1);
    }
    50% {
        transform: translate(50px, 50px) scale(1.1);
    }
}

.game-container {
    max-width: 1400px;
    width: 100%;
    position: relative;
    z-index: 1;
}

h1 {
    text-align: center;
    color: white;
    font-size: 4em;
    font-weight: 800;
    margin-bottom: 30px;
    text-shadow: 0 5px 15px rgba(0,0,0,0.3);
    letter-spacing: 3px;
    animation: titleGlow 2s ease-in-out infinite alternate;
}

@keyframes titleGlow {
    from {
        text-shadow: 0 5px 15px rgba(0,0,0,0.3), 0 0 30px rgba(255,255,255,0.3);
    }
    to {
        text-shadow: 0 5px 15px rgba(0,0,0,0.3), 0 0 50px rgba(255,255,255,0.5);
    }
}

.game-status {
    background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.85) 100%);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 30px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.5);
}

#current-player {
    font-size: 1.4em;
    font-weight: 700;
    color: #667eea;
    text-transform: uppercase;
    letter-spacing: 1px;
}

#game-message {
    margin-top: 12px;
    font-size: 1.1em;
    color: #e74c3c;
    font-weight: 600;
    min-height: 30px;
    animation: messagePulse 0.5s ease-in-out;
}

@keyframes messagePulse {
    0% {
        opacity: 0;
        transform: translateY(-10px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.computer-hand, .player-hand {
    margin: 30px 0;
    position: relative;
}

h3 {
    color: white;
    text-align: center;
    margin-bottom: 20px;
    font-size: 1.8em;
    font-weight: 700;
    text-shadow: 0 3px 10px rgba(0,0,0,0.3);
    letter-spacing: 1px;
}

.card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
    min-height: 150px;
    padding: 25px;
    background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.08) 100%);
    border-radius: 20px;
    box-shadow: inset 0 4px 20px rgba(0,0,0,0.1), 0 8px 30px rgba(0,0,0,0.2);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.2);
}

.card {
    width: 90px;
    height: 135px;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1.2em;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3), inset 0 1px 2px rgba(255,255,255,0.3);
    border: 4px solid white;
    padding: 8px;
    word-wrap: break-word;
    overflow: hidden;
    position: relative;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.3) 0%, transparent 50%);
    border-radius: 8px;
    pointer-events: none;
}

.card:hover {
    transform: translateY(-15px) scale(1.05);
    box-shadow: 0 15px 40px rgba(0,0,0,0.4), inset 0 1px 2px rgba(255,255,255,0.3);
}

.card.disabled {
    opacity: 0.4;
    cursor: not-allowed;
    filter: grayscale(50%);
}

.card.disabled:hover {
    transform: none;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

.card-back {
    background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #2c3e50 100%);
    color: white;
    cursor: pointer;
    font-size: 1.1em;
    letter-spacing: 2px;
}

.card.red {
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 50%, #e74c3c 100%);
    color: white;
}

.card.yellow {
    background: linear-gradient(135deg, #f1c40f 0%, #f39c12 50%, #f1c40f 100%);
    color: #2c3e50;
}

.card.green {
    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 50%, #2ecc71 100%);
    color: white;
}

.card.blue {
    background: linear-gradient(135deg, #3498db 0%, #2980b9 50%, #3498db 100%);
    color: white;
}

.card.wild {
    background: linear-gradient(135deg, #2c3e50 0%, #e74c3c 25%, #f1c40f 50%, #2ecc71 75%, #3498db 100%);
    color: white;
    animation: wildShimmer 3s infinite linear;
    background-size: 200% 200%;
}

@keyframes wildShimmer {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.card-value {
    font-size: 2.5em;
    text-align: center;
    line-height: 1.2;
    max-width: 100%;
    word-wrap: break-word;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    position: relative;
    z-index: 1;
    font-weight: 900;
}

.game-table {
    display: flex;
    justify-content: center;
    margin: 50px 0;
    position: relative;
}

.game-table::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    top: 50%;
    left: 0;
}

.deck-area {
    display: flex;
    gap: 50px;
    align-items: center;
    position: relative;
    z-index: 1;
}

.card-pile {
    position: relative;
    transition: transform 0.3s ease;
}

.card-pile:hover {
    transform: scale(1.05);
}

#draw-pile {
    position: relative;
}

#draw-pile::after {
    content: '';
    position: absolute;
    width: 90px;
    height: 135px;
    background: rgba(44, 62, 80, 0.3);
    border-radius: 12px;
    top: 5px;
    left: 5px;
    z-index: -1;
}

#draw-pile .card {
    cursor: pointer;
    animation: cardPulse 2s ease-in-out infinite;
}

#draw-pile .card .card-value {
    font-size: 1.1em;
    letter-spacing: 2px;
}

@keyframes cardPulse {
    0%, 100% {
        box-shadow: 0 6px 20px rgba(0,0,0,0.3), 0 0 0 0 rgba(102, 126, 234, 0.7);
    }
    50% {
        box-shadow: 0 6px 20px rgba(0,0,0,0.3), 0 0 0 10px rgba(102, 126, 234, 0);
    }
}

#discard-pile .card {
    cursor: default;
    animation: cardAppear 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

@keyframes cardAppear {
    0% {
        transform: scale(0) rotate(-180deg);
        opacity: 0;
    }
    100% {
        transform: scale(1) rotate(0deg);
        opacity: 1;
    }
}

#new-game-btn {
    display: block;
    margin: 30px auto;
    padding: 18px 40px;
    font-size: 1.3em;
    font-weight: 700;
    color: white;
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 6px 25px rgba(231, 76, 60, 0.4);
    text-transform: uppercase;
    letter-spacing: 2px;
    position: relative;
    overflow: hidden;
}

#new-game-btn::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255,255,255,0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

#new-game-btn:hover::before {
    width: 300px;
    height: 300px;
}

#new-game-btn:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 10px 35px rgba(231, 76, 60, 0.6);
}

#new-game-btn:active {
    transform: translateY(-1px) scale(1.02);
}

/* Modal */
.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.8);
    backdrop-filter: blur(5px);
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.modal-content {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    margin: 10% auto;
    padding: 40px;
    border-radius: 25px;
    width: 90%;
    max-width: 450px;
    text-align: center;
    position: relative;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    animation: slideDown 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

@keyframes slideDown {
    from {
        transform: translateY(-100px) scale(0.8);
        opacity: 0;
    }
    to {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
}

.modal-content h3 {
    color: #2c3e50;
    margin-bottom: 30px;
    font-size: 2em;
    text-shadow: none;
}

.close-modal {
    position: absolute;
    top: 15px;
    right: 20px;
    font-size: 2.5em;
    font-weight: bold;
    color: #95a5a6;
    cursor: pointer;
    background: none;
    border: none;
    padding: 0;
    width: 40px;
    height: 40px;
    line-height: 40px;
    transition: all 0.3s ease;
    border-radius: 50%;
}

.close-modal:hover {
    color: #e74c3c;
    background: rgba(231, 76, 60, 0.1);
    transform: rotate(90deg);
}

.color-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.color-btn {
    padding: 25px;
    font-size: 1.3em;
    font-weight: 700;
    border: none;
    border-radius: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
    color: white;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    position: relative;
    overflow: hidden;
}

.color-btn::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255,255,255,0.4);
    transform: translate(-50%, -50%);
    transition: width 0.5s, height 0.5s;
}

.color-btn:hover::after {
    width: 200px;
    height: 200px;
}

.color-btn:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.color-btn:active {
    transform: translateY(-2px) scale(1.02);
}

.color-btn.red {
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
}

.color-btn.yellow {
    background: linear-gradient(135deg, #f1c40f 0%, #f39c12 100%);
    color: #2c3e50;
}

.color-btn.green {
    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
}

.color-btn.blue {
    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
}

/* Computer cards (back side) */
#computer-cards .card {
    background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #2c3e50 100%);
    color: white;
    cursor: default;
}

#computer-cards .card:hover {
    transform: none;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

#computer-cards .card .card-value {
    font-size: 1.1em;
    letter-spacing: 2px;
}

/* Responsive Design */
@media (max-width: 768px) {
    h1 {
        font-size: 2.5em;
    }
    
    .card {
        width: 70px;
        height: 105px;
    }
    
    .card-value {
        font-size: 2em;
    }
    
    .deck-area {
        gap: 30px;
    }
    
    .color-buttons {
        grid-template-columns: 1fr;
    }
}"""

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✓ Updated CSS for symbol styling")
print("\n" + "="*60)
print("CARD SYMBOLS UPDATED:")
print("="*60)
print("⊘ Skip card - Crossed circle symbol")
print("⇄ Reverse card - Bidirectional arrows")
print("+2 Draw 2 card - Simple +2")
print("+4 Wild Draw 4 card - Simple +4")
print("WILD Wild card - Text for regular wild")
print("\n✓ Increased symbol size to 2.5em for better visibility")
print("✓ Made symbols bold (font-weight: 900)")
print("✓ Kept number cards with regular size")
print("="*60)
print("Refresh your browser to see the new symbols!")
print("="*60)
