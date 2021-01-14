import numpy as np
import sys

def solution(shape, nPizzerias, pizzerias ):

    #using numpy.zeros is easier than building an empy array by hand
    city = np.zeros(shape=(shape, shape), dtype=int)

    #Going through every pizzeria
    for pizzeria in range(0, nPizzerias):
        #Going through every column 
        for column in range(0, len(city)):
            #Going through every row 
            for row in range(0, len(city[column])):
                #Using the absolute value because the value can be negative
                #Getting the difference between the cell y and the pizzeria y
                diffY = abs(column - (pizzerias[pizzeria][0]-1))
                #Getting the difference between the cell x and the pizzeria x
                diffX = abs(row - (pizzerias[pizzeria][1]-1))
                #DiffX + DiffY returns the manhattan distance between the cell and the pizzeria
                #This value should be <= max distance that the delivery guy can travel in the manhattan distance
                if (diffX + diffY <= pizzerias[pizzeria][2]):
                    city[column][row] += 1

    return(max(map(max, city)))


if __name__ == "__main__":
    fileData = []
    for line in sys.stdin:
        fileData.append(line.replace('\n', ''))
    
    shape = int(fileData[0].split(' ')[0])

    nPizzerias = int(fileData[0].split(' ')[1])

    pizzerias = []
    for i in range(1, len(fileData)):
        pizzerias.append([float(x) for x in fileData[i].split(' ')])
    
    print(solution(shape, nPizzerias, pizzerias))
