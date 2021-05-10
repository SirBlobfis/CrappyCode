import math
import time

"""-----Variables-----"""

cameraPosition = [-1, 0, 0] #x, y, z
cameraDirection = [0, 0] #relative to x and z axes
fov = 90

screen = [] #x, y
screen2 = [] #used to change the "True"s and "False"s to something else
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
    ),
    (
        (2, 1, 0),
        (2, 2, 0),
        (2, 1, 1)
    )
)

trianglesAsAngles = [] #triple nested arrays; x, z (angles); the "triangles" as angles from the camera

screenTriangles = [] #triple nested arrays; x, y (coordinates); the triangles that appear on the screen; still needs to be pixelated

def buildScreen():
    global screen
    for a in range(screenX):
        screen.append([])
        screen2.append([])
        for e in range(screenY):
            screen[a].append(0)
            screen2[a].append("0")

def maxViewAngles(): #basically give bounding box for what is within the "view cone" of the camera
    global maxAnglePosX, maxAngleNegX, maxAnglePosZ, maxAngleNegZ
    maxAnglePosX = cameraDirection[0] + fov / 2
    maxAngleNegX = cameraDirection[0] - fov / 2
    maxAnglePosZ = cameraDirection[1] + fov / 2
    maxAngleNegZ = cameraDirection[1] - fov / 2

def findAngles(first, second): #take in two points (3d)
    try:
        angZ = math.degrees(math.atan((first[0] - second[0]) / (first[2] - second[2])))
    except ZeroDivisionError:
        angZ = 0
    try:
        angX = math.degrees(math.atan((first[0] - second[0]) / (first[1] - second[1])))
    except ZeroDivisionError:
        angX = 0
    return [angX, angZ] #output angles; relative to x and z axis

def triPointsToAngles(): #takes the "triangles" variable and gives "trianglesAsAngles" according to each point from the camera
    global trianglesAsAngles
    trianglesAsAngles = []
    for i in range(len(triangles)):
        trianglesAsAngles.append([[], [], []])
        trianglesAsAngles[i][0] = findAngles(cameraPosition, triangles[i][0])
        trianglesAsAngles[i][1] = findAngles(cameraPosition, triangles[i][1])
        trianglesAsAngles[i][2] = findAngles(cameraPosition, triangles[i][2])

def triangleProject(): #take "trianglesAsAngles" and give "screenTriangles"
    global screenTriangles
    screenTriangles = []
    for a in range(len(trianglesAsAngles)):
        #print("triCor: " + str(triangles[a]))
        if(checkTriInViewCone(trianglesAsAngles[a])):
            screenTriangles.append([])
            screenTriangles[len(screenTriangles) - 1] = [[], [], []]
            for i in range(3):
                print("BBBBB" + str(math.degrees(math.tan(math.radians(trianglesAsAngles[a][i][0])))))
                screenTriangles[len(screenTriangles) - 1][i].append(math.degrees(math.tan(math.radians(trianglesAsAngles[a][i][0]))))
                screenTriangles[len(screenTriangles) - 1][i].append(math.degrees(math.tan(math.radians(trianglesAsAngles[a][i][1]))))

def checkTriInViewCone(tri):
    #print("triAngs: " + str(tri))
    for i in range(3):
        if(tri[i][0] > maxAnglePosX and tri[i][0] < maxAngleNegX and tri[i][1] > maxAnglePosZ and tri[i][1] < maxAngleNegZ):
            return False
    return True

def pointInTri(tri, point): #takes triangle and point, returning true or false if the point is inside the (2D) triangle
    #print(str(point) + str(tri))
    a = triArea(tri[0], tri[1], tri[2])
    a1 = triArea(point, tri[1], tri[2])
    a2 = triArea(tri[0], point, tri[2])
    a3 = triArea(tri[0], tri[1], point)
    fudge = .00000
    if(a < a1 + a2 + a3 - fudge):
        return False
    return True

def triArea(p1, p2, p3):
    return .5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))

def rasterify():
    global screen
    #print(screenX)
    #print(screenY)
    #print(screenTriangles)
    for a in range(screenX):
        for e in range(screenY):
            for i in range(len(screenTriangles)):
                screen[a][e] = pointInTri(screenTriangles[i], [a, e])

if __name__ == "__main__":
    buildScreen()
    while True:
        maxViewAngles()
        #print(maxAnglePosX)
        #print(maxAngleNegX)
        #print(maxAnglePosZ)
        #print(maxAngleNegZ)
        triPointsToAngles()
        triangleProject()
        rasterify()
        for e in range(10):
            print("\n")
        for i in range(screenX):
            for r in range(screenY):
                if(screen[i][r]):
                    screen2[i][r] = "1"
                else:
                    screen2[i][r] = "."
        for i in range(screenY):
            print(screen2[i])
        print(trianglesAsAngles)
        print(screenTriangles)
        print(cameraDirection)
        cameraPosition[1] += .2
        #cameraDirection[1] += 2
        time.sleep(.5)