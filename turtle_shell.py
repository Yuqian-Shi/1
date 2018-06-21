# Turtle-shell program
# fill the picture with given pattern
# Author： Yuqian Shi
# ====================================
# Approach:
# All pixels can be divided into three groups: background, line and cross points.
# The cross points (point) were separated into two types: A and B, depending on
# which side the horizontal line is.
# Each point should have three lines connected to it and
# each line consists three pixels (except the cross point).
# Maintain a list of undraw-points-list
# And the other end points of the three lines could be added to undraw-points-list.
# After drawing a point from the undraw-points-list (list), remove it.
# Repeat until the list is empty.
# If the required picture is too small in width or height,
# first generate a larger picture and then cut it smaller.
# ====================================
# 1. Set a initial point at (0,3) and add it to the list.
# 2. Try to draw lines around the point(s) in list.
# 3. Remove the drew point and add new points (drawable) into the list.
# 4. Repeat 3 until the list is empty

import PIL.Image as pim

# a function that transfers a list of strings in to a tuple of ints
def list2tuple(l):
    l = [ int(x) for x in l ]
    return tuple(l)

# Draw a line of 4 pixels (including the start point)
# Outputs: The end point position if its valid (in range)
# Inputs: The position of start point and the direction of line
def drawL(pos,dire):
    for i in range(3):
        try:
            pos = (pos[0]+dire[0],pos[1]+dire[1])
            img.putpixel((pos[0],pos[1]),l_c)
        except:
            pass
    if pos[0]<width and pos[1]<height:
        return pos
    else:
        return

# Drawing three lines for each type of point
# Outputs: A list of points to be added to the undraw-points-list
# Inputs: The position of start point and the type of that point
def draw(pos,typeA):
    if typeA:
        # drawing directions for type A
        dires = [(1,0),(-1,1),(-1,-1)]
    else:
        # drawing directions for type B
        dires = [(-1,0),(1,1),(1,-1)]
    re = []
    for dire in dires:
        try:
            # detect whether this direction have been drew before
            if img.getpixel((pos[0]+dire[0],pos[1]+dire[1])) == l_c:
                pass
            else:
                pos1 = drawL(pos,dire)
                if len(pos1) ==2:
                    re.append(pos1)
        except:
            pass

    return re

# Tell if a given point is type A
# Outputs: A Boolean value (True for type A)
# Inputs: The position of the point
def tellA(pos):
    Blist = [(pos[0]-1,pos[1]),(pos[0]+1,pos[1]+1),(pos[0]+1,pos[1]-1)]
    for point in Blist:
        if (point[0] in range(width)) and (point[1] in range(height)):
            if img.getpixel((point[0],point[1])) == l_c:
                return False
    else:
        return True



# ====================================================
# ====================================================
# Get inputs
size = input('Enter size of image (width height): ').split(' ')
bgc = input('Enter background colour (r g b): ').split(' ')
l_c = input('Enter line colour (r g b): ').split(' ')
width = int(size[0])
height = int(size[1])
bgc = list2tuple(bgc)
l_c = list2tuple(l_c)
img = pim.new("RGB",(width,height))

# If the required picture is too small,
# then treat it with different way
small_flag = False
old_w = width
old_h = height
if width<4:
    width = 4
    small_flag = True
if height < 4:
    height = 4
    small_flag = True
old_img = img
img = pim.new("RGB",(width,height))

# Set background
for x in range(width):
    for y in range(height):
        img.putpixel((x,y),bgc)

# set initial point
pos = (0,3)
points = [pos]
# The initial point's type must be assigned
img.putpixel(pos,l_c)
points.extend(draw(pos,False))
# Start drawing
while len(points):
    point = points[0]
    points = points[1:]
    if tellA(point) == True:
        points.extend(draw(point,True))
    else:
        points.extend(draw(point,False))
# Cutting the pictures
if small_flag:
    for x in range(old_w):
        for y in range(old_h):
            pos = (x,y)
            old_img.putpixel(pos,img.getpixel(pos))
    old_img.save('output.png')
else:
    img.save('output.png')
