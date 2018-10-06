#!/usr/bin/python3

def main(number, divisor):

  n = int(number) % int(divisor)

  if n == 0:
    print('%d is divisible by %d' % (int(number), int(divisor)))
  else:
    print('%d is not divisible by %d' % (int(number), int(divisor)))

number = input('Number: ')
divisor = input('Divisor: ')

main(number, divisor)