import turtle
import math 

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(turtle_object):
  '''
  Draws a sine curve.
  args:
  return:
  '''
  start_x_coord = -360
  start_y_coord = math.sin(math.radians(-360))
  turtle_object.penup()
  turtle_object.goto(start_x_coord, start_y_coord)
  turtle_object.pendown()
  for i in range(-360, 361):
    x_coord = i
    y_coord = math.sin(math.radians(i))
    turtle_object.goto(x_coord, y_coord)
  print("Your sine curve has been drawn.")

def drawCosineCurve(turtle_object):
  '''
  Draws a cosine curve.
  args:
  return:
  '''
  start_x_coord = -360
  start_y_coord = math.cos(math.radians(-360))
  turtle_object.penup()
  turtle_object.goto(start_x_coord, start_y_coord)
  turtle_object.pendown()
  for i in range(-360, 361):
    x_coord = i
    y_coord = math.cos(math.radians(i))
    turtle_object.goto(x_coord, y_coord)
  print("Your cosine curve has been drawn.")

def drawTangentCurve(turtle_object):
  '''
  Draws a tangent curve.
  args:
  return:
  '''
  start_x_coord = -360
  start_y_coord = math.tan(math.radians(-360))
  turtle_object.penup()
  turtle_object.goto(start_x_coord, start_y_coord)
  turtle_object.pendown()
  for i in range(-360, 361):
    x_coord = i
    y_coord = math.tan(math.radians(i))
    turtle_object.goto(x_coord, y_coord)
  print("Your tangent curve has been drawn.")
 
def setupWindow(screen_object):
  '''
  Sets the world coordinates of a window for drawing trigonometric functions.
  args:
  return:
  '''
  screen_object.setworldcoordinates(-400, -2, 400, 2)

def setupAxis(turtle_object):
  '''
  Sets up an axis for drawing trigonometric functions.
  args:
  return:
  '''
  turtle_object.penup()
  turtle_object.goto(0, -2)
  turtle_object.pendown()
  turtle_object.goto(0,2)
  turtle_object.goto(0,0)
  turtle_object.goto(360, 0)
  turtle_object.goto(-360, 0)

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
