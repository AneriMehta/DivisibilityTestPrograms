endin = ['0','25', '50', '75', '00']
n = input('Input to test for divisibility by 25: ')
if n[-2:] in endin:
    print('Divisible by 25')
else:
    print('Not Divisible by 25') 