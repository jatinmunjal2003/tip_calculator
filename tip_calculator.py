print("welcome to the tip calculator.")
bill=float(input("what was the total bill? $"))
percentage_of_bill=int(input("what percentage tip would you like to give? 10,12 or 15?"))
split=int(input("how many people to get split the bill?"))
tip=bill / 100 * percentage_of_bill
paying=tip+bill
spliting=float(paying/split)
print("Each person should pay: $" ,round(spliting,2))