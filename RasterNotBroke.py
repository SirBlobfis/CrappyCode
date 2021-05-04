import math

"""-----Variables-----"""

cameraPosition = [0, 0, 0] #x, y, z
cameraDirection = [0, 0] #relative to x and z axes
fov = 90

screen = [] #x, y
#\/ these are the resolution
screenX = 10
screenY = 10

maxAnglePosX = 0
maxAngleNegX = 0
maxAnglePosZ = 0
maxAngleNegZ = 0

triangles = ( #triple nested tuples; x, y, z
    (
        (2, 0, 0),
        (2, 1, 0),
        (2, 0, 1)
    )
)

trianglesAsAngles = [] #triple nested arrays; x, z (angles); the "triangles" as angles from the camera

def buildScreen():
    global screen
    for a in range(screenX):
        screen.append([])
        for e in range(screenY):
            screen[a].append(0)

def maxViewAngles(): #basically give bounding box for what is within the "view cone" of the camera
    global maxAnglePosX, maxAngleNegX, maxAnglePosZ, maxAngleNegZ
    maxAnglePosX = cameraDirection[0] + fov / 2
    maxAngleNegX = cameraDirection[0] - fov / 2
    maxAnglePosZ = cameraDirection[1] + fov / 2
    maxAngleNegZ = cameraDirection[1] - fov / 2

def findAngles(first, second): #take in two points (3d)
    mathmathmath
    return ["answer"] #output angles; relative to x and z axis

def triPointsToAngles(): #takes the "triangles" variable and gives "trianglesAsAngles" according to each point from the camera
    global trianglesAsAngles
    for i in len(triangles):
        trianglesAsAngles[i][0] = findAngles(cameraPosition, triangles[i][0])
        trianglesAsAngles[i][1] = findAngles(cameraPosition, triangles[i][1])
        trianglesAsAngles[i][2] = findAngles(cameraPosition, triangles[i][2])

def triangleProject():
    global screen
    for a in range(len(trianglesAsAngles))
        for e in range(screenX):
            for i in range(screenY):
                if(pointInTri(triangles[])):

def pointInTri(tri, point):
    a1 = 
    a2 = 
    a3 = 

def triArea(p1, p2, p3):
    return .5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))

"""project onto screen place"""
#angle triangle points --> trig (hypotenuse changes, but not leg)
#give triangles on screen plane

"""rasterify"""
#take in screen plane with triangles
#go across every pixel, checking if inside a triangle

"""angle module"""
#take in two points --> angle from x axis & angle from z axis