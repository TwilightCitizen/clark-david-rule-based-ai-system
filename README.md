# Building a Rule-Based AI System with Python

**David Clark**  
#0004796375  
CAP320-O  
Term C202509  
Section 01

## Part 1: Prompting the AI for Project Ideas

### Prompt(s) Supplied

> I am working on a Python school project to create a very simple Artificial Intelligence (AI) system based on rules or heuristics that a user can operate simply from a console/terminal. This is for an assignment to demonstrate how simple AI systems worked before the advent of Machine Learning (ML). Please suggest some project ideas for a simple console/terminal rule-based AI system. You may include examples like chatbots, recommendation systems, or diagnostic tools, but I would prefer simple games like Hi Lo, One Player Blackjack, Guess My Number, and similar.

### Ideas from GPT Responses

- Guess My Number: The computer picks a random number, and the user tries to guess it. The AI gives hints like "higher" or "lower" based on the guess.

- Hi-Lo Game: The AI presents a number, and the user guesses if the next number will be higher or lower. The AI uses rules to determine win/loss.

- One Player Blackjack: The user plays a simplified version of Blackjack against the computer, with the AI following basic rules for "hit" or "stand".

- Rock, Paper, Scissors: The user plays against the computer, and the AI follows the standard rules to determine the winner.

- Simple Chatbot: A rule-based chatbot that responds to user inputs with pre-defined answers or patterns (e.g., greetings, simple questions).

- Animal Guessing Game: The AI asks yes/no questions to guess the animal the user is thinking of, using a decision tree of rules.

- Basic Medical Symptom Checker: The AI asks about symptoms and suggests possible conditions based on rule-based logic.

- Simple Recommendation System: The AI recommends a movie, book, or activity based on user preferences using if-else rules.

- Text Adventure Game: The user navigates a simple story or dungeon, with the AI responding to commands using rule-based logic.

- Tic-Tac-Toe: The user plays against the computer, with the AI following basic strategies and rules.

### Selected Idea with Justification

Tic-Tac-Toe: This is a simple and fun game, but it will be interesting to see how the AI implements it.  Not only must it implement the rules for managing gameplay and determining the winner, but it must also implement a reasonable console user interface (UI) to display the gameboard.  Plus, there will be opportunity to tweak it a bit so that it can employ perfect strategy or just play the computer's turn randomly, making it easier for the human player to win.  Also, while I was thinking of simply card games, this just did not occur to me.

## Part 2: Designing Your Rule-Based System

### Prompt(s) Supplied

> I would like to implement the Tic-Tac-Toe game in Python.  Ideally, I envision a game loop running small functions that update the gameboard after the computer or human player takes a turn, prompt the human player for the row and column they wish to mark on their turn, allow the human player to quit at anytime, and determine when the computer or human player wins.  Can you briefly describe the various routines you would create and the conditions that would drive when each of them are run through each iteration of such a game loop?

### Rules from GPT Response

#### Game Loop Routines

- display_board(board):

    - Prints the current state of the gameboard to the console.
    
    - Called at the start of each turn to show the updated board.

- get_human_move(board):

    - Prompts the human player for their move (row and column), checks for valid input, and allows quitting.

    - Called when it’s the human player’s turn.

- get_computer_move(board):

    - Determines the computer’s move using a rule-based or random strategy.

    - Called when it’s the computer’s turn.

- make_move(board, row, col, player):

    - Updates the board with the player’s mark at the specified location.

    - Called after a valid move is chosen.

- check_winner(board):

    - Checks if there is a winner or if the game is a draw.

    - Called after each move to determine if the game should end.

- play_game():

    - The main game loop that alternates turns, calls the above routines, and manages game flow.

    - Runs until a win, draw, or quit.

#### Typical Game Loop

- display_board(board)
- If human’s turn: get_human_move(board)
- If computer’s turn: get_computer_move(board)
- make_move(board, row, col, player)
- check_winner(board)
- Repeat until win, draw, or quit

## Part 3: Coding Your Rule-Based System

### Prompt(s) Supplied

> Please implement the Tic Tac Toe game you just decribed in the file tic_tac_toe.py.  Ideally, use no external libraries or dependencies, relying soley on native Python functionality.  Use functional idioms over object-oriented idioms wherever possible.  If a function exceeds 5 lines of code, consider refactoring it into smaller functions.

> Please factor the creation of lines in check_winner into a separate function.

### Remarks on Implementation

The AI did a good job creating a coherent and performant implementation.  It did produce some functions that were much larger than 5 lines, so these functions were doing a lot more work than smaller more focal ones would do, making them harder to reason about at a glance.  Refactoring the AI's work by hand not only reduced the size and scope of the fuctions, but it assured better undertanding of what the AI produced, why it produced what it did, and how it all actually worked.  The resulting code after human refinment is more lines and functions, but they are better named, self-documenting, and far easier to reason about.

## Part 4: Reflection and Submission

### How the Rule-Based System Works

The rule-based system for Tic-Tac-Toe works by  running a loop indefinitely until certain conditions are met, namely when the human player quits the game or either player wins or draws.  While those conditions are outstanding, the logic retrieves human input, processes valid plays for both players, cautions the human player on invalid input, and updates and displays the game board each turn.  Of particular note, the computer simply takes the first open spot on the Tic-Tac-Toe board for its turn.  This could be modified to choose a random open spot, or to employ a more winning strategy.

All code paths work appropriately, handling good and bad human inputs, processing human and computer wins and draw, and human quitting.  Bad inputs are differentiated between garbage, out-of-bounds, and taken spots.

### Challenges Encountered

No challenges were encountered.