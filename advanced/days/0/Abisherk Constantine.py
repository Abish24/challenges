#Import
import math

#Measurements
line1 = 2546375247
line2 = 45987482082

#Hypotenuse
line1_sq = line1*line1
line2_sq = line2*line2
line3 = line1_sq + line2_sq
hypo = math.isqrt(line3)

#Area
sq = line1*line2
area = sq/2

#Perimeter
perimeter = line1 + line2 + hypo

#Answer
print(area)
print(perimeter)
