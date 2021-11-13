import math

def distance(point2,point1):
    x2 = point2[0]
    y2 = point2[1]
    x1 = point1[0]
    y1 = point1[1]
    dx = x2 - x1
    dy = y2 - y1
    dx = dx * dx
    dy = dy * dy
    distance = math.sqrt(dx+dy)
    return distance

class Node:
    def __init__(self,data,parent,path,heuristic):
        self.parent = parent
        self.value = data
        self.g = path
        self.h = heuristic
        self.f = self.g + self.h

    def expandNode(self,child):
        self.children.append(child)

    def expandPath(self,node):
        if (node in self.path) == False:
            self.path.append[node]

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setPathCost(self,goal):
        y1 = goal[0]
        x1 = goal[1]
        y2 = self.value[0]
        x2 = self.value[1]
        path = (abs(y2-y1)+abs(x2-x1))
        self.g = path
        self.f = self.g + self.h

    def getChildren(self,location,grid):
        children = []
        fill = 0
        y = location[0]
        x = location[1]
        #down
        if(self.value[y+1][x] == 1):
            fill+=1
        else:
            children.append([y+1,x])
        #right
        if(self.value[y][x+1] == 1):
            fill+=1
        else:
            children.append([y,x+1])
        #left
        if(self.value[y][x-1] == 1):
            fill+=1
        else:
            children.append([y,x-1])
        #up
        if(self.value[y-1][x] == 1):
            fill+=1
        else:
            children.append([y-1,x])
        return children

class GridIO:
    def __init__(self):
        self.value = []
        self.open_list = []
        self.closed_list = []

    def ReadGrid(self,filename):
        opened_file = open(filename, "r+")
        file_rows = opened_file.readlines()

        number_of_rows = len(file_rows)
        number_of_cols = len(file_rows[0].split())

        self.value = [[0 for x in range(number_of_cols)] for y in range(number_of_rows)]

        y = 0
        for row in file_rows:
            row_elements = row.split()
            x = 0
            for element in row_elements:
                self.value[y][x] = int(element)
                x += 1
            y += 1

        #return return_array

    def WriteGrid(self,filename):
        file_path = filename
        open(file_path, "w").write("")

        number_of_rows = len(self.value)
        number_of_cols = len(self.value[0])

        for y in range(number_of_rows):
            for x in range(number_of_cols):
                open(file_path, "a").write(str(self.value[y][x]) + " ")
            open(file_path, "a").write("\n")
        print(">:write successful")

    def ModifyGrid(self,location, value):
        y = location[0]
        x = location[1]

        self.value[y][x] = value

    def FindAllFreeLocs(self):
        return_list = []

        number_of_rows = len(self.value)
        number_of_cols = len(self.value[0])

        for y in range(number_of_rows):
            for x in range(number_of_cols):
                if self.value[y][x] == 0:
                    return_list.append([y, x])
        return return_list

    def display(self):
        for row in self.value:
            printRow = ""
            for element in row:
                printRow += str(element) + " "
            print(printRow)

    def getChildren(self,location):
        children = []
        fill = 0
        y = location[0]
        x = location[1]
        #down
        if(self.value[y+1][x] == 1):
            fill+=1
        else:
            children.append([y+1,x])
        #right
        if(self.value[y][x+1] == 1):
            fill+=1
        else:
            children.append([y,x+1])
        #left
        if(self.value[y][x-1] == 1):
            fill+=1
        else:
            children.append([y,x-1])
        #up
        if(self.value[y-1][x] == 1):
            fill+=1
        else:
            children.append([y-1,x])
        return children

    def informedSearch(self,start,goal):
        open_list = []
        closed_list = []
        children = []
        initial = Node(start,0,0,distance(start,goal))
        open_list.append(initial)
        node = start

        key = int(input("enter 1 for greedy: enter 2 for A*: "))
        if key == 1:
            while node != goal:
                if len(open_list) == 0:
                    print("ERROR: open list empty")
                    return -1
                #sort the list based on the heuristic node value
                open_list.sort(key=lambda x: x.h, reverse=False)
                node = open_list.pop(0).value
                if (node in closed_list) == False:
                    closed_list.append(node)
                if node == goal:
                    return closed_list
                if node != goal:
                    children = []
                    children = self.getChildren(node)
                    for x in range (len(children)):
                        if(children[x] in open_list and children[x] in closed_list) == False:
                            dist = distance(children[x],goal)
                            n = Node(children[x],node,0,dist)
                            open_list.append(n)
                            if children[x] in closed_list:
                                open_list.pop()
        if key == 2:
            while node != goal:
                if len(open_list) == 0:
                    print("ERROR: open list empty")
                    return -1
                #sort the list based on f node value
                open_list.sort(key=lambda x: x.f, reverse=False)
                node = open_list.pop(0).value
                if (node in closed_list) == False:
                    closed_list.append(node)
                if node == goal:
                    return closed_list
                if node != goal:
                    children = []
                    children = self.getChildren(node)
                    for x in range (len(children)):
                        if(children[x] in open_list and children[x] in closed_list) == False:
                            dist = distance(children[x],goal)
                            n = Node(children[x],node,0,dist)
                            n.setPathCost(goal)
                            open_list.append(n)
                            if children[x] in closed_list:
                                open_list.pop()




def Main():
    #read and show grid layout
    grid = GridIO()
    grid.ReadGrid("practiceGrid.txt")
    print(grid.value)
    print(" ")
    grid.display()

    #select start location
    y = int(input("Enter grid starting location y: "))
    x = int(input("Enter grid starting location x: "))
    if grid.value[y][x] == 1:
        print("ERORR: VALUE AT LOCATION IS NON TRAVERSABLE! ")
        return -1
    start = [y,x]
    print("start: " + str(start))
    print(" ")
    #grid.ModifyGrid(start,"S")

    #select goal location
    y = int(input("Enter grid goal location y: "))
    x = int(input("Enter grid goal location x: "))
    if grid.value[y][x] == 1:
        print("ERORR: VALUE AT LOCATION IS NON TRAVERSABLE! ")
        return -1
    goal = [y,x]
    print("goal: " + str(goal))
    print(" ")
    #search using greedy or A*
    path = grid.informedSearch(start,goal)
    if path == -1:
        print("No Soulution found: ")
        return -1
    print(" ")
    #modify the grid to display start,end and path locations
    for x in range(len(path)):
        grid.ModifyGrid(path[x],"*")
    grid.ModifyGrid(start,"S")
    grid.ModifyGrid(goal,"G")
    #write grid to a file and display heuristic used.
    print("Solution found")
    print("Number of states expanded: " + str(len(path)))
    print("path: " +str(path))
    print("Heuristic: The distance formula sqrt((x2-x1)^2 + (y2-y1)^2)")
    print(" ")
    grid.display()
    grid.WriteGrid("outputSearch.txt")


Main()

