import time
import keyboard
import random
import numpy
import array
import curses

"""
Made by SirBlobfis
-started April 12, 2021
-never ended
"""

Piece = 0
crappy_fps = 0
avg_crap = 0
a = 0
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c = 0
d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
e = 0
lines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lines_cleared = 0
moveDownDelay = 2
down_delay = 0
rand = random.randrange(0, 7)
Piece_location = [0, 5]
move_clear = True
rotation = 0
failure = "** ** ** ** ** !?!?WHAT HAVE YOU DONE?!?! ** ** ** ** **"
last_time = 0
#control buttons
cw = False
cw_ = False
ccw = False
ccw_ = False
left = False
left_ = False
right = False
right_ = False
down = False

Debbie_index = 0
Debbie = 0
#RIP Tim

current_shape = []
current_shape_center = []
piece_preview = []
piece_preview_ = []

Jeff = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

Jiff = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

Jaff = [
    ["3", "3", "3", "3"],
    ["3", "3", "3", "3"]
    ]

#0
Bill = [
    [1, 1, 1, 1]
    ]
Bill_center = [0, 0]

#1
Sandy = [
    [1, 0, 0],
    [1, 1, 1]
    ]
Sandy_center = [1, 1]

#2
Mike = [
    [0, 0, 1],
    [1, 1, 1]
    ]
Mike_center = [1, 1]

#3
My_Leg = [
    [1, 1],
    [1, 1]
    ]
My_Leg_center = [1, 1]

#4
Sussana = [
    [0, 1, 1],
    [1, 1, 0]
    ]
Sussana_center = [1, 1]

#5
Leroy = [
    [1, 1, 0],
    [0, 1, 1]
    ]
Leroy_center = [1, 1]

#6
Billy = [
    [0, 1, 0],
    [1, 1, 1]
    ]
Billy_center = [1, 1]


def choose():
    global piece, rand
    piece = rand
    rand = random.randrange(0, 7)

def averageTheCrap(stdscr):
    global a, b, c
    a += 1
    if(a == 59):
        a = 0
    b[a] = (time.time() - Debbie)
    c = 0.0
    for o in range(len(b)):
        c += b[o]
    c = c/60
    stdscr.addstr("avg frame time:" + str(round(c, 4)))
    stdscr.addstr("max frame time:" + str(round(1/60, 4)))

def getMaxCrap(stdscr):
    global b, e
    e = 0
    for i in range(len(b)):
        if(b[i] > e):
            e = b[i]
    stdscr.addstr("max time frame:" + str(round(e, 4)))

def piece_shape():
    global current_shape
    global current_shape_center
    #print(current_shape)
    if(piece == 0):
        current_shape = []
        current_shape_center = []
        current_shape.extend(Bill)
        current_shape_center.extend(Bill_center)
    elif(piece == 1):
        current_shape = []
        current_shape_center = []
        current_shape.extend(Sandy)
        current_shape_center.extend(Sandy_center)
    elif(piece == 2):
        current_shape = []
        current_shape_center = []
        current_shape.extend(Mike)
        current_shape_center.extend(Mike_center)
    elif(piece == 3):
        current_shape = []
        current_shape_center = []
        current_shape.extend(My_Leg)
        current_shape_center.extend(My_Leg_center)
    elif(piece == 4):
        current_shape = []
        current_shape_center = []
        current_shape.extend(Sussana)
        current_shape_center.extend(Sussana_center)
    elif(piece == 5):
        current_shape = []
        current_shape_center = []
        current_shape.extend(Leroy)
        current_shape_center.extend(Leroy_center)
    elif(piece == 6):
        current_shape = []
        current_shape_center = []
        current_shape.extend(Billy)
        current_shape_center.extend(Billy_center)
    else:
        print(failure)

def check_collisions(DLR, stdscr):
    global move_clear, Piece_location, current_shape_center
    checkers = []
    ah = 0
    ran = False
    #move down check
    if(DLR == 0):
        if((Piece_location[0] - current_shape_center[0] + len(current_shape)) != 20):
            for a in range(len(current_shape[0])):
                while True:
                    if(current_shape[len(current_shape) - 1 - ah][a] == 0):
                        ah += 1
                    else:
                        checkers.append(ah)
                        ah = 0
                        break
            for e in range(len(current_shape[0])):
                if((Jeff[Piece_location[0] - checkers[e] + len(current_shape) - current_shape_center[0]][Piece_location[1] + e - current_shape_center[1]] == 0) and ran == False):
                    move_clear = True
                else:
                    move_clear = False
                    ran = True
                    break
        else:
            move_clear = False

    #move left check
    elif(DLR == 1):
        if((Piece_location[1] - current_shape_center[1] - 1) >= 0):
            for a in range(len(current_shape)):
                while True:
                    if(current_shape[a][ah] == 0):
                        ah += 1
                    else:
                        checkers.append(ah)
                        ah = 0
                        break
            for e in range(len(current_shape)):
                #stdscr.addstr(checkers)
                #stdscr.addstr(Piece_location[0] + e - current_shape_center[0])
                #stdscr.addstr(Piece_location[1] + checkers[e] - current_shape_center[1])
                if((Jeff[Piece_location[0] + e - current_shape_center[0]][Piece_location[1] + checkers[e] - current_shape_center[1] - 1] == 0) and ran == False):
                    move_clear = True
                else:
                    move_clear = False
                    ran = True
                    break
        else:
            move_clear = False

    #move right check
    elif(DLR == 2):
        if((Piece_location[1] - current_shape_center[1] + len(current_shape[0]) + 1) <= 10):
            for a in range(len(current_shape)):
                while True:
                    if(current_shape[a][len(current_shape[0]) - 1 - ah] == 0):
                        ah += 1
                    else:
                        checkers.append(ah)
                        ah = 0
                        break
            #stdscr.addstr(checkers)
            for e in range(len(current_shape)):
                #print(Piece_location[0] + e - current_shape_center[0])
                #print(Piece_location[1] - checkers[e] - current_shape_center[1] + len(current_shape[0]))
                if((Jeff[Piece_location[0] + e - current_shape_center[0]][Piece_location[1] - checkers[e] - current_shape_center[1] + len(current_shape[0])] == 0) and ran == False):
                    move_clear = True
                else:
                    move_clear = False
                    ran = True
                    break
        else:
            move_clear = False

    else:
        print(failure)

