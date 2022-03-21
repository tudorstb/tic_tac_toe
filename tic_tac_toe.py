import random



def game_state(raw,collum,current_player):
    raw-=1
    collum-=1
    if current_player%2==0:
        tic_tac_toe_list[raw][collum]='O'
    else:
        tic_tac_toe_list[raw][collum]='X'

def verify_int(n):
    try:
        n=int(n)
        assert n<4 and n>0
    except:
        print("invalid option choose")
        return -1
    else:
        return n

def verify_int_bot(n):
    try:
        n=int(n)
        assert n<4 and n>0
    except:
        return -1
    else:
        return n


def intro():
    print('|Welcome to tic tac toe|')
    print('------------------------')
    game_tipe=input('|Select game tipe , 1vs1 (press 1) or 1vs machine (press 2):')
    return game_tipe

def verifi_pozition(raw,collum):
    if tic_tac_toe_list[raw-1][collum-1]=='O' or tic_tac_toe_list[raw-1][collum-1]=='X':
        print("\n Pozition already occupied \n")

        return 0
    else:
        return 1
def verifi_pozition_bot(raw,collum):
    if tic_tac_toe_list[raw-1][collum-1]=='O' or tic_tac_toe_list[raw-1][collum-1]=='X':

        return 0
    else:
        return 1
def verifi_win(raw, collum,o_x):
    #line verify
    if tic_tac_toe_list[raw - 1].count(o_x) ==3:
        print(f'"{o_x}" won')
        return True
    #raw verify
    raw_verifi_count=0
    for elem in tic_tac_toe_list:
        if elem[collum-1]==o_x:
            raw_verifi_count+=1
    if raw_verifi_count==3:
        return True,print(f'"{o_x}" won')
    #diagonal verify
    #main diagonal
    if tic_tac_toe_list[0][0] ==  tic_tac_toe_list[1][1] == tic_tac_toe_list[2][2] ==o_x:
        return True,print(f'{o_x} won')
    #second diagonal
    if tic_tac_toe_list[0][2]==tic_tac_toe_list[1][1]==tic_tac_toe_list[2][0]==o_x:
        return True,print(f'"{o_x}" won')




    return False


replay='R'
players=intro()
if players=='1':
    while replay=='R' or replay=='r':
        r1 = ['-', '-', '-']
        r2 = ['-', '-', '-']
        r3 = ['-', '-', '-']

        tic_tac_toe_list = [r1, r2, r3]
        print("Player who cohoose 'o' starts")
        game_won=False

        current_player=0
        print(f'{r1}\n{r2}\n{r3}\n')

        entry_count = 0
        while game_won==False and entry_count!=9:
            raw=0
            collum=0
            if current_player%2==0:
                print('"O" turn')
                raw=-1
                while raw==-1:
                    raw=input('Select raw:')
                    raw=verify_int(raw)

                collum = -1
                while collum == -1:
                    collum = input('Select collum:')
                    collum = verify_int(collum)
                verifi = verifi_pozition(raw, collum)
                if verifi == 1:
                    game_state(raw, collum, current_player)
                    print(f'{r1}\n{r2}\n{r3}\n')
                    current_player += 1
                    game_won=verifi_win(raw, collum,"O")
                    entry_count += 1


            else:
                print('"X" turn')
                raw = -1
                while raw == -1:
                    raw = input('Select raw:')
                    raw = verify_int(raw)
                collum = -1
                while collum == -1:
                    collum = input('Select collum:')
                    collum = verify_int(collum)
                verifi = verifi_pozition(raw, collum)
                if verifi==1:
                    game_state(raw, collum, current_player)
                    print(f'{r1}\n{r2}\n{r3}\n')
                    current_player += 1
                    game_won=verifi_win(raw, collum,"X")
                    entry_count += 1

        if entry_count==9:
            print('Tie,you ran out of moves ')
        replay=input("If you wish to replay press (R):")
elif players=='2':

    while replay == 'R' or replay == 'r':
        r1 = ['-', '-', '-']
        r2 = ['-', '-', '-']
        r3 = ['-', '-', '-']

        tic_tac_toe_list = [r1, r2, r3]
        print("Player who cohoose 'o' starts")
        game_won = False

        current_player = 0
        print(f'{r1}\n{r2}\n{r3}\n')

        entry_count = 0
        choose = ""
        while choose!="o" and choose!="O" and choose!="x" and choose!="X":
            choose=input("Choose what you want to be(O/X)")
        if choose=='o' or choose=='O':
            while game_won == False and entry_count != 9:
                raw = 0
                collum = 0
                if current_player % 2 == 0:
                    print('"O" turn')
                    raw = -1
                    while raw == -1:
                        raw = input('Select raw:')
                        raw = verify_int(raw)

                    collum = -1
                    while collum == -1:
                        collum = input('Select collum:')
                        collum = verify_int(collum)
                    verifi = verifi_pozition(raw, collum)
                    if verifi == 1:
                        game_state(raw, collum, current_player)
                        print(f'{r1}\n{r2}\n{r3}\n')
                        current_player += 1
                        game_won = verifi_win(raw, collum, "O")
                        entry_count += 1

                else:
                    raw = -1
                    while raw == -1:
                        raw = random.randint(0,3)
                        raw =verify_int_bot(raw)
                    collum = -1
                    while collum == -1:
                        collum = random.randint(0,3)
                        collum = verify_int_bot(collum)
                    verifi = verifi_pozition_bot(raw, collum)
                    if verifi == 1:
                        game_state(raw, collum, current_player)
                        print(f'{r1}\n{r2}\n{r3}\n')
                        current_player += 1
                        game_won = verifi_win(raw, collum, "X")
                        entry_count += 1
        if choose=='x' or choose=='X':
            while game_won == False and entry_count != 9:
                raw = 0
                collum = 0
                if current_player % 2 == 0:
                    raw = -1
                    while raw == -1:
                        raw = random.randint(0, 3)
                        raw = verify_int_bot(raw)
                    collum = -1
                    while collum == -1:
                        collum = random.randint(0, 3)
                        collum = verify_int_bot(collum)
                    verifi = verifi_pozition_bot(raw, collum)
                    if verifi == 1:
                        game_state(raw, collum, current_player)
                        print(f'{r1}\n{r2}\n{r3}\n')
                        current_player += 1
                        game_won = verifi_win(raw, collum, "O")
                        entry_count += 1
                else:
                    print('"X" turn')
                    raw = -1
                    while raw == -1:
                        raw = input('Select raw:')
                        raw = verify_int(raw)

                    collum = -1
                    while collum == -1:
                        collum = input('Select collum:')
                        collum = verify_int(collum)
                    verifi = verifi_pozition(raw, collum)
                    if verifi == 1:
                        game_state(raw, collum, current_player)
                        print(f'{r1}\n{r2}\n{r3}\n')
                        current_player += 1
                        game_won = verifi_win(raw, collum, "X")
                        entry_count += 1
        if entry_count == 9:
            print('Tie,you ran out of moves ')
        replay = input("If you wish to replay press (R):")