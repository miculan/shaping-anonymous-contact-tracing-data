import random
import numpy
import matplotlib.pyplot as plt

NUMPOINTS = 15000
AREASIDE = 1000
DISTANCE = 10

xpos = numpy.empty(NUMPOINTS, dtype=object)
ypos = numpy.empty(NUMPOINTS, dtype=object)

def circle(cx,cy,r,x,y):
	return (x-cx)*(x-cx) + (y-cy)*(y-cy) <= r*r

def rect(ax, ay, bx, by, x,y):
	return (ax <= x) and (x <= bx) and (ay <= y) and (y <= by)

def triangle(x, y):
	return x+y <= AREASIDE

def L(x,y):
	return rect(100,100,800,400,x,y) or rect(100,100,400,800,x,y)

def T(x,y):
	return rect(100,100,800,400,x,y) or rect(100,100,400,800,x,y)

def bowtie(x,y):
	return rect(0,0,500,500,x,y) or rect(300,300,800,800,x,y) 

def eight(x,y):
	return circle(400,500,200,x,y) or circle(700,500,200,x,y)

# filter returns true if the point falls in the shape
# uncomment the desired shape, or add your own
def filter(x,y):
	return circle(500,500,500,x,y)
#	return rect(100,100,800,500,x,y)
#	return triangle(x,y)
#	return L(x,y)
#	return bowtie(x,y)
#	return eight(x,y)

def contact(x1,y1,x2,y2):
	return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) <= DISTANCE*DISTANCE 

def addedges(i):
	for j in range(0,i-1):
		if contact(xpos[i],ypos[i],xpos[j],ypos[j]):
			print i, "--", str(j)+";"

def saveplot():
	plt.scatter(xpos,ypos)
	plt.gca().set_aspect('equal', adjustable='box')
	plt.savefig('plot.png')


print(
'''graph G {
layout = sfdp;
overlap = true;
node [shape=point];
edge [weight=3,style=invis];
'''
    )

i = 0
while i < NUMPOINTS:
	x = random.randint(0,AREASIDE)
	y = random.randint(0,AREASIDE)
	if filter(x,y):
		xpos[i] = x
		ypos[i] = y
		addedges(i)
		i = i + 1

print '}'

saveplot()
