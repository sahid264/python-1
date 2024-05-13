print("welcome to tip calculator")
bill = float (input("what was the total bill ?"))
tip = int(input("how much tip would you like to give ? 10,12, or 15 ?"))
people = int(input("how many people to split the bill ?"))

total_bill = tip / 100 * bill + bill

      #other way
# tip_as_percent = tip/100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount 

bill_per_people = total_bill / people
final_amt = round(bill_per_people , 2)
print(f"Each person should pay : {final_amt}")



