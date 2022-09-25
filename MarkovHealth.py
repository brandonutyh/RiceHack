from collections import defaultdict as patientList
import random
import matplotlib.pyplot as plt 
import numpy as np

#PROBABILITY
dataExpected = [[0.6081, 0.3919, 0],
                [0.0497, 0.9441, 0.0062],
                [0, 0.0439, 0.9561]]

patientDict= [["I", 10], ["S", 10], ["D", 10]]
countDict =  [["I",0], ["S",0], ["D", 0]]

#helper method to classify one person based on the given key INT they start at
def simulateExpected(lst, pList, cList, num):
    #generate random number for that person
        rand_num = random.random()
        print("the random number is", rand_num)
#iterates through each column to check if the probability falls into that range
        prob=0
        length= len(lst[num])
    #iterate through each element in the columns
        for col in range(length):
            #update the probability
            prob += lst[num][col]
            #if the probability falls into the range, then increment the counter by 1
            if rand_num<= prob:
                cList[col][1]+=1
                return (cList)

        #return (cList)

 #create main method that will loop through the number of patients for each state
#so add in a for loop to iterate through each state, and another for loop to test what state each patient lands in

def totalExpected(lst, pList, cList):
    #iterate through each state in the patientDict
    num =0        
    for state in pList:
        #test what state each individual will be in next, repeat for the number of patients there are
        for patient in range(state[1]):
            simulateExpected(lst, pList, cList, num)
        num+=1
    print(cList)

#print (simulateExpected(dataExpected, patientDict, countDict, 0))
print (totalExpected(dataExpected, patientDict, countDict))
print(countDict)

#plotting the graph
#n=4
#r = np.arange(n)

# x axis values 
x = ["I","S","D"] 
# corresponding y axis values 
end = [countDict[0][1],countDict[1][1],countDict[2][1]] 
start = [patientDict[0][1], patientDict[1][1], patientDict[2][1]]
# plotting the points  

X_axis=np.arange(len(x))
  
plt.bar(X_axis - 0.2, start, 0.4, label = 'start')
plt.bar(X_axis + 0.2, end, 0.4, label = 'end')

plt.xticks(X_axis, x)
# naming the x axis 
plt.xlabel('States') 
# naming the y axis 
plt.ylabel('Frequency') 
    
# giving a title to my graph 
plt.title('Patient changes in hospital stages over time') 
# plt.grid(linestyle='--')
plt.legend()
# function to show the plot 
plt.show() 
