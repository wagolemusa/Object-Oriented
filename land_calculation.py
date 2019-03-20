# One area of land is eqvaent to 43,560 squere feat. write a program that
# ask the a user to enter the total squere feat in a tract of land and 
# calculate the number of acres in the tract.
# Hint: Divide ths amount entered by 43,560 to get the number of acres.
landsize = 43560

UsertotalSqureFeat =  int( input("Please anter the total amount of the squere feat") )


numberOfarea = ( UsertotalSqureFeat /  landsize )  * 1

print ("Number of acres: " + format(numberOfarea, ".2f"))