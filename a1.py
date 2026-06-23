# DO NOT modify or add any import statements
from support import *

ALL_WORDS = load_words("words.txt")

# Name: Tushar Kalaskar
# Student Number: s5018315
# Favorite Word: tennis
# -----------------------------------------------------------------------------

# Define your functions here
def is_unique(guess:str)->bool:
    """Check if all characters in guess are unique.

    Parameters: guess (str)
    Returns: bool
    """
    a = ""
    for i in guess:
        if i not in a:
            a += i
    if (a == guess):
        print(True)
    else:
        print(False)


def num_hours()->float:
    """Return estimated hours spent.

    Parameters: None
    Returns: float
    """
    return float(5)

def has_won(guess: str, target: str) -> bool:
    """Return estimated hours spent.

        Parameters: None
        Returns: float
    """
    if guess==target:
        return True
    return False

def get_max_guesses() -> int:
    """Prompt user for number of guesses between 5 and 9.

       Parameters: None
       Returns: int
    """
    while True:
        guess = input(GET_NUM_GUESSES_MESSAGE)
        if guess.isdigit():
            # 3. Only convert to int NOW, because we know it's a number
            guess = int(guess)

            # 4. Check the bounds
            if 5 <= guess <= 9:
                return guess

def create_board(max_guesses: int) ->list[tuple[str, str]]:
    """Create empty game board.

        Parameters: max_guesses (int)
        Returns: list[tuple[str, str]]
    """
    entry = GUESS_LENGTH*EMPTY
    board = []
    for i in range(max_guesses):
        board.append((entry,entry))

    return board

def display_board(board: list[tuple[str, str]]) ->None:
    """Display current game board.

      Parameters: board (list[tuple[str, str]])
      Returns: None
    """
    for i, entry in enumerate(board):
        guess = entry[0]
        feedback = entry[1]
        print(SEP)
        print(f"Guess {i + 1}:  {guess}")
        print(f"Feedback: {feedback}")

    print(SEP)

def generate_secret_word() -> str:
    """Select a random word from word list.

        Parameters: None
        Returns: str
    """
    index=randint(0,len(ALL_WORDS)-1)
    return ALL_WORDS[index]

def validate_input(command:str) -> bool:
    """Validate user command or guess.

       Parameters: command (str)
       Returns: bool
    """
    if command in HELP_COMMAND or command in QUIT_COMMAND or command in KEYBOARD_COMMAND:
        return True

        # Must be exactly GUESS_LENGTH alphabetic characters
    if len(command) != GUESS_LENGTH or not command.isalpha():
        print(INVALID_FORMAT_MESSAGE)
        return False

        # Must be all lowercase and all characters must be unique
    if not command.islower() or len(set(command)) != len(command):
        print(INVALID_CHARACTERS_MESSAGE)
        return False

        # Must appear in the game's vocabulary
    if command not in ALL_WORDS:
        print(INVALID_GUESS_MESSAGE)
        return False

    return True




def get_command() -> str:
    """Prompt user for a valid command.

      Parameters: None
      Returns: str
    """
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        if validate_input(command):
            return command


def get_feedback(guess: str, target: str) -> str:
    """Generate feedback string for a guess.

        Parameters: guess (str), target (str)
        Returns: str
    """
    feedback = ""
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback+='G'
        elif guess[i] in target:
            feedback+='Y'
        else:
            feedback+='B'

    return feedback

def update_board(board: list[tuple], guess_num: int, guess: str, target: str) -> None:
    """Update board with guess and feedback.

        Parameters: board (list), guess_num (int), guess (str), target (str)
        Returns: None
    """
    feedback = get_feedback(guess, target)
    board[guess_num-1]=(guess, feedback)

def display_keyboard(keyboard: dict[str, str]) -> None:
    """Display keyboard status.

        Parameters: keyboard (dict[str, str])
        Returns: None
    """
    print("Keyboard:")
    print(SEP)

    keys = list(keyboard.keys())
    for i in range(0, len(keys), 3):
        row_keys = keys[i: i + 3]
        row_string = ""

        for key in row_keys:
            row_string += f"{key}: {keyboard[key]}    "

        print(row_string)

    print(SEP)


def update_keyboard(board: list[tuple], keyboard: dict[str, str], guess_num: int) -> None:
    """Update keyboard based on latest guess.

        Parameters: board (list), keyboard (dict), guess_num (int)
        Returns: None
    """
    guess = board[guess_num - 1][0]
    feedback = board[guess_num - 1][1]
    for i in range(len(guess)):
        letter = guess[i]
        if letter in keyboard and keyboard[letter] != GREEN:
            keyboard[letter] = feedback[i]


def play_game() -> None:
    """Run the Weirdle game loop.

        Parameters: None
        Returns: None
    """
    print(WELCOME_MESSAGE)
    max_guesses = get_max_guesses()
    secret_word = generate_secret_word()
    board = create_board(max_guesses)
    keyboard = create_keyboard()

    display_board(board)

    guess_num = 1
    game_over = False

    while not game_over:
        command = get_command()

        if command in QUIT_COMMAND:
            game_over = True
        elif command in HELP_COMMAND:
            print(HELP_MESSAGE)
        elif command in KEYBOARD_COMMAND:
            display_keyboard(keyboard)
        elif not validate_input(command):
            continue
        else:
            update_board(board, guess_num, command, secret_word)
            update_keyboard(board, keyboard, guess_num)
            display_board(board)

            if has_won(command, secret_word):
                print(WIN_MESSAGE)
                game_over = True
            elif guess_num == max_guesses:
                print(f"{LOST_MESSAGE} The word was: {secret_word}")
                game_over = True
            else:
                guess_num += 1


def main() -> None:
    """Run game and handle replay.

        Parameters: None
        Returns: None
    """
    play_game()

    while True:
        again = input(RETRY_MESSAGE)
        if again.lower() == 'y':
            play_game()
        else:
            break


if __name__ == "__main__":
    main()