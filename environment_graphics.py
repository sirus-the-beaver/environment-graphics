from graphics import *
from time import *
import random

# Function to make the cloud and append to list

def cloud(win):

    global cloud_list
    cloud_list = []

    # Make a cloud of 10 circles with randomized centers
    
    for i in range(10):

        rand_x = random.uniform(5, 10)
        rand_y = random.uniform(20, 22)
        cloud_center = Point(rand_x, rand_y)
        cloud_object = Circle(cloud_center, 2)
        cloud_object.setFill('white')
        cloud_object.setOutline('white')
        cloud_object.draw(win)
        cloud_list.append(cloud_object)
        
    return

# Function to draw the trees

def drawTree(x, y, gcolor, unit, win):

    trunk = Rectangle(Point(x - unit/2, y), Point(x + unit/2, y + unit * .825))
    trunk.setFill('brown')
    trunk.setOutline('brown')
    trunk.draw(win)

    triangle1 = Polygon(Point(x - unit*2, y + unit*.825), Point(x, y + unit * 3.125), Point(x + unit*2, y + unit*.825))
    triangle1.setFill(gcolor)
    triangle1.setOutline(gcolor)
    triangle1.draw(win)

    triangle2 = Polygon(Point(x - unit*1.5, y + unit*2), Point(x, y + unit*4), Point(x + unit*1.5, y + unit*2))
    triangle2.setFill(gcolor)
    triangle2.setOutline(gcolor)
    triangle2.draw(win)

    triangle3 = Polygon(Point(x - unit*1.25, y + unit*3.125), Point(x, y + unit*4.575), Point(x + unit*1.25, y + unit*3.125))
    triangle3.setFill(gcolor)
    triangle3.setOutline(gcolor)
    triangle3.draw(win)

# Function to call the drawTree function and create a forest

def drawForest(win, numTreeInRow):

    x1, x2, y1, y2 = 4, 36, 3, 13

    color_list = ['forestgreen', 'darkolivegreen', 'olivedrab', 'yellowgreen', 'limegreen', 'seagreen', 'darkseagreen', 'mediumseagreen', 'lightseagreen', 'springgreen', 'greenyellow', 'lime']

    for i in range(numTreeInRow):

        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)
        color = random.randrange(len(color_list) - 1)
        gcolor = color_list[color]
        unit = random.uniform(.4, .8)
        drawTree(x, y, gcolor, unit, win)
        
    return

# Function to create the buttons

def createButtons(win):
    
    button_lst = []
    label = ['Day', 'Night', 'Windy', 'Breeze', 'Exit']
    x = 2
    
    for i in range(len(label)):

        button_lower = Point(x, 2)
        button_upper = Point(x + 4, 4)
        button = Rectangle(button_lower, button_upper)
        button.setFill('gray')
        button.draw(win)

        message = Text(Point(x + 2, 3), label[i])
        message.setFill('white')
        message.setStyle('bold')
        message.draw(win)

        x += 5

# Function to make the cloud move

def cloud_move(win, speed):

    # For each circle in the cloud, move it some x distance
    
    for c in cloud_list:

        c.move(speed, 0)
        c_center = c.getCenter()
        x = c_center.getX()

        # Condition: once the cloud reaches the far right of the winow, reappear on far left of window
        if x>= 40:

            c.move(-40, 0)

    return                

# Function to generate the window and call in previous functions

