from Areas import area_of_circle, area_of_rectangle, area_of_square
from Volume import volume_of_cuboid, volume_of_cylinder, volume_of_cube

# Calculate the area
from Areas import area_of_circle, area_of_rectangle, area_of_square

print("The area of a circle with radius of 5 is {}".format(area_of_circle(5)))
print(
    "The area of a rectangle with length of 6 and width of 7 is {}".format(
        area_of_rectangle(6, 7)
    )
)
print("The area of a square with side length of 8 is {}".format(area_of_square(8)))
print()

# Calculate Volume
print(
    "The volume of a cylinder with radius of 5 and height of 10 is {}".format(
        volume_of_cylinder(5, 10)
    )
)
print(
    "The volume of a cuboid with length of 6, width of 7 and height of 10 is {}".format(
        volume_of_cuboid(6, 7, 10)
    )
)
print("The volume of a cube with side length of 8 is {}".format(volume_of_cube(8)))
