from collections import deque

MapList = []
with open("puzzle.txt", "r") as data:
    for t in data:
        Line = t.strip()
        MapList.append(Line)

WallSet = set()
OpenSet = set()
for y, m in enumerate(MapList):
    for x, c in enumerate(m):
        if c == "#":
            WallSet.add((x,y))
        elif c == ".":
            OpenSet.add((x,y))
        elif c == "E":
            Endpoint = (x,y)
            OpenSet.add((x,y))
        elif c == "S":
            Startpoint = (x,y)
            OpenSet.add((x,y))

SpaceScore = {}
ImperialCore = set()
ImperialFrontier = deque()
ImperialFrontier.append((0,Startpoint))
Directions = [(0,1),(0,-1),(1,0),(-1,0)]
while ImperialFrontier:
    Distance, Location = ImperialFrontier.pop()
    if Location in ImperialCore:
        continue
    SpaceScore[Location] = Distance
    ImperialCore.add(Location)
    if Location == Endpoint:
        break
    X,Y = Location

    for DX,DY in Directions:
        NX,NY = X+DX,Y+DY
        NewLoc = (NX,NY)
        if NewLoc in ImperialCore or NewLoc not in OpenSet:
            continue
        ImperialFrontier.append((Distance+1,NewLoc))


CheatDistances = [(2,0),(-2,0),(0,2),(0,-2),(1,1),(-1,1),(1,-1),(-1,-1)]
for dx in range(-20,21):
    for dy in range(-20,21):
        ManDist = abs(dx)+abs(dy)
        if ManDist > 20 or ManDist < 3:
            continue
        CheatDistances.append((dx,dy))

Part1Answer = 0
Part2Answer = 0
for Location in ImperialCore:
    X, Y = Location
    HomeScore = SpaceScore[Location]
    for DX, DY in CheatDistances:
        NX,NY = X+DX,Y+DY
        NewLoc = (NX,NY)
        if NewLoc not in ImperialCore:
            continue
        PhasePointScore = SpaceScore[NewLoc]
        CheatLength = abs(DX) + abs(DY)
        if PhasePointScore - HomeScore >= 100 + CheatLength:
            Part2Answer += 1
            if CheatLength == 2:
                Part1Answer += 1

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")