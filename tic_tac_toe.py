r1 =['-','-','-']
r2 =['-','-','-']
r3 =['-','-','-']

tic_tac_toe_list=[r1,r2,r3]

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
    except:
        print("invalid option choose")
    else:
        return n


def intro():
    print('|Welcome to tic tac toe|')
    print('------------------------')
    game_tipe=input('|Select game tipe , 1vs1 (press 1) or 1vs machine (press 2):')
    return game_tipe

if intro()=='1':
    print("Player who cohoose 'o' starts")
    game_won=False

    current_player=0
    print(f'{r1}\n{r2}\n{r3}\n')

def verifi_pozition(raw,collum):
    if tic_tac_toe_list[raw][collum]=='O' or tic_tac_toe_list[raw][collum]=='X':



    while game_won==False:
        raw=0
        collum=0
        if current_player%2==0:
            print('"O" turn')
            raw=input('Select raw:')
            raw=verify_int(raw)
            collum=input('Select collum:')
            collum=verify_int(collum)
            game_state(raw,collum,current_player)
            print(f'{r1}\n{r2}\n{r3}\n')
        else:
            print('"X" turn')
            raw = input('Select raw:')
            raw = verify_int(raw)
            collum = input('Select collum:')
            collum = verify_int(collum)
            game_state(raw, collum, current_player)
            print(f'{r1}\n{r2}\n{r3}\n')
        current_player+=1

