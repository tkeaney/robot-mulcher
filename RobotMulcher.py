# CS3100 - Fall 2023 - Programming Assignment 2

# Sources: Introduction to Algorithms, Cormen, https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python,
#################################
import copy
import math
class RobotMulcher:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest tree.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest distance
    # and return that value from this method
    #
    # @return the distance between the closest trees 
    def compute(self, file_data):
        treePairsbyX = []
        for line in file_data:
            x, y = map(float, line.split())
            treePairsbyX.append(Pair(x, y))
        treePairsbyX = sorted(treePairsbyX , key=lambda pair: pair.x)

        return self.closestPair(treePairsbyX)
    def closestPair(self, treePairsbyX):
        length = len(treePairsbyX)
        #brute force base case
        if length <= 3:
            return self.bruteForce(treePairsbyX, float('inf'))

        mid = length//2


        leftX = treePairsbyX[:mid]
        rightX = treePairsbyX[mid: length]
        minDist = min(self.closestPair(leftX), self.closestPair(rightX))

        #create runway
        runway = []
        for pair in treePairsbyX:
            comparing = abs(pair.x - treePairsbyX[mid].x)
            if(comparing < minDist):
                runway.append(pair)
        runway = sorted(runway, key=lambda pair: pair.y)
        for i in range(len(runway)):
            pair1= runway[i]
            for j in range(len(runway)):
                pair2 = runway[j]
                if i != j:
                    dist = self.find_dist(pair1, pair2)
                    if dist < minDist:
                        minDist = dist
        return minDist
    def bruteForce(self, list, minDist):
        for i in range(len(list)):
            point = list[i]
            for j in range(len(list)):
                point2 = list[j]
                if i != j:
                    dist = self.find_dist(point, point2)
                    if dist < minDist:
                        minDist = dist
        return minDist
    def find_dist(self, pair1, pair2):
        return math.sqrt((pair1.x - pair2.x) ** 2 + (pair1.y - pair2.y) ** 2)

#Pair class
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
