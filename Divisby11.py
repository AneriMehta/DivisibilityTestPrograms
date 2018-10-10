while True:
    try: 
        number = int(input('What is your number? '))
    except:
        "That isn't a number."
        continue

    if number == 0:
        print('Dividing by zero!? You\'re a mad man(or woman)!')
    elif number % 11 == 0:
        print('This number is divisible by 11!')
    else:
        print('This number is not divisible by 11!')

    cont = input('Type \'again\' to start over. ').lower()
    if cont == 'again':
        continue
    else:
        break

