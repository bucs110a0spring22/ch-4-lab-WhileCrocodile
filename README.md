#### CS 110
# Chapter 4 - Lab - Functions

### [Assignment Description](https://docs.google.com/document/d/1V20D_upUX4MO8YmskKlRB25Yu2pCEv3-h8z4EAfrSno/edit?usp=sharing)

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
Uses the turtle module to draw a graph of sin, cos, and tan.
(Axes are not labelled).

## GRACE DAYS
Grace days used for this assignment: 0

Grace days remaining: 5/5

## KNOWN BUGS AND INCOMPLETE PARTS:
N/A

## REFERENCES:
Turtle documentation.

## MISCELLANEOUS COMMENTS:
The function for drawing a tan graph is much more complicated than for sin and cosin, because parts of the graph go to infinity. This is a problem for two reasons. Firstly, it forces the turtle to go to values approaching infinity, which breaks some stuff. Second, because the graph is not continous, you need a way to determine which points are connected and which aren't.

You could write the tan function the same way as the sin and cos functions, and it would kind of work. This is because the turtle approaches infinity from the left, then emerges from negative infinity without a connecting line between the two. This way, you kind of get a working tan graph. However, I don't think the turtle was meant to ever go to infinity, so parts of the graph just disappear.

I tried fixing this by making sure the turtle was within bounds of the window before it would draw the tan graph. I also made sure that no line would be drawn if the y distance between 2 points was greater than 2. This fixed the going to infinity problem, while only letting points that should be connected to be connected.

I'm not sure if the original broken implementation of the drawing tan function would have been accepted, but the "fixed" version is a lot more complicated than I would have expected (for my beginner skill level anyways :sob:)