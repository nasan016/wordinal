from random import randint
from os import system

system('cls')

words = open('words.txt', 'r').readlines()

random_integer = randint(0, len(words) - 1)
random_word = (words[random_integer]).strip('\n').upper()
random_word_temp = []
[random_word_temp.append(j) for j in random_word]


available_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
                     ,'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                     'X', 'Y', 'Z']
letters_used = []

num_guess = 6

green_square = '\U0001f7e9' #Correct Letter/Place
red_square = '\U0001f7e5' #Wrong Letter
yellow_square = '\U0001f7e8' #Correct Letter

prev = []


ending = 'You Lose! The word was {}.'.format(random_word)
print("\nWelcome to Wordinal!\n ")

while num_guess != 0:

    letter_1 = red_square
    letter_2 = red_square
    letter_3 = red_square
    letter_4 = red_square
    letter_5 = red_square

    status = '{}{}{}{}{}'.format(letter_1, letter_2, letter_3, letter_4,
                                 letter_5)
    print('Letter Bank: ' + (' '.join(str(x) for x in available_letters)))
    print('Letters Used: ' + ' '.join(str(k) for k in letters_used))
    print('Previous Guess:')

    #Append previous guess and previous status, print to one line both.

    print(('\n'.join(str(o) for o in prev)))



    guess = input('\nGuess: ')[:5].upper()


    if guess == random_word:
        ending = 'You Win!'
        break
    else:
        for i in range(len(guess)):
            if guess[i] in available_letters:
                index = available_letters.index(guess[i])
                del available_letters[index]
            if guess[i] not in letters_used:
                letters_used.append(guess[i])

            if guess[i] in random_word_temp:
                if i == 0:
                    if guess[i] in random_word_temp:
                        letter_1 = yellow_square
                    if guess[i] == random_word_temp[i]:
                        letter_1 = green_square

                elif i == 1:
                    if guess[i] in random_word:
                        letter_2 = yellow_square
                    if guess[i] == random_word_temp[i]:
                        letter_2 = green_square

                elif i == 2:
                    if guess[i] in random_word_temp:
                        letter_3 = yellow_square
                    if guess[i] == random_word_temp[i]:
                        letter_3 = green_square

                elif i == 3:
                    if guess[i] in random_word_temp:
                        letter_4 = yellow_square
                    if guess[i] == random_word_temp[i]:
                        letter_4 = green_square


                elif i == 4:
                    if guess[i] in random_word_temp:
                        letter_5 = yellow_square
                    if guess[i] == random_word_temp[i]:
                        letter_5 = green_square


    status = '{}{}{}{}{}'.format(letter_1, letter_2,
                                 letter_3, letter_4, letter_5)


    prev_guess_status = '{} {}'.format(guess, status)
    prev.append(prev_guess_status)
    letters_used.sort()

    num_guess -= 1


    system('cls')

print(ending)


