# This program will allow you to convert Degrees to Radians to Decimal Degrees etc.
import math
import cmath

# Display start of program
print("-------------------")
print("CONVERT...")
# Display options
print("1. DEGREES > RADIANS")
print("2. DEGREES > DMS")
print("3. RADIANS > DEGREES")
print("4. RADIANS > DMS")
print("5. DMS > DEGREES")
print("6. DMS > RADIANS")
print("7. <QUIT>")

# Make user choose an option
print("-------------------")
label = int(input("Pick conversion (1-7): "))
# Automatically quits when input is 7 or outside of boundaries

# Work out all the formulas
if label == 1:
    degree = int(input("Enter value of DEGREE: "))
    radian = degree*(math.pi/180)
    print(degree, " degrees equals ", radian, "radians")

if label == 2:   
    degree = float(input("Enter value of DEGREE: "))
    seconds_rounding = int(input("Rounding on SECONDS:  "))
    minutes = degree%1.0*60
    seconds = minutes%1.0*60
    print(degree, "degrees equals", math.floor(degree), "degrees", math.floor(minutes), "minutes and", round(seconds, seconds_rounding), "seconds")

if label == 3:
    radian = int(input("Enter value of RADIAN: "))
    degree = radian*(180/math.pi)
    print(radian, " radians equals ", degree, "degrees")

if label == 4:
    radian = float(input("Enter value of RADIAN: "))
    seconds_rounding = int(input("Rounding on SECONDS:  "))
    degree = radian*(180/math.pi)
    minutes = degree%1.0*60
    seconds = minutes%1.0*60
    print(radian, "radians equals", math.floor(degree), "degrees", math.floor(minutes), "minutes and", round(seconds, seconds_rounding), "seconds")

if label == 5:
    d = int(input('Enter value of Degrees: '))
    m = int(input("Enter value of Minutes: "))
    s = int(input("Enter value of Seconds: "))
    degree = (d + (m/60) + (s/3600))
    print(d, "degrees,", m, "minutes and", s, "seconds equal", degree, "degrees")
 
if label == 6:
    d = int(input('Enter value of Degrees: '))
    m = int(input("Enter value of Minutes: "))
    s = int(input("Enter value of Seconds: "))
    degree = (d + (m/60) + (s/3600))
    radian = degree*(math.pi/180)
    print(d, "degrees,", m, "minutes and", s, "seconds equal", radian, "radians")    


print("-------------------")