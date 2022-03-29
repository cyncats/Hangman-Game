#Step 1 
import random
from hangman_words import word_list


import hangman_words


word_choosen = random.choice(hangman_words.word_list)
print(word_choosen)

end_of_game = False
lifes = 6

#create blanks
display = []
word_length = len(word_choosen)

#letters_separate = list(word_choosen.split())
for _ in word_choosen:
    display += "_"


from hangman_art import logo
print(logo)

while not end_of_game:
    guessLetter = input("type a letter: ").lower()

    if guessLetter in display:
       print(f"You already guessed that letter {guessLetter}")

    #check guessed letters
    for position in range(len(word_choosen)):
        letter = word_choosen[position]
        if letter == guessLetter:
            display[position] = letter
    if guessLetter not in word_choosen:
        print(f"You guessed {guessLetter}, that's not in the word, you lose a life.")
        lifes -= 1
        if lifes == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")     

    if "_" not in display:
        end_of_game = True
        print("you won! ")
        
    from hangman_art import stages
    print(stages[lifes])        


