import random
import time

def player():
    while (True):
        while (True):
            try:
                N = int(input("Give the number of queens (>3)\n "))
                break
            except ValueError:
                print ("That was no valid number.")
        if (N > 3):
            return N


def printer(board):  #ektypwnei ton pinaka poy fainontai oi basilisses an exoyn topo8etei8ei
    a = "\u265B"
    b = "\u25EF"
    for i in range(0,N):
        print()
        for j in range(0,N):
            if (board[i][j] == 0):
                print(b," ", end="")    
            else:
                print(a," ",end="")
    print()


def multitool (a,b,c,d):
    if (a != None and b != None):   # antigrafei to b ston a
        for i in range(0,N):
            a[i]= b[i]
    # gemizei ton pinaka c me 0 an exei do8ei pinakas c && d
    if (c != None and d != None): 
        for i in range(0,N):
            for j in range(0,N):
                c[i][j] = 0
        for i in range(0,N):        # topo8etei basilissa
            c[d[i]][i] = 1


def firstQueens(board, state):  # topo8eteitai tyxaia mia basilissa (mia ana sthlh)
    random.seed() 
    for i in range(0,N):
        state[i] = random.randint(0, N-1)   # random 8esh 
        board[state[i]][i] = 1              # queen placed


def FindNeighbour(board, state):
    # orismos kai arxikopoihsh twn pinakwn opboard and opState (optimal)
    # bash tou pinaka kai antistoixou state pou exoun do8ei
    opboard = [[0 for i in range(N)] for j in range(N)]
    opState = [0 for i in range(N)]
    multitool(opState, state, opboard, opState)
    
    item = calculate(opboard, opState)  # initialise optimal item value

    # orismos kai arxikopoihsh twn pinakwn Neighbourboard and NeighbourState
    # bash tou pinaka kai antistoixou state pou exoun do8ei
    # xrhsimopoiountai ston ypologismo tou optimal neighbour
    Neighbourboard = [[0 for i in range(N)] for j in range(N)]
    NeighbourState = [0 for i in range(N)]
    multitool(NeighbourState, state, Neighbourboard, NeighbourState)

    for i in range(0,N):
        for j in range(0,N):
            if (j != state[i]):     #if not current state
                NeighbourState[i] = j
                Neighbourboard[NeighbourState[i]][i] = 1
                Neighbourboard[state[i]][i] = 0 
                
                temp = calculate(Neighbourboard, NeighbourState)

                # if better arangement found:
                # update item, opboard and opState
                if (temp <= item):
                    item = temp
                    multitool(opState, NeighbourState, opboard, opState)
                    
                # topo8etountai ek neou oi arxikes times sta 
                # Neighbourboard kai NeighbourState
                Neighbourboard[NeighbourState[i]][i] = 0
                NeighbourState[i] = state[i]       
                Neighbourboard[state[i]][i] = 1    

    multitool(state, opState, None, None)
    for i in range(0,N):
        for j in range(0,N):
            board[i][j] = 0
    multitool(None, None, board, state)


def calculate(board, state):
    attack = 0
    for i in range(0,N):
        # aristera
        x = state[i]
        y = i - 1
        while(y >= 0 and board[x][y] != 1):
            y -= 1
        if (y >= 0 and board[x][y] == 1):
            attack += 1
            
        # deksia
        x = state[i]
        y = i + 1
        while (y < N and x < N and board[x][y] != 1):
            y += 1
        if (y < N and x < N and board[x][y] == 1):
            attack += 1

        # diagwnia panw deksia
        x = state[i] - 1
        y = i + 1
        while (y < N and x >= 0 and board[x][y] != 1):
            y += 1
            x -= 1
        if (y < N and x >= 0 and board[x][y] == 1):
            attack += 1

        # diagvnia katv deksia
        x = state[i] + 1
        y = i + 1
        while (y < N and x < N and board[x][y] != 1):
            y += 1
            x += 1
        if (y < N and x < N and board[x][y] == 1):
            attack += 1

        # diagwnia panw aristera
        x = state[i] - 1
        y = i - 1
        while (y >= 0 and x >= 0 and board[x][y] != 1):
            y -= 1
            x -= 1
        if (y >= 0 and x >= 0 and board[x][y] == 1):
            attack += 1

        # diagwnia katw aristera
        x = state[i] + 1
        y = i - 1
        while (y >= 0 and x < N and board[x][y] != 1):
            y -= 1
            x += 1
        if (y >= 0 and x < N and board[x][y] == 1):
            attack += 1

    return (int)(attack / 2) #giati h ka8e epi8esh ypologizetai apo 2 basilisses

	
def HillClimbing(board, state):
    neighbourboard = [[0 for i in range(N)] for j in range(N)]
    neighbourState = [0 for i in range(N)]
    multitool(neighbourState, state, neighbourboard, neighbourState)
    while (True):
        multitool(state, neighbourState, board, state)
        FindNeighbour(neighbourboard, neighbourState)
        f = True    # comparing state-neighbourState
        for i in range(0,N):
            if (state[i] != neighbourState[i]):
                f = False
                break 
        if (f):
            printer(board)
            break
        if(calculate(board, state) == calculate(neighbourboard, neighbourState)):   
            neighbourState[random.randint(0,N-1)] = random.randint(0,N-1)
            multitool(None, None, neighbourboard, neighbourState)


def game(N):
    # arxikopoihsh board, state me 0 (kamia basilissa)
    board = [[0 for i in range(N)] for j in range(N)] 
    state = [0 for i in range(N)]

    start = time.time()
    print("\n", N, "x", N)
    firstQueens(board, state)   # arikopoihsh basilisswn
    HillClimbing(board, state)
    end = time.time()

    takentime = end-start
    print ("\nTotal time for", N, "x", N, "gueens problem is:", takentime)
    playagain()

def playagain():
    while (True):
        answer = input("\nDo you want to try for a different amount of queens? \nPress y for Yes οr n for No\n")
        if (answer.upper() !="Y" and answer.upper()!="N"):
            print("Invalid option.")
            continue
        break

    if (answer.upper()=="Y"):
        global N
        N = player()
        game(N)
        
    elif (answer.upper()=="N"):
        print ("The game will be terminated")
        exit()

N = player() #number of queens 
game(N)
