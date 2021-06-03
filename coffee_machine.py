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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there isnt enough water{item}.')
            return False
    return True
def process_coint():
    """
    Returs True when order can be made , False if ingredients are infufficient

    """
    print('Please insert coins..')
    total = int(input('How mony quarters?: ')) * 0.25
    total += int(input('How mony dimes?: ') )* 0.1
    total += int(input('How mony nickles?: ')) * 0.05
    total += int(input('How mony pennies?: ') )* 0.01
    return total

def is_transaction_succesfull(money_received,drink_cost):
    """ Return True when payment is accepted, or False if money is insuffficient """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f'Here is ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry thats not enough money. Money refunded')


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️Enjoyy !')
is_on = True
while is_on:
    choice = input('What would you like?(espresso/latte/cappucciono):')
    if choice =='off':
        is_on =False
    elif choice == 'report':
        print(f"Water:{resources['water']} ml")
        print(f"Milk:{resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money:{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink['ingredients']):
            payment = process_coint()
            if is_transaction_succesfull(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
