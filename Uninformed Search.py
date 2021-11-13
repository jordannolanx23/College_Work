# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:31:06 2018
Uninformed search for AI.
@author: jorda
"""
import random

class Node:
    def __init__(self,data):
        self.parent
        self.children
        self.value = data
        
    def getChildren(self,location):
        children = []
        fill = 0
        y = location[0]
        x = location[1]
        #down
        if(location[y+1][x] == 1):
            fill+=1
        else:
            children.append([y+1,x])
        #right
        if(location[y][x+1] == 1):
            fill+=1
        else:
            children.append([y,x+1])
        #left
        if(location[y][x-1] == 1):
            fill+=1
        else:
            children.append([y,x-1])
        #up
        if(location[y-1][x] == 1):
            fill+=1
        else:
            children.append([y-1,x])
        return children
        
    def expandNode(self,children):
        self.children = children
        for x in range(len(children)):
            children[x].parent = self
            
    def search(self,start,goal):
        node = start
        open_list = []
        closed_list = []
        key = input("enter b for BFS: enter d for DFS")
        if key == "b":
            while node != goal:
                if open_list.empty == True:
                    open_list = node.children
                node = open_list.pop()
                if node == goal:
                    return closed_list
                closed_list.add(node)
                
                
            

class GridIO:
    def __init__(self):
        self.open_list = []
        self.closed_list = []
  
    def ReadGrid(self,filename):
		opened_file = open(filename, "r+")
		file_rows = opened_file.readlines()

		number_of_rows = len(file_rows)
		number_of_cols = len(file_rows[0].split())

		return_array = [[0 for x in range(number_of_cols)] for y in range(number_of_rows)]

		y = 0
		for row in file_rows:
			row_elements = row.split()
			x = 0
			for element in row_elements:
				return_array[y][x] = int(element)
				x += 1
			y += 1

		return return_array

    def WriteGrid(self,filename, grid):
		file_path = filename
		open(file_path, "w").write("")

		number_of_rows = len(grid)
		number_of_cols = len(grid[0])

		for y in range(number_of_rows):
			for x in range(number_of_cols):
				open(file_path, "a").write(str(grid[y][x]) + " ")
			open(file_path, "a").write("\n")
		print ">:write successful"

    def ModifyGrid(self,grid, location, value):
		y = location[0]
		x = location[1]

		grid[y][x] = value
		return grid

    def FindAllFreeLocs(self,grid):
		return_list = []

		number_of_rows = len(grid)
		number_of_cols = len(grid[0])

		for y in range(number_of_rows):
			for x in range(number_of_cols):
				if grid[y][x] == 0:
					return_list.append([y, x])
		return return_list
    
    def getChildren(self,grid,location):
        children = []
        fill = 0
        y = location[0]
        x = location[1]
        #down
        if(grid[y+1][x] == 1):
            fill+=1
        else:
            children.append([y+1,x])
        #right
        if(grid[y][x+1] == 1):
            fill+=1
        else:
            children.append([y,x+1])
        #left
        if(grid[y][x-1] == 1):
            fill+=1
        else:
            children.append([y,x-1])
        #up
        if(grid[y-1][x] == 1):
            fill+=1
        else:
            children.append([y-1,x])
        return children
        
    def search(self,grid,start,goal):
        node = start
        open_list = []
        closed_list = []
        children = []
        key = int(input("enter 1 for BFS: enter 0 for DFS: "))
        
        if key == 1:
            while node != goal:
                #if list is empty it needs data
                if len(open_list) == 0:
                    open_list = self.getChildren(grid,node)

                #this happens every loop////
                node = open_list[0]
                open_list.remove(open_list[0])
                closed_list.append(node)
                #/////////////////////////////#

                if node == goal:
                    return closed_list
                    break

                # get childreen
                if len(open_list) >= 0:
                    children.append(self.getChildren(grid,node))
                    # check if childreen are in open or closed
                    for c in range (len(children)):
                        # if childreen are not in ethier open or close add to open list
                        if children[c] in open_list is False and children[c] in closed_list is False:
                            open_list.append[children[c]]

        if key == 0:
            while node != goal:
                if len(open_list) == 0:
                    open_list = self.getChildren(grid,node)
                node = open_list.pop()
                closed_list.append(node)
                if node == goal:
                    return closed_list
                    break
                if len(open_list) >= 0:
                    children.append(self.getChildren(grid,node))
                    for c in range (len(children)):
                        if children[c] in open_list == False and children[c] in closed_list == False:
                            open_list.append[children[c]]


def Main():
   #read and show grid layout
   grid = GridIO()
   layout = grid.ReadGrid("practiceGrid.txt")
   print(layout)
   print(" ")
   
   #put start location visually on grid
   y = int(input("Enter grid starting location y: "))
   x = int(input("Enter grid starting location x: "))
   if layout[y][x] == 1:
       print("ERORR: VALUE AT LOCATION IS NON TRAVERSABLE! ")
       exit
   start = [y,x]
   print("start: " + str(start))
   grid.ModifyGrid(layout,start,"S")
   
   #put goal location visually on grid
   y = int(input("Enter grid goal location y: "))
   x = int(input("Enter grid goal location x: "))
   if layout[y][x] == 1:
       print("ERORR: VALUE AT LOCATION IS NON TRAVERSABLE! ")
       exit
   goal = [y,x]
   print("goal: " + str(goal))
   grid.ModifyGrid(layout,goal,"G")
   
   #test = grid.getChildren(layout,start)
   #print(test)
   #search using DFS AND BFS
   path = grid.search(layout,start,goal)
   print(path)
   
   
   
   #free = grid.FindAllFreeLocs(layout)
   #print(free)
   #for x in range(len(free)):
   #    grid.ModifyGrid(layout,free[x],random.randint(2,9))
   #print(" ")
   #print(layout)
   #grid.WriteGrid("outputIO.txt",layout)         

Main()