def welcome_screen():
    """This function is printing the 'welcome screen' to the user"""
    HANGMAN_ASCII_ART = str("""

    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝""""")

    MAX_TRIES_ART = """
     ██████╗     ████████╗██████╗ ██╗███████╗███████╗
    ██╔════╝     ╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝
    ███████╗        ██║   ██████╔╝██║█████╗  ███████╗
    ██╔═══██╗       ██║   ██╔══██╗██║██╔══╝  ╚════██║
    ╚██████╔╝       ██║   ██║  ██║██║███████╗███████║
     ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                   """
    print(HANGMAN_ASCII_ART, MAX_TRIES_ART)


def check_valid_input(players_guess, old_letters_guessed):
    """This function returns a bolian value that represents if the char is valid
    :param old_letters_guessed: a list of all te letters that have been guessed
    :type:list
    :return:list
    :rtype: bool
    :param players_guess:a guessed letter
    :type:str
    :return:str
    :rtype:bool, str"""
    if len(players_guess) > 1 or not players_guess.isalpha():
        return False
    elif players_guess in old_letters_guessed:
        return False
    elif players_guess.isalpha():
        return True


def errors(players_guess):
    """This function gives an error messages to the user if he makes any
    :param: players_guess: the input that the user gave
    :type: str
    :return: str
    :rtype: bool , str"""
    if len(players_guess) > 1 and not players_guess.isalpha():
        return False, print("E3\n Oppss got confused there huh?")
    elif not players_guess.isalpha() and not players_guess.isdigit():
        return False, print("E3\n Oppss got confused there huh?")
    elif not players_guess.isalpha():
        return False, print("E2\nI am sorry, i am not a calculator :(")
    elif len(players_guess) > 1:
        return False, print("E1\n No no one letter at a time please.")
    else:
        return True


def try_update_letter_guessed(old_letters_guessed, players_guess, secret_word):
    """This function uses the function is_valid_input and does 2 things:
    1.If the letter is valid and haven't been guessed its adds it to the list of letters that have been guessed and
     prints "true" to the player screen.
    2.If the letter is not valid the function returns "X" and underneath the list of letters that have been
     guessed(old_letters_guessed)
    :param secret_word: the hidden word
    :type: str
    :return:str
    :rtype: str
    :param old_letters_guessed: a list of all te letters that have been guessed
    :type:list
    :return:list
    :rtype: str
    :param players_guess:a guessed letter
    :type:str
    :return:str
    :rtype:str. """
    if players_guess in secret_word and check_valid_input(players_guess, old_letters_guessed) == True:
        old_letters_guessed += players_guess
        print("nice! You guessed right!:)")
    elif players_guess not in secret_word and check_valid_input(players_guess, old_letters_guessed) == True:
        old_letters_guessed.append(players_guess)
        return print("X\nSorry that's not it :(\n", " -> ".join(old_letters_guessed))


def show_hidden_word(secret_word, old_letters_guessed):
    """this function shows the player if he was correct with his guess or not
    :param secret_word: the hidden word
    :type: str
    :return:str
    :rtype: bool
    :param old_letters_guessed: a list of all te letters that have been guessed
    :type:list
    :return:list
    :rtype: bool"""
    reveal_word = ""
    for char in secret_word:
        if char in old_letters_guessed:
            reveal_word += char
        elif char not in old_letters_guessed:
            reveal_word += "_ "
    print(reveal_word)
    if "_" in reveal_word:
        return False
    elif "_" not in reveal_word:
        return True


def print_hangman(num_of_tries):
    """this function is responsible to print the right image by the number of tries the player has left
     :param: num_of_tries: represents the number of tries the player have
     :type: dict
     :rtype:str"""
    HANGMAN_PHOTOS = {6: """    x-------x """,
                      5: """     
        x-------x
        |
        |
        |
        |
        |""",
                      4: """
        x-------x
        |       |
        |       0
        |
        |
        |
    """,
                      3: """   
        x-------x
        |       |
        |       0
        |       |
        |
        |""",
                      2: """   
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
    """,
                      1: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    """,
                      0: """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """}
    print(HANGMAN_PHOTOS[num_of_tries],"\n" *3)
    if num_of_tries == 0:
        print("Sorry it's GAME OVER for you :)")


def choose_word(file_path, index):
    """this function is responsible on choosing the 'secret word'(by players input)
    :param: file_path: thats the file path were the word is in
    :type: str
    :rtype: str
    :param:index: the input that chooses the word in the file
    :type: int
    :rtype: str"""
    file = open(file_path, "r")
    file_list = file.read().split(" ")
    file.close()
    list_of_words = []
    for word in file_list:
        if word not in list_of_words:
            list_of_words.append(word)
    if index > len(list_of_words):
        index = index % len(list_of_words)
    word_chosen = list_of_words[int(index) - 1]
    return word_chosen


def main():
    welcome_screen()
    file_path = input("place your file path here please!: \n")
    index = int(input("place here the index please: \n"))
    secret_word = choose_word(file_path, index)
    tbg_word = len(secret_word) * "_ "  # tbg= to be guessed word
    print(tbg_word, "\n"*4)
    old_letters_guessed = []
    old_letters_guessed.sort()
    MAX_TRIES = 6
    print_hangman(MAX_TRIES)
    while True:
        players_guess = input("Are you ready?\nGuess a letter! :\n").lower()
        if players_guess not in secret_word and players_guess.isalpha() and len(players_guess) <= 1\
                and players_guess not in old_letters_guessed:
            MAX_TRIES += -1
        check_valid_input(players_guess, old_letters_guessed)
        try_update_letter_guessed(old_letters_guessed, players_guess, secret_word)
        errors(players_guess)
        show_hidden_word(secret_word, old_letters_guessed)
        print_hangman(MAX_TRIES)
        if MAX_TRIES == 0:
            break
        elif show_hidden_word(secret_word, old_letters_guessed) == True:
            print("THATS IT!! YOU WIN!!")
            break
    print("Thank's for playing!")


if __name__ == '__main__':
    main()
