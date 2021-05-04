import math
import time
import keyboard

#HELP:
#https://math.stackexchange.com/questions/1385137/calculate-3d-vector-out-of-two-angles-and-vector-length
#https://www.scratchapixel.com/lessons/3d-basic-rendering/rasterization-practical-implementation
#https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/

"""
- variables - variables - variables - variables - variables - 
"""

#x, y, z
triangles = [
    [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
]

screenTriangles = []

screen = [] #x, y
screenX = 10
screenY = 10

camera = [0, 0, 2] #x, y, z
cameraPointOffset = 1
cameraPoint = [0, 0, 2]
cameraSquareSizeX = 2
cameraSquareSizeY = 2
cameraDirection = [0, 180] #x, z
fov = 90

cameraMaxSlopePosX = 0
cameraMaxSlopeNegX = 0
cameraMaxSlopePosY = 0
cameraMaxSlopeNegY = 0
cameraMaxSlopePosZ = 0
cameraMaxSlopeNegZ = 0

"""
- functions - functions - functions - functions - functions - 
"""

def buildScreen():
    screenBuild = []
    for a in range(screenX):
        screenBuild.append([])
        for e in range(screenY):
            screenBuild[a].append(0)
    return screenBuild

def cameraOffset():
    global cameraPoint
    cameraPoint[0] = round(cameraPointOffset * math.cos(math.radians(cameraDirection[0])) * math.sin(math.radians(cameraDirection[1])), 4)
    cameraPoint[1] = round(cameraPointOffset * math.cos(math.radians(cameraDirection[0])) * math.cos(math.radians(cameraDirection[1])), 4) 
    cameraPoint[2] = round(cameraPointOffset * math.sin(math.radians(cameraDirection[0])), 4)

def cameraMaxSlopes(): #NOT DONE
    global cameraMaxSlopePosX, cameraMaxSlopeNegX, cameraMaxSlopePosY, cameraMaxSlopeNegY, cameraMaxSlopePosZ, cameraMaxSlopeNegZ
    try:
        cameraMaxSlopePosX = (cameraPoint[0] / (cameraSquareSizeX / 2))
    except ZeroDivisionError:
        cameraMaxSlopePosX = float("inf")
    
    try:
        cameraMaxSlopeNegX = 0
    except ZeroDivisionError:
        cameraMaxSlopeNegX = float("inf")
    
    try:
        cameraMaxSlopePosY = 0
    except ZeroDivisionError:
        cameraMaxSlopePosY = float("inf")
    
    try:
        cameraMaxSlopeNegY = 0
    except ZeroDivisionError:
        cameraMaxSlopeNegY = float("inf")
    
    try:
        cameraMaxSlopePosZ = 0
    except ZeroDivisionError:
        cameraMaxSlopePosZ = float("inf")
    
    try:
        cameraMaxSlopeNegZ = 0
    except ZeroDivisionError:
        cameraMaxSlopeNegZ = float("inf")

def trianglesToScreen():
    withinViewCone = True
    print(triangles)
    for a in range(len(triangles)):
        if(withinViewCone):
            projectOntoScreen(triangles[a])

def projectOntoScreen(tri):
    global screenTriangles
    intermediateTri = []
    projectedTriDirection = [0, 0]
    print("tri: " + str(tri))
    for i in range(3):
        #projectedTriDistance = distance(tri[i], cameraPoint)
        try:
            projectedTriDirection[1] = math.degrees(math.atan((cameraPoint[0] - tri[i][0]) / (cameraPoint[2] - tri[i][2])))
        except ZeroDivisionError:
            projectedTriDirection[1] = 0
        try:
            projectedTriDirection[0] = math.degrees(math.atan((cameraPoint[0] - tri[i][0]) / (cameraPoint[1] - tri[i][1])))
        except ZeroDivisionError:
            projectedTriDirection[0] = 0
        intermediateTri.append([])
        #print("projectedTriDirection: " + str(projectedTriDirection))
        intermediateTri[i].append((projectedTriDirection[0] / (fov / 2)) * screenX)
        intermediateTri[i].append((projectedTriDirection[1] / (fov / 2)) * screenY)
    screenTriangles.append(intermediateTri)

def distance(first, second):
    return abs(math.sqrt((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2 + (first[2] - second[2]) ** 2))

def raster():
    print("---screenTriangles---")
    for a in range(len(screenTriangles)):
        print(screenTriangles[a][0])
        print(screenTriangles[a][1])
        print(screenTriangles[a][2])
        for e in range(screenX):
            for i in range(screenY):
                point = [a, e]
                if checkPixelInTriangle(screenTriangles[a], point):
                    screen[a][e] = 1
                else:
                    screen[a][e] = 0
    print("---screenTriangles---")

def turn():
    global cameraDirection
    if(keyboard.is_pressed('down')):
        cameraDirection[1] += 5
    if(keyboard.is_pressed('up')):
        cameraDirection[1] -= 5
    if(keyboard.is_pressed('right')):
        cameraDirection[0] += 5
    if(keyboard.is_pressed('left')):
        cameraDirection[0] -= 5

def checkPixelInTriangle(tri, point): #leave triangle depth for otherwhere
    for i in range(3):
        A0 = triangleArea(tri)
    
        A1_ = [0, 0, 0]
        A1_[0] = [point[0], point[1]]
        A1_[1] = [tri[1][0], tri[1][1]]
        A1_[2] = [tri[2][0], tri[2][1]]
        A1 = triangleArea(A1_)
        
        A2_ = [0, 0, 0]
        A2_[0] = [tri[0][0], tri[0][1]]
        A2_[1] = [point[0], point[1]]
        A2_[2] = [tri[2][0], tri[2][1]]
        A2 = triangleArea(A2_)
        
        A3_ = [0, 0, 0]
        A3_[0] = [tri[0][0], tri[0][1]]
        A3_[1] = [tri[1][0], tri[1][1]]
        A3_[2] = [point[0], point[1]]
        A3 = triangleArea(A3_)

        if(A0 == A1 + A2 + A3):
            return True
        else:
            return False

def triangleArea(tri):
    #print("##########:" + str(tri))
    return abs((tri[0][0] * (tri[1][1] - tri[2][1]) + tri[1][0] * (tri[2][1] - tri[0][1]) + tri[2][0] * (tri[0][1] - tri[1][1])) / 2.0)

"""
- main loop - main loop - main loop - main loop - main loop - 
"""

if __name__ == ("__main__"):
    screen = buildScreen()
    #print(screen)
    while True:
        cameraOffset()
        #cameraMaxSlopes()
        #print("cameraDirection: " + str(cameraDirection) + str(camera) + str(cameraPoint))
        turn()
        screenTriangles = []
        trianglesToScreen()
        for i in range(len(screenTriangles)):
            #print("screenTriangles: " + str(screenTriangles[i]))
            pass
        raster()

        for i in range(screenY):
            print(screen[i])
            pass
        for i in range(10):
            print("\n")
        time.sleep(.1)