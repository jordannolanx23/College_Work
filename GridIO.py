# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:59:22 2018

@author: Nolan Jordan
"""
import random
from random import randint

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


def Main():
   grid = GridIO()
   layout = grid.ReadGrid("practiceGrid.txt")
   print(layout)
   print(" ")
   free = grid.FindAllFreeLocs(layout)
   print(free)
   for x in range(len(free)):
       grid.ModifyGrid(layout,free[x],random.randint(2,9))
   print(" ")
   print(layout)
   grid.WriteGrid("outputIO.txt",layout)         

Main()
        
        
        
        
        