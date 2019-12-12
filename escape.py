import turtle as turtle #imports

print("The application does a basic function of doing a simple escape for the robot/turtle. The turtle goes until he escapes and the application quits when that pramater is meet")
# draws the bag to screen
def draw_bag():
    turtle.shape("turtle") # draws shape of turtle
    turtle.pen(pencolor='brown',pensize=5) # the calor the pen when it draws the grid
    turtle.penup() # pen to draw is up -> not able to draw
    turtle.goto(-35,35) # Goto position for x an y fro start position
    turtle.pendown()# pen to draw is down -> able to draw
    turtle.right(90) # turtle right and angle 90
    turtle.forward(70) # forward direction and angle 70
    turtle.left(90) # left direction and angle 90
    turtle.forward(70) # direction forward and angle 70
    turtle.left(90) # left direction and angle 90
    turtle.forward(70) # forward direction and angle

# reposition of the robot/turtle at 0,0
    turtle.up() # gets the turtle in the middle facing the top of bag that is opened
    turtle.goto(0,0) # goes to that position of 0,0
    turtle.forward(70)  # forward at a 70 degrees facing the top of the bag


def draw_line():
    angle = 90 # gets the angle to draw the line
    step = 90 # the steps to do so
    t = turtle.Turtle()
    while not escaped(t.position()):# checks to see if the opject has escaped
        t.left(angle) # checkes the angle to see if the turtle has escaped
        t.forward(step) # checks how long it took by steps

# draws the square
def draw_square(t, size): # takes in the number and the size
  L = [] # gets an empty array
  for i in range(4):# gets the the range from 0 to 4
    t.forward(size) # tutle size and forward
    t.left(90) # direction of angle left
    store_position_data(L, t) # stores the position of data for number and size
  return L # return the array

# draws mulitple squares
def draw_squares(number): # Draws squares that extends
  t = turtle.Turtle() # gets the turtle position to be drawn
  L = [] # gets an empty array that will hold the number of squres that are drawn
  for i in range(1, number + 1): # keeps drawing squares until
    t.penup() # drawing the squere is up to repostion
    t.goto(-i, -i)# gets the location to start the extion of the squares
    t.pendown()# pend down to draw
    L.extend(draw_square(t, i * 2))# draws the ever expanding squares until the turtle escapes
  return L # returns array of number of squares drawn

# function that draws triangles
def draw_triangles(number):# draws the triangels
  t = turtle.Turtle() # gets the library to draw the turtle
  for i in range(1, number): # gets the range of how many of the triangels that will be drawn
    t.forward(i*10)# get the forward direction
    t.right(120) # Gets the left or right direction

# function that draws spirals
def draw_spirals_until_escaped(): # draws the spirals
    t = turtle.Turtle() # gets turle position
    t.penup() # pen Up -> not able to draw
    t.left(random.randint(0,360)) # direction at random on left
    t.pendown()# pen down -> draws the triangle
    i=0# start position is at 0
    turn = 360/random.randint(1,10)# gets the random turn from 0-360 and start position as 1 and end step at 10
    L=[]# empty array to be used and stored
    store_position_data(L,t)# stores the position data
    while not escaped(t.position()): # while loop the checks to see if the turtle has escaped
        i += 1 # increases each time by one spirals until the turtle escapeds
        t.forward(i*5)# get the forward postion and mutliplies that by 5
        t.right(turn)# takes in right position as turn
        store_position_data(L,t)# stores the position as the position of turle to be stored if escaped to check
    return L # returns when check is down and escaped

# function that Draws random spirangles
def draw_random_spirangles():# draws
    L=[]# gets an empty array to be used
    for i in range (10):# gets the steps to be used from 1 - 10
        L.extend(draw_spirals_until_escaped())# extends the spirals until escaped from "bag"
    with open("data_rand","wb") as f: # gets the random data
        pickle.dump(L,f)# uses another linbary called pickle to get the random data

# checks is the turle has escaped
def escaped(position): # gets the escape position
  x = int(position[0]) # gets the x position
  y = int(position[1]) # gets the y position
  return x < -35 or x > 35 or y < -35 or y > 35 # checks the  position of turtle to see if it has escaped by X or Y

# function stores the data of the turtle
def store_position_data(L, t): # stores that data as y and x
  position = t.position() # gets the potion of the turtle
  L.append([position[0], position[1], escaped(position)]) # appends to position of x and y plus checks to see if turtle has esacped -> escaped position

# runs the main loop
if __name__ == '__main__':
    turtle.setworldcoordinates(-70.,-70.,70.,70.) # gets world cordanates for grid
    draw_bag()# draws the bag
    #draw_square()# draws the sqaure
    #draw_triangles()# draws triangles
    #escaped()#checks if the robot has escape
    #draw_line()# draws line
    turtle.mainloop()# continues main lopp of code





