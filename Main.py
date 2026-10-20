
import sys
import time
from RobotMulcher import RobotMulcher

fp = open("test2.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the compute function passing in the
# contents of the file
start = time.time()
rm = RobotMulcher()
print(rm.compute(points))
end = time.time()
print("time: "+ str(end-start))
