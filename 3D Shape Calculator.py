print("Welcome To The 3D Shape Volume Calculator")

x = int(input("Enter a number "))
y = int(input("Enter a number "))
z = int(input("Enter a number "))

import cube
c = cube.cubetwonos(x)
print("The Volume Of The Cube Is:",c)

import rect
r = rect.prismtwonos(x,y,z)
print("The Volume Of The Rectangular Prism Is:",r)

import sphere
s = sphere.spheretwonos(x,y)
print("The Volume Of The Sphere Is:",s)

import cylin
C = cylin.cylindertwonos(x,y)
print("The Volume Of The Cylinder Is:",C)


    
