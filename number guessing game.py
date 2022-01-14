import random
number = input (" Guess what my number between 1 and 100 is!")
x = random.randint (1,100)
while number != x:
  if 1 < float (number) < x:
    print (number + "? Guess higher!")
    number = input ("Guess another number!")
  elif 101 > float (number) > x:
    print (number + "? Guess lower!")
    number = input ("Guess another number!")
  elif float (number) <= 0 or float (number) >= 100:
    print (number + "? Hey, i said guess a number between 1 to 100!")
    number = input ("Guess another number!")
  if float (number) == x:
    print (number + "? Congrats! You won the game!")
    break