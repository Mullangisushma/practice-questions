"""
The program is supposed to calculate the sum of  distance between three points from each other.

For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6

Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2"""

import math
x1,y1=1,1
x2,y2=2,4
x3,y3=3,6

diff1=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
diff2=math.sqrt(math.pow((x3-x2),2)+math.pow((y3-y2),2))
diff3=math.sqrt(math.pow((x3-x1),2)+math.pow((y3-y1),2))
print(round(diff1,2),round(diff2,2),round(diff3,2))