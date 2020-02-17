from info import *

import random


current_level = 1
game_still_going = True
max_level = 3


def pickup_words():
    words_list = []
    while len(words_list) < current_level + 3:
        random_word = random.choice(levels_map[current_level])
        if random_word in words_list:
            continue
        else:
            words_list.append(random_word)

    return words_list


def pickup_choices(words_list):
    alpha_dic = letters_count.copy()
    letters = []
    for a in alphabets:
        for i in words_list:
            x = i.lower().count(a)
            if x > alpha_dic[a+'_count']:
                alpha_dic[a+'_count'] = x
        if alpha_dic[a+'_count'] != 0:
            for e in range(alpha_dic[a+'_count']):
                letters.append(a)

    return letters


def start_game():
    not_completed = True
    new_words_list = pickup_words()
    remaining = current_level + 3
    choices = pickup_choices(new_words_list)
    extras = []
    known = []
    print('Level ' + str(current_level)+'\n')
    print('Guess ' + str(remaining) + ' Words\n')
    print()
    while not_completed:
        print('Guess a word !\t\t\t', choices)
        ans = input()
        if ans in new_words_list and ans not in known:
            remaining -= 1
            known.append(ans)
            if remaining != 0:
                print('You got it ' + str(remaining) + ' words remaining !')
        elif ans in levels_map[current_level]:
            in_there = True
            for a in ans:
                if a.lower() not in choices or ans.count(a) > choices.count(a.lower()):
                    in_there = False
                    break
            if in_there and ans not in extras and ans not in known:
                extras.append(ans)
                print('added to the extra, Keep moving !')
            else:
                print('Nope, Try again buddy !')
        else:
            print('Nope, Try again buddy!')
        if remaining == 0:
            not_completed = False
    print('Yay, You completed the first level ! Press any key to continue..')
    input()


while game_still_going:
    if current_level > max_level:
        print('You finished the game boss !!!')
        game_still_going = False
    else:
        start_game()
        current_level += 1
