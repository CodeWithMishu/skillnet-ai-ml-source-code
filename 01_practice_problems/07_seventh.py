# Coffee Machine Program
# Based on the requirements and menu specifications

# Coffee Machine Resources
resources = {
    "water": 300,    # ml
    "milk": 200,     # ml  
    "coffee": 100,   # g
    "money": 0       # $
}

# Menu with drink requirements and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def print_report():
    """Print the current resource values"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources_sufficient(drink_name):
    """Check if there are enough resources to make the drink"""
    drink = MENU[drink_name]
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    """Calculate the total value of coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    
    total = quarters + dimes + nickles + pennies
    return total

def check_transaction_successful(money_received, drink_cost):
    """Check if the transaction is successful and handle change"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # Add the cost to machine's money
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name):
    """Deduct resources and serve the drink"""
    drink = MENU[drink_name]
    
    # Deduct ingredients from resources
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]
    
    print(f"Here is your {drink_name} ☕. Enjoy!")

def coffee_machine():
    """Main coffee machine function"""
    is_on = True
    
    while is_on:
        # Prompt user for their choice
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == "off":
            # Turn off the machine
            print("Coffee machine is turning off...")
            is_on = False
            
        elif choice == "report":
            # Print current resources
            print_report()
            
        elif choice in MENU:
            drink = MENU[choice]
            
            # Check if resources are sufficient
            if check_resources_sufficient(choice):
                # Process payment
                payment = process_coins()
                
                # Check transaction
                if check_transaction_successful(payment, drink["cost"]):
                    # Make coffee
                    make_coffee(choice)
                    
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")

# Start the coffee machine
if __name__ == "__main__":
    print("☕ Welcome to the Coffee Machine! ☕")
    coffee_machine()
