def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ').lower()

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()


def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ').lower()

    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()


def order_mocha():
    while True:
        res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>").lower()
        if res == 'a':
            return "peppermint mocha"
        elif res == 'b':
            return 'mocha'
        print_message()

