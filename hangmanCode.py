import random
from hangmanWords import word_list
from hangmanArt import stages,logo

#choosing a random word from list of words and setting max wrong tries(lives) as 6
chosenWord = random.choice(word_list)
lives = 6

#hangman logo    
print(logo)

#generating empty list and then displaying '_' for each letter
display = []
for i in range(len(chosenWord)):
     display.append("_")

#actual game of guessing the word
while "_" in display:
     guess = input("\nGuess a letter: ").lower()
     for i in range(len(chosenWord)):
         letter = chosenWord[i]
         if letter == guess:
             display[i] = letter
     if guess not in chosenWord:
        lives = lives-1
        if lives == 0:
            print("\nYou lose")
            exit(1)
     print(f"{' '.join(display)}")
     print(stages[lives])
else:
     print("\nYou have won")

