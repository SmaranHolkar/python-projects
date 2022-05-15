import csv
import tkinter
from tkinter import *
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
 
window=Tk()
c = CurrencyRates()

#def function each on it gets the input and then it coverts the amount and then it converts it in to a string and then it outputs it.

def button_clicked():
	entered_text = entry1.get()
	
	output = c.convert('GBP', 'USD', float(entered_text))
	converted_string=(str(output))
	
	manipulated_text= "your converted money = " + converted_string
	output_text.delete(0.0,END)
	output_text.insert(END, manipulated_text)

def eur_GBP():
	entered_text = entry1.get()
	
	output = c.convert('EUR', 'GBP', float(entered_text))
	converted_string=(str(output))
	
	manipulated_text= "your converted money = " + converted_string
	output_text.delete(0.0,END)
	output_text.insert(END, manipulated_text)

def india():
	entered_text = entry1.get()
	
	output = c.convert('USD', 'GBP', float(entered_text))
	converted_string=(str(output))
	
	manipulated_text= "your converted money = " +converted_string
	output_text.delete(0.0,END)
	output_text.insert(END, manipulated_text)

Label(window, text="Enter amount").grid(row=1, column=0, sticky=W)
#if you press any of the desired conversions it calls the appropriate functions. 

Button(window, text="GBP-USD", width=5, command=button_clicked).grid(row=3, column=0, sticky=W)
Button(window, text="Eur-GBP", width=5, command=eur_GBP).grid(row=3, column=1, sticky=W)
Button(window, text="USD-GBP", width=5, command=india).grid(row=3, column=3, sticky=W)


Label(window, text="Enter amount").grid(row=1, column=0, sticky=W)
entry1 = Entry(window, width=15, bg="light blue")
entry1.grid(row=2, column=0, columnspan=2, sticky=W)
output_text= Text(window, width=20, height=6, wrap=WORD, background="lightblue")
output_text.grid(row=4, column=0, columnspan=2, sticky=W)

with open('data.csv',newline='') as csvfile:
	reader= csv.reader(csvfile)
	dataset_ =list(reader)
	dataset = dataset_[1:25]
	dataset.reverse()
	
for i in dataset:
	print(i) 

date=[]
price=[]
count=0

for i in dataset:
	date.append(dataset[count][0])
	price.append(dataset[count][1])
	count+=1

for i in price:
	print(i)

plt.plot(date, price)
plt.show()

window.mainloop()