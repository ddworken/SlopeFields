from __future__ import print_function  # used for 2,3 compat
from __future__ import division  # used for 2,3 compat
import argparse  # used to parse arguments
import matplotlib.pyplot as plt  # used for graphing
import numpy as np  # used for fast arrays and np.arange
import math  # used for math.sqrt
from math import *  # used for when we eval() math expressions
from sys import argv  # used to grab the first argument (aka the equation)

parser=argparse.ArgumentParser(description='Generate a slope field for a given function. ')
parser.add_argument('--xMin', dest='xMin', help='Minimum x value. ')
parser.add_argument('--xMax', dest='xMax', help='Maximum x value. ')
parser.add_argument('--yMin', dest='yMin', help='Minimum y value. ')
parser.add_argument('--yMax', dest='yMax', help='Maximum y value. ')
parser.add_argument('--initX', dest='initX', help='The initial x value. ')
parser.add_argument('--initY', dest='initY', help='The initial y value. ')
parser.add_argument('--dX', dest='dX', help='The dX value used in euler\'s method. ')
parser.add_argument('--line', dest='line', help='If you want to draw a line connecting the dots. Note this may cause problems on functions with asymptotes. ', action='store_true')
parser.add_argument('--approximate', dest='approximate', help='If you want to approximate f(a). ')
parser.add_argument('equation', help='The equation')
args = parser.parse_args()

initX = 0  # starting x value
if args.initX:
    initX = float(args.initX)
initY = 1  # starting y value
if args.initY:
    initY = float(args.initY)
dX = .0001  # the value that is used for dX in the euler's method calculation
if args.dX:
    dX = float(args.dX)
numberPoints = 1000000  # the max number of points we calculate when doing euler's method
step = .5  # the dX and dY between the slopes on the slope field
lengthSlope = .5  # the length of the slope

xMin = -10  # use to adjust the domain and range of the graph
if args.xMin:
    xMin = float(args.xMin)
xMax = 10
if args.xMax:
    xMax = float(args.xMax)
yMin = -10
if args.yMin:
    yMin = float(args.yMin)
yMax = 10
if args.yMax:
    yMax = float(args.yMax)

equation = args.equation.replace('^','**')

def getPoint(x, y):  # gets a point to be plotted on the slope field
    return [x, y, dydx(x,y)]  # returns xVal, yVal, slope

def dydx(x, y):  # calculates the slope at a given point
    return eval(equation)

def calcPointsFromPointAndSlope(x, y, slope, len):  # in order to plot a slope at a point, we need to generate the two points we want connected by the line
    a= math.sqrt((len*len)/(4+4*slope*slope))  # a is calculated based off of the len of the line and the slope so as to ensure all the slopes have a constant length
    x1 = x-a
    x2 = x+a
    y1 = y-a*slope
    y2 = y+a*slope
    return [(x1,y1),(x2,y2)]  # returns a list of two points

def getPointsFromEulersMethod(initX, initY, dX, numberPoints, equation):  # returns a list of points that were found using euler's method
    def getRow(x, y, dx):  # returns a row in the the euler's method table
        return [x, dx, y, dydx(x,y)*dx]

    def floatingEquals(a, b):
        return abs(a-b) <= dX
    haveFoundApproxSolution = False

    # we calculate forward and backward from the initX point
    forwardTable = [getRow(initX, initY, dX)]  # initial list that will hold all of the rows for euler's method going forward
    currCountPoints = 0  # the number of points calculated so far
    while currCountPoints < numberPoints:  # while we have calculated fewer than numberPoints
        y = forwardTable[-1][2]  # the y value
        try:
            denom = eval(equation.split('/')[1])  # calculate the denom
        except:
            denom = 1  # if no denom, then the denom is 1
        if (denom < -.1 or denom > .1):  # if denom!~=0: used so as to avoid problems with function definition
            try:
                row = getRow(forwardTable[-1][0]+forwardTable[-1][1], forwardTable[-1][2], forwardTable[-1][1])  # get the next row based off of the last row
            except:
                break
            row[2] = row[2]+forwardTable[-1][3]  # update the y value in the row by addying the previous dy
            forwardTable.append(row)  # add the row to the table
        if abs(forwardTable[-1][0]) > max([abs(xMin), abs(xMax)]):  # if the x value > 10 or < -10, then we have gone past the axes on the graph so break
            break
        if args.approximate and not haveFoundApproxSolution:
            if floatingEquals(forwardTable[-1][0], float(args.approximate)):
                print("f("+args.approximate+")="+str(forwardTable[-1][2]))
                haveFoundApproxSolution = True
        currCountPoints += 1
    currCountPoints = 0  # reset for calculating backwards
    backwardTable = [getRow(initX, initY, dX)]
    while currCountPoints < numberPoints:
        y = backwardTable[-1][2]
        try:
            denom = eval(equation.split('/')[1])
        except:
            denom = 1
        if (denom < -.1 or denom > .1):
            try:
                row = getRow(backwardTable[-1][0]-backwardTable[-1][1], backwardTable[-1][2], backwardTable[-1][1])
            except:
                break
            row[2] = row[2]-backwardTable[-1][3]
            backwardTable.append(row)
        if abs(backwardTable[-1][0]) > max([abs(xMin), abs(xMax)]):
            break
        if args.approximate and not haveFoundApproxSolution:
            if floatingEquals(backwardTable[-1][0], float(args.approximate)):
                print("f("+args.approximate+")="+str(backwardTable[-1][2]))
                haveFoundApproxSolution = True
        currCountPoints += 1
    fullTable = backwardTable[::-1] + forwardTable  # full table of points is both forward and backward combined
    return [(item[0], item[2]) for item in fullTable]  # we only need the x and y coordinates (not the dx and dy)

def getListOfPointsAndSlopes(step):  # returns a list of points and slopes for plotting on the slope field
    table = [] #holds a list of tuples: (x, y, dy/dx)
    for x in np.arange(xMin, xMax, step):  # x in range between -10 and 10 incremented by the step size
        for y in np.arange(yMin, yMax, step):  # same but for y
            try:
                table.append(getPoint(x,y))
            except ZeroDivisionError:  # if the slope has a divide by zero error, we pass
                pass
            except ValueError:
                pass
    return table

table = getListOfPointsAndSlopes(step)  # get list of points and slopes to be put on the slope field

ax = plt.subplot()  # create the axes

for pointSlope in table:  # iterate through the point and slope pairs
    points = calcPointsFromPointAndSlope(pointSlope[0], pointSlope[1], pointSlope[2], lengthSlope)  # get the points rather than a point slope pair
    ax.plot([points[0][0], points[1][0]], [points[0][1],points[1][1]])  # graph a line between those points

ax.grid()  # enable the grid layout on the graph
ax.set_xlim([xMin, xMax])  # set the axes limits
ax.set_ylim([yMin, yMax])

points = getPointsFromEulersMethod(initX, initY, dX, numberPoints, equation)  # get all of the points from euler's method
xPoints = [x for [x,y] in points]  # break them into lists of x values and y values
yPoints = [y for [x,y] in points]

if args.line:
    ax.plot(xPoints, yPoints, 'r-', linewidth=5)  # graph the points from euler's method
else:
    ax.plot(xPoints, yPoints, 'ro', linewidth=5)

plt.title("Slope Field: " + equation.replace('**','^'))

plt.show()  # display the graph
