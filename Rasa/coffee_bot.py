from utils import print_message, get_size, order_latte, order_mocha


def coffee_bot():
    print('Welcome to the cafe!')
    order_drink = "y"
    drinks = []
    while order_drink == "y":
        size = get_size()
        drink_type = get_drink_type()

        drink = '{} {}'.format(size, drink_type)
        print('Alright, that\'s a {}!'.format(drink))
        while True:
            drinks.append(drink)
            order_drink = input("Would you like to order another drink? (y/n)")

            if order_drink.lower() in ["y", "n"]:
                break
        print('Okay, so I have:')

    for drink in drinks:
        print('-', drink)

    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your order will be ready shortly.'.format(name))


def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ').lower()

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()


# Define new functions here!


coffee_bot()
