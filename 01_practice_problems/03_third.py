# Restaurant Tip simulator give the tip according to the amount of bill 
# 1 split the bill in number of friend and print each person bill 
# 2 give the tip — 10 % to 50 % of bill amount
import random
print("Welcome to Restaurant Tip simulator :")

Total_bill = float(input("Enter the amount of total bill :"))
num_friends = int(input("Enter no. of person you all are :"))
split_amount = Total_bill/num_friends
for i in range(num_friends):
    print(f" {i}st friends bill amount: {split_amount}")

Tip = (random.randint(10,50)/100)*split_amount
print(f"{Tip} ! jaldi se itni tip dedo varna jaane nhin dunga ")