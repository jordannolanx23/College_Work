import math #or whatever gives euler's number (e)
import random
import nqueens

class Simulated_Annealing:

  def __init__(self, T, board, minimum_T_value, decay):
    self.T = float(T)
    self.current = board
    self.min_T = float(minimum_T_value)
    self.decay = float(decay)
      
  #def findDeltaE(self, next_board):#Armond's method that returns next_board.h - self.current.h
    #return next_board.h - self.current.h
    
  def findDeltaE(next_board):#Armond's method that returns next_board.h - self.current.h
    currentH = self.current.h
    nextH = nqueens.numAttackingQueens(next_board)
    deltaE = nextH - currentH

    return deltaE
  
  #def threshold(self, delta_E):#Allen's code that returns math.exp(delta_E / self.T)
    #return math.exp(delta_E / self.T)
    
  def threshold(delta_E):#Allen's code that returns math.exp(delta_E / self.T)
    threshold = math.e.exp(delta_E/self.T)
    return threshold
  
  def decrement_T(self):#Nolan's method that decrements T and doesn't return anything.
    self.T *= self.decay
    
  def annealing(self, original_call):
    complete = False
    self.current.h = nqueens.numAttackingQueens(self.current)
    if (self.T <= self.min_T):
      complete = True
    else:
      next_boards = nqueens.getSuccessorStates(self.current)#I might not be calling this right, but hopefully you get the idea
      next_board = next_boards[random.randint(0,len(next_boards)-1)]
      next_board.h = nqueens.numAttackingQueens(next_board)
      delta_E = self.findDeltaE(next_board)#The method that armond's writing.
      if delta_E > 0:
        self.current = next_board
      else:
        if random.random > self.threshold(delta_E):#The method that Allen's writing.
          self.current = next_board
      self.decrement_T()#The method that Nolan's already written. Nolan, please correct the syntax of this line if incorrect.
      self.annealing(False)
    if original_call:
      self.current.printBoard()
      print self.current.h
    
def ConsoleMain():#This main method is primarily for testing. The one that outputs to a file is below.
  stdout = "Please pick from the following options to determine the board size:"
  stdout += "\n a) 4\n b) 8\n c) 16\n>: "
  response = ""
  while response not in ["a","A","b","B","c","C"]:
    response = raw_input(stdout)
    if response not in ["a","A","b","B","c","C"]:
      print "*Incorrect input. Please enter the letter that corresponds to your choice\n"
  if response in ["a","A"]:
    board = nqueens.Board(4)
  elif response in ["b","B"]:
    board = nqueens.Board(8)
  else:
    board = nqueens.Board(16)
  board.rand()
  stay_in_loop = True
  while stay_in_loop:
    try:
      T = float(raw_input("Enter a value for T: "))
      min_T = float(raw_input("Enter a value for threshold of termination: "))
      decay = float(raw_input("Enter a value for the rate of decay: "))
      print ""
      stay_in_loop = False
    except:
      print "Invalid value entered. Try again.\n"
  schedule = Simulated_Annealing(T, board, min_T, decay)
  print decay
  schedule.annealing(True)
  #print solved_board.h

def FileInputMain():
  return false

def Main():
  response = ""
  stdout = "Do you want to interact with this program through the console (a),"
  stdout += "\nor have it's output written to a file (b)?\n>:"
  while response not in ["a","A","b","B"]:
    response = raw_input(stdout)
    if response not in ["a","A","b","B"]:
      print "*Incorrect input. Please enter the letter that corresponds to your choice\n"
  if response in ["a","A"]:
    ConsoleMain()
  else:
    FileInputMain()

Main()
