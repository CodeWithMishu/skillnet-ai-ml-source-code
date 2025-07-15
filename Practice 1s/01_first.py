# Bottle drinking program

bottles = int(input("Enter total water bottles: "))

left_bottle = bottles
day = 1

while left_bottle > 0:
    bottles_per_day = int(input("Enter bottles you drink per day: "))
    if left_bottle >= bottles_per_day:
        drinked_bottle = bottles_per_day
    else:
        drinked_bottle = left_bottle
    
    left_bottle -= drinked_bottle
    
    print(f"Day {day}: Drank {drinked_bottle} bottles. {left_bottle} left.")
    
    if left_bottle == 0:
        print("No more bottles left!")
        break
    day += 1
