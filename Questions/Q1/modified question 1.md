In this task, we aim to reach the number one from a given integer in as few steps as possible if it is feasible. In each step, we can perform any of the following operations (if they are permitted): 

(a) If the number is divisible by 7, we can subtract 20 
(b) If the number is divisible by 5, we can subtract 16 
(c) If the number is divisible by 2, we can halve it 
(d) We can always choose to subtract 7 

If we start with the number 70, we can reach one in 4 steps by choosing c, d, d, and finally a (70/2=35, 35-7=28, 28-7=21, 21-20=1). If instead, we start with 623, it requires 9 steps: dcccdcdda. In this task, you are required to write functions that return the number of steps but do not present which steps need to be taken.
Write a program that takes an integer as an input parameter and returns the number of steps required to reach 1 according to the above. If no solution is found, the program should return -1. Use a recursive depth first search approach.