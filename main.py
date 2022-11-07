print("Welcome to the 'Guess the Number' game.")
print()

print("I will pick a number between 0 and 1 000 000 and you guess the number.")
print()

print("Everytime you key in your response press enter. Goodluck!!!")

def showWinMessage(count):
  print("Well done! It only took you", count,"attempts.")  
  print() 
num = 37
count = 0

while True:
  count+=1
  print()
  try:
    num = int(input("Guess the number. "))
    print()
  except ValueError:
    print()
    print("I am expecting positive numbers.")
    print()
    continue
  if num == 37 :
    showWinMessage(count)
    break
  elif num > 37:
    print()
    print("too high.")
  elif num < 37:
    print()
    print('too low.')
  elif num < 0:
    print("I don't like negative numbers. Goodbye.")
    break 


def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run """)
    print()
    continue


if __name__=="__main__":
  endGame()
