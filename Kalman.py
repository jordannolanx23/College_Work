import math
import random

#To implement 1D kalman filter mean and var values will be numeric and not an array

def initial():
    x = random.uniform(1,10)
    y = random.uniform(1,10)
    newbelief = [x,y]
    return newbelief

def predict(list, action):
    motionUN = 2.0

    x = list[0] + action
    y = list[1] + motionUN

    newbelief = [x,y]
    return newbelief

def update(list, measurment):
    measurUN = 4.0

    x = ((measurUN * list[0]) + (list[1] * measurment))/(list[1] + measurUN)
    y = 1/((1/list[1])+(1/measurUN))

    newbelief = [x,y]
    return newbelief

def main():
    # un- coment bellow for a random initial state
    #belief = initial()

    #initial values for update and prediction
    up = [0.0,0.0]
    pre = [0.0,0.0]
    # measurment and motion list
    measurments = [5.0,6.0,7.0,9.0,10.0]
    motion = [1.0,1.0,2.0,1.0,1.0]

    belief = [0.0,1000.0]
    print("Inital state: " +str(belief))

    #main loop threw motions to effect agent belief.
    for i in range(len(motion)):
        move = motion[i]
        measur = measurments[i]

        up = update(belief, measur)
        print('Update: ' + str(up))
        belief = up

        pre = predict(belief, move)
        print('Predict: ' + str(pre))
        belief = pre

main()