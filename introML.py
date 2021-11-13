import numpy as np
import matplotlib.pyplot as plt

#1
data = np.loadtxt(open("iris.csv", "rb"), delimiter=",", skiprows=1)
print("intial data")
print(data.shape)
#print(data)
print(" ")

#2
#matplot first 2 colums of data
plt.scatter(data[0:,0], data[0:,1])
#plt.plot(data)
plt.show()

#3
data_stack = np.loadtxt(open("iris_stack.csv", "rb"), delimiter=",", skiprows=1)
#print(data_stack)
print("stack_shape: " + str(data_stack.shape))

#4
data = np.vstack((data,data_stack))
print("vertical stack data")
#print(data)
print("stack_shape: " + str(data.shape))
print(" ")

#5
print("reshape data")
temp = data.view()
print("data_size: " + str(data.size))
size = data.size
data_single_row = np.reshape(temp,(1,size) )
print("single_row_shape: " + str(data_single_row.shape))
#print(data_single_row)

#6
plt.scatter(data[0:,1] , data[0:, 0])
#plt.plot(data)
plt.show()



