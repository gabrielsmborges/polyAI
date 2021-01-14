from __future__ import print_function
import numpy as np
import sys

from numpy.core.fromnumeric import shape




def solution(shape, nPizzerias, pizzerias ):

    #using numpy.zeros is easier than building an empy array by hand
    city = np.zeros(shape=(shape, shape))

    for pizzeria in range(0, nPizzerias):
        for column in range(0, len(city)):
            for row in range(0, len(city[column])):
                diffY = abs(column - (pizzerias[pizzeria][0]-1))
                diffX = abs(row - (pizzerias[pizzeria][1]-1))
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
    