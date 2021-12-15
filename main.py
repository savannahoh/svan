import random


def lucky():
  roll=random.randrange(1,10)
  if roll > 5:
    return True
  else: 
    return False


def main():
  money= 1254
  print('its morning, you wake up the alarm buzzing.')

  choice = input('do you [wake] up or [sleep] through the alarm')
  if choice== 'wake' or choice==' wake':
    print("you wake up on time")

    choiceb=input("you take the 'train' or 'school bus'")
    if choiceb=="train" or choiceb==" train":
      print("you drop your project and a rat eats it .")
      main()
    else:
      print("the bus gets a flat tire and you have to walk")


  if choice == 'sleep' or choice==' sleep':
    print("you oversleep and rush out the house without your art project.")

    choicea=input("you 'run' or 'walk'")
    if choicea=="run" or choicea==" run":
      print("a homeless person throws food at you, then chases you in the opposite direction.")
      main()
    else:
      print("you see someone commit a murder")
      if lucky():
        print("you are lucky, and quickly ran away before the cops came")
        choice1 = input("do you wish to 'quit' or 'restart' game")
        if choice1== 'quit' or choice=="  quit":
          exit()
        else:
          main()
        

      else: 
        print("you are not lucky, and the police caught you trying to flee the scene")



main()