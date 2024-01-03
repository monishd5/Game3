from tkinter import*
from PIL import Image, ImageTk
from random import randint
import turtle
win=Tk()
win.configure(bg="#C0C0C0")



def shape():
    # Setting up the GUI
    root = Tk()
    root.title("Shapes Drawer")

    canvas = Canvas(root, width=800, height=600)
    canvas.pack()

    # Initialize Turtle screen
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")
    
    # Initialize Turtle
    drawer = turtle.RawTurtle(screen)
    drawer.speed(0)
    drawer.hideturtle()
    
    # Function to draw shapes
    def draw_shape(shape):
        color = color_entry.get().lower()
    
        drawer.clear()
        drawer.penup()
        drawer.goto(-50, -50)
        drawer.pendown()
        drawer.color(color)
        drawer.begin_fill()
    
        if shape == "Square":
            for _ in range(4):
                drawer.forward(100)
                drawer.right(90)
        elif shape == "Rectangle":
            for _ in range(2):
                drawer.forward(150)
                drawer.right(90)
                drawer.forward(80)
                drawer.right(90)
        elif shape == "Triangle":
            for _ in range(3):
                drawer.forward(120)
                drawer.left(120)
        elif shape == "Circle":
            drawer.circle(50)
        elif shape == "Pentagon":
            for _ in range(5):
                drawer.forward(100)
                drawer.right(72)
        drawer.end_fill()
    
    # Function to handle button click
    def on_button_click(shape):
        draw_shape(shape)
    
    # Creating buttons for shape selection
    shapes = ["Square", "Rectangle", "Triangle", "Circle", "Pentagon"]
    
    for shape in shapes:
        btn = Button(root, text=shape, command=lambda s=shape: on_button_click(s))
        btn.pack(side=LEFT, padx=5, pady=5)
    
    # Creating entry for color code
    color_label = Label(root, text="Enter color name or color code")
    color_label.pack()
    color_entry = Entry(root)
    color_entry.pack()
    
    root.mainloop()
        
