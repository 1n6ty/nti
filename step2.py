import math
Xa, Ya, Xb, Yb = map(int, input().split()) #Coords of line
N, M = map(int, input().split()) #Count of stars and planets
coordsStars = [list(map(int, input().split())) for i in range(N)] # Coordinates of all stars
coordsPlanets = [list(map(int, input().split())) for i in range(M)] # Cordinates of all planets

def squareOfTriangle(*coords):
    a = math.sqrt((coords[0][0] - coords[1][0]) ** 2 + (coords[0][1] - coords[1][1]) ** 2)
    b = math.sqrt((coords[1][0] - coords[2][0]) ** 2 + (coords[1][1] - coords[2][1]) ** 2)
    c = math.sqrt((coords[2][0] - coords[0][0]) ** 2 + (coords[2][1] - coords[0][1]) ** 2)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def sideDetection(point:list):
    global Xa, Ya, Xb, Yb
    num = (Xb - Xa) * (point[1] - Ya) - (Yb - Ya) * (point[0] - Xa)
    if num > 0:
        return 1
    else:
        return -1
try:
    maxStarLeft = max([squareOfTriangle(i, (Xa, Ya), (Xb, Yb)) for i in coordsStars if sideDetection(i) == 1])
except:
    maxStarLeft = 0
try:
    maxStarRight = max([squareOfTriangle(i, (Xa, Ya), (Xb, Yb)) for i in coordsStars if sideDetection(i) == -1])
except:
    maxStarRight = 0
try:
    maxPlanetLeft = max([squareOfTriangle(i, (Xa, Ya), (Xb, Yb)) for i in coordsPlanets if sideDetection(i) == 1])
except:
    maxPlanetLeft = 0
try:
    maxPlanetRight = max([squareOfTriangle(i, (Xa, Ya), (Xb, Yb)) for i in coordsPlanets if sideDetection(i) == -1])
except:
    maxPlanetRight = 0

print(f"{max([maxPlanetLeft * maxStarRight, maxPlanetRight * maxStarLeft, maxPlanetRight, maxPlanetLeft, maxStarLeft, maxStarRight]):.{2}f}")