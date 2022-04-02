import tkinter
import math
#import graphics as g
from matplotlib import pyplot as plt
import matplotlib as mp
#from graphics import *
#main_circle=g.Circle(g.Point(100,100),50)
ci=plt.Circle(xy=(100,100),radius=50)
pa=mp.Path
# L=[g.Circle(i,100) for i in [g.Point(k,l) for k,l in range(30,61)]]
# win=g.GraphWin("Окръжности",200,200)
# for l in L:
#     l.draw(win)
L_points=[]
for k in range(50,151):
    for m in range(50,151):
        L_points.append((k,m))

test=pa.contains_points(self, L_points, transform=None, radius=50)
L_new=L_points[test]
print(len(L_new))

# p=mp.Circle(center=(100,100),radius=50)
# pa=p.Path()
#
# print(pa)

# fig, ax = plt.subplots()
# #Set up the subplot for the circle
# ax.set(xlim=(-1, 1), ylim = (-1, 1))
#
# a_circle = plt.Circle((0, 0), .5)
# ax.add_artist(a_circle)

# import time
#
#
# def main():
#     win = GraphWin('Back and Forth', 300, 300)
#     #win.  # make right side up coordinates!
#
#     rect = Rectangle(Point(200, 90), Point(220, 100))
#     rect.setFill("blue")
#     rect.draw(win)
#
#     cir1 = Circle(Point(40, 100), 25)
#     cir1.setFill("yellow")
#     cir1.draw(win)
#
#     cir2 = Circle(Point(150, 125), 25)
#     cir2.setFill("red")
#     cir2.draw(win)
#
#     for i in range(46):
#         cir1.move(5, 1)
#         time.sleep(.05)
#
#     for i in range(46):
#         cir1.move(-5, 1)
#         time.sleep(.05)
#
#     #win.promptClose(win.getWidth() / 2, 20)
#
#
# main()