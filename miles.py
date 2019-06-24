"""
A car's miles-per-gollen (MPG) can be calculated with the following
fornula
MPG = Miles driven / Gallen of gass used

Write a program that ask a user the number of miles-per-gollen driven
and the gallen of the gas used. it should calculate the car's MPG and 
display the result.
Starting out with python.

"""

miles = float( input("Enter the miles driven") )
gallen = float( input("Enter the gallen used") )

MPG = miles/gallen

print("The car's miles-per-gollen" + str(MPG) + "Miles")