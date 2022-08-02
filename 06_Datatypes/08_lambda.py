#lambda argument: expression

add10 = lambda x: x + 10
print(f"lambda x: x + 10 \nadd10(5) result:{add10(5)}")


mult = lambda x,y: x * y
print(f"\n\nlambda x,y: x * y \nmult(2, 7) result:{mult(2, 7)}")

#---------------------------------

points2D = [ (11,3), (14, 22), (1, 2), (31, 2)]
points2D_sorted = sorted(points2D)
print(f"points2D: {points2D}\npoints2D_sorted:{points2D_sorted}")
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(f"sorted(points2D, key=lambda x: x[1]): \npoints2D_sorted:{points2D_sorted}")

points2D_sorted = sorted(points2D, key=lambda x: x[0]+x[1])
print(f"sorted(points2D, key=lambda x: x[0]+x[1]): \npoints2D_sorted:{points2D_sorted}")

