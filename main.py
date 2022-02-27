import turtle
import math 

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(myturtle=None):
  '''
  Draws a sine curve.
  args:
    myturtle[turtle.Turtle]: a turtle object created by the turtle module
  return:
  '''
  start_x_coord = -360
  start_y_coord = math.sin(math.radians(-360))
  myturtle.penup()
  myturtle.goto(start_x_coord, start_y_coord)
  myturtle.pendown()
  for i in range(-360, 361):
    x_coord = i
    y_coord = math.sin(math.radians(i))
    myturtle.goto(x_coord, y_coord)
  print("Your sine curve has been drawn.")

def drawCosineCurve(myturtle=None):
  '''
  Draws a cosine curve.
  args:
    myturtle[turtle.Turtle]: a turtle object created by the turtle module
  return:
  '''
  start_x_coord = -360
  start_y_coord = math.cos(math.radians(-360))
  myturtle.penup()
  myturtle.goto(start_x_coord, start_y_coord)
  myturtle.pendown()
  for i in range(-360, 361):
    x_coord = i
    y_coord = math.cos(math.radians(i))
    myturtle.goto(x_coord, y_coord)
  print("Your cosine curve has been drawn.")

def drawTangentCurve(myturtle=None):
  '''
  Draws a tangent curve.
  args:
    myturtle[turtle.Turtle]: a turtle object created by the turtle module
  return:
  '''
  start_x_coord = -360
  start_y_coord = math.tan(math.radians(-360))
  myturtle.penup()
  myturtle.goto(start_x_coord, start_y_coord)
  myturtle.pendown()
  for i in range(-360, 361):
    x_coord = i
    y_coord = math.tan(math.radians(i))
    window_top = 2
    window_bottom = -2
    max_distance = 2
    # Checks if the next position is within the
    # bounds of the window; if not, it skips that position.
    # This is to prevent the turtle from going to positions
    # approaching infinity and breaking the graph.
    if window_top > y_coord and window_bottom < y_coord:
      # Checks if the distance between the turtle's current 
      # position and next position is greater than 2 (the max distance).
      # This is to prevent noncontinous parts of the tan graph from being
      # connected (i.e. the areas where they point to infinity).
      if myturtle.ycor() - y_coord > max_distance: 
        myturtle.penup()
        myturtle.goto(x_coord, y_coord)
        myturtle.pendown()
      else:
        myturtle.goto(x_coord, y_coord) 
      
  print("Your tangent curve has been drawn.")
 
def setupWindow(mywindow=None):
  '''
  Sets the world coordinates of a window for drawing trigonometric functions.
  args:
    mywindow[turtle._Screen]: a window created by the turtle module
  return:
  '''
  mywindow.setworldcoordinates(-400, -2, 400, 2)

def setupAxis(myturtle=None):
  '''
  Sets up an axis for drawing trigonometric functions.
  args:
    myturtle[turtle.Turtle]: a turtle object created by the turtle module
  return:
  '''
  myturtle.penup()
  myturtle.goto(0, -2)
  myturtle.pendown()
  myturtle.goto(0,2)
  myturtle.goto(0,0)
  myturtle.goto(360, 0)
  myturtle.goto(-360, 0)

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
