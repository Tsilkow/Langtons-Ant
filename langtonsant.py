import glob
import random
import sys
import os
from PIL import Image,ImageDraw
from math import pi, sin, cos, sqrt

dimensions = [101, 101]
tileSize = 2
tileVerticies = 6
start = (dimensions[0]//2, dimensions[1]//2)
antColor = (255, 255, 255)
colors = []
rule = "1203214"
colorTotal = 12
isDrawing = 1
maxStep = 100000

# functions for creating n colors on the wheel of colors
def colorValue(point):
    while point < 0: point += 1
    while point >= 1: point -= 1

    if   point <= 1/6: return point*6
    elif point <= 3/6: return 1
    elif point <= 4/6: return (4/6 - point) * 6
    else: return 0

def colorFromRange(point):
    return (round(255 * colorValue(point + 2/6)),
            round(255 * colorValue(point      )),
            round(255 * colorValue(point - 2/6)))

colors.append((0, 0, 0))
for i in range(colorTotal):
    colors.append(colorFromRange(i/(colorTotal-1)))

#for i in range(colorTotal):
#    colors.append((round(255 * sqrt(i/colorTotal)), round(128 * sqrt(i/colorTotal)), 0))

if len(sys.argv) > 1: isDrawing = int(sys.argv[1])
if len(sys.argv) > 2: rule = sys.argv[2]
if len(sys.argv) > 3: tileSize = float(sys.argv[3])
if len(sys.argv) > 4: dimensions[0] = int(sys.argv[4])
if len(sys.argv) > 5: dimensions[1] = int(sys.argv[5])
if len(sys.argv) > 6: tileVerticies = int(sys.argv[6])

start = (dimensions[0]//2, dimensions[1]//2)

if tileVerticies == 4:
    width  = dimensions[0] * tileSize
    height = dimensions[1] * tileSize
elif tileVerticies == 6:
    width =  dimensions[0] * tileSize
    height = dimensions[1] * tileSize

width = int(width)
height = int(height)

im = Image.new('RGBA', (width, height), "#000000ff")
draw = ImageDraw.Draw(im)

def drawTile(x, y, color):
    
    if tileVerticies == 4:
        draw.polygon([( x      * tileSize,  y      * tileSize),
                      ((x + 1) * tileSize-1,  y      * tileSize),
                      ((x + 1) * tileSize-1, (y + 1) * tileSize-1),
                      ( x      * tileSize, (y + 1) * tileSize-1)],
                     fill = color)
    elif tileVerticies == 6:
        draw.polygon([((x     + 0.5 * (y%2)) * tileSize  ,  y      * tileSize  ),
                      ((x + 1 + 0.5 * (y%2)) * tileSize-1,  y      * tileSize  ),
                      ((x + 1 + 0.5 * (y%2)) * tileSize-1, (y + 1) * tileSize-1),
                      ((x     + 0.5 * (y%2)) * tileSize  , (y + 1) * tileSize-1)],
                     fill = color)
    #    draw.polygon([((x + 0.5 + 0.5 * (y % 2)) * tileSize, (y * 0.75       ) * tileSize),
    #                  ((x + 1   + 0.5 * (y % 2)) * tileSize, (y * 0.75 + 0.25) * tileSize),
    #                  ((x + 1   + 0.5 * (y % 2)) * tileSize, (y * 0.75 + 0.75) * tileSize),
    #                  ((x + 0.5 + 0.5 * (y % 2)) * tileSize, (y * 0.75 + 1   ) * tileSize),
    #                  ((x       + 0.5 * (y % 2)) * tileSize, (y * 0.75 + 0.75) * tileSize),
    #                  ((x       + 0.5 * (y % 2)) * tileSize, (y * 0.75 + 0.25) * tileSize)],
    #                 fill = color)

def getNeighbour(x, y, d):
    if tileVerticies == 4:
        if   d == 0: return (x  , y-1)
        elif d == 1: return (x+1, y  )
        elif d == 2: return (x  , y+1)
        elif d == 3: return (x-1, y  )
    elif tileVerticies == 6 and y % 2 == 0:
        if   d == 0: return (x  , y-1)
        elif d == 1: return (x+1, y  )
        elif d == 2: return (x  , y+1)
        elif d == 3: return (x-1, y+1)
        elif d == 4: return (x-1, y  )
        elif d == 5: return (x-1, y-1)
    elif tileVerticies == 6 and y % 2 == 1:
        if   d == 0: return (x+1, y-1)
        elif d == 1: return (x+1, y  )
        elif d == 2: return (x+1, y+1)
        elif d == 3: return (x  , y+1)
        elif d == 4: return (x-1, y  )
        elif d == 5: return (x  , y-1)

data = [[0 for i in range(dimensions[0])] for j in range(dimensions[1])]

antDirection = 0
antPosition = start
step = 0
maxDetected = 0

if isDrawing == 1:
    print(os.getcwd() + "/" + rule + "/")
    try:
        os.mkdir(os.getcwd() + "/" + rule + "/")
    except OSError:
        print ("Creation of the directory failed")
    else:
        print ("Successfully created the directory")

while 1:
    step += 1
    if step >= maxStep: break
    antDirection = (antDirection + int(rule[data[antPosition[0]][antPosition[1]] % len(rule)])) % tileVerticies

    data[antPosition[0]][antPosition[1]] += 1
    maxDetected = max(maxDetected, data[antPosition[0]][antPosition[1]])
    
    if isDrawing == 1:
        drawTile(antPosition[0], antPosition[1], colors[data[antPosition[0]][antPosition[1]] % len(colors)])
        
    antPosition = getNeighbour(antPosition[0], antPosition[1], antDirection)
    if (antPosition[0] < 0 or antPosition[0] >= dimensions[0]-1 or
        antPosition[1] < 0 or antPosition[1] >= dimensions[1]-1):
        break
    
    if isDrawing == 1:
        drawTile(antPosition[0], antPosition[1], antColor)
        im.save(rule + "/" + "{:05d}".format(step) + "ant.png", "PNG")
        if step % 100 == 0: print(rule + "/" + "{:05d}".format(step) + "ant.png")

if isDrawing == 0:
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            drawTile(x, y, colors[data[x][y] % len(colors)])
    im.save("samples/" + rule + ".png", "PNG")

# making a gif out of it
#img, *imgs = [Image.open(f) for f in sorted(glob.glob("output/*ant.png"))]
#img.save(fp="out.gif", format='GIF', append_images=imgs, save_all=True, duration=1, loop=0)
