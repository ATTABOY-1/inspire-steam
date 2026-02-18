# Alvin Njuguna
# 2/17/2026
# program to calculate sine, cosine, tangent of an angle in degrees in a table format

import math
print("Angle\tSine\tCosine\tTangent")
for angle in range(0, 91, 15):
    radians = math.radians(angle)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)
    print(f"{angle}\t{sine:.4f}\t{cosine:.4f}\t{tangent:.4f}")
        

