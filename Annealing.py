import math #or whatever gives euler's number (e)
import random
import nqueens
import decimal

class Simulated_Annealing:

  def __init__(self, T, board, minimum_T_value, decay):
    self.T = float(T)
    self.current = board
    self.min_T = float(minimum_T_value)
    self.decay = float(decay)
      
  #def findDeltaE(self, next_board):#Armond's method that returns next_board.h - self.current.h
    #return next_board.h - self.current.h
    
  def findDeltaE(self, next_board):#Armond's method that returns next_board.h - self.current.h
    deltaE = next_board.h - self.current.h
    return deltaE
    
  def threshold(self,delta_E):#Allen's code that returns math.exp(delta_E / self.T)
    threshold = math.exp(delta_E/self.T)
    return threshold
  
  def decrement_T(self):
    self.T = self.T * self.decay
    
  def annealing(self):#sam's method that does algoritom 
    counter = 0
    complete = False
    while complete == False:
	    self.current.h = nqueens.numAttackingQueens(self.current)
	    if self.current.h == 0:
	      complete = True
	      print ">Solution found no attacking queens!<"
	      break
	    elif (self.T <= self.min_T):
	      complete = True
              print ">Timeout termination final state as above<"
	      break
	    else:
	      next_boards = nqueens.getSuccessorStates(self.current)
	      index = random.randint(0,len(next_boards)-1)
	      next_board = next_boards[index]
	      next_board.h = nqueens.numAttackingQueens(next_board)
	      delta_E = self.findDeltaE(next_board)#The method that armond's writing.
	      if delta_E < 0 and self.current.h > next_board.h:
		self.current = next_board
		self.current.h = nqueens.numAttackingQueens(self.current)
	      else:
		if random.random > self.threshold(delta_E):#The method that Allen's writing.
		  self.current = next_board
		  self.current.h = nqueens.numAttackingQueens(self.current)
	      self.decrement_T()
	    print "run: " + str(counter)
	    self.current.printBoard()
	    print "h value: " +str(self.current.h)
	    print " "
	    counter += 1
    
def main():#Nolan put everyones methods together and made main.
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
  print "##############################"
  print "decay rate is: " + str(decay)
  print "##############################"
  print " "
  print " "
  print " "
  schedule.annealing()
  #print solved_board.h

def FileInputMain():
  return false

main()
