def gcd(x, y):
	while y : 
		x=y
		y=x%2
		return x 
		
    
    
print("------------------------------------------------------------------")    

number=int(input("Enter the first integer\n"))
number2=int(input("Enter the second integer \n"))

print("The greatest common divisor of the integers you have just entered is %d"%(gcd(number,number2)))