def sps():
    # main window
    root = Toplevel(win)
    root.title("Rock Scissor Paper")
    root.configure(background="black")

    # picture
    rock_img = ImageTk.PhotoImage(Image.open("rock_comp.png"))
    paper_img = ImageTk.PhotoImage(Image.open("paper_comp.png"))
    scissor_img = ImageTk.PhotoImage(Image.open("scissors_comp.png"))
    rock_img_comp = ImageTk.PhotoImage(Image.open("rock_user.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("paper_user.png"))
    scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors_user.png"))

    # insert picture
    user_label = Label(root, image=scissor_img, bg="black")
    comp_label = Label(root, image=scissor_img_comp, bg="black")
    comp_label.grid(row=1, column=0)
    user_label.grid(row=1, column=4)


    # scores
    playerScore = Label(root, text=0, font=100, bg="black", fg="white")
    computerScore = Label(root, text=0, font=100, bg="black", fg="white")
    computerScore.grid(row=1, column=1)
    playerScore.grid(row=1, column=3)

    # indicators
    user_indicator = Label(root, font=50, text="USER", bg="black", fg="white")
    comp_indicator = Label(root, font=50, text="COMPUTER",bg="black", fg="white")
    user_indicator.grid(row=0, column=3)
    comp_indicator.grid(row=0, column=1)
    # messages
    msg = Label(root, font=50, bg="black", fg="white")
    msg.grid(row=3, column=2)

    # update message


    def updateMessage(x):
        msg['text'] = x

    # update user score


    def updateUserScore():
        score = int(playerScore["text"])
        score += 1
        playerScore["text"] = str(score)

    # update computer score


    def updateCompScore():
        score = int(computerScore["text"])
        score += 1
        computerScore["text"] = str(score)

    # check winner


    def checkWin(player, computer):
        if player == computer:
            updateMessage("Its a tie!!!")
        elif player == "rock":
            if computer == "paper":
                updateMessage("You lose")
                updateCompScore()
            else:
                updateMessage("You Win")
                updateUserScore()
        elif player == "paper":
            if computer == "scissor":
                updateMessage("You lose")
                updateCompScore()
            else:
                updateMessage("You Win")
                updateUserScore()
        elif player == "scissor":
            if computer == "rock":
                updateMessage("You lose")
                updateCompScore()
            else:
                updateMessage("You Win")
                updateUserScore()

        else:
            pass


    # update choices

    choices = ["rock", "paper", "scissor"]


    def updateChoice(x):

        # for computer
        compChoice = choices[randint(0, 2)]
        if compChoice == "rock":
            comp_label.configure(image=rock_img_comp)
        elif compChoice == "paper":
            comp_label.configure(image=paper_img_comp)
        else:
            comp_label.configure(image=scissor_img_comp)


    # for user
        if x == "rock":
            user_label.configure(image=rock_img)
        elif x == "paper":
            user_label.configure(image=paper_img)
        else:
            user_label.configure(image=scissor_img)

        checkWin(x, compChoice)


    # buttons
    rock = Button(root, width=20, height=2, text="ROCK",
                  bg="white", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1)
    paper = Button(root, width=20, height=2, text="PAPER",
                   bg="white", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2)
    scissor = Button(root, width=20, height=2, text="SCISSOR",
                     bg="white", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

    root.mainloop()


def game():
    import turtle
    import random
    import math
    bot=turtle.Turtle()
    '''
    score_label=turtle.Turtle()
    score_label.penup()
    score_label.goto(0,250)
    score_label.hideturtle()
    '''
    x=300
    y=300
    bot.penup()
    bot.goto(-x,-y)
    bot.pendown()
    bot.pensize(5)                                              

    #BUILD THE PLAYGROUND
    bot.speed(100)
    bot.fillcolor('aqua')
    bot.begin_fill()
    bot.forward(2*x)
    bot.left(90)
    bot.forward(2*y)
    bot.left(90)
    bot.forward(2*x)
    bot.left(90)
    bot.forward(2*y)
    bot.left(90)
    bot.end_fill()
    bot.penup()
    bot.goto(0,+y)
    bot.pendown()
    bot.write("HUNGRY TURTLE", align='center',font=('Courier New',50,'bold'))


    #CREATE A PLAYER
    player = turtle.Turtle('turtle')
    player.shapesize(1)
    player.pencolor('black')
    player.penup()
    speed=1.5
    score=0

    #CREATE FOOD
    n=3
    listOfFood=[]
    for i in range(n):
        food=turtle.Turtle('circle')
        food.color("dark green")
        randomX=random.randint(-x,+x)
        randomY=random.randint(-y,+y)
        food.penup()
        food.speed(100)
        food.goto(randomX,randomY)
        listOfFood.append(food)

    def left():
         player.left(20)

    def right():
        player.right(20)

    def increaseSpeed():
        global speed
        speed=1
        speed=speed+1

    def decreaseSpeed():
        global speed
        speed=1
        speed=speed-1

    def didCollide(t1,t2):
        x1=t1.xcor()
        x2=t2.xcor()
        y1=t1.ycor()
        y2=t2.ycor()

        distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))

        if(distance<20):
            return True
        else:
            return False
    

    turtle.listen()

    turtle.onkey(left,'Left')
    turtle.onkey(right,'Right')
    turtle.onkey(increaseSpeed,'Up')
    turtle.onkey(decreaseSpeed,'Down')

    while(True):
        player.forward(speed)

        

    #BOUNDARY LIMITS
        if(player.xcor()>x-10 or player.xcor()< -x+10 or player.ycor()>y-10 or player.ycor()<-y+10):
            score=score-10
            scoreMsg="Score:"+str(score)
            print(scoreMsg)
            bot.clear()
            bot.write(scoreMsg, font=("Calibri", 15))
            

    #CHECK IF PLAYER AND FOOD COLLIDES
        for i in range(n):
            
            if(didCollide(player,listOfFood[i])==True):
                randomX=random.randint(-x,+x)
                randomY=random.randint(-y,+y)
                listOfFood[i].goto(randomX,randomY)
                score=score+10
                scoreMsg="Score:"+str(score)
                print(scoreMsg)
                bot.clear()
                bot.write(scoreMsg,font=('Calibri',15))
    #IF PLAYER HITS THE BORDER
            if(player.xcor()>x-10 or player.xcor()< -x+10 or player.ycor()>y-10 or player.ycor()<-y+10):
                turtle.write("GAME OVER", align='center',font=('Calibri',30))
                turtle.mainloop()
           
    turtle.done()
    




l1=Label(win,text="CHOOSE YOUR DESIRED GAME",font=('Calibri',70),fg="black",bg="#C0C0C0")
b1=Button(win,font='Impact',text="DRAW SHAPES",command=shape,fg="white",bg="#B0190F",width=20,height=20)
b2=Button(win,font='Impact',text="STONE PAPER SCISSORS",command=sps,fg="white",bg="#E79A5D",width=20,height=20)
b3=Button(win,font='Impact',text="HUNGRY TURTLE GAME",command=game,fg="white",bg="#2D0101",width=20,height=20)

l1.pack()
b1.place(x=450,y=105)
b2.place(x=650,y=105)
b3.place(x=850,y=105)