def check_lose():
    if(Jeff[0] != d):
        stdscr.addstr("YOU LOSE")
        quit()

def place_piece():
    global Piece_location
    global rotation
    global piece
    #Jeff[Piece_location[0]][Piece_location[1]] = 1
    #print("here" + str(len(current_shape)))
    #print("here" + str(len(current_shape[0])))
    for u in range(len(current_shape)):
        for y in range(len(current_shape[0])):
            if(current_shape[u][y] == 1):
                if((0 - current_shape_center[0] + Piece_location[0] + u) >= 0):
                    Jeff[(0 - current_shape_center[0] + Piece_location[0] + u)][(0 - current_shape_center[1] + Piece_location[1] + y)] = 1
    
def check_line():
    global lines
    r = 0
    for y in range(20):
        r = numpy.sum(Jeff[y])
        if(r == 10):
            lines[y] = 1

def line_clear():
    global lines, lines_cleared, Jeff
    line_clear = 0
    for u in range(20):
        if (lines[u] == 1):
            lines_cleared += 1
            lines[u] = 0
            #place_piece()
            #new_piece()
            Jeff.pop(u)
            Jeff.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def new_piece():
    global Piece_location
    Piece_location = [0, 5]
    choose()
    piece_shape()

def move_down(stdscr):
    global Piece_location, down_delay, move_clear, down
    down_delay += 1
    if(down_delay >= moveDownDelay):
        unplace_piece()
        down_delay = 0
        check_collisions(0, stdscr)
        if(move_clear == True):
            Piece_location[0] += 1
        else:
            place_piece()
            check_lose()
            check_line()
            line_clear()
            new_piece()
        place_piece()

def move_left(stdscr):
    if(left == True):
        check_collisions(1, stdscr)
        if(move_clear == True):
            unplace_piece()
            Piece_location[1] -= 1
            place_piece()

def move_right(stdscr):
    if(right == True):
        check_collisions(2, stdscr)
        if(move_clear == True):
            unplace_piece()
            Piece_location[1] += 1
            place_piece()

def check_buttons():
    global cw, cw_, ccw, ccw_, left, left_, right, right_, down, down_
    #cw
    try:
        if(keyboard.is_pressed('a') and (cw_ == False)):
            cw = True
            cw_ = True
        else:
            cw = False
        if(False == keyboard.is_pressed('a')):
            cw_ = False
    except:
        pass

    #ccw
    try:
        if(keyboard.is_pressed('s') and (ccw_ == False)):
            ccw = True
            ccw_ = True
        else:
            ccw = False
        if(False == keyboard.is_pressed('s')):
            ccw_ = False
    except:
        pass

    #left
    try:
        if(keyboard.is_pressed('right_arrow') and (left_ == False)):
            left = True
            left_ = True
        else:
            left = False
        if(False == keyboard.is_pressed('right_arrow')):
            left_ = False
    except:
        pass

    #right
    try:
        if(keyboard.is_pressed('left_arrow') and (right_ == False)):
            right = True
            right_ = True
        else:
            right = False
        if(False == keyboard.is_pressed('left_arrow')):
            right_ = False
    except:
        pass
    
    #down
    try:
        if(keyboard.is_pressed('up_arrow')):
            down = True
        else:
            down = False
    except:
        pass

def rotate():
    global current_shape, cw, ccw
    if(piece == 3):
        pass
    else:
        #rotate
        if(cw == True):
            unplace_piece()
            #this beautiful line was ripped from interwebs
            current_shape = list(zip(*current_shape[::-1]))
            current_shape = numpy.array(current_shape)
            place_piece()
        if(ccw == True):
            unplace_piece()
            for y in range(3):
                #this beautiful line was ripped from interwebs
                current_shape = list(zip(*current_shape[::-1]))
                current_shape = numpy.array(current_shape)
            place_piece()

