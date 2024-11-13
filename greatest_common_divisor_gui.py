import tkinter as tk
from tkinter import messagebox
def gcd( x, y ):
 while y:
  z = x
  x = y
  y = z % y
 return x 
def calculate(): 
	
		num1=int(entry_num1.get())
		num2=int(entry_num2.get()) 
		result = gcd(num1, num2)
		return result_label.config(text="Our result is %d "%(result))
		
		
		  
       

root=tk.Tk()
root.title("GCD")    
title_label=tk.Label(root, text="Greatest Common Divisor calculator")
title_label.pack()
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(padx=5, pady=5)
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(padx=5, pady=5)
calculate_button=tk.Button(root, text="Calculate GCD",command=calculate)
calculate_button.pack(padx=5, pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.geometry("600x300")
root.mainloop()




