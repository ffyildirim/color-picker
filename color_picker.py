from PIL import Image
from random import randint

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list
      


      

import numpy

colors = dict((
((196, 2, 51), "RED"),
((255, 165, 0), "ORANGE"),
((255, 205, 0), "YELLOW"),
((0, 128, 0), "GREEN"),
((0, 0, 255), "BLUE"),
((127, 0, 255), "VIOLET"),
((0, 0, 0), "BLACK"),
((255, 255, 255), "WHITE"),))

def rgb_to_ycc(r, g, b): #http://bit.ly/1blFUsF
    y = .299*r + .587*g + .114*b
    cb = 128 -.168736*r -.331364*g + .5*b
    cr = 128 +.5*r - .418688*g - .081312*b
    return y, cb, cr

def to_ycc( color ): 
    """ converts color tuples to floats and then to yuv """
    return rgb_to_ycc(*[x/255.0 for x in color])

def color_dist( c1, c2):
    """ returns the squared euklidian distance between two color vectors in yuv space """
    return sum( (a-b)**2 for a,b in zip(to_ycc(c1),to_ycc(c2)) )

def min_color_diff( color_to_match, colors):
    """ returns the `(distance, color_name)` with the minimal distance to `colors`"""
    return min( # overal best is the best match to any color:
        (color_dist(color_to_match, test), colors[test]) # (distance to `test` color, color name)
        for test in colors)


def ColorDistance(rgb1,rgb2):
    rgb1 = rgb1[0][1:]
    rgb2 = rgb2[0][1:]
    
    #exit()

    rgb1 = numpy.array((int(rgb1[0:2],16),int(rgb1[2:4],16),int(rgb1[4:6],16)))
    rgb2 = numpy.array((int(rgb2[0:2],16),int(rgb2[2:4],16),int(rgb2[4:6],16)))

    #print(rgb1)
    #print(rgb2)

    #rgb1 = numpy.array(rgb1)
    #rgb2 = numpy.array(rgb2)

    diff = abs(rgb1-rgb2)

    
    '''d = {} distance between two colors(3)'''
    rm = 0.5*(rgb1[0]+rgb2[0])
    d = sum((2+rm,4,3-rm)*(diff)**2)**0.5
    #print(d)
    return d

img = Image.open('/home/furkan/Desktop/im1.png', 'r')
pixalValue = img.load()

width, height = img.size
allColors = []

output = "<style>div{height:3px;width:3px;float:left}</style>"
def rgb2hex(a):
    return "#{:02x}{:02x}{:02x}".format(a[0],a[1],a[2])

for y in range(0, width):
    for x in range(0, height):
        if(x==0):
            output = output + '<div style="clear:both;"></div>'
        output = output + ('<div style="background-color:'+rgb2hex(pixalValue[x,y])+'"></div>')
        allColors.append(rgb2hex(pixalValue[x,y]))
        #output = output + ('<div style="background-color:#'+str('{0:x}'.format(pixalValue[x,y][0]))+str('{0:x}'.format(pixalValue[x,y][1]))+str('{0:x}'.format(pixalValue[x,y][2]))+'"></div>')

uniques =  dict()
tmp = unique(allColors)
for x in range(0,len(tmp)):
    uniques[tmp[x]] = 0

for x in range(0,len(allColors)):
    uniques[allColors[x]] += 1

uniques = sorted(uniques.items(), key=lambda x: x[1], reverse=True)


treshold = 10 #int(len(tmp)/2)

major = dict()
for x in range(0,len(uniques[:treshold])):
    #print(uniques[x][0],uniques[x][1])
    major[uniques[x][0]] = (uniques[x][1])
minor = uniques[treshold:]


maxval = 0
tmp = 0
tmpmajor = dict()
for x in range(0,len(major.keys())):
    rgb1 = major.keys()[x][1:]
    rgb = ((int(rgb1[0:2],16),int(rgb1[2:4],16),int(rgb1[4:6],16)))
    tmpmajor[rgb] = (major.keys()[x])

replacer = dict()
for x in range(0,len(minor)):
    rgb1 = minor[x][0][1:]
    
    
    #exit()
    
    rgb = numpy.array((int(rgb1[0:2],16),int(rgb1[2:4],16),int(rgb1[4:6],16)))
    ##print(rgb)
    tmp = min_color_diff(rgb,tmpmajor)
    """    for y in range(0,treshold):
        if(maxval<ColorDistance(,uniques[y])):
            print("inside")
            maxval=ColorDistance(minor[x],uniques[y])
            tmp = uniques[y][0]
    major[tmp] += 1 """
    ##print(tmp)
    replacer[minor[x][0]] = tmp[1]

#print(replacer)
for x in range(0,len(major)):
    
    replacer[major.keys()[x]] = major.keys()[x]


for y in range(0, width):
    for x in range(0, height):
        color = replacer[rgb2hex(pixalValue[x,y])]
        if(x==0):
            output = output + '<div style="clear:both;"></div>'
        output = output + ('<div style="background-color:'+str(color)+'"></div>')



#print(major)


print(output)

exit()

colors = []

howMany = []

x = 1
y = 1
counter = 0
c = 0

while True:
 
    if x == width and y == height:
        break

    for k in range(0, len(colors)):
        if pixalValue[x, y] == colors[k]:
           
            c += 1
          
    if c == 0:
        for j in range(1, height):
            for i in range(1, width):
                if pixalValue[x, y] == pixalValue[i, j]:
                    counter += 1
                
        
        
        colors.append(pixalValue[x, y])
        howMany.append(counter)
        
    else:
        c = 0
        counter = 0
        if x < width-1 :
            x += 1
        elif x == width - 1:
            x = 1
            y += 1
            if y == height:
                break
        continue

    counter = 0
    
    if x < width-1 :
        x += 1
    elif x == width - 1:
        x = 1
        y += 1
        if y == height:
                break
    

myMap = []

for i in range(0, len(colors)):  
    myMap.append([howMany[i], colors[i]]) 


insertion_sort(myMap)


for j in range(len(howMany) - 30, len(howMany)):
    for i in range(0, len(howMany)- 30):
        if abs(myMap[i][1][0] - myMap[j][1][0]) < 5 and abs(myMap[i][1][1] - myMap[j][1][1]) <5 and abs(myMap[i][1][2] - myMap[j][1][2]) <5 :
            myMap[j][0] += 1
            continue

mySecondList = []

for i in range(0, 30):
    mySecondList.append(myMap[len(howMany) - 1 - i])

insertion_sort(mySecondList)

for i in range(0, len(mySecondList)):  
    print('<div style="background-color:rgb('+mySecondList[i][1]+'"></div>')
    #print(mySecondList[i])
    #print("-------------")
 

