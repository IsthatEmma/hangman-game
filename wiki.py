import random

def is_letter_in_word(letter, word_list):
  
    return letter in word_list

def hangman(word):
   
    word_list = list(word)  
    guessed_letters = ["_"] * len(word_list) 
    attempts = 6  
    guessed_set = set() 
    
    print("Welcome to Hangman!")
    print(" ".join(guessed_letters))  
    while attempts > 0 and "_" in guessed_letters:
        guess = input("Guess a letter! :) ").lower()

     
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
       
        if guess in guessed_set:
            print("Silly, You already guessed that letter! Try again!")
            continue

        guessed_set.add(guess)

      
        if is_letter_in_word(guess, word_list):
            print("Good guess so far :D!")
           
            for i, letter in enumerate(word_list):
                if letter == guess:
                    guessed_letters[i] = guess
        else:
            print("No Sorry! :(")
            attempts -= 1  
        
      
        print(" ".join(guessed_letters))
        print(f"Attempts remaining: {attempts}")
    
   
    if "_" not in guessed_letters:
        print("Congrats! You guessed the word yay! :) ", word)
    else:
        print("Game over! The correct was:", word)


words = ["Mr Marestaing", "Brawl Stars", "Amazing", "Heart", "Dancing"]


random_word = random.choice(words)
hangman(random_word)
