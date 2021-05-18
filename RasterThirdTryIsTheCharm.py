import time
import triangles
import keyboard

triangles = triangles.triangles

trianglesAsSlopes = [] #y/x, z/x

trianglesOnPlane = []

cameraPoint = [0, 0, 0] #x, y, z
cameraSize = 51
cameraCenter = [round(cameraSize/2) - 1, round(cameraSize/2) - 1]
cameraPlane = []
cameraDirection = [0, 0]

cameraMoveAmount = .1

def zeroTriangles():
    global trianglesAsSlopes, trianglesOnPlane
    trianglesAsSlopes = []
    trianglesOnPlane = []
    for a in range(len(triangles)):
        trianglesAsSlopes.append([])
        trianglesOnPlane.append([])
        for _ in range(3):
            trianglesAsSlopes[a].append([0, 0, 0])
            trianglesOnPlane[a].append([0, 0, 0])

def createCamera():
    global cameraPlane
    cameraPlane = []
    for a in range(cameraSize):
        cameraPlane.append([])
        for _ in range(cameraSize):
            cameraPlane[a].append(" ")
    #print(cameraPlane)

def slopes(pointA, pointB): #points are arrays of x, y, z
    try:
        slopeYonX = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])
    except ZeroDivisionError:
        slopeYonX = float("inf")
    try:
        slopeZonX = (pointB[2] - pointA[2]) / (pointB[0] - pointA[0])
    except ZeroDivisionError:
        slopeZonX = float("inf")
    return [slopeYonX, slopeZonX]

def trianglesToSlopes():
    global trianglesAsSlopes
    for a in range(len(triangles)):
        for e in range(3):
            triSlopes = slopes(triangles[a][e], cameraPoint)
            #print("triSlopes: " + str(triSlopes))
            trianglesAsSlopes[a][e][0] = triSlopes[0]
            trianglesAsSlopes[a][e][1] = triSlopes[1]

def triSlopesToPlane():
    global trianglesOnPlane
    for a in range(len(trianglesAsSlopes)):
        for e in range(3):
            trianglesOnPlane[a][e][0] = trianglesAsSlopes[a][e][0]
            trianglesOnPlane[a][e][1] = trianglesAsSlopes[a][e][1]

def raster():
    global cameraPlane
    for a in range(cameraSize):
        for e in range(cameraSize):
            for i in range(len(trianglesOnPlane)):
                if pointInTriangle(trianglesOnPlane[i], [(a - cameraCenter[0])/25, (e - cameraCenter[1])/25]):
                    cameraPlane[a][e] = triangles[i][3]

def pointInTriangle(triangle, point): #trinagle - 3 points x, y, z; point - x, y, z
    a = triangleArea(triangle[0], triangle[1], triangle[2])
    a1 = triangleArea(point, triangle[1], triangle[2])
    a2 = triangleArea(triangle[0], point, triangle[2])
    a3 = triangleArea(triangle[0], triangle[1], point)
    fudge = .000001 #maybe use depending on if float rounding errors occur
    if a >= a1 + a2 + a3 - fudge:
        return True
    return False

def triangleArea(p1, p2, p3):
    return .5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))

def cleanCameraOutput():
    buffer = ""
    for a in range(cameraSize):
        for e in range(cameraSize):
            buffer = " " + str(cameraPlane[e][a]) + buffer
        buffer = "\n" + buffer
    return buffer

if __name__ == "__main__":
    key = ""
    while key != "q":
        zeroTriangles()
        #print(trianglesAsSlopes)
        createCamera()
        trianglesToSlopes()
        triSlopesToPlane()
        raster()
        #print(triangles)
        #print(trianglesAsSlopes)
        #print(trianglesOnPlane)
        #print(cameraPlane)
        print(cleanCameraOutput())
        time.sleep(.5)
        key = ""
        try:
            if(keyboard.is_pressed('a')):
                key = "a"
        except:
            pass
        try:
            if(keyboard.is_pressed('d')):
                key = "d"
        except:
            pass
        try:
            if(keyboard.is_pressed('s')):
                key = "s"
        except:
            pass
        try:
            if(keyboard.is_pressed('w')):
                key = "w"
        except:
            pass
        try:
            if(keyboard.is_pressed('q')):
                key = "q"
        except:
            pass
        print(key)
        if key == "a":
            cameraPoint[1] += cameraMoveAmount
        if key == "d":
            cameraPoint[1] -= cameraMoveAmount
        if key == "w":
            cameraPoint[2] += cameraMoveAmount
        if key == "s":
            cameraPoint[2] -= cameraMoveAmount