def rotate_bandaid():
    try:
        if ((piece == 1) and (current_shape[0][0] != 1) and (current_shape[0][1] != 0) and (current_shape[0][2] != 0) and (current_shape[1][0] != 1) and (current_shape[1][1] != 1) and (current_shape[2][1] != 1)):
            current_shape_center = [0, 1]
            #[[1, 0, 0], [1, 1, 1]]
        else:
            current_shape_center = [1, 1]
        if ((piece == 2) and (current_shape[0][0] != 0) and (current_shape[0][1] != 0) and (current_shape[0][2] != 1) and (current_shape[1][0] != 1) and (current_shape[1][1] != 1) and (current_shape[2][1] != 1)):
            current_shape_center = [0, 0]
            #[[0, 0, 1], [1, 1, 1]]
        else:
            current_shape_center = [1, 1]
    except:
        pass

def unplace_piece():
    global Jeff, Piece_location
    for u in range(len(current_shape)):
        for y in range(len(current_shape[0])):
            if(current_shape[u][y] == 1):
                if((0 - current_shape_center[0] + Piece_location[0] + u) >= 0):
                    Jeff[(0 - current_shape_center[0] + Piece_location[0] + u)][(0 - current_shape_center[1] + Piece_location[1] + y)] = 0

def down_speed():
    global moveDownDelay
    if(down == True):
        moveDownDelay = 4
    else:
        moveDownDelay = 10

def preview_piece(stdscr):
    global rand, piece_preview, Jaff, piece_preview_
    piece_preview_ = [
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"]
        ]
    Jaff = [
        ["3", "3", "3", "3"],
        ["3", "3", "3", "3"]
        ]
    if(rand == 0):
        piece_preview = []
        piece_preview.extend(Bill)
    elif(rand == 1):
        piece_preview = []
        piece_preview.extend(Sandy)
    elif(rand == 2):
        piece_preview = []
        piece_preview.extend(Mike)
    elif(rand == 3):
        piece_preview = []
        piece_preview.extend(My_Leg)
    elif(rand == 4):
        piece_preview = []
        piece_preview.extend(Sussana)
    elif(rand == 5):
        piece_preview = []
        piece_preview.extend(Leroy)
    elif(rand == 6):
        piece_preview = []
        piece_preview.extend(Billy)
    else:
        print(failure)
    for o in range(len(piece_preview)):
        piece_preview_.append([])
        for e in range(len(piece_preview[0])):
            piece_preview_[0].append([])
            piece_preview_[o][e] = str(piece_preview[o][e])
            #print(piece_preview_)
            if(piece_preview_[o][e] == "1"):
                Jaff[o][e] = "2"
    for o in range(len(piece_preview)):
        stdscr.addstr(Jaff[o][0] + Jaff[o][1] + Jaff[o][2] + Jaff[o][3])
    #print(Jaff)




def main(stdscr):
    global Piece, crappy_fps, avg_crap, a, b, c, d, e, lines, lines_cleared, moveDownDelay, down_delay, down_delay, rand, Piece_location, move_clear, rotation, last_time, Debbie_index, Debbie, current_shape, current_shape_center, piece_preview, piece_preview_
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)
    
    choose()
    new_piece()
    place_piece()
    Debbie = time.time()

    while True:
        Debbie_index += 1/60
        #print(str(Piece) + str(int(100000 * (time.time() - Debbie))))
        #print(piece)
        #print(Piece_location)
        #print(move_clear)
        
        check_buttons()
        move_left(stdscr)
        move_right(stdscr)
        rotate()
        move_down(stdscr)
        rotate_bandaid()
        down_speed()
        preview_piece(stdscr)

        for e in range(20):
            for u in range(10):
                Jiff[e][u] = str(Jeff[e][u])
                if(Jeff[e][u] == 0):
                    Jiff[e][u] = str(Jiff[e][u].replace("0", "3"))
                elif(Jeff[e][u] == 1):
                    Jiff[e][u] = str(Jiff[e][u].replace("1", "2"))
                else:
                    print(failure)
                stdscr.addstr(str(Jiff[e][u]), curses.color_pair(int(Jiff[e][u])))
                stdscr.addstr(str(Jiff[e][u]), curses.color_pair(int(Jiff[e][u])))
                index = curses.getsyx()
                curses.setsyx((index[1] + 1), 0)
            stdscr.addstr("                    ")

        try:
            if keyboard.is_pressed('esc'):
                break
        except:
            break

        #averageTheCrap(stdscr)
        #getMaxCrap(stdscr)
        #print(1/60 - (time.time() - Debbie - Debbie_index))
        #print(Debbie_index)
        
        #print(1/60)
        #print(time.time() - Debbie - Debbie_index)
        #print(time.time() % 1/60)

        last_time = time.time()
        if((1/60 - (time.time() - Debbie - Debbie_index)) > 0):
            time.sleep(1/60 - (time.time() - Debbie - Debbie_index))
        #if((time.sleep(1/60 - (time.time() % 1/60))) > .01):
        #    time.sleep(.005)
        stdscr.refresh()
        #curses.setsyx(1, 1)
        stdscr.clear()

curses.wrapper(main)