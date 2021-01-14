from math import inf
import numpy as np




def solution(shape, nPizzerias, pizzerias ):

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
    print("Load File")