def scene():

    # Generate the window
    
    win = GraphWin('Mountain Scene', 800, 600)
    win.setCoords(0, 0, 40, 30)

    # Generate the sky
    
    p1_sky = Point(0, 30)
    p2_sky = Point(40, 15)
    
    sky = Rectangle(p1_sky, p2_sky)
    sky.setFill('light blue')
    
    sky.draw(win)

    #Generate the ground
    
    p1_ground = Point(0, 15)
    p2_ground = Point(40, 0)

    ground = Rectangle(p1_ground, p2_ground)
    ground.setFill('light green')

    ground.draw(win)

    #Generate the sun
    
    center_sun = Point(20, 25)
    
    sun = Circle(center_sun, 2)
    sun.setFill('yellow')

    sun.draw(win)

    #Generate the moon
    
    center_moon1 = Point(20, 25)

    moon1 = Circle(center_moon1, 2)
    moon1.setFill('white')
    moon1.setOutline('white')

    moon1.draw(win)
    
    center_moon2 = Point(20.75, 26)

    moon2 = Circle(center_moon2, 2)
    moon2.setFill('navy')
    moon2.setOutline('navy')

    moon2.draw(win)

    #Generate the mountains

    p1_mount = Point(0, 15)
    p2_mount = Point(15, 25)
    p3_mount = Point(35,15)

    mountain1 = Polygon(p1_mount, p2_mount, p3_mount)
    mountain1.setFill('dark green')

    mountain1.draw(win)

    p4_mount = Point(10, 15)
    p5_mount = Point(23, 23)
    p6_mount = Point(40, 15)

    mountain2 = Polygon(p4_mount, p5_mount, p6_mount)
    mountain2.setFill('dark green')

    mountain2.draw(win)

    # Generate the message

    p_text = Point(20, 29)

    text = Text(p_text, 'Sunny Day')

    text.setFill('red')
    text.setStyle('bold')
    
    text.draw(win)

    # Generate the clouds

    cloud(win)    

    # Generate the trees

    drawForest(win, 20)

    # Generate the buttons

    createButtons(win)

    # Make the forever loop
    # Initial condition: sunny day so remove moon at first
    # Initialize state/status

    moon1.undraw()
    moon2.undraw()
    state = 0
    speed = .1
    wind = speed * 4
    status = 'normal'
    
    while True:

        if status == 'windy':
            
            cloud_move(win, wind)

            if state == 1:

                text.setText('Sunny Windy Day')

            elif state == 2:

                text.setText('Moon Windy Night')

        elif status == 'normal':

            cloud_move(win, speed)

        
        click = win.checkMouse()

        # If the user clicks, check the x and y coordinates of the click
        
        if click != None:
                
            x_coor = click.getX()
            y_coor = click.getY()

            # If the click is within range of the Sunny button
        
            if x_coor >= 2 and x_coor <= 6 and y_coor >= 2 and y_coor <= 4:

                state = 1
                moon1.undraw()
                moon2.undraw()
                sun.draw(win)
                sky.setFill('light blue')
                text.setText('Sunny Day')
                cloud_move(win, speed)

                for d in cloud_list:

                    d.setFill('white')
                    d.setOutline('white')

            # If the click is within the Night button
            
            if x_coor >= 7 and x_coor <= 11 and y_coor >= 2 and y_coor <= 4:

                state = 2
                sun.undraw()
                moon1.draw(win)
                moon2.draw(win)
                sky.setFill('navy')
                text.setText('Moon Night')
                

                for e in cloud_list:
                    
                    e.setFill('gray')
                    e.setOutline('gray')

            # If the click is within the Windy button
            
            if x_coor >= 12 and x_coor <= 16 and y_coor >= 2 and y_coor <= 4:

                cloud_move(win, wind)

                # Condition: if window was just opened or day button was last button clicked

                if state == 1 or state == 0:

                    text.setText('Sunny Windy Day')
                    status = 'windy'

                #Condition: if night button was last button clicked

                elif state == 2:

                    sun.undraw()    
                    text.setText('Moon Windy Night')
                    status = 'windy'

            # If the click is within the Breeze button
    
            if x_coor >= 17 and x_coor <= 21 and y_coor >= 2 and y_coor <= 4:
            
                cloud_move(win, speed)
                status = 'normal'

                #Condition: if window was just opened or day button was last button clicked

                if state == 1 or state == 0:
            
                    text.setText('Sunny Day')

                #Condition: if night button was last button clicked
            
                elif state == 2:

                    text.setText('Moon Night')
                    sun.undraw()


            # If the click is within the exit button
            
            if x_coor >= 22 and x_coor <= 26 and y_coor >= 2 and y_coor <= 4:

                win.close()
                
                break
            
scene()
