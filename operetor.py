"""
Task
Read two integers and print two lines. The first line should contain integer
 division, a//b . The second line should contain float division, a/b
You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, a
.The second line contains the second integer, b
Output Format

Print the two lines as described above.

Sample Input 0

4
3
"""

a = int(input("Enter your first number"))

b = int(input("Enter your second"))

print ("{0}\n{1}".format(a//b, a/b))

