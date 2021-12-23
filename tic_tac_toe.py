import turtle

#######################################
#   function for deciding the winner 
####################################### 
def winner(turn):
    turtle.speed(10)
    if(turn % 2 == 1):
        turtle.color("red")
        turtle.circle(75)
        print("Red wins! Blue sucks!")
        app()
    else:
        turtle.color("blue")
        turtle.circle(75)
        print("Blue wins! Red sucks!")
        app()
    app()


#############################################################
#   drawing TicTacToe grid, two horizontal and vertical lines
############################################################# 
def TTT_grid():
    turtle.width(3)
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-100,300)
    turtle.pendown()
    turtle.setpos(-100, -300)

    turtle.penup()
    turtle.setpos(100,300)
    turtle.pendown()
    turtle.setpos(100, -300)

    turtle.penup()
    turtle.setpos(-300,100)
    turtle.pendown()
    turtle.setpos(300, 100)

    turtle.penup()
    turtle.setpos(-300,-100)
    turtle.pendown()
    turtle.setpos(300, -100)

########################################################################################################################################################
#   placing dots on TTT board, passing in the user input, the turn, and the current matrix of the board, returning updated matrix so that TTT function gets updated matrix 
########################################################################################################################################################
def TTT_dots(user_input, turn, button):             
    if(turn % 2 == 0):                                               #checking to see whose turn it is
        turtle.speed(0)
        if(int(user_input) == 1):                                    #checking input by user 1
            if(button[0][0] == 1 or button[0][0] == 2):              #want to check if current position on board is already occupied, if it is occupied, ask for new input
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:                                                    #if spot is not occupied, update the location with 1
                button[0][0] = 1                                     #updating corresponding matrix element with 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(-200, 150)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()

        if(int(user_input) == 2):
            if(button[0][1] == 1 or button[0][1] == 2):               #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else: 
                button[0][1] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(0,150)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 3):
            if(button[0][2] == 1 or button[0][2] == 2):               #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[0][2] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(200,150)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 4):
            if(button[1][0] == 1 or button[1][0] == 2):                #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[1][0] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(-200, -50)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 5):
            if(button[1][1] == 1 or button[1][1] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[1][1] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(0,-50)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 6):
            if(button[1][2] == 1 or button[1][2] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[1][2] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(200,-50)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 7):
            if(button[2][0] == 1 or button[2][0] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[2][0] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(-200,-250)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 8):
            if(button[2][1] == 1 or button[2][1] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else: 
                button[2][1] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(0,-250)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 9):
            if(button[2][1] == 1 or button[2][1] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else: 
                button[2][2] = 1
                print(button)
                turtle.color("red")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(200,-250)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()

    elif(turn % 2 == 1):
        turtle.speed(0)
        if(int(user_input) == 1):
            if(button[0][0] == 1 or button[0][0] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[0][0] = 2                                        #updating matrix element with 2 when users2 turn 
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(-200, 150)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 2):
            if(button[0][1] == 1 or button[0][1] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else: 
                button[0][1] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(0,150)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 3):
            if(button[0][2] == 1 or button[0][2] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[0][2] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(200,150)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 4):
            if(button[1][0] == 1 or button[1][0] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[1][0] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(-200, -50)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 5):
            if(button[1][1] == 1 or button[1][1] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[1][1] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(0,-50)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 6):
            if(button[1][2] == 1 or button[1][2] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else: 
                button[1][2] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(200,-50)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 7):
            if(button[2][0] == 1 or button[2][0] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else: 
                button[2][0] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(-200,-250)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 8):
            if(button[2][1] == 1 or button[2][1] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[2][1] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(0,-250)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
        if(int(user_input) == 9):
            if(button[2][2] == 1 or button[2][2] == 2):                 #want to check if current position on board is already occupied, if it is occupied, take new input. 
                print("Try again\n")
                TTT_dots(input("User input:"), turn, button)
            else:
                button[2][2] = 2
                print(button)
                turtle.color("blue")
                turtle.begin_fill()
                turtle.penup()
                turtle.setpos(200,-250)
                turtle.pendown()
                turtle.circle(50)
                turtle.end_fill()
    return button 

#######################################################
#               TicTacToe function:
# Checking when there are three in a row for either user
####################################################### 
def TTT():
    TTT_grid()                                                            #creating board lines
    turn = 0                                                              #variable to switch turns
    button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]                            #button matrix to keep track of moves
    while(True):
        button = TTT_dots(input("User Input:"), turn, button)             #button matrix gets updated with new matrix after turn is complete
        turn = turn + 1                                                   #switching turns
        if((button[0][0] == 1 and button[0][1] == 1 and button[0][2] == 1) or (button[1][0] == 1 and button[1][1] == 1 and button[1][2] == 1) or (button[2][0] == 1 and button[2][1] == 1 and button[2][2] == 1)):
            winner(turn)
        elif((button[0][0] == 2 and button[0][1] == 2 and button[0][2] == 2) or (button[1][0] == 2 and button[1][1] == 2 and button[1][2] == 2) or (button[2][0] == 2 and button[2][1] == 2 and button[2][2] == 2)):
            winner(turn)
        elif((button[0][0] == 1 and button[1][0] == 1 and button[2][0] == 1) or (button[0][1] == 1 and button[1][1] == 1 and button[2][1] == 1) or (button[0][2] == 1 and button[1][2] == 1 and button[2][2] == 1)):
            winner(turn)
        elif((button[0][0] == 2 and button[1][0] == 2 and button[2][0] == 2) or (button[0][1] == 2 and button[1][1] == 2 and button[2][1] == 2) or (button[0][2] == 2 and button[1][2] == 2 and button[2][2] == 2)):
            winner(turn)
        elif((button[0][0] == 1 and button[1][1] == 1 and button[2][2] == 1) or (button[0][2] == 1 and button[1][1] == 1 and button[2][0] == 1)):
             winner(turn)
        elif((button[0][0] == 2 and button[1][1] == 2 and button[2][2] == 2) or (button[0][2] == 2 and button[1][1] == 2 and button[2][0] == 2)):
             winner(turn)
        elif(turn == 9):
            print("It's a tie! You both suck!")
            button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            app()



#######################################
#   Rock, paper, scissors function
#######################################       


def app():
    turtle.clear()
    turtle.color("turquoise")
    print("Enter numbers corresponding to squares 1, 2, 3 for top row, 3, 4, 5 for the middle row, 6, 7, 8 for bottom row")
    TTT();

app()

