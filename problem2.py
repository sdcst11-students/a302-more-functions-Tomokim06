#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(x, y, z):
    list = [x,y,z]
    list.sort()
    if x+y < z or x+z < y or z+y < x:
        return 0
    elif (list[0]**2)+(list[1]**2) == (list[2])**2:
        return 2
    elif (list[0]**2)+(list[1]**2) > (list[2])**2:
        return 1
    elif (list[0]**2)+(list[1]**2) < (list[2])**2:
        return 3


def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
