import tkinter as tk
import functools
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

def add_numbers():
    text = entry.get().replace(",", " ")  
    parts = text.split()
    try:
        numbers = [float(x) for x in parts]  
        total = sum(numbers)
        result.config(text=f"Sum: {total}")
    except ValueError:
        result.config(text="Enter valid numbers!")

def subtract_numbers():
    text = entry.get().replace(",", " ")
    try:
        numbers = [float(x) for x in text.split()]
        result_val = numbers[0] - sum(numbers[1:])
        result.config(text=f"Result: {result_val}")
    except:
        result.config(text="Enter valid numbers!")

def multiply_numbers():
    text = entry.get().replace(",", " ")
    numbers = [float(x) for x in text.split()]
    result_val = math.prod(numbers)  
    result.config(text=f"Result: {result_val}")

def divide_numbers():
    text = entry.get().replace(",", " ")
    try:
        numbers = [float(x) for x in text.split()]
        result_val = functools.reduce(lambda x, y: x / y, numbers)
        result.config(text=f"Result: {result_val}")
    except:
        result.config(text="Enter valid numbers!")

def factorial_number():
    try:
        num = int(entry.get())
        result_val = math.factorial(num)
        result.config(text=f"Factorial: {result_val}")
    except:
        result.config(text="Enter a valid integer!")

label = tk.Label(root, text="Calculator", font=("Arial", 20))
label.grid(row=0, column=0, columnspan=4, pady=10)

entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_plus = tk.Button(root, text="+", font=("Arial", 20), command=add_numbers)
button_plus.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

button_minus = tk.Button(root, text="-", font=("Arial", 20), command=subtract_numbers)
button_minus.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

button_mul = tk.Button(root, text="×", font=("Arial", 20), command=multiply_numbers)
button_mul.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

button_div = tk.Button(root, text="÷", font=("Arial", 20), command=divide_numbers)
button_div.grid(row=2, column=3, sticky="nsew", padx=5, pady=5)

button_fac = tk.Button(root, text="!", font=("Arial", 20), command=factorial_number)
button_fac.grid(row=3, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

result = tk.Label(root, text="Result: ", font=("Arial", 15))
result.grid(row=4, column=0, columnspan=4, pady=10)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

