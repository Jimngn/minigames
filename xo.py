#tic tac toe - random 2 turns
#create frame 320x320
#explore canvas.draw_line()
#explore canvas.draw_circle()
#change color of circle in new turn
#write a function to check if there are 3 circle-same-color in straight line. Return 0 if not, 1 if yes


#Make computer play tic tac toe with you
# Part 1: random play:In the computer's turn, it can go at a random position

# Part 2: make computer smarter
# 1.Write a function to check if there is 2 same-color-circle in the same row/column/diagonal
# 2.Play at the remained position

import simplegui
color_line = 'white'
x =[10,110,210,310]
y =[10,110,210,310]
#coordinate of center
xc = [(x[0]+x[1])/2,(x[1]+x[2])/2,(x[2]+x[3])/2]
yc = [(y[0]+y[1])/2,(y[1]+y[2])/2,(y[2]+y[3])/2]
color_circle = [['black','black','black'],['black','black','black'],['black','black','black']]
color_value = [[0,0,0],[0,0,0],[0,0,0]]

radius = 20

frame = simplegui.create_frame("ABC",320,320)

def check_straight_line(cc):
    win = 0
    #3 rows
    if cc[0][0] == cc[0][1] and cc[0][1] == cc[0][2] and cc[0][0] != 'black':
        win = 1
    elif cc[1][0] == cc[1][1] and cc[1][1] == cc[1][2] and cc[1][0] != 'black':
        win = 1
    elif cc[2][0] == cc[2][1] and cc[2][1] == cc[2][2] and cc[2][0] != 'black':
        win = 1
#3 columns
    elif cc[0][0] == cc[1][0] and cc[1][0] == cc[2][0] and cc[0][0] != 'black':
        win = 1
    elif cc[0][1] == cc[1][1] and cc[1][1] == cc[2][1] and cc[0][1] != 'black':
        win = 1
    elif cc[0][2] == cc[1][2] and cc[2][2] == cc[2][2] and cc[0][2] != 'black':
        win = 1
    # 2 diagonals:
    elif cc[0][0] == cc[1][1] and cc[1][1] == cc[2][2] and cc[0][0] != 'black':
        win = 1
    elif cc[0][2] == cc[1][1] and cc[1][1] == cc[2][0] and cc[0][2] != 'black':
        win = 1
    return win


check = 9
def check_2_in_line(cc):
    global check
    check = 9
    #check row
    for j in range(3):
        if cc[0][j] + cc[1][j] + cc[2][j] == 2:
            check = j
        elif cc[0][j] + cc[1][j] + cc[2][j] == 200:
            check = j
    #check column
    for i in range(3):
        if cc[i][0] + cc[i][1] + cc[i][2] == 2:
            check = 10 + i
        elif cc[i][0] + cc[i][1] + cc[i][2] == 200:
            check = 10 + i

    #check diagonal 
    if cc[0][0]+cc[1][1]+cc[2][2] == 2:
        check = 4
    elif cc[0][0]+cc[1][1]+cc[2][2] == 200:
        check = 4
    #check diagonal
    if cc[2][0]+cc[1][1]+cc[0][2] == 2:
        check = 5
    elif cc[2][0]+cc[1][1]+cc[0][2] == 200:
        check = 5
    return check   
    


def draw_handler(canvas):
    #horizontal
    canvas.draw_line((x[0], y[0]), (x[3], y[0]), 1, color_line)
    canvas.draw_line((x[0], y[1]), (x[3], y[1]), 1, color_line)
    canvas.draw_line((x[0], y[2]), (x[3], y[2]), 1, color_line)
    canvas.draw_line((x[0], y[3]), (x[3], y[3]), 1, color_line)
    #vertical
    canvas.draw_line((x[0], y[0]), (x[0], y[3]), 1, color_line)
    canvas.draw_line((x[1], y[0]), (x[1], y[3]), 1, color_line)
    canvas.draw_line((x[2], y[0]), (x[2], y[3]), 1, color_line)
    canvas.draw_line((x[3], y[0]), (x[3], y[3]), 1, color_line)

    #canvas.draw_circle((xc[0],yc[0]),1,10,color_circle)

    for i in range(3):
        for j in range(3):
            canvas.draw_circle((xc[i],yc[j]),1,radius,color_circle[i][j])

count = 0
import random

def click(pos): #pos[0] = x of mouse, pos[1] = y of mouse
    global x,y,color_circle,count, color_value
    
    if (count%2 == 0):
        if check_2_in_line(color_value) == 9:
            i = random.randint(0,2)
            j = random.randint(0,2)
            while (color_circle[i][j] != 'black'):
                i = random.randint(0,2)
                j = random.randint(0,2)
            color_circle[i][j] = 'green'
            frame.set_draw_handler(draw_handler)
        elif check_2_in_line(color_value) < 3:
            j = check_2_in_line(color_value)
            for i in range(3):
                if color_circle[i][j] == 'black':
                    color_circle[i][j] = 'green'
                    frame.set_draw_handler(draw_handler)
        elif check_2_in_line(color_value) == 4:
            for i in range(3):
                if color_circle[i][i] == 'black':
                    color_circle[i][i] = 'green'
                    frame.set_draw_handler(draw_handler)
        elif check_2_in_line(color_value) == 5:
            for i in range(3):
                if color_circle[i][2-i] == 'black':
                    color_circle[i][2-i] = 'green'
                    frame.set_draw_handler(draw_handler)
        elif check_2_in_line(color_value) >9:
            i = check_2_in_line(color_value) - 10
            for j in range(3):   
                if color_circle[i][j] == 'black':
                    color_circle[i][j] = 'green'
                    frame.set_draw_handler(draw_handler)
        count += 1
        #decide who win
        #if check_straight_line(color_circle) == 1:
            #print color_circle[i][j], 'win'
    else:
        for i in range(3):
            for j in range(3):
                if x[i] < pos[0] and pos[0] < x[i+1] and y[j] < pos[1] and pos[1] < y[j+1]:
                    if color_circle[i][j] == 'black': 
                        color_circle[i][j] = 'red'
                        frame.set_draw_handler(draw_handler)
                        count += 1
                    #decide who win
                    if check_straight_line(color_circle) == 1:
                        print color_circle[i][j], 'win'
  
    for i in range(3):
        for j in range(3):
            if color_circle[i][j] == 'black':
                color_value[i][j] = 0
            elif color_circle[i][j] == 'green':
                color_value[i][j] = 1
            elif color_circle[i][j] == 'red':
                color_value[i][j] = 100
    print check_2_in_line(color_value)

        
    #for i in range(3):
        #for j in range(3):
            #if x[i] < pos[0] and pos[0] < x[i+1] and y[j] < pos[1] and pos[1] < y[j+1]:
                #if count%2 == 0 and color_circle[i][j] == 'black': 
                    #color_circle[i][j] = 'green'
                    #frame.set_draw_handler(draw_handler) 
                #if count%2 == 1 and color_circle[i][j] == 'black': 
                    #color_circle[i][j] = 'red'
                    #frame.set_draw_handler(draw_handler)

            #decide who win
                #if check_straight_line(color_circle) == 1:
                    #print color_circle[i][j], 'win'



frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw_handler)
frame.start()
