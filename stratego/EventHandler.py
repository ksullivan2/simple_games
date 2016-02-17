        '''activities associated with leaving the current state
        change the current status to the new status
        activities associated with entering the new state
        '''

        #-1 is new window
        #0 is game setup, no piece selected
        #1 is game setup, piece selected
        #2 is all pieces placed
        #3 is gameplay, no piece selected
        #4 is gaemplay, piece selected
        #5 is player conflict


- 1 start:
    newgame: to 0

0 game setup, no piece selected:
    gamepiece press: place in hand, to 1
    all pieces placed: to 2

1 game setup, piece selected
    gamepiece press: remove from hand, to 0
    square press: place pieceinhand on square, to 0

2 all pieces placed:
        #figure out if there's a popup here, wonky now
    gamepiece press: place in hand, to 1
    done button press: if activeplayer is red, to 0, else to 3, switch active player

3 gameplay: no piece selected
    gamepiece press: place in hand, to 4


4 gameplay: piece selected
    gamepiece press: remove from hand, to 3
    opponent piece press: to 5

5 player conflict
    #player conflict actions here
    if not won, to 3
    if won, to 6

6 win popup
    newgame, to 0
    close: close window



