import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['dolap','perde','deve','eşşek']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Psst, the solution: {chosen_word}')
      
display = []

for _ in range(word_length):
      display +='_'
lives = 6

    

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
      
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives==0:
            end_of_game =True
            print('You lose')   
            
            
            

    print(f"{' '.join(display)}")

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True   
        
        print("You win.")        
        
    print(stages[lives])
           
