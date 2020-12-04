import numpy
width = int(input ("Enter width of rectangle: :"))
height = int(input ("Enter height of rectangle: "))
perimeter = 2*(width+height)
print(f"The perimter is: " +str(perimeter))
area = width*height
print(f"The area is: "+str(area))
print("Do you want to calculate the volumn of a rectagular space? ")

depth = int(input ("Enter depth of rectangular space: "))
volumn = width*height*depth
print(f"The volumn of the rectangular space is: "+str(volumn))
