# Blackjack Game 🎲

A command-line implementation of the popular card game **Blackjack** in Python, where you can play against the computer. The objective is to score as close to 21 as possible without going over.

## Features

- **Blackjack Rules**: Basic rules are implemented, including card drawing, score calculation, and determining the winner.
- **User vs. Computer**: The player competes against the computer, which acts as the dealer.
- **Simple and Interactive**: Offers a clear text-based interface for interaction.
- **Replay Option**: After each round, the player can choose to play again or exit the game.

## How to Play

1. **Initial Deal**: Both the player and the computer are dealt two cards.
2. **Player's Turn**: The player can choose to draw an additional card or pass.
3. **Computer's Turn**: The computer draws cards until its score is at least 17.
4. **Game Ends**: The game ends when either the player or the computer reaches Blackjack (21), exceeds 21, or passes.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/tarun1847/blackjack.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd blackjack-game
    ```

3. **Run the game**:

    ```bash
    python main.py
    ```

## Rules of the Game

- **Blackjack (21)**: A hand of 21 points with just two cards (an Ace and a 10-point card) is called Blackjack.
- **Bust**: If a player’s score exceeds 21, they lose.
- **Player's Turn**: After being dealt two cards, the player can choose to:
  - Draw a card.
  - Pass (stick with their current hand).
- **Computer's Turn**: The computer (dealer) will draw cards until its score is 17 or higher.

## Example Gameplay

```bash
WELCOME TO BLACKJACK!!!
Your cards: [10, 8] and Your current score is: 18
Computer's card: 9
type 'y' if you want a third card or 'n' to pass: n
Computer's final cards were [9, 7, 3] and score: 19
You lose!
