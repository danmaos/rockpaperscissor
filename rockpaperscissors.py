import random
choice = ['k', 'n', 'b']
a, b = 0, 0

def check_ans(t):
    if t == 'k':
        print('kamen')
    elif t == 'b':
        print('bumaga')
    elif t == 'n':
        print('nozhnicy')

def main():
    global a
    global b
    while True:
        turn = input("please enter your turn: ('k', 'n', 'b'): ").lower()
        while True:
            if turn not in 'knb':
                turn = input("enter only ('k', 'n', 'b'): ").lower()
            else:
                break
        if turn == 'exit':
            break
        else:
            check_ans(turn)
        c_turn = random.choice(choice)
        check_ans(c_turn)

        if turn == 'k' and c_turn == 'n' or turn == 'b' and c_turn == 'k' or turn == 'n' and c_turn =='b':
            print('you win')
            a += 1
        elif c_turn == 'k' and turn == 'n' or c_turn == 'b' and turn == 'k' or c_turn == 'n' and turn == 'b':
            print('comp win')
            b += 1
        elif turn == c_turn:
            print('draw')
        print('Your score: ', a)
        print('Comp score: ', b)
main()