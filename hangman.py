import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'pineapple', 'watermelon']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def main():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    while True:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        if incorrect_guesses == max_attempts:
            print("You've run out of attempts. The word was '{}'.".format(word))
            break

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word '{}' correctly!".format(word))
            break

if __name__ == "__main__":
    main()
