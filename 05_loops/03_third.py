
bottles = int(input("Enter the no. of bottles:"))
drinked_bottle = int(input("Enter the no. of bottles drink per day:"))
while True:
    drank = drinked_bottle
    print(f"Day {count} : Drank {drinked_bottle} . {bottles-drinked_bottle} left")

# when bottles less than 50 print only 40 to 50 left andd when 0 refill the stock